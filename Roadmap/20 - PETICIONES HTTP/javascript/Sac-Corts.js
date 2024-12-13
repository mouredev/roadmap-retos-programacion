const id = 10;
const urljson = `https://jsonplaceholder.typicode.com/posts/${id}`;

fetch(urljson)
  .then(response => {
    if (!response.ok) {
      throw new Error("Request error: " + response.status);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error("There was a problem with the request Fetch:", error);
  });

// Extra Exercise //

async function getPokemonInfo(pokemon) {
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon.toLowerCase()}`);
        const pokemonData = await response.json();

        console.log('Pokemon data:', pokemonData.forms[0]["name"]);

        console.log('Name:', pokemonData.name);

        console.log('ID:', pokemonData.id);

        console.log('Weight:', pokemonData.weight);

        console.log('Height:', pokemonData.height);

        console.log('Types:');
        pokemonData.types.forEach(type => {
            console.log('-', type.type.name);
        });

        const speciesResponse = await fetch(pokemonData.species.url);
        const speciesData = await speciesResponse.json();
        const evolutionChainUrl = speciesData.evolution_chain.url;
        const evolutionChainResponse = await fetch(evolutionChainUrl);
        const evolutionChainData = await evolutionChainResponse.json();

        console.log('Evolution chain:');
        let evolutionChain = evolutionChainData.chain;
        while (evolutionChain) {
            console.log('-', evolutionChain.species.name);
            evolutionChain = evolutionChain['evolves_to'][0];
        }

        console.log('Games in which it appears:');
        pokemonData.game_indices.forEach(game => {
            console.log('-', game.version.name);
        });

    } catch (error) {
        console.error('Error:', error.message);
    }
}

const pokemon = '3'; 
getPokemonInfo(pokemon);

// Thanks to cesar-ch