import os
import requests

import subprocess
import time
import requests
import os
import yaml
import base64
import re
import subprocess

GITHUB_TOKEN = "" # os.getenv("GHE_TOKEN")
def RaisePR(GITHUB_TOKEN):

    headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "title": "AI Fix feature",
        "body": "This PR implements the authentication feature using AIOps",
        "head": "issue-fix",
        "base": "main"
    }

    response = requests.post("https://github.com/Fadi-Farid/python-web-app/pulls", headers=headers, json=data)

    if response.status_code == 201:
        print("Pull request created successfully.")
    else:
        print(f"Failed to create pull request. Status code: {response.status_code}")
        print(response.json())
        

def main():

                command=(f'git clone https://github.com/Fadi-Farid/python-web-app.git')
                os.system(command)
                command=("git init && \
                git checkout  issue-fix && \
                cp -f ../app.py . && \
                git add . && git commit -m 'Fix Commit' &&\
                git push https://github.com/Fadi-Farid/python-web-app.git issue-fix")
                os.system(command)
                with open("../password", "r", encoding="utf-8") as file:
                   lines = file.read().strip()
                print(lines)                
                RaisePR(lines)

if __name__ == "__main__":
    main()
