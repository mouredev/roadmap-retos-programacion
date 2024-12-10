# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import requests

class GitHubUserReport:
    BASE_URL = "https://api.github.com"

    def __init__(self, username):
        self.username = username

    def fetch_data(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error fetching data from {url}: {response.status_code}")
        return response.json()

    def get_user_info(self):
        return self.fetch_data(f"users/{self.username}")

    def get_repos(self):
        return self.fetch_data(f"users/{self.username}/repos")

    def generate_report(self):
        user_info = self.get_user_info()
        repos = self.get_repos()

        # Metric 1: Most used language
        languages = {}
        for repo in repos:
            if repo['language']:
                languages[repo['language']] = languages.get(repo['language'], 0) + 1
        most_used_language = max(languages, key=languages.get) if languages else "Unknown"

        # Metric 2: Total number of repositories
        total_repos = len(repos)

        # Metric 3: Total stars received
        total_stars = sum(repo['stargazers_count'] for repo in repos)

        # Metric 4: Followers
        followers = user_info.get('followers', 0)

        # Metric 5: Following
        following = user_info.get('following', 0)

        # Generate the report
        report = {
            "\t[+] - Username": self.username,
            "\t[+] - Most Used Language": most_used_language,
            "\t[+] - Total Repositories": total_repos,
            "\t[+] - Total Stars": total_stars,
            "\t[+] - Followers": followers,
            "\t[+] - Following": following,
        }
        return report


if __name__ == "__main__":
    username = input("[+] - Enter the GitHub username: ")
    report_generator = GitHubUserReport(username)
    try:
        report = report_generator.generate_report()
        print("\n[+] - GitHub User Report:")
        for key, value in report.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"[+] - Error: {e}")
