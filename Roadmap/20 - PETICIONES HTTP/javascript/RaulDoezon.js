// https://kinsta.com/es/base-de-conocimiento/javascript-peticion-http/
// https://lenguajejs.com/javascript/peticiones-http/ajax/

/*
  EJERCICIO:
  Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
  una petición a la web que tú quieras, verifica que dicha petición
  fue exitosa y muestra por consola el contenido de la web.
*/

fetch("https://digi-api.com/api/v1/digimon/202")
  .then((response) => {
    return response.ok ? response.json() : Promise.reject(response);
  })
  .then((json) => {
    console.log("+++++++++ PETICIÓN DE EJEMPLO +++++++++");
    console.log("La petición fue exitosa. Se muestra la información obtenida sobre ¡WAR GREYMON!");
    console.log(json);
  })
  .catch((error) => {
    console.log(error);
  });
/*
  DIFICULTAD EXTRA (opcional):
  Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
  terminal al que le puedas solicitar información de un Pokémon concreto
  utilizando su nombre o número.
  - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
  - Muestra el nombre de su cadena de evoluciones
  - Muestra los juegos en los que aparece
  - Controla posibles errores
*/

async function getData(id) {
  try {
    let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
    let information = await response.json();

    console.log("\n+++++++++ POKÉAPI +++++++++");
    console.log(information);

    console.log(`NAME: ${information.name}`);
    console.log(`ID: ${information.id}.`);
    console.log(`HEIGHT: ${information.height}.`);
    console.log("TYPE(S):");

    for (const type of information.types) {
      console.log(`- ${type.type.name}.`);
    }

    console.log("VIDEO GAMES:");

    for (const games of information.game_indices) {
      console.log(`- ${games.version.name}.`);
    }
  } catch (error) {
    console.log(error);
  }

  try {
    let speciesResponse = await fetch(`https://pokeapi.co/api/v2/evolution-chain/${id}`);
    let pokemonSpecies = await speciesResponse.json();

    console.log(`ESPECIES:`);

    function allEvolutions(evolution) {
      if ("evolves_to" in evolution) {
        for (const evolve of evolution.evolves_to) {
          console.log(`- ${evolve.species.name}`);

          return allEvolutions(evolve);
        }
      }
    }

    allEvolutions(pokemonSpecies.chain);
  } catch (error) {
    
  }
}

const whatPokemon = prompt("Por favor, ingresa el ID del Pokémon que quieres revisar:");

async function getPokemon() {
  switch (whatPokemon) {
    case '':
      alert("Debes ingresar un número.");
      break;
  
    default:
      await getData(whatPokemon);
      break;
  }
}

getPokemon();
