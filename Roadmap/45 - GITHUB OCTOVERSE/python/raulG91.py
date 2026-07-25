import requests
import json
from collections import Counter

TOKEN = "YOUR TOKEN"

def getFollowers(user):
    header =  {
        "Authorization": f'Bearer {TOKEN}',
        "Accept": "application/vnd.github+json"
    }
    try:
        result = requests.get(f'https://api.github.com/users/{user}/followers',headers=header)
        if result.status_code>=200 and result.status_code<=299:
            followers = json.loads(result.text)
            return len(followers)
        else:
            print("Error getting user followers with code", result.status_code)
            return 0
    except Exception as e:
        print("Error getting user followers ", e)    

def getFollowing(user):
    header = {
        "Authorization": f'Bearer {TOKEN}',
        "Accept": "application/vnd.github+json"
    }
    try:
        result = requests.get(f'https://api.github.com/users/{user}/following',headers=header)
        if result.status_code>=200 and result.status_code<=299:
            following = json.loads(result.text)
            return len(following)
        else:
            print("Error getting user followings with code", result.status_code)
            return 0
    except Exception as e:
        print("Error getting user followings ", e)   
def getNumberRepos(user):
    header = {
        "Authorization": f'Bearer {TOKEN}',
        "Accept": "application/vnd.github+json"
    }
    try:
        result = requests.get(f'https://api.github.com/users/{user}/repos',headers=header)
        if result.status_code>=200 and result.status_code<=299:
            repos = json.loads(result.text)
            return len(repos)
        else:
            print("Error getting user repositories with code", result.status_code)
            return 0
    except Exception as e:
        print("Error getting user repositories ", e)  

def getPullRequests(user):
    header = {
        "Authorization": f'Bearer {TOKEN}',
        "Accept": "application/vnd.github+json"
    }
    try:
        result = requests.get(f'https://api.github.com/users/{user}/events',headers=header)
        if result.status_code>=200 and result.status_code<=299:
            events_array = json.loads(result.text)
            pull_request =  [event for event in events_array if event["type"] == 'PullRequestEvent']
            return len(pull_request)
        else:
            print("Error getting user events with code", result.status_code)
            return 0
    except Exception as e:
        print("Error getting user events ", e)   
def getLanguage(user):
    languages = []
    header = {
        "Authorization": f'Bearer {TOKEN}',
        "Accept": "application/vnd.github+json"
    }
    try:
        result = requests.get(f'https://api.github.com/users/{user}/repos',headers=header)
        if result.status_code>=200 and result.status_code<=299:
            repos = json.loads(result.text)
            for repo in repos:
                if repo["language"] != None:
                    languages.append(repo["language"])
            #Get the most used language        
            counter = Counter(languages)
            return counter.most_common(1)[0][0]

        else:
            print("Error getting user repositories with code", result.status_code)
            return 0
    except Exception as e:
        print("Error getting user repositories ", e)                     

user = input("Insert user to get information ")

print("Followers user :",getFollowers(user))
print("Following user ",getFollowing(user))
print("Repositories for user: ",getNumberRepos(user))
print("Number pull request: ",getPullRequests(user))
print("Most used languge is: ",getLanguage(user))