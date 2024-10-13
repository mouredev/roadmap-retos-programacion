const prompt = require('prompt-sync')();

//Ejecicio

const url = 'https://api.coindesk.com/v1/bpi/currentprice.json';

async function showResponse() {
  await fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
    }
  )
  .then(data => console.log(`La cotización del bitcoin es: ${data.bpi.USD.rate_float}$`))
  .catch(error=> console.log(error));
}

//showResponse();

//Extra

let pokemon = prompt('Nombre del pokemon: ', '').toLowerCase();

const pokeApiUrl = `https://pokeapi.co/api/v2/pokemon/${pokemon}/`;
let pokemonName;
fetch(pokeApiUrl)
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error, pokemon no encontrado! Status: ${response.status}`);
  }
  return response.json();
  }
)
.then(data => {
  pokemonName = data;
})
.then(() => {
  console.log(`Nombre: ${pokemonName.species.name}, \nId: ${pokemonName.id}, \nPeso: ${pokemonName.weight}, \nAltura: ${pokemonName.height}`);
})
.then(() => {
  console.log('Tipo(s):');
  for (const key in pokemonName.types) {
    if (Object.hasOwnProperty.call(pokemonName.types, key)) {
      console.log(`${pokemonName.types[key].type.name}`);
    }
  }
})
.then(() => {
  const pokeApiUrlEvolutionChain = `https://pokeapi.co/api/v2/pokemon-species/${pokemon}/`;
  let pokemonEvolutionChainUrl;
  fetch(pokeApiUrlEvolutionChain)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error, Status: ${response.status} obteniendo evoluciones`);
    }
    return response.json();
    }
  )
  .then(data => {
    pokemonEvolutionChainUrl = data['evolution_chain']['url'];
  })
  .then(() => {
    fetch(pokemonEvolutionChainUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status} en busqueda de cadena de evolución`);
      }
      return response.json();
      }
    )
    .then(data => {
      console.log('Cadena de evolución:');
      let getEvolves = data => {
        console.log(data['species']['name']);
        if (data.hasOwnProperty('evolves_to')) {
          for (const iterator of data['evolves_to']) {
            getEvolves(iterator);
          }
        }
      }
      getEvolves(data['chain']);
    })
    .catch(error=> console.log(error))
  })
  .catch(error=> console.log(error))
})
.then(() => {
  console.log('Juegos:');
  for (const key in pokemonName.game_indices) {
    if (Object.hasOwnProperty.call(pokemonName.game_indices, key)) {
      console.log(`${pokemonName.game_indices[key].version.name}`);
    }
  }
})
.catch(error=> console.log(error))