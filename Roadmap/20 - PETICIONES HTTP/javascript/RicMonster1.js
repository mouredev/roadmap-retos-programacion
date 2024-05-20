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

//EJERCICIO
/*
let url = 'https://rickandmortyapi.com/api/character/7';
fetch(url)
	.then((response) => response.json())
	.then((data) => {
		console.log(data);
	})
	.catch((error) => console.log(error));
*/
const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

async function getPokeData(id) {
	let baseUrl = 'https://pokeapi.co/api/v2/pokemon/';
	let speciesUrl;
	let chainUrl;

	await fetch(`${baseUrl}/${id}`)
		.then((response) => response.json())
		.then((data) => {
			console.log(`Name: ${data.name}`);
			console.log(`Id: ${data.id}`);
			console.log(`Weight: ${data.weight}`);
			console.log(`Height: ${data.height}`);
			console.log(`Type: ${data.types.map((type) => type.type.name)}`);
			console.log('Games: ');
			data.game_indices
				.map((game) => game.version.name)
				.forEach((element) => {
					console.log(` *${element}`);
				});
			speciesUrl = data.species.url;
		})
		.catch((error) => console.log(error));

	await fetch(speciesUrl)
		.then((response) => response.json())
		.then((data) => {
			chainUrl = data.evolution_chain.url;
		})
		.catch((error) => console.log(error));

	await fetch(chainUrl)
		.then((response) => response.json())
		.then((data) => {
			console.log(data);
		})
		.catch((error) => console.log(error));
}

getPokeData('snivy');

rl.close();
