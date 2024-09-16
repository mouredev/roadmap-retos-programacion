const apiPokemon = "https://pokeapi.co/api/v2/pokemon";

// async function callApi(url) {
//   try {
//     const res = await fetch(url);
//     const data = await res.json();
//     console.log(data);
//     console.log('llamado de api')
//   } catch (error) {
//     console.log(error)
//   }
// }
// getAPokemon()

// callApi(apiPokemon);

// -------- extra
// * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
//  * terminal al que le puedas solicitar información de un Pokémon concreto
// * utilizando su nombre o número.
// * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
// * - Muestra el nombre de su cadena de evoluciones
// * - Muestra los juegos en los que aparece
// * - Controla posibles errores

async function getAPokemon(num) {
  try {
    const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${num}`);
    const data = await res.json();
    console.log("el nombre de mi pokemon es : " + data.name);
    console.log("el id de mi pokemon es : " + data.id);
    console.log("el peso de mi pokemon es : " + data.weight);
    const typesPokemon = data.types.map((tipe) => tipe.type.name);
    console.log("Tipos : " + typesPokemon);
    const games = data.game_indices.map((game) => game.version.name);
    console.log("Juegos: ", games);
    // console.log(data.evolution_chain.url) undefined
    // ---------------------------
    const res1 = await fetch(
      `https://pokeapi.co/api/v2/pokemon-species/${num}`
    );
    const data1 = await res1.json();
    const res2 = await fetch(data1.evolution_chain.url);
    const data2 = await res2.json();
    const chain = data2.chain

    function getElvolves (chain) {
      console.log(chain["species"]["name"] + ' : evoluciona a ')
      if(chain.evolves_to[0] === undefined){
        console.log( 'No tiene evoluciones')
      }else{
        for (const evol of chain.evolves_to) {
          getElvolves(evol)

        }
        
      }
    }

    getElvolves(chain)

    // console.log(chain.evolves_to[0].species.name)
    // console.log(chain.evolves_to[0].evolves_to[0].species.name)
     
    
  } catch (error) {
    console.error("Error al obtener el Pokémon:", error);
  }
}
//numero de 1 al 1302
getAPokemon(1);
getAPokemon(132);


// https://pokeapi.co/api/v2/evolution-chain/1/

// {
//
//     "chain":
//    {
//
//
//           "evolves_to": [
//             {
//
//
//               "is_baby": false,
//               "species": {
//                 "name": "venusaur",
//                 "url": "https://pokeapi.co/api/v2/pokemon-species/3/"
//               }
//             }
//           ],
//           "is_baby": false,
//           "species": {
//             "name": "ivysaur",
//             "url": "https://pokeapi.co/api/v2/pokemon-species/2/"
//           }
//         }
//       ],
//       "is_baby": false,
//       "species": {
//         "name": "bulbasaur",
//         "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
//       }
//     },
//     "id": 1
//   }
