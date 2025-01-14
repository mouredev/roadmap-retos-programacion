import https from 'https';
import readline from 'readline';

type Headers = { [key: string]: string };

class GitHubUserReport {
    private username: string;
    private baseApiUrl: string = "https://api.github.com";
    private headers: Headers = {
        "User-Agent": "GitHub-Report-App",
        "Accept": "application/vnd.github.v3+json"
    };

    constructor(username: string) {
        this.username = username;
    }

    private apiRequest<T>(endpoint: string): Promise<T> {
        const url = `${this.baseApiUrl}${endpoint}`;

        return new Promise((resolve, reject) => {
            const options = {
                headers: this.headers
            };

            https.get(url, options, (res) => {
                let data = '';

                res.on('data', chunk => {
                    data += chunk;
                });

                res.on('end', () => {
                    if (res.statusCode === 200) {
                        resolve(JSON.parse(data));
                    } else {
                        reject(new Error(`Error al conectar con la API de GitHub (HTTP ${res.statusCode}). Verifica el nombre de usuario.`));
                    }
                });
            }).on('error', (err) => {
                reject(new Error(`Error de conexión: ${err.message}`));
            });
        });
    }

    private getUserInfo(): Promise<any> {
        return this.apiRequest(`/users/${this.username}`);
    }

    private getUserRepos(): Promise<any[]> {
        return this.apiRequest(`/users/${this.username}/repos`);
    }

    public async generateReport(): Promise<void> {
        try {
            const userInfo = await this.getUserInfo();
            const repos = await this.getUserRepos();

            const totalRepos = repos.length;
            const followers = userInfo.followers;
            const following = userInfo.following;

            const languages = repos.map(repo => repo.language).filter(Boolean);
            const languageCounts = languages.reduce((counts: { [key: string]: number }, lang: string) => {
                counts[lang] = (counts[lang] || 0) + 1;
                return counts;
            }, {});

            const topLanguage = Object.keys(languageCounts).sort((a, b) => languageCounts[b] - languageCounts[a])[0] || "N/A";

            const totalStars = repos.reduce((sum, repo) => sum + repo.stargazers_count, 0);
            const totalForks = repos.reduce((sum, repo) => sum + repo.forks_count, 0);

            console.log(`=== Informe de GitHub para el usuario: ${this.username} ===`);
            console.log(`Nombre: ${userInfo.name}`);
            console.log(`Bio: ${userInfo.bio}`);
            console.log(`Ubicación: ${userInfo.location}`);
            console.log(`Total de repositorios: ${totalRepos}`);
            console.log(`Seguidores: ${followers}`);
            console.log(`Seguidos: ${following}`);
            console.log(`Lenguaje más utilizado: ${topLanguage}`);
            console.log(`Total de estrellas: ${totalStars}`);
            console.log(`Total de forks: ${totalForks}`);
        } catch (error: any) {
            console.error(error.message);
        }
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Ingrese el nombre de usuario de GitHub: ", (username: string) => {
    if (!username) {
        console.error("Debe ingresar un nombre de usuario.");
        rl.close();
        return;
    }

    const report = new GitHubUserReport(username);
    report.generateReport().finally(() => rl.close());
});
