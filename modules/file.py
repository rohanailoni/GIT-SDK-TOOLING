
import os
import requests
import json
import base64

def get_package_json(repo_name,user_name):
    """To be rememberd that the file return a """
    git_pulls_api = "https://api.github.com/repos/{0}/{1}/contents/package.json".format(
        user_name,
        repo_name)
    
    r = requests.get(
        git_pulls_api,
        
        )
   
    if r.status_code==404:
        return {}
    dic=json.loads(r.text)
    try:
        ans=requests.get(dic["download_url"])
        return json.loads(ans.text)
    except:
        return {}



def update_json(repo_name,user_name,dic,git_token,message):
    git_pulls_api = "https://api.github.com/repos/{0}/{1}/contents/package.json".format(
        user_name,
        repo_name)
    headers = {
        "Authorization": "token {0}".format(git_token),
        "Content-Type": "application/json",
        
        }
    dic=json.dumps(dic,indent=4)
    sample_string = dic
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    blob=json.loads(requests.get("https://api.github.com/repos/{0}/{1}/contents/package.json".format(user_name,repo_name)).text)
    data={
        "message":message,
        "content":base64_string,
        "sha":blob['sha']
    }
    r = requests.put(
        git_pulls_api,
        headers=headers,
        data=json.dumps(data)
        )
    if not r.ok:
        print("Request Failed: {0}".format(r.text))
    
    
ans=get_package_json("Whatsapp-clone","rohanailoni")
dep=ans['dependencies']

"""Testing on updating the files"""
if __name__=="__main__":
    if ans['dependencies']['@material-ui/core']:
        
        ans['dependencies']['@material-ui/core']="^4.11.5"
        print(ans)
        update_json("Whatsapp-clone","rohanailoni",ans,"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","updated the version of matrial UI")