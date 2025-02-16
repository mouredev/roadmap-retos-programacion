/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 */




/*fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al realizar la petición: ' + response.status 
                + ' ' + response.statusText) ;
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.log('Error: ' + error);
    });
*/

/* DIFICULTAD EXTRA (opcional):
* Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
* terminal al que le puedas solicitar información de un Pokémon concreto
* utilizando su nombre o número.
* - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
* - Muestra el nombre de su cadena de evoluciones
* - Muestra los juegos en los que aparece
* - Controla posibles errores
*/
const readline = require("readline"); // Importar el módulo readline, que permite leer datos del usuario
const rl = readline.createInterface({ // Crear una interfaz de lectura
    input: process.stdin, // Establecer la entrada de la interfaz
    output: process.stdout // Establecer la salida de la interfaz
});


function getPokemon(pokemon) {
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al realizar la petición: ' + response.status 
                    + ' ' + response.statusText) ;
            }
            return response.json();
        })
        .then(data => {
            console.log(`Nombre: ${data.name}`);
            console.log(`ID: ${data.id}`);
            console.log(`Peso: ${data.weight}`);
            console.log(`Altura: ${data.height}`);
            console.log('Tipos:');
            data.types.forEach(type => {
                console.log(`- ${type.type.name}`);
            });
            return fetch(data.species.url);
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al realizar la petición: ' + response.status 
                    + ' ' + response.statusText) ;
            }
            return response.json();
        })
        .then(data => {
            console.log(`Cadena de evolución: ${data.evolves_from_species ? data.evolves_from_species.name : 'Ninguna'}`);
            return fetch(data.varieties[0].pokemon.url);
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al realizar la petición: ' + response.status 
                    + ' ' + response.statusText) ;
            }
            return response.json();
        })
        .then(data => {
            console.log('Juegos en los que aparece:');
            data.game_indices.forEach(game => {
                console.log(`- ${game.version.name}`);
            });
        })
        .catch(error => {
            console.log('Error: ' + error);
        });
}
rl.question("Introduce el nombre o número de un Pokémon: ", function(pokemon) {
    getPokemon(pokemon);
    rl.close();
});// Cerrar la interfaz de lectura cuando se introduce un Pokémon




