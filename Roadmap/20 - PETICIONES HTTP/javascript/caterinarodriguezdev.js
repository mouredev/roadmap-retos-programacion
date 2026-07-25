/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */

fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
  .then((resp) => {
    return resp.json();
  })
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });

const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

rl.question(
  "Dame el nombre de un Pokemon y te diré lo que sé de él -> ",
  (resp) => {
    const pokemon = resp;

    fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`)
      .then((resp) => {
        if (resp.status === 404) {
          console.log("No se ha encontrado el nombre del pokemon");
          return;
        }
        return resp.json();
      })
      .then( async (data) => {
        if (data != undefined) {
          console.log(
            `Nombre: ${data.name}, id: ${data.id}, peso: ${data.weight}, altura: ${data.height}`
          );
          console.log("Tipos:");
          data.types.forEach((type) => {
            console.log("-", type.type.name);
          });
          console.log('Juegos en los que aparece:');
          data.game_indices.forEach(game => {
              console.log('-', game.version.name);
          });  

          const speciesResponse = await fetch(data.species.url);
          const speciesData = await speciesResponse.json();
          const evolutionChainUrl = speciesData.evolution_chain.url;
          const evolutionChainResponse = await fetch(evolutionChainUrl);
          const evolutionChainData = await evolutionChainResponse.json();
  
          console.log('Cadena de evolución:');
          let evolutionChain = evolutionChainData.chain;
          while (evolutionChain) {
              console.log('-', evolutionChain.species.name);
              evolutionChain = evolutionChain['evolves_to'][0];
          }
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }
);
