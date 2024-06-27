import requests
from datetime import datetime, timedelta
import os
import os.path as osp


dict = []
# GitHub repository owner and name
access_token = os.environ["token"]
owner = os.environ["repo_owner"]
repo = os.environ["repo_name"]


# GitHub API endpoint for pull requests
endpoint = f'https://api.github.com/repos/{owner}/{repo}/pulls'

# Calculate the date 7 days ago
last_week = (datetime.now() - timedelta(days=7)).isoformat()

# Parameters for the API request
params = {
    'state': 'all',  # include open and closed pull requests
    'sort': 'created',  # sort by creation date
    'direction': 'desc',  # in descending order (newest first)
    'since': last_week  # filter pull requests created since last_week
}

# Headers with authorization using personal access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/vnd.github.v3+json'
}
item = {}
def get_github_pr():
    try:
        # Make GET request to GitHub API
        response = requests.get(endpoint, params=params, headers=headers)
        response.raise_for_status()  # Raise exception for bad response status

        # Extract and print relevant information from the response
        pull_requests = response.json()
        print(f"From: Ronnie Webb \nTo: Brad Hein \nSubject: PR Summary for {owner}/{repo} \n ")

        for pr in pull_requests:
            item = {"pr_number": pr['number'],
                    "pr_title":  pr['title'],
                    "pr_state":  pr['state']
                }
            pr_number = pr['number']
            pr_title = pr['title']
            pr_state = pr['state']
            print(f'Number  Title      State \n ')
            print(f'#{pr_number}: {pr_title} ({pr_state})')
        
            dict.append(item)
    except Exception as e:
            print(f'Error fetching pull requests: ', e)
    return dict 
            
