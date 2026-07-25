import  readline  from "readline"

const COLORS = Object.freeze({
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  blue: "\x1b[34m",
  purple: "\x1b[35m",
  reset: "\x1b[0m",
})

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const askUsername = () => new Promise(r => rl.question(COLORS.purple + "Enter the username to generate the report: " + COLORS.reset, r))

const printError = err => console.error(COLORS.red + "Error: " + err + COLORS.reset)
const printReport = (name, report) => console.log(`${COLORS.green}--- ${name}'s report ---\n` +
                                                  `${COLORS.blue}Followers:${COLORS.yellow} ${report.followers}\n` +
                                                  `${COLORS.blue}Gists:${COLORS.yellow} ${report.gists}\n` +
                                                  `${COLORS.blue}Total stars:${COLORS.yellow} ${report.stars}\n` +
                                                  `${COLORS.blue}Forks:${COLORS.yellow} ${report.forks}\n` +
                                                  `${COLORS.blue}All languages:${COLORS.yellow} ${report.languages.join(", ")}${COLORS.reset}`
)

const fetchUser = async (username) => {
  const response = await fetch(`https://api.github.com/users/${username}`)

  if (response.status === 404) {
    throw new Error("User not found")
  }

  return response.json()
}

const fetchRepos = async (username) => {
  const response = await fetch(`https://api.github.com/users/${username}/repos?per_page=100`)

  return response.json()
}

const createReport = (userInfo, userReposInfo) => {
  const gists = userInfo.public_gists
  const followers = userInfo.followers
  const totalStars = userReposInfo.reduce((stars, repo) => stars + repo.stargazers_count, 0)
  const totalForks = userReposInfo.reduce((forks, repo) => forks + repo.forks, 0)
  const languages = [...new Set(
    userReposInfo
      .map(repo => repo.language)
      .filter(Boolean)
  )]

  return {
    gists,
    followers,
    stars: totalStars,
    forks: totalForks,
    languages
  }
}

async function getUser () {
  while (true) {
    const username = (await askUsername()).trim()

    try {
      if (!!username) return await fetchUser(username)

      printError("Username cannot be empty")
    } catch (e) {
      printError(e.message)
    }
  }
}

async function main () {
  try {
    const user = await getUser()
    const userReposInfo = await fetchRepos(user.login)

    const report = createReport(user, userReposInfo)
  
    printReport(user.login, report)
  
    rl.close()

  } catch (e) {
    printError(e.message)
  } finally {
    rl.close()
  }
}

main() 