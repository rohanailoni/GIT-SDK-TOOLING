



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">SDK tooling</h3>

  <p align="center">
    Every tool is a combinations of diffe
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



<p align="right">(<a href="#top">back to top</a>)</p>



### Built With
* Python
	**Modules used:-**
	*	requests
		*	For using github api's to get, pull request, fork repos's
	*	pandas
		*	For easy way of handling csv input and output files

	*	optparse	
		*	this module is used to handle the request 
* System
    * Fedora 36 Linux 
    * Python 3.9.10
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

So ther are some important things needed to be noted before cloning the project. Like installing correct version of python

### Installation and project Demo in the below unlisted video
https://www.youtube.com/watch?v=Sbi6jnDfReQ
### Pre-requisites

As the whole project is based on python here we can go with installing correct version of python first in system:- 

* Install python in debian:-
  ```sh
  sudo apt-get install python3
  ```
* Install python 3 in fedora:-
```sh
	sudo dnf install python3
```
## Installation

1. Get a free API Key at [https://github.com/settings/tokens](https://github.com/settings/tokens)
![Image not found](https://drive.google.com/uc?export=view&id=1c_kyOxWzEvM0FOLQTfCHq_doWpRStJzb)
2. Clone the repo

 ```sh
 	git clone  https://github.com/dyte-submissions/dyte-vit-2022-rohanailoni
```
3.Creating and activating  virtual environment
```sh
	virtualenv venv
	source venv/bin/activate
```
4.  Install pip packages
 ```sh
   pip install -r requirments.txt
 ```

5. Enter your API in `config.json`
 ```json
   {
	   "config":<your api key (personal token from github)>,
			"user":<your github username>
   }
```

6. Running testing with some of my friends repo's (As it is a private repository i have kept my personal github keys in config.json)

```sh
	python main.py -i test.csv -u <library>@<version>
	
```



## Usage
 According to github we cannot make a pull request to non owned repo , unless we make a fork and make commits in forked repo and pull-request the changes.

![Image not found](https://drive.google.com/uc?export=view&id=1NfqWp34io34lIwhxHNL_i0WllPhruhJF)


There are few issuse with making pull request to the user , as there will be 2 cases:	
1 . We are the owner of the repo:-
		This case is easy to handle as I am the owner of the repo we can direcly make the commit rather than making a pull-	   request i.e can be resolved making a branch 
2. We are making the version change to another repo which is open source:-
		Accoring to Verified answer from stackoverflow it is not possible to make a pull request without forking the library.
		Following diagram describes the process of making a pull request.
![image not found](https://drive.google.com/uc?export=view&id=1lQUu5R_b1r0hdZSki1dTADM3KjF-mkN0)
		

<p align="right">(<a href="#top">back to top</a>)</p>



# Roadmap
## Module Helper functions:-
Before going to the direct implementation, I will go forward to show how I am acessing github api using custom functions created using python requests module at **Modules** folder location in the repo


## `modules/branch.py`:-
#### This file Handles creating a branch with random branch name with the help of previous commit *SHA* keys , where the username and repo_name and git_token are inputs.

```python
def create_branch(user_name,repo_name,git_token):
    num=random.randint(1,1000000)
    num="version_update_"+str(num)
    git_pulls_api = "https://api.github.com/repos/{0}/{1}/git/refs".format(
        user_name,
        repo_name)
    headers = {
        "Authorization": "token {0}".format(git_token),
        "Content-Type": "application/json",
        
        }
    data={
        "ref":"/heads/"+num,
        "sha":"c8b4ebc04d8b71ad2f8148ad0dc7b66c477456a2"
    }
    print(data)
    r = requests.post(
        git_pulls_api,
        headers=headers,
        data=json.dumps(data)
        )
    print(r.text)
    if not r.ok:
        print("Request Failed: {0}".format(r.text))
```

## `modules/file.py`
### function 1:-`get_package_json()`
#### As the repo is open sourced there is no need for API auth token to get the package.json from the file. This function will fetch the file and convert into a dictionary.

```python
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
```


### function 2:- `update_json()`
#### Now we have got the  package dictionary we need to change the version. Also  we need also to push to the github server with auth keys :
**NOTE:-** github only accepts base64 for content change

```python
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
```


### These two functions are to be used simultaneously 
**Example:-**
```python
"""Testing on updating the files"""
if __name__=="__main__":
		ans=get_package_json("Whatsapp-clone","rohanailoni")
		dep=ans['dependencies']
    if ans['dependencies']['@material-ui/core']:
        
        ans['dependencies']['@material-ui/core']="^4.11.5"
        print(ans)
        update_json("Whatsapp-clone","rohanailoni",ans,<API-TOKEN>,"updated the version of matrial UI")
```





## `modules/fork.py`
### This functions is used to fork a repository into the API_key owner's and we can make our own commits:-
```python
def create_fork(user_name,repo_name,git_token):

    git_pulls_api = "https://api.github.com/repos/{0}/{1}/forks".format(
        user_name,
        repo_name)
    headers = {
        "Authorization": "token {0}".format(git_token),
        "Content-Type": "application/json",
        
        }
    print(git_pulls_api)
    r = requests.post(
        git_pulls_api,
        headers=headers
        
        )
   
    if not r.ok:

        print("Request Failed: {0}".format(r.text))
        return "failed"
    return "success"
```


## `modules/list.py`
### This module is only testing purpose and will not be used. However this is required to list pull-requests.
```python
def list_pull_request(user_name,repo_name,title,description,head_branch,base_branch,git_token):
    git_pulls_api = "https://api.github.com/repos/{0}/{1}/pulls".format(
        user_name,
        repo_name)
    headers = {
        "Authorization": "token {0}".format(git_token),
        "Content-Type": "application/json"}

    payload = {
        "title": title,
        "body": description,
        "head": head_branch,
        "base": base_branch,
    }

    r = requests.get(
        git_pulls_api,
        headers=headers,
        )
    print(len(r.text))
    if not r.ok:
        print("Request Failed: {0}".format(r.text))
```

## `modules/merge.py`:-
### After making a commit we need to look into a possibility of conflict before code is  merged into a main branch. As github's pull-request is only created when there are no conflicts.

```python
def create_pull_request(user_name, repo_name, title, description, head_branch, base_branch, git_token):
    
    git_pulls_api = "https://api.github.com/repos/{0}/{1}/pulls".format(
        user_name,
        repo_name)
    headers = {
        "Authorization": "token {0}".format(git_token),
        "Content-Type": "application/json"}

    payload = {
        "title": title,
        "body": description,
        "head": head_branch,
        "base": base_branch,
    }

    r = requests.post(
        git_pulls_api,
        headers=headers,
        data=json.dumps(payload)
        )
    print(r.text)
    print(len(r.text))
    if not r.ok:
        print("Request Failed: {0}".format(r.text))

```

## `modules/retireve_config.py`
### This is used to retrieve the config.json in the directory like username and token
```python
def retrieve_config(filename):
    
    home = os.path.expanduser("~/Desktop/scripts/dyte-vit-2022-rohanailoni")
    path = os.path.join(home, filename)

    if not os.path.exists(path):
        return {}

    f = open(path, "r")
    config = json.load(f)
    f.close()
    
    return config
```


## `modules/version_check.py`:-
### This is used when we have to  check for original and input version whether it is satisfy the given condition:-
### <ins>Data Structures used to check version</ins>
#### As most of the version's are in  the order x.x.x.x  . I have used 2 pointer method to `version_check()`
![image not found](https://drive.google.com/uc?export=view&id=1z5asoT77NHAR73pDADT4weF9JJMurlHb)
### A1 and A2 are pointers which  are moved at every iteration and they are being checked with condition given below:-

```python
"""
return true if the current version is greater than the specified version
    True=version satisfy
    False=Unsatisfy
"""
def check_version(version,current_version):
    version=version.split(".")
    current_version=current_version.split(".")
    n=max(len(version),len(current_version))
    #print(current_version,n)
    if len(version)!=n:
        while(len(version)<n):
            version=version+['0']
    if len(current_version)!=n:
        while(len(current_version)<n):
            current_version=current_version+['0']
    """Using 2 pointer method to check version"""
    for i in range(n):
        if int(version[i])==int(current_version[i]):
            continue
        elif int(version[i])>int(current_version[i]):
            # i.e the version required is greater
            return False
        else:
            return True
    return True
```



# Arguments :-
#### -i/--input with input file path

#### optional -u/--update to update the lower version



- [x] Feature 1
	As It is possible to update a single modules with the below command
	#### Check only:-
	```sh
	python3 main.py -i input.csv axios@0.23.0
	```
	### output:-
	![image not found](https://drive.google.com/uc?export=view&id=1L6mFUtx__77KUOPSc7SHchH3ioRS9It2)

	### it also handles, if the library is not found:-
	#### Output:-
	![image not found](https://drive.google.com/uc?export=view&id=1qQgb5IpunvtmSNCaWE0qVesUbkN09UCc)

	## update with below shell code:-
	```sh
	python3 main.py -i input.csv -u axios@0.23.0
	```




- [x] Feature 2
	My cli can also check depency for multiple files:-
	```sh
	python3 main.py -i input.csv axios@0.23.0 react@12.2.1
	```
	#### output:-
	![image not found](https://drive.google.com/uc?export=view&id=1d22fNaUzJmiO80iLJTC3bj20xCsEZmdZ)
### update multiple files
```sh
python3 main.py -i input.csv -u axios@0.23.0 react@12.2.1
```

![image not found](https://drive.google.com/uc?export=view&id=1CKbA1cJQR537XW2nAVhoHRmioCTxzo4K)
## output of pull requests
### PR1
![image not found](https://drive.google.com/uc?export=view&id=1HbOoJyFyOKCNvVK4mq5gRpQEWvrMVbtc)
![image not found](https://drive.google.com/uc?export=view&id=1YEZrsA5iE3riNcoTulQBr1_sZEG4OGqD)
### PR2
![image not found](https://drive.google.com/uc?export=view&id=1aWUbyzHlH-g2dqZptbSt_nm675ZlyeEd)
![image not found](https://drive.google.com/uc?export=view&id=1dMm7P9WZZvmOGqHbsaEGBxr5hILO0HXl)
### PR3
![image not found](https://drive.google.com/uc?export=view&id=1q6bo7KvYtiq22XHIzpQMBScoLk36bJLW)
![image not found](https://drive.google.com/uc?export=view&id=1kOVHS3ZMZ6qyOqStuIO_Z8wQXy-R73JL)

- [x]  Feature 3
   Once the pull request is completed, link for pull request will be stored in `output.csv`
	### Output(/output.csv)
![image not found](https://drive.google.com/uc?export=view&id=1Bu76nOARInQQ3RIQpw1GoP7w4GmqAoR5)

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

# Installation and project Demo in the below unlisted video
https://www.youtube.com/watch?v=Sbi6jnDfReQ

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b new_ff`)
3. Commit your Changes (`git commit -m 'added some new feature'`)
4. Push to the Branch (`git push origin new_ff`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Aileni Rohan Reddy - [@linkedin](https://www.linkedin.com/in/rohan-ailoni-119319121/) - 
Email:-`rohanailoni@gmail.com`
Contact No:-`8008260370`
Github:-https://github.com/rohanailoni/
Leetcode:-https://leetcode.com/aileni_rohan/
Project Link: [https://github.com/dyte-submissions/dyte-vit-2022-rohanailoni](https://github.com/dyte-submissions/dyte-vit-2022-rohanailoni)

<p align="right">(<a href="#top">back to top</a>)</p>







