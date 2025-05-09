/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#45 GITHUB OCTOVERSE
-------------------------------------------------------
* EJERCICIO:
 * GitHub ha publicado el Octoverse 2024, el informe
 * anual del estado de la plataforma:
 * https://octoverse.github.com
 *
 * Utilizando el API de GitHub, crea un informe asociado
 * a un usuario concreto.
 * 
 * - Se debe poder definir el nombre del usuario
 *   sobre el que se va a generar el informe.
 *   
 * - Crea un informe de usuario basándote en las 5 métricas
 *   que tú quieras, utilizando la informración que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
 */
// ________________________________________________________
import fetch from 'node-fetch';
import readlineSync from 'readline-sync';

class GitHubApi {
    constructor(userName) {
        this.userName = userName;
        this.userData = null;
    }

    async getJson(url) {
        try {
            const response = await fetch(url);

            if (!response.ok) {
                console.error(`Error: ${response.status} - ${response.statusText}`);
                return {};
            }

            const text = await response.text();
            if (text.trim() === "") {
                console.error("Error: Respuesta vacía de la API.");
                return {};
            }

            try {
                return JSON.parse(text);
            } catch (jsonError) {
                console.error(`Error al parsear JSON: ${jsonError.message}`);
                return {};
            }

        } catch (error) {
            console.error(`Error de red: ${error.message}`);
            return {};
        }
    }

    async verifyStatus() {
        if (!this.userData) {
            console.error(`Usuario '${this.userName}' no encontrado.`);
            return false;
        }
        return true;
    }

    getRepoInfo(repo) {
        return `
            Lang:  ${repo.full_name || "Desconocido"}
            Repo:  ${repo.language || "Desconocido"}
            Stars: ${repo.stargazers_count || 0}
            Forks: ${repo.forks_count || 0}
        `.replace(/^\s+/gm, '').trim();
    }

    async printBasicInfo() {
        if (!await this.verifyStatus()) return;

        const { name, created_at, public_repos, public_gists, followers, following } = this.userData;
        console.log('');
        console.log(`
            -------------------------------------------
            Nombre:     ${name || "Desconocido"}
            Creación:   ${created_at || "Desconocido"}
            Repos:      ${public_repos || 0}
            Gists:      ${public_gists || 0}
            Seguidores: ${followers || 0}
            Seguidos:   ${following || 0}
            -------------------------------------------
        `.replace(/^\s+/gm, '').trim());
    }

    async printReposInfo() {
        if (!await this.verifyStatus()) return;

        const reposUrl = this.userData.repos_url || null;
        if (!reposUrl) {
            console.error("No se encontró la URL de los repositorios.");
            return;
        }

        const reposData = await this.getJson(reposUrl);
        const languages = new Map();

        console.log("Repositorios públicos:");
        for (const repo of reposData) {
            const language = repo.language;
            console.log('')
            console.log(this.getRepoInfo(repo));

            if (language) {
                languages.set(language, (languages.get(language) || 0) + 1);
            }
        }

        // Encuentra el lenguaje más utilizado
        let mostUsedLanguage = null;
        let maxCount = 0;
        for (const [language, count] of languages) {
            if (count > maxCount) {
                mostUsedLanguage = language;
                maxCount = count;
            }
        }

        console.log("________");
        console.log(`Total de repositorios: ${reposData.length}`);
        console.log(`El lenguaje más utilizado: ${mostUsedLanguage} (${maxCount})`);
    }

    async init() {
        const url = `https://api.github.com/users/${this.userName}`;
        this.userData = await this.getJson(url);
    }
}

// Ejecución principal
(async () => {
    console.log("Informe sobre los datos del usuario en GitHub");
    const userName = readlineSync.question("Usuario: ");
    const github = new GitHubApi(userName);

    await github.init();
    await github.printBasicInfo();
    await github.printReposInfo();
})();
