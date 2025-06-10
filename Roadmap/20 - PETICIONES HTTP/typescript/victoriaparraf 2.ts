import axios from 'axios';

async function fetchWebContent(url: string): Promise<void> {
    try {
        const response = await axios.get(url);
        console.log('Status:', response.status);
        console.log('Headers:', response.headers);
        console.log('Data:', response.data);
    } catch (error) {
        console.error('Error fetching the web content:', error);
    }
}

// Llamada a la función con una URL de ejemplo
fetchWebContent('https://wattpad.com');

/************************************************************/

interface Pokemon {
    name: string;
    id: number;
    weight: number;
    height: number;
    types: Array<{ type: { name: string } }>;
    species: { url: string };
    game_indices: Array<{ version: { name: string } }>;
}

interface EvolutionChain {
    chain: {
        species: { name: string };
        evolves_to: Array<any>;
    };
}

async function getPokemonInfo(identifier: string | number): Promise<void> {
    try {
        const response = await axios.get<Pokemon>(`https://pokeapi.co/api/v2/pokemon/${identifier}`);
        const pokemon = response.data;

        console.log(`Name: ${pokemon.name}`);
        console.log(`ID: ${pokemon.id}`);
        console.log(`Weight: ${pokemon.weight}`);
        console.log(`Height: ${pokemon.height}`);
        console.log('Types:', pokemon.types.map(type => type.type.name).join(', '));

        // Get evolution chain
        const speciesResponse = await axios.get<{ evolution_chain: { url: string } }>(pokemon.species.url);
        const evolutionResponse = await axios.get<EvolutionChain>(speciesResponse.data.evolution_chain.url);
        const evolutionChain = evolutionResponse.data.chain;
        
        const evolutionNames: string[] = [];
        let current = evolutionChain;
        while (current) {
            evolutionNames.push(current.species.name);
            current = current.evolves_to[0];
        }
        console.log('Evolution Chain:', evolutionNames.join(' -> '));

        // Get game appearances
        console.log('Games:', pokemon.game_indices.map(game => game.version.name).join(', '));
    } catch (error) {
        console.error('Error fetching Pokémon information:', error);
    }
}

// Llamada a la función con un nombre o número de Pokémon
getPokemonInfo('pikachu'); // Puedes usar el nombre o el número del Pokémon
getPokemonInfo(1); // También puedes usar el número del Pokémon


