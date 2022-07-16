import json
import requests
import optparse
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