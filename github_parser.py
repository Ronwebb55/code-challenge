import os
import os.path as osp
from flask import json
from github import Github
import json


def get_github_pr():
    token = os.environ["token"]
    repo_owner = os.environ["repo_owner"]
    repo_name = os.environ["repo_name"]

    pull_request=()
    token = Github(token)

    repo = token.get_repo(f"{repo_owner}/{repo_name}")
    pr_list = []
    item = {}
    items = []
    test = {}
    #Iterate through all open pull requests in the repository
    print(f"From: Ronnie Webb \nTo: Brad Hein \nSubject: PR Summary \n ")
    for pull_request in repo.get_pulls(state='all'):
        item = {"Number": pull_request.number,
               "Title": pull_request.title,
               "State": pull_request.state
               }
        
        pr_list.append(item)
           
    return pr_list

    