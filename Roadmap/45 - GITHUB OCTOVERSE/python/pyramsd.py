import requests

base_url = "https://api.github.com"

user = input("Github user: ")

followers_users = [follower["login"] for follower in requests.get(f"{base_url}/users/{user}/followers").json()]

following_users = [follower["login"] for follower in requests.get(f"{base_url}/users/{user}/following").json()]

starreds = [starred["full_name"] for starred in requests.get(f"{base_url}/users/{user}/starred").json()]

user_repos = [repos["name"] for repos in requests.get(f"{base_url}/users/{user}/repos"). json()]

user_repos_forks = [(repos["name"], repos["fork"]) for repos in requests.get(f"{base_url}/users/{user}/repos"). json() if repos["fork"] == True]

print("Seguidores:", ', '.join(i for i in followers_users))
print("Usuarios que sigue:", ', '.join(i for i in following_users))
print("Repositorios favoritos: ", ', '.join(i for i in starreds))
print("Repositorios públicos:", ', '.join(i for i in user_repos))
print("Repositorios forkeados:", ', '.join(i[0] for i in user_repos_forks))
