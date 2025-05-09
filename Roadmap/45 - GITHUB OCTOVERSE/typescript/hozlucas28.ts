import readline from 'node:readline/promises'

/* -------------------------------------------------------------------------- */
/*                                    TYPES                                   */
/* -------------------------------------------------------------------------- */

interface GitHubAPI {
    user: {
        avatar_url: string
        bio: string
        blog: string
        company?: string
        created_at: string
        email?: string
        events_url: string
        followers_url: string
        followers: number
        following_url: string
        following: number
        gists_url: string
        gravatar_id: string
        hireable: true
        html_url: string
        id: number
        location: string
        login: string
        name: string
        node_id: string
        organizations_url: string
        public_gists: number
        public_repos: number
        received_events_url: string
        repos_url: string
        site_admin: boolean
        starred_url: string
        subscriptions_url: string
        twitter_username: string
        type: string
        updated_at: string
        url: string
        user_view_type: string

        public_repos_data: {
            allow_forking: boolean
            archive_url: string
            archived: boolean
            assignees_url: string
            blobs_url: string
            branches_url: string
            clone_url: string
            collaborators_url: string
            comments_url: string
            commits_url: string
            compare_url: string
            contents_url: string
            contributors_url: string
            created_at: string
            default_branch: string
            deployments_url: string
            description: string
            disabled: boolean
            downloads_url: string
            events_url: string
            fork: boolean
            forks_count: number
            forks_url: string
            forks: number
            full_name: string
            git_commits_url: string
            git_refs_url: string
            git_tags_url: string
            git_url: string
            has_discussions: boolean
            has_downloads: boolean
            has_issues: boolean
            has_pages: boolean
            has_projects: boolean
            has_wiki: boolean
            homepage: string
            hooks_url: string
            html_url: string
            id: number
            is_template: boolean
            issue_comment_url: string
            issue_events_url: string
            issues_url: string
            keys_url: string
            labels_url: string
            language: string
            languages_url: string
            merges_url: string
            milestones_url: string
            mirror_url?: string
            name: string
            node_id: string
            notifications_url: string
            open_issues_count: number
            open_issues: number
            private: boolean
            pulls_url: string
            pushed_at: string
            releases_url: string
            size: number
            ssh_url: string
            stargazers_count: number
            stargazers_url: string
            statuses_url: string
            subscribers_url: string
            subscription_url: string
            svn_url: string
            tags_url: string
            teams_url: string
            trees_url: string
            updated_at: string
            url: string
            visibility: string
            watchers_count: number
            watchers: number
            web_commit_signoff_required: boolean
        }[]

        stars: {
            avatar_url: string
            events_url: string
            followers_url: string
            following_url: string
            gists_url: string
            gravatar_id: string
            html_url: string
            id: number
            login: string
            node_id: string
            organizations_url: string
            received_events_url: string
            repos_url: string
            site_admin: boolean
            starred_url: string
            subscriptions_url: string
            type: string
            url: string
            user_view_type: string
        }[]
    }
}

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

interface GetUserInputParams {
    message: string
    onFail?: (userInput: string) => void
    validator?: (userInput: string) => boolean
}

async function getUserInput({
    message,
    onFail = () => {},
    validator = () => true,
}: GetUserInputParams): Promise<string> {
    let userInput: string

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    userInput = await rl.question(message)

    while (!validator(userInput)) {
        onFail(userInput)
        userInput = await rl.question(message)
    }

    rl.close()

    userInput = userInput.trim()

    return userInput.trim()
}

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

interface GitHubUserData {
    followers: number
    following: number
    forks: number
    name: string
    publicRepositories: number
    stars: number
    userName: string
}

interface IGitHubService {
    fetchUserData: (userName: string) => Promise<GitHubUserData>
}

class GitHubService implements IGitHubService {
    public constructor() {}

    private userDataAdapter(userData: GitHubAPI['user']): GitHubUserData {
        let forks: number = 0
        for (const publicRepo of userData.public_repos_data) {
            if (publicRepo.fork) forks++
        }

        return {
            followers: userData.followers,
            following: userData.following,
            forks,
            name: userData.name,
            publicRepositories: userData.public_repos,
            stars: userData.stars.length,
            userName: userData.login,
        }
    }

    public async fetchUserData(userName: string): Promise<GitHubUserData> {
        let response = await fetch(`https://api.github.com/users/${userName}`)
        if (!response.ok)
            throw new Error('An error occurred on fetch user data')

        const userData = (await response.json()) as GitHubAPI['user']

        response = await fetch(
            `https://api.github.com/users/${userName}/starred`
        )
        if (!response.ok)
            throw new Error('An error occurred on fetch user data')

        const stars = (await response.json()) as GitHubAPI['user']['stars']
        userData.stars = stars

        response = await fetch(userData.repos_url)
        if (!response.ok)
            throw new Error('An error occurred on fetch user data')

        const publicRepositories =
            (await response.json()) as GitHubAPI['user']['public_repos_data']
        userData.public_repos_data = publicRepositories

        return this.userDataAdapter(userData)
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    let userData: GitHubUserData
    const githubService: IGitHubService = new GitHubService()

    let userInput: string = await getUserInput({
        message: '> Enter a GitHub username (-1 to exit): ',
    })

    while (userInput !== '-1') {
        try {
            userData = await githubService.fetchUserData(userInput)

            console.clear()

            console.log('+'.padEnd(55, '-') + '+')
            console.log(
                '+' + userData.userName.padStart(27, ' ').padEnd(54, ' ') + '+'
            )
            console.log('+'.padEnd(55, '-') + '+')

            console.log(`+ Name: ${userData.name}.`.padEnd(55, ' ') + '+')
            console.log(
                `+ Public repositories: ${userData.publicRepositories}.`.padEnd(
                    55,
                    ' '
                ) + '+'
            )
            console.log(
                `+ Repositories stared: ${userData.stars}.`.padEnd(55, ' ') +
                    '+'
            )
            console.log(
                `+ Number of repositories forked: ${userData.forks}.`.padEnd(
                    55,
                    ' '
                ) + '+'
            )
            console.log(
                `+ Following: ${userData.following}.`.padEnd(55, ' ') + '+'
            )
            console.log(
                `+ Followers: ${userData.followers}.`.padEnd(55, ' ') + '+'
            )

            console.log('+'.padEnd(55, '-') + '+')
        } catch (error) {
            console.log(
                `\n> An error occurred on fetch "${userInput}" username! Try again...`
            )
        }

        userInput = await getUserInput({
            message: '\n> Enter a new GitHub username (-1 to exit): ',
        })
    }
})()
