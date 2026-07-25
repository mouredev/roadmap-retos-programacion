# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods,broad-exception-raised,broad-exception-caught

from abc import ABCMeta, abstractmethod
from os import system
from typing import TypedDict
import requests


# ---------------------------------------------------------------------------- #
#                              TYPES - GITHUB API                              #
# ---------------------------------------------------------------------------- #

GitHubPublicRepos = TypedDict("GitHubPublicRepos", {"fork": bool})

GitHubStars = TypedDict("GitHubStars", {"url": str})

GitHubUserData = TypedDict(
    "GitHubUserData",
    {
        "followers": int,
        "following": int,
        "login": str,
        "name": str,
        "public_repos": int,
        "repos_url": str,
        "public_repos_data": list[GitHubPublicRepos],
        "stars": list[GitHubStars],
    },
)

GitHubAPI = TypedDict("GitHubAPI", {"user": GitHubUserData})


# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #

UserData = TypedDict(
    "UserData",
    {
        "followers": int,
        "following": int,
        "forks": int,
        "name": str,
        "public_repositories": int,
        "stars": int,
        "userName": str,
    },
)


class GitHubAdapters:
    @staticmethod
    def user_data(*, _user_data: GitHubUserData) -> UserData:
        forks: int = 0
        for public_repo in _user_data["public_repos_data"]:
            if public_repo["fork"]:
                forks += 1

        return {
            "followers": _user_data["followers"],
            "following": _user_data["following"],
            "forks": forks,
            "name": _user_data["name"],
            "public_repositories": _user_data["public_repos"],
            "stars": len(_user_data["stars"]),
            "userName": _user_data["login"],
        }


class AbcGitHubService(metaclass=ABCMeta):
    @abstractmethod
    def fetch_user_data(self, *, user_name: str) -> UserData:
        pass


class GitHubService(AbcGitHubService):
    __api_token: str

    def __init__(self, *, api_token: str) -> None:
        self.__api_token = api_token

    def fetch_user_data(self, *, user_name: str) -> UserData:

        headers: dict[str, str] = {
            "Authorization": f"Bearer {self.__api_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        response: requests.Response = requests.get(
            url=f"https://api.github.com/users/{user_name}",
            headers=headers,
            timeout=1000,
        )

        if response.status_code != 200:
            raise Exception("An error occurred on fetch user data")

        _user_data: GitHubUserData = response.json()

        response: requests.Response = requests.get(
            url=f"https://api.github.com/users/{user_name}/starred",
            headers=headers,
            timeout=1000,
        )

        if response.status_code != 200:
            raise Exception("An error occurred on fetch user data")

        stars: list[GitHubStars] = response.json()
        _user_data["stars"] = stars

        response: requests.Response = requests.get(
            url=_user_data["repos_url"],
            headers=headers,
            timeout=1000,
        )

        if response.status_code != 200:
            raise Exception("An error occurred on fetch user data")

        public_repos: list[GitHubPublicRepos] = response.json()
        _user_data["public_repos_data"] = public_repos

        return GitHubAdapters.user_data(_user_data=_user_data)


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #

API_TOKEN: str = "XXX"  # Complete with your personal GitHub Access Token.

github_service: AbcGitHubService = GitHubService(api_token=API_TOKEN)
user_input: str = input("> Enter a GitHub username (-1 to exit): ").strip()

while user_input != "-1":
    try:
        user_data: UserData = github_service.fetch_user_data(user_name=user_input)

        system(command="clear")

        print(f"+ {'':{'-'}<52} +")
        print(f'+ {user_data["userName"]:^52} +')
        print(f"+ {'':{'-'}<52} +")

        print(f"{f'+ Name: {user_data["name"]}.':<54} +")
        print(f"{f'+ Public repositories: {user_data["public_repositories"]}.':<54} +")
        print(f"{f'+ Repositories stared: {user_data["stars"]}':<54} +")
        print(f"{f'+ Number of repositories forked: {user_data["forks"]}.':<54} +")
        print(f"{f'+ Following: {user_data["following"]}.':<54} +")
        print(f"{f'+ Followers: {user_data["followers"]}.':<54} +")

        print(f"+ {'':{'-'}<52} +")
    except Exception as error:
        print(f"\n> An error occurred on fetch '{user_input}' username! Try again...")

    user_input: str = input("\n> Enter a GitHub username (-1 to exit): ").strip()
