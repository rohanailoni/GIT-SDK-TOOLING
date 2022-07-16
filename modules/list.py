import json
import requests
import optparse
import json
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

#list=list_pull_request("rohanailoni","test","addition of some lines","lol","dyte","main",config['config'])


