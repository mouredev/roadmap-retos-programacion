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

async function getPokeData(id) {
	let baseUrl = 'https://pokeapi.co/api/v2/pokemon/';
	await fetch(`${baseUrl}/${id}`)
		.then((response) => response.json())
		.then((data) => {
			console.log(`Nombre: ${data.name}`);
			console.log(`Id: ${data.id}`);
			console.log(`Peso: ${data.weight}`);
			console.log(`Altura: ${data.height}`);
			console.log(`Tipo(s): ${data.types.map((type) => type.type.name)}`);
			console.log(
				`Juegos: ${data.game_indices.map((game) => game.version.name)}`
			);
		})
		.catch((error) => console.log(error));

	// await fetch(`https://pokeapi.co/api/v2/evolution-chain/${id}`)
	// 	.then((response) => response.json())
	// 	.then((data) => {
	// 		console.log(data);
	// 	})
	// 	.catch((error) => console.log(error));
}

getPokeData(495);
