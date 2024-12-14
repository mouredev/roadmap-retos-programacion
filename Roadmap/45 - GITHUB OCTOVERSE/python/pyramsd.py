import requests, asyncio, aiohttp

base_url = "https://api.github.com"
user = input("Github user: ")

async def get_data(url, session):
    async with session.get(url) as response:
        return await response.json()


async def tareas():
    async with aiohttp.ClientSession() as session:
        followers_users = [follower["login"] for follower in await get_data(f"{base_url}/users/{user}/followers", session)]
        following_users = [follower["login"] for follower in await get_data(f"{base_url}/users/{user}/following", session)]
        starreds = [starred["full_name"] for starred in await get_data(f"{base_url}/users/{user}/starred", session)]
        user_repos = [repos["name"] for repos in await get_data(f"{base_url}/users/{user}/repos", session)]
        user_repos_forks = [(repos["name"], repos["fork"]) for repos in await get_data(f"{base_url}/users/{user}/repos", session) if repos["fork"] == True]
        return followers_users, following_users, starreds, user_repos, user_repos_forks


async def main():
    followers_users, following_users, starreds, user_repos, user_repos_forks = await tareas()
    print("Seguidores:", ', '.join(i for i in followers_users))
    print("Usuarios que sigue:", ', '.join(i for i in following_users))
    print("Repositorios favoritos: ", ', '.join(i for i in starreds))
    print("Repositorios públicos:", ', '.join(i for i in user_repos))
    print("Repositorios forkeados:", ', '.join(i[0] for i in user_repos_forks))

asyncio.run(main())
