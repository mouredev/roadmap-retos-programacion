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

const pokeApiUrl = 'https://pokeapi.co/api/v2/pokemon/ditto';
let pokemonName;
fetch(pokeApiUrl)
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
  return response.json();
  }
)
.then(data => {
  pokemonName = data;
})
.then(() => {
  console.log(pokemonName.species.name);
})
.catch(error=> console.log(error))