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
    
    if not r.ok:
        print("Request Failed: {0}".format(r.text))
        exit(0)
    else:
        return json.loads(r.text)

#if __name__=="__main__":
    # create_pull_request(
    #     "rohanailoni", # project_name
    #     "test", # repo_name
    #     "My pull request title", # title
    #     "My pull request description lol this request for pull request is working", # description
    #     "dyte", # head_branch
    #     "main", # base_branch
    #     "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" #git_token
    # )
    # create_pull_request(
    #     "rohanailoni", # project_name
    #     "test", # repo_name
    #     "My ", # title
    #     "My pull request description lol this request for pull request is working", # description
    #     "dyte", # head_branch
    #     "main", # base_branch
    #     "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" #git_token
    # )