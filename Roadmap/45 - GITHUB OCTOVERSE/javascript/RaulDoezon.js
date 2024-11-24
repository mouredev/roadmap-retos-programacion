/*
  EJERCICIO:
  GitHub ha publicado el Octoverse 2024, el informe
  anual del estado de la plataforma:
  https://octoverse.github.com
 
  Utilizando el API de GitHub, crea un informe asociado
  a un usuario concreto.
  
  - Se debe poder definir el nombre del usuario
    sobre el que se va a generar el informe.
    
  - Crea un informe de usuario basándote en las 5 métricas
    que tú quieras, utilizando la informración que te
    proporciona GitHub. Por ejemplo:
    - Lenguaje más utilizado
    - Cantidad de repositorios
    - Seguidores/Seguidos
    - Stars/forks
    - Contribuciones
    (lo que se te ocurra)
*/

const userName = prompt('Por favor, ingresa el nombre de usuario de GitHub que quieres consultar:');
const apiRequest = async () => {
  const apiURL = `https://api.github.com/users/${userName}`;
  const starredAPI = `${apiURL}/starred`;

  try {
    const [data1, data2] = await Promise.all([
      fetch(apiURL),
      fetch(starredAPI),
    ]);

    const dataBase = await data1.json();
    const dataStarred = await data2.json();

    console.log(`Informe del usuario ${dataBase.login}:`);
    console.log(`1. Fecha de creación de la cuenta: ${dataBase.created_at}`);
    console.log(`2. Número de repositorios públicos: ${dataBase.public_repos}`);
    console.log(`3. Número de estrellas: ${dataStarred.length}`);
    console.log(`4. Número de seguidores:  ${dataBase.followers}`);
    console.log(`5. Número de usuarios a los que sigue: ${dataBase.following}`);
  } catch (error) {
    console.log(error);
  }
}

apiRequest();
