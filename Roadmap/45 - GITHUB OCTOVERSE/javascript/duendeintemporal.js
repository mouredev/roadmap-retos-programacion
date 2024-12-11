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

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #45.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #45. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #45'); 
});


async function fetchGitHubData(username) {
    const response = await fetch(`https://api.github.com/users/${username}`);
    const data = await response.json();
    return data;
  }
  
  async function generateUserReport(username) {
    const userData = await fetchGitHubData(username);
  
    const metrics = [
      { name: 'Most Used Language', key: 'language' },
      { name: 'Number of Repositories', key: 'public_repos' },
      { name: 'Followers/Following', key: 'followers_following_ratio' },
      { name: 'Stars/Forks', key: 'stars_forks_ratio' },
      { name: 'Contributions', key: 'contributions' },
    ];
  
    let report = `GitHub User Report for ${username}:\n\n`;
    for (const metric of metrics) {
      let value;
      switch (metric.key) {
        case 'language':
          value = userData.language || 'N/A';
          break;
        case 'public_repos':
          value = userData.public_repos;
          break;
        case 'followers_following_ratio':
          value = (userData.followers / userData.following).toFixed(2);
          break;
        case 'stars_forks_ratio':
          value = (userData.stargazers_count / userData.forks_count).toFixed(2);
          break;
        case 'contributions':
          value = userData.contributions || 'N/A';
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
  
    //Possible output: 
    /* 
        GitHub User Report for mouredev:
            Most Used Language: N/A
            Number of Repositories: 47
            Followers/Following: 13050.00
            Stars/Forks: NaN
            Contributions: N/A
    */