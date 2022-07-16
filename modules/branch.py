import json
import os
import random
import requests


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


"""Testing the Create Branch Function"""

create_branch(
    "rohanailoni",
    "whatsapp-clone",
    "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",
)