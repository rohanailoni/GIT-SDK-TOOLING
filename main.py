import json
import time
import requests
import optparse
import os
import sys
import pandas as pd
import numpy as np

# importing modules 
from modules.create import create_pull_request
from modules.list import list_pull_request
from modules.file import get_package_json
from modules.file import update_json
from modules.retrieve_config import retrieve_config
from modules.version_check import check_version
from modules.fork import create_fork



config=retrieve_config("config.json")

if __name__=="__main__":
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input",
                  dest = "input_file",
                  help = "Include the input file to be changed",
                  metavar = "FILE")
    parser.add_option("-u", "--update",
                    action="store_true",
                    dest = "update", default = False,
                    help = "update the version of the library")
    (options, args) = parser.parse_args()
    
    
    
    if options.input_file==None:

        print("Input File must be fed into the command line")
        exit(0)
    else:
        args=[i.split("@") for i in args]
        input_file=options.input_file
        repos=pd.read_csv(input_file)
        version_cache=[]
        main_cache={}
        for i in repos['repo']:
            temp=i.split("/")
            user=temp[3]
            repository=temp[4]
            package_json=get_package_json(repository,user)
            arit_cache=[]
            tempo_cache=[]
            for j in args:
                try:
                    # print(j)
                    # print("ppp",j[0])
                    if(package_json["dependencies"][j[0]][0]=="^"):
                        current_version=package_json["dependencies"][j[0]][1:]
                    else:
                        current_version=package_json["dependencies"][j[0]]
                    
                    version=j[1]
                    print(version,current_version)
                    satisf=check_version(version,current_version)
                    if satisf==False:
                        tempo_cache.append(j)

                    arit_cache.append(satisf)
                except KeyError:
                    arit_cache.append("Lib not found")
            main_cache[i]=tempo_cache
                
            version_cache.append(arit_cache)
        version_cache=np.array(version_cache)
        
        
        for j in range(len(args)):
            repos[args[j][0]+" Version Satisfy"]=version_cache[:,j]
        print(repos)
        # print(main_cache)
        if options.update:
            """This code Have forks to be managed of len of cahce is 0 that is no dependecy or change in verison"""
            for i in main_cache:
                if len(main_cache[i])!=0:
                    test_temp=i.split("/")
                    if create_fork(test_temp[3],test_temp[4],config['config'])=="failed":
                        print("created a fork has been failed ")
                    else:
                        print("forked the repo sucessfully :-",i)

            
            """Wait time for the fork to happen"""
            time.sleep(20)
            """this below code changes  to commit under the forked repo"""
            for i in main_cache:
                if len(main_cache[i])!=0:
                    test_temp=i.split("/")
                    user=config['user']
                    repo=test_temp[4]
                    package=get_package_json(repo,user)
                    
                    for j in main_cache[i]:
                        if package['dependencies'][j[0]]:
                            package['dependencies'][j[0]]=j[1]
                    
                    update_json(repo,user,package,config['config'],"Version updated")
                
            """This below code is for creating a pull request"""
            pull_request=pd.DataFrame()
            pull_cache=[]
            for i in main_cache:
                if len(main_cache[i])!=0:
                    test_temp=i.split("/")
                    r=requests.get(i.replace("github.com","api.github.com/repos")+"/branches")
                    # print(i.replace("github.com","api.github.com/repos")+"/branches")
                    try:
                        foo=json.loads(r.text)[0]['name']
                        #print(foo)
                        from_pull=config['user']+":"+foo
                        to_pull=test_temp[3]+":"+foo
                        title="Change in Version of "
                        for j in main_cache[i]:
                            title+=j[0]+"@"+j[1]+" "
                        
                        pull=create_pull_request(
                            test_temp[3], # user_name
                            test_temp[4], # repo_name
                            title, # title
                            "change in version of the package.json", # description
                            from_pull, # head_branch
                            foo, # base_branch
                            config['config'] #git_token
                        )
                        
                        print("Created a pull request succesfull in ",to_pull)
                    except KeyError:
                        print("No branch has been found")
        else:
            print("Update options havent been provided")
            repos.to_csv("output.csv")



       




