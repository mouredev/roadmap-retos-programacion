/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */

async function fetchData() {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    const data = await response.json();
    console.log(data);
}

// fetchData();
/* prints:
{
  userId: 1,
  id: 1,
  title: 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
  body: 'quia et suscipit\n' +
    'suscipit recusandae consequuntur expedita et cum\n' +
    'reprehenderit molestiae ut ut quas totam\n' +
    'nostrum rerum est autem sunt rem eveniet architecto'
}
*/


/*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */


const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function getPokemon(pokemon) {
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`);
        
        if (!response.ok) {
            throw new Error('Data not found.');
        }

        const data = await response.json();
        return data;
    } catch(err) {
        console.error(err);
    }
}

function askPokemon() {
    rl.question('Enter a Pokémon name or Id:\n> ', (pokemon) => {
        getPokemon(pokemon)
        .then(data => {
            if (!data) {
                return;
            }

            const {name, weight, height, types} = data;

            console.log('\nName:', name?.charAt(0).toUpperCase() + name?.slice(1));
            console.log('Pokémon Id:', data?.id);
            console.log('Pokémon weight:', weight);
            console.log('Pokémon height:', height);
            console.log('Pokémon type(s):');
            types?.forEach(({slot, type}) => {
                console.log(`  ${slot}.`, type?.name);
            });
        });
        rl.close();
    });
}

askPokemon();