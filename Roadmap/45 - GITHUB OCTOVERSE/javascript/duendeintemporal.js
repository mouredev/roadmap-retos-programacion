//#45 GITHUB OCTOVERSE
/*
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
 *   que tú quieras, utilizando la información que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
 */

//#45 GITHUB OCTOVERSE
/*
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
 *   que tú quieras, utilizando la información que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
 */

let log = console.log;

window.addEventListener('load', () => {
    const body = document.querySelector('body');
    const title = document.createElement('h1');

    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');

    title.textContent = 'Retosparaprogramadores #45.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');

    body.appendChild(title);

    setTimeout(() => {
        alert('Retosparaprogramadores #45. Please open the Browser Developer Tools.');
    }, 2000);
    log('Retosparaprogramadores #45');
});

async function fetchGitHubData(username) {
    const userResponse = await fetch(`https://api.github.com/users/${username}`);
    const userData = await userResponse.json();

    const reposResponse = await fetch(`https://api.github.com/users/${username}/repos`);
    const reposData = await reposResponse.json();

    return { userData, reposData };
}

async function generateUserReport(username) {
    const { userData, reposData } = await fetchGitHubData(username);

    // Calculate metrics
    const metrics = [
        { name: 'Most Used Language', key: 'language' },
        { name: 'Number of Repositories', key: 'public_repos' },
        { name: 'Followers/Following', key: 'followers_following_ratio' },
        { name: 'Stars/Forks', key: 'stars_forks_ratio' },
        { name: 'Contributions', key: 'contributions' },
    ];

    let mostUsedLanguage = null;
    let totalStars = 0;
    const totalRepos = reposData.length;
    const followers = userData.followers || 0;
    const following = userData.following || 1; // Avoid division by zero
    const contributions = userData.contributions || 'N/A'; // This may still be N/A

    // Analyze repositories
    const languageCount = {};
    reposData.forEach(repo => {
        if (repo.language) {
            languageCount[repo.language] = (languageCount[repo.language] || 0) + 1;
            totalStars += repo.stargazers_count || 0;
        }
    });

    if (Object.keys(languageCount).length > 0) {
        mostUsedLanguage = Object.keys(languageCount).reduce((a, b) => languageCount[a] > languageCount[b] ? a : b);
    }

    const followersFollowingRatio = (followers / following).toFixed(2);
    const starsForksRatio = (totalRepos > 0) ? (totalStars / totalRepos).toFixed(2) : 'N/A';

    let report = `GitHub User Report for ${username}:\n\n`;
    for (const metric of metrics) {
        let value;
        switch (metric.key) {
            case 'language':
                value = mostUsedLanguage || 'N/A';
                break;
            case 'public_repos':
                value = totalRepos;
                break;
            case 'followers_following_ratio':
                value = followersFollowingRatio;
                break;
            case 'stars_forks_ratio':
                value = starsForksRatio;
                break;
            case 'contributions':
                value = contributions;
                break;
            default:
                value = 'N/A';
        }
        report += `${metric.name}: ${value}\n`;
    }

    return report;
}

let username = 'mouredev';
generateUserReport(username)
    .then((report) => log(report))
    .catch((error) => console.error(error));

    //Output:
    /*  Most Used Language: Swift
        Number of Repositories: 30
        Followers/Following: 13220.50
        Stars/Forks: 1392.87
        Contributions: N/A  */ 