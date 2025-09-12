// Autor: Héctor Adán 
// GitHub: https://github.com/hectorio23

// Realiza una petición HTTP a un sitio web de ejemplo
fetch('https://www.example.com')
    .then(response => {
        // Verifica si la respuesta es exitosa
        if (!response.ok) {
            // Lanza un error si la respuesta no es exitosa
            throw new Error('Network response was not ok ' + response.statusText);
        }
        // Convierte la respuesta en texto
        return response.text();
    })
    .then(data => {
        // Muestra el contenido de la web en la consola
        console.log(data);
    })
    .catch(error => {
        // Maneja cualquier error que ocurra durante la petición
        console.error('There was a problem with the fetch operation:', error);
    });

// Función para obtener datos de una URL dada
async function fetchData(url) {
    try {
        // Realiza la petición HTTP a la URL especificada
        const response = await fetch(url);
        // Verifica si la respuesta es exitosa
        if (!response.ok) {
            // Lanza un error si la respuesta no es exitosa
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        // Convierte y devuelve la respuesta en formato JSON
        return await response.json();
    } catch (error) {
        // Maneja cualquier error que ocurra durante la petición
        console.error('There was a problem with the fetch operation:', error);
        return null;
    }
}

// Función para imprimir los detalles del Pokémon
async function printPokemonDetails(pokemon) {
    // Imprime el nombre, ID, altura y peso del Pokémon
    console.log(`Name: ${pokemon.name}`);
    console.log(`ID: ${pokemon.id}`);
    console.log(`Height: ${pokemon.height}`);
    console.log(`Weight: ${pokemon.weight}`);

    // Imprime los tipos del Pokémon
    console.log('Types:');
    pokemon.types.forEach(type => {
        console.log(`- ${type.type.name}`);
    });

    // Obtiene e imprime la cadena de evoluciones
    const speciesData = await fetchData(pokemon.species.url);
    if (speciesData) {
        const evolutionChainUrl = speciesData.evolution_chain.url;
        const evolutionData = await fetchData(evolutionChainUrl);
        if (evolutionData) {
            console.log('Evolution Chain:');
            let currentEvolution = evolutionData.chain;
            while (currentEvolution) {
                console.log(`- ${currentEvolution.species.name}`);
                currentEvolution = currentEvolution.evolves_to[0];
            }
        }
    }

    // Imprime los juegos en los que aparece el Pokémon
    console.log('Games:');
    pokemon.game_indices.forEach(game => {
        console.log(`- ${game.version.name}`);
    });
}

// Función principal
async function main() {
    // Parte 1: Realizar una petición HTTP a un sitio web de ejemplo
    try {
        // Realiza la petición HTTP a la URL especificada
        const exampleResponse = await fetch('https://www.example.com');
        // Verifica si la respuesta es exitosa
        if (!exampleResponse.ok) {
            // Lanza un error si la respuesta no es exitosa
            throw new Error(`Network response was not ok: ${exampleResponse.statusText}`);
        }
        // Convierte la respuesta en texto
        const exampleData = await exampleResponse.text();
        // Muestra el contenido de la web en la consola
        console.log(exampleData);
    } catch (error) {
        // Maneja cualquier error que ocurra durante la petición
        console.error('There was a problem with the fetch operation:', error);
    }

    // Parte 2: Interacción con la PokéAPI
    // Solicita al usuario que ingrese el nombre o ID de un Pokémon
    const pokemonNameOrId = prompt('Enter the name or ID of the Pokémon:');
    // Construye la URL de la API utilizando el nombre o ID del Pokémon
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemonNameOrId}`;
    // Obtiene los datos del Pokémon desde la API
    const pokemonData = await fetchData(url);
    if (pokemonData) {
        // Imprime los detalles del Pokémon si los datos son válidos
        await printPokemonDetails(pokemonData);
    } else {
        // Muestra un mensaje de error si no se pudieron obtener los datos del Pokémon
        console.error('Error fetching Pokémon data. Please check the name or ID and try again.');
    }
}

// Ejecuta la función principal
main();
