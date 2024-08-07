/** #20 - JavaScript ->Jesus Antonio Escamilla */

const { error } = require("console");

/**
 * HTTP define un conjunto de métodos de petición para indicar la acción que se desea realizar para un recurso determinado.
 * La API Fetch proporciona una interfaz JavaScript para acceder y manipular partes del canal HTTP, tales como peticiones y respuestas.
 */

//---EJERCIÓ---
// URL donde se utilizara las peticiones
const url = 'https://jsonplaceholder.typicode.com/posts/1';

// Realizaron las peticiones HTTP
fetch(url)
    .then(response => {
        // Se checa la petición que se sea => 200 - OK
        if (!response.ok) {
            throw new Error('La respuesta de NETWORK no fue correcta' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Se muestra los datos de la url
        // console.log(data);
    })
    .catch(error => {
        console.error('Hubo un error con la peticiones fetch:', error);
    });



/**-----DIFICULTAD EXTRA-----*/

//  Se requiere esto para leer en la consola
const readline = require('node:readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
const baseURL = 'https://pokeapi.co/api/v2/pokemon';
const namePokemon = (texto) => {
    if (!isNaN(parseInt(texto))) {
        return texto;
    }
    return texto.toLowerCase();
}

//  El sistema Pokemon, "Pokedex"
const Pokedex = async (pokemon) => {
    try {
        //  URL del PokéAPI
        const response = await fetch(`${baseURL}/${namePokemon(pokemon)}`);
        if (!response.ok) {
            throw new Error('La respuesta de NETWORK no fue correcta: ' + response.statusText);
        }
        const pokemonData = await response.json();

        //  Se recorre los datos
        const { id, name, weight, height, types } = pokemonData;
        const typeNames = types.map(typeInfo => typeInfo.type.name);

        //  Se muestra los datos
        console.log(`Nombre: ${name}`);
        console.log(`ID: ${id}`);
        console.log(`Peso: ${weight}`);
        console.log(`Altura: ${height}`);
        console.log(`Tipo(s): ${typeNames.join(', ')}`);

        //  Encontramos la especie del Pokemon
        const speciesResponse = await fetch(pokemonData.species.url);
        if (!speciesResponse.ok) {
            throw new Error('La respuesta de NETWORK no fue correcta' + response.statusText);
        }
        const speciesData = await speciesResponse.json();
        
        //  Obteniendo la cadena de evolución
        const evolutionResponse = await fetch(speciesData.evolution_chain.url);
        if (!evolutionResponse.ok) {
            throw new Error('La respuesta de NETWORK no fue correcta' + response.statusText);
        }
        const evolutionData = await evolutionResponse.json();

        //  Se muestro la evolución del pokemon
        const evolutionNames = [];
        let currentEvolution = evolutionData.chain;
        do {
            evolutionNames.push(currentEvolution.species.name);
            currentEvolution = currentEvolution.evolves_to[0];
        } while (currentEvolution);
        console.log(`Cadena de evoluciones: ${evolutionNames.join(' -> ')}`);

        //  En los juegos que se encuentra
        const gameIndices = pokemonData.game_indices.map(gameIndex => gameIndex.version.name);
        console.log(`Aparece en los juegos: ${gameIndices.join(', ')}`);

    } catch (error) {
        console.error('Se encontró error:', error);
    }
};

rl.question('¿Nombre o Numero de Pokemon? ', nameNumber => {
    Pokedex(nameNumber);
    rl.close();
});

/**-----DIFICULTAD EXTRA-----*/