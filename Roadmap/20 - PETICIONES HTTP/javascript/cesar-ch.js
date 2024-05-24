/*
    * 20 PETICIONES HTTP 
*/

/*
    * DIFICULTAD EXTRA
*/
async function getPokemonInfo(pokemon) {
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon.toLowerCase()}`);
        const pokemonData = await response.json();

        console.log('Datos del pokemon:', pokemonData.forms[0]["name"]);
        // Nombre
        console.log('Nombre:', pokemonData.name);

        // ID
        console.log('ID:', pokemonData.id);

        // Peso
        console.log('Peso:', pokemonData.weight);

        // Altura
        console.log('Altura:', pokemonData.height);

        // Tipos
        console.log('Tipos:');
        pokemonData.types.forEach(type => {
            console.log('-', type.type.name);
        });

        // Cadena de evolución
        const speciesResponse = await fetch(pokemonData.species.url);
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

        // Juegos en los que aparece
        console.log('Juegos en los que aparece:');
        pokemonData.game_indices.forEach(game => {
            console.log('-', game.version.name);
        });

    } catch (error) {
        console.error('Error:', error.message);
    }
}

const pokemon = 'pikachu'; 
getPokemonInfo(pokemon);
