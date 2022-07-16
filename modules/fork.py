

import json
import os
import requests


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
    return "sucess"
