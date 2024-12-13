const id: number = 10;
const urljson: string = `https://jsonplaceholder.typicode.com/posts/${id}`;

fetch(urljson)
.then((response: Response) => {
    if (!response.ok) {
        throw new Error("Request error: " + response.status);
    }
    return response.json();
})
.then((data: any) => {
    console.log(data);
})
.catch((error: Error) => {
    console.error("There was a problem with the request Fetch:", error);
});

// ** Extra Exercise ** //

interface PokemonType {
    type: {
        name: string;
    };
}

interface PokemonData {
    forms: { name: string }[];
    name: string;
    id: number;
    weight: number;
    height: number;
    types: PokemonType[];
    species: {
        url: string;
    };
    game_indices: {
        version: {
            name: string;
        };
    }[];
}

interface EvolutionChain {
    species: {
        name: string;
    };
    evolves_to: EvolutionChain[];
}

async function getPokemonInfo(pokemon: string): Promise<void> {
    try {
        const response: Response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon.toLowerCase()}`);
        const pokemonData: PokemonData = await response.json();

        console.log('Pokemon data:', pokemonData.forms[0]["name"]);
        console.log('Name:', pokemonData.name);
        console.log('ID:', pokemonData.id);
        console.log('Weight:', pokemonData.weight);
        console.log('Height:', pokemonData.height);
        console.log('Types:');
        pokemonData.types.forEach((type: PokemonType) => {
            console.log('-', type.type.name);
        });

        const speciesResponse: Response = await fetch(pokemonData.species.url);
        const speciesData: any = await speciesResponse.json();
        const evolutionChainUrl: string = speciesData.evolution_chain.url;
        const evolutionChainResponse: Response = await fetch(evolutionChainUrl);
        const evolutionChainData: { chain: EvolutionChain } = await evolutionChainResponse.json();

        console.log('Evolution chain:');
        let evolutionChain: EvolutionChain | null = evolutionChainData.chain;
        while (evolutionChain) {
            console.log('-', evolutionChain.species.name);
            evolutionChain = evolutionChain.evolves_to[0] || null;
        }

        console.log('Games in which it appears:');
        pokemonData.game_indices.forEach(game => {
            console.log('-', game.version.name);
        });

    } catch (error) {
        console.error('Error:', error.message);
    }
}

const pokemon: string = '3'; 
getPokemonInfo(pokemon);
