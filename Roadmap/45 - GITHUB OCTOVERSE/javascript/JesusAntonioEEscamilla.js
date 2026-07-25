/** #45 - JavaScript -> Jesus Antonio Escamilla */

/**
 * GITHUB OCTOVERSE.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const GITHUB_API_URL = "https://api.github.com";

async function fetchGitHubData(username) {
    try {
        const headers = {
            "User-Agent": "GitHub-User-Report",
        };

        // Obtener datos básicos del usuario
        const userResponse = await fetch(`${GITHUB_API_URL}/users/${username}`, {
            headers
        });
        if (!userResponse.ok) {
            throw new Error(`Error en la solicitud: ${userResponse.statusText}`);
        }
        const userData = await userResponse.json();

        // Obtener repositorios del usuario
        const reposResponse = await fetch(`${GITHUB_API_URL}/users/${username}/repos?per_page=100`, {
            headers
        });
        if (!reposResponse.ok) {
            throw new Error(`Error en la solicitud: ${reposResponse.statusText}`);
        }
        const reposData = await reposResponse.json();

        // Procesar métricas
        const languageCount = {};
        let totalStars = 0;
        const topRepos = reposData
            .map((repo) => {
                totalStars += repo.stargazers_count;
                if (repo.language) {
                    languageCount[repo.language] = (languageCount[repo.language] || 0) + 1;
                }
                return { name: repo.name, stars: repo.stargazers_count };
            })
            .sort((a, b) => b.stars - a.stars)
            .slice(0, 3);

        const mostUsedLanguage = Object.keys(languageCount).reduce((a, b) =>
            languageCount[a] > languageCount[b] ? a : b
        );

        // Crear informe
        return {
            username: userData.login,
            name: userData.name || "Nombre no disponible",
            publicRepos: userData.public_repos,
            followers: userData.followers,
            following: userData.following,
            mostUsedLanguage,
            topRepos,
            totalStars,
        };
    } catch (error) {
        throw new Error(`Error en la solicitud: ${error.message}`);
    }
}

// Ejemplo de uso
(async () => {
    const username = "mouredev";
    try {
        const report = await fetchGitHubData(username);
        printReport(report);
    } catch (error) {
        console.error("Error:", error.message);
    }
})();

function printReport(report) {
    if (!report) return;
    console.log(`\n--- Informe de Usuario: ${report.username} ---`);
    console.log(`Nombre: ${report.name}`);
    console.log(`Repositorios Públicos: ${report.publicRepos}`);
    console.log(`Seguidores: ${report.followers}, Seguidos: ${report.following}`);
    console.log(`Lenguaje más utilizado: ${report.mostUsedLanguage}`);
    console.log(`Repositorios con más estrellas:`);
    report.topRepos.forEach((repo, index) => {
        console.log(`  ${index + 1}. ${repo.name} - ${repo.stars} estrellas`);
    });
    console.log(
        `Total de estrellas en todos los repositorios: ${report.totalStars}`
    );
}
