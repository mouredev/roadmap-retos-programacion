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
  console.log(`Nombre: ${pokemonName.species.name}, \nId: ${pokemonName.id}, \nPeso: ${pokemonName.weight}, \nAltura: ${pokemonName.height}, \nCadena de evoluciones: ${pokemonName}`);
})
.then(() => {
  console.log('Tipo(s):');
  for (const key in pokemonName.types) {
    if (Object.hasOwnProperty.call(pokemonName.types, key)) {
      console.log(`${pokemonName.types[key].type.name}`);
      
    }
  }
})
.catch(error=> console.log(error))