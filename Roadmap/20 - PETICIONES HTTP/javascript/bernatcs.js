// ** EJERCICIO 

let url = 'https://bernatcucarella.com'

fetch(url)
  .then(response => response.text())
  .then(data => console.log(data))


// ** DIFICULTAD EXTRA ** ----------------------------------------------------------------------------------------------------------------------------------------------------

// const https = require('node:https');

// function obtenerInfoPokemon(nombreONumero) {
//   const url = `https://pokeapi.co/api/v2/pokemon/${nombreONumero.toLowerCase()}`;

//   https.get(url, (response) => {
//     let data = '';

//     // Recibir los datos en trozos
//     response.on('data', (chunk) => {
//       data += chunk;
//     });

//     // Cuando se termina de recibir la respuesta
//     response.on('end', () => {
//       if (response.statusCode === 200) {
//         try {
//           const pokemon = JSON.parse(data);

//           // Mostrar información del Pokémon
//           console.log(`Nombre: ${pokemon.name}`);
//           console.log(`ID: ${pokemon.id}`);
//           console.log(`Peso: ${pokemon.weight} kg`);
//           console.log(`Altura: ${pokemon.height * 10} cm`); // Altura en decímetros
//           console.log(`Tipos: ${pokemon.types.map(type => type.type.name).join(', ')}`);

//           // Obtener la cadena de evolución del Pokémon
//           obtenerCadenaEvolucion(pokemon.species.url);
//         } catch (error) {
//           console.error('Error al parsear la respuesta JSON:', error.message);
//         }
//       } else {
//         console.error(`Error al obtener información del Pokémon. Código de estado: ${response.statusCode}`);
//       }
//     });
//   }).on('error', (error) => {
//     console.error('Error al hacer la solicitud:', error.message);
//   });
// }

// function obtenerCadenaEvolucion(speciesUrl) {
//   https.get(speciesUrl, (response) => {
//     let data = '';

//     // Recibir los datos en trozos
//     response.on('data', (chunk) => {
//       data += chunk;
//     });

//     // Cuando se termina de recibir la respuesta
//     response.on('end', () => {
//       if (response.statusCode === 200) {
//         try {
//           const species = JSON.parse(data);
//           const evolutionChainUrl = species.evolution_chain.url;

//           // Obtener la cadena de evolución desde la URL de la cadena
//           https.get(evolutionChainUrl, (response) => {
//             let data = '';

//             // Recibir los datos en trozos
//             response.on('data', (chunk) => {
//               data += chunk;
//             });

//             // Cuando se termina de recibir la respuesta
//             response.on('end', () => {
//               if (response.statusCode === 200) {
//                 try {
//                   const evolutionChain = JSON.parse(data);
//                   const cadenaEvolucion = obtenerNombreCadenaEvolucion(evolutionChain.chain);
//                   console.log(`Cadena de Evolución: ${cadenaEvolucion}`);
//                 } catch (error) {
//                   console.error('Error al parsear la cadena de evolución:', error.message);
//                 }
//               } else {
//                 console.error(`Error al obtener la cadena de evolución. Código de estado: ${response.statusCode}`);
//               }
//             });
//           }).on('error', (error) => {
//             console.error('Error al hacer la solicitud de la cadena de evolución:', error.message);
//           });

//         } catch (error) {
//           console.error('Error al parsear la respuesta JSON:', error.message);
//         }
//       } else {
//         console.error(`Error al obtener información de la especie del Pokémon. Código de estado: ${response.statusCode}`);
//       }
//     });
//   }).on('error', (error) => {
//     console.error('Error al hacer la solicitud de la especie del Pokémon:', error.message);
//   });
// }

// function obtenerNombreCadenaEvolucion(chain) {
//   let cadena = '';
//   let currentPokemon = chain.species.name;

//   if (chain.evolves_to.length > 0) {
//     cadena += currentPokemon + ' -> ';
//     let nextChain = chain.evolves_to[0];
//     while (nextChain) {
//       cadena += nextChain.species.name + ' -> ';
//       nextChain = nextChain.evolves_to[0];
//     }
//     cadena = cadena.slice(0, -4); // Eliminar el último ' -> '
//   } else {
//     cadena = currentPokemon;
//   }

//   return cadena;
// }

// // Capturar el nombre o número del Pokémon desde la línea de comandos
// const nombreONumero = process.argv[2];

// if (!nombreONumero) {
//   console.error('Por favor, proporciona el nombre o número del Pokémon como argumento.');
// } else {
//   obtenerInfoPokemon(nombreONumero);
// }