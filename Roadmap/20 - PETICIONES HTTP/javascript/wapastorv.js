/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 */




fetch('https://jsonplaceholder.typicode.com/posts/1')
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

/* DIFICULTAD EXTRA (opcional):
* Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
* terminal al que le puedas solicitar información de un Pokémon concreto
* utilizando su nombre o número.
* - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
* - Muestra el nombre de su cadena de evoluciones
* - Muestra los juegos en los que aparece
* - Controla posibles errores
*/

function getPokemon(pokemon) {
    fetch(`https://pokeapi.co/api/v2/ability/${pokemon}/`)
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
}
console.log('Digite el nombre de un pokemon');
let pokemon = ReadableByteStreamController;
getPokemon('charmander');
getPokemon('pikachu');
getPokemon('bulbasaur');


