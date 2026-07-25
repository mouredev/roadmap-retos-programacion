
const https = require('node:https');
const { hostname } = require('node:os');

const TOKEN = 'YOUR TOKEN';
const HOSTNAME = 'api.github.com'
const header = {

    'Authorization': `Bearer ${TOKEN}`,
    "Accept": "application/vnd.github+json",
    'User-Agent': 'raulG91'
}

async function getUserInfo(user) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: HOSTNAME,
            path: `/users/${user}`,
            method: 'GET',
            headers: header

        };
        let userInfo = ''

        https.get(options, (res) => {

            res.on('data', (data) => {
                userInfo += data
            })

            res.on('end', () => {
                let info = JSON.parse(userInfo)
                resolve(info)
            })

        }).on('error', (error) => {
            reject('Error occurs')
        })

    })

}

async function getReposInformation(user) {

    return new Promise((resolve, reject) => {
        const options = {
            hostname: HOSTNAME,
            path: `/users/${user}/repos`,
            method: 'GET',
            headers: header

        };
        let repo_info = '';

        https.get(options, (res) => {

            res.on('data', (data) => {
                repo_info += data
            })

            res.on('end', () => {

                let repos = []
                repo_list = JSON.parse(repo_info)

                for (let repo of repo_list) {
                    repos.push({
                        "name": repo.name,
                        "language": repo.language,
                        "stars": repo.stargazers_count,
                        "forks": repo.forks
                    })

                }
                resolve(repos)
            })
        }).on('error', (error) => {
            console.log("Error occurs " + error)
            reject(error)
        })

    })
}


async function main() {

    const USER = "mouredev"
    //Get user stats 
    try {
        let userInfo = await getUserInfo(USER)
        console.log("Number of followers is: " + userInfo.followers)
        console.log("Number of following users: " + userInfo.following)
        console.log("Number of public repositories: " + userInfo.public_repos)
    } catch (error) {
        console.log("Error getting user data")
    }


    //Get user's repos
    try {
        let repos = await getReposInformation(USER)
        let languages = {}

        for (let repo of repos) {

            console.log("Repository name: " + repo.name)
            console.log("Repository  main language: " + repo.language)
            console.log("Repository stars: " + repo.stars)
            console.log("Repository forks: " + repo.forks)

            if ((repo.language != null) && !(repo.language in languages)) {

                languages[repo.language] = 1

            }
            else if (repo.language != null) {
                languages[repo.language] += 1
            }
        }
        // Get most used language 
        let most_used_language = ""
        let max_used_times = 0
        for (let item in languages) {
            if (languages[item] > max_used_times) {
                max_used_times = languages[item]
                most_used_language = item
            }
        }
        console.log("Most used language is: " + most_used_language + " it has been used: " + max_used_times + " times")
    } catch (error) {

        console.log("Error getting data for repositories")
    }


}

main()