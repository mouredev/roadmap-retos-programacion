// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const fetch = require("node-fetch");
// npm install node-fetch

class GitHubUserReport {
    constructor(username) {
        this.username = username;
        this.BASE_URL = "https://api.github.com";
    }

    async fetchData(endpoint) {
        const url = `${this.BASE_URL}/${endpoint}`;
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`[+] - Error fetching data from ${url}: ${response.status}`);
        }
        return await response.json();
    }

    async getUserInfo() {
        return this.fetchData(`users/${this.username}`);
    }

    async getRepos() {
        return this.fetchData(`users/${this.username}/repos`);
    }

    async generateReport() {
        const userInfo = await this.getUserInfo();
        const repos = await this.getRepos();

        // Metric 1: Most used language
        const languages = {};
        repos.forEach(repo => {
            if (repo.language) {
                languages[repo.language] = (languages[repo.language] || 0) + 1;
            }
        });
        const mostUsedLanguage = Object.keys(languages).reduce((a, b) =>
            languages[a] > languages[b] ? a : b, "Unknown");

        // Metric 2: Total number of repositories
        const totalRepos = repos.length;

        // Metric 3: Total stars received
        const totalStars = repos.reduce((sum, repo) => sum + repo.stargazers_count, 0);

        // Metric 4: Followers
        const followers = userInfo.followers || 0;

        // Metric 5: Following
        const following = userInfo.following || 0;

        // Generate the report
        return {
            Username: this.username,
            "Most Used Language": mostUsedLanguage,
            "Total Repositories": totalRepos,
            "Total Stars": totalStars,
            Followers: followers,
            Following: following,
        };
    }
}

(async () => {
    const username = process.argv[2];
    if (!username) {
        console.error("[+] - Please provide a GitHub username.");
        process.exit(1);
    }

    const reportGenerator = new GitHubUserReport(username);
    try {
        const report = await reportGenerator.generateReport();
        console.log("\n[+] - GitHub User Report:");
        for (const [key, value] of Object.entries(report)) {
            console.log(`${key}: ${value}`);
        }
    } catch (error) {
        console.error(`[-] - Error: ${error.message}`);
    }
})();
