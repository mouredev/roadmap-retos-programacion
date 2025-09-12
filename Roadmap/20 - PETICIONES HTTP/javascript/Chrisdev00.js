// * EJERCICIO:
// * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
// * una petición a la web que tú quieras, verifica que dicha petición
// * fue exitosa y muestra por consola el contenido de la web.
// *
// * DIFICULTAD EXTRA (opcional):
// * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
// * terminal al que le puedas solicitar información de un Pokémon concreto
// * utilizando su nombre o número.
// * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
// * - Muestra el nombre de su cadena de evoluciones
// * - Muestra los juegos en los que aparece
// * - Controla posibles errores

fetch ("https://dummyapi.io/data/v1/user/", {
    headers: {
        "app-id": "62b0433d2dfd91d4bf56c584"
    }
})
.then(response => {
    if (response.ok) {
        return response.json();
    }else{
        throw new Error("La solicitud no fue exitosa codigo de estado." + response.status);
    }
})
.then(data => {
    var result = data.data[0];
    console.log(result);
})
.catch(error => {
    console.error("Error", error);
})


///////---------------------------------- EXTRA ---------------------------------------- /////////////

const fetch = require('node-fetch');
const { type } = require('os');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


function capitalize(str) {
    if (!str) return str; 
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

// Funcion para encontrar la cadena de evolucion

const getEvolutionChain = async(speciesUrl) => {
    try {
        const speciesResponse = await fetch(speciesUrl);
        if (!speciesResponse.ok) throw new Error(`Error al obtener species: ${speciesResponse.status}`);
        const speciesData = await speciesResponse.json();
        const evolutionChainUrl = speciesData.evolution_chain.url;

        const evolutionResponse = await fetch(evolutionChainUrl);
        if (!evolutionResponse.ok) throw new Error(`Error al obtener la cadena de evolución: ${evolutionResponse.status}`);
        const evolutionData = await evolutionResponse.json();

        const evolutionNames = [];
        let currentEvolution = evolutionData.chain;

        while(currentEvolution){
            evolutionNames.push(capitalize(currentEvolution.species.name));
            currentEvolution = currentEvolution.evolves_to[0];
        }

        return evolutionNames;

    } catch(error){
        console.error("Error:", error);
    }
}


// Preguntar al usuario por el ID o nombre del Pokémon

rl.question("Por favor, introduce el ID o nombre del Pokémon: ", async (idOrName) => {
  try{
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${idOrName}`);
    if (!response.ok) throw new Error(`La solicitud no fue exitosa. Código de estado: ${response.status}`);

    const data = await response.json();

    const {name, id, weight, height, types, species, game_indices} = data;
    const typesNames = types.map(typeInfo => capitalize(typeInfo.type.name));
    const gameNames = game_indices.map(game => capitalize(game.version.name));

    const evolutionChain = await getEvolutionChain(species.url);

    console.log(`Nombre del pokemon: ${capitalize(name)}`);
    console.log(`Id del pokemon: ${id}`);
    console.log(`Peso del pokemon: ${weight}`);
    console.log(`Altura del pokemon: ${height}`);
    console.log(`Tipo de pokemon: ${typesNames.join(', ')}`);
    console.log(`Cadena de evolucion: ${evolutionChain.join(' -> ')}`);
    console.log(`Juegos en los que aparece: ${gameNames.join(', ')}`);

  }catch(error){
    console.error("Error:", error);
  }finally{
    rl.close();
  }
});