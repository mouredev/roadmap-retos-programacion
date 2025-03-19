// #20 PETICIONES HTTP

/**
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 */

// Usando modulos de nodejs
import https from 'node:https';
const URL = 'https://info.cern.ch/hypertext/WWW/TheProject.html';

https
	.get(URL, (res) => {
		const data = [];
		const headerDate =
			res.headers && res.headers.date ? res.headers.date : 'no response date';
		console.log('Status Code:', res.statusCode);
		console.log('Date in Response header:', headerDate);
		res.on('data', (chunk) => {
			data.push(chunk);
		});
		if (res.statusCode === 200) {
			res.on('end', () => {
				const body = Buffer.concat(data).toString();
				console.log('Body:', body);
			});
		}
	})
	.on('error', (err) => {
		console.log('Error: ', err.message);
	});

/**
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */

import readline from 'node:readline';

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const API = 'https://pokeapi.co/api/v2/pokemon/';
const API_SPECIES = 'https://pokeapi.co/api/v2/pokemon-species/';

rl.question('What pokemon do you want? ', (answer) => {
	const reqPokemon = API + answer.toLowerCase();
	const reqSpecies = API_SPECIES + answer.toLowerCase();

	getPokemon(reqPokemon, answer);
	getEvolChainURL(reqSpecies, answer);

	rl.close();
});

function getPokemon(req, id) {
	fetch(req, { method: 'GET' })
		.then((response) => {
			if (response.status !== 200) {
				console.log(`${response.status} - ${id} isn't a pokemon`);
				return null;
			} else {
				console.log('Status Code:', response.status);
				return response.json();
			}
		})
		.then((data) => {
			if (data) {
				getInfo(data);
				getGames(data);
			}
		});
}

function getEvolChainURL(req, id) {
	fetch(req, { method: 'GET' })
		.then((response) => {
			if (response.status !== 200) {
				console.log(`${response.status} - ${id} isn't a pokemon species`);
				return null;
			} else {
				return response.json();
			}
		})
		.then((data) => {
			if (data) {
				showEvolChain(data.evolution_chain.url);
			}
		});
}

function showEvolChain(data) {
	fetch(data, { method: 'GET' })
		.then((response) => {
			if (response.status !== 200) {
				console.log(`${response.status} something went wrong`);
				return null;
			} else {
				return response.json();
			}
		})
		.then((data) => {
			if (data) {
				console.log('Evolutions: ');
				searchEvol(data.chain);
			}
		});
}

function searchEvol(chain) {
	console.log(chain.species.name);
	if (chain.evolves_to) {
		for (let evo in chain.evolves_to) {
			searchEvol(chain.evolves_to[evo]);
		}
	}
}

function getInfo(data) {
	const { name, id, weight, height, types } = data;
	const typesNames = types.map((type) => type.type.name).join(' - ');
	console.log(`Name: ${name}`);
	console.log(`ID: ${id}`);
	console.log(`Weight: ${weight}`);
	console.log(`Height: ${height}`);
	console.log(`Types: ${typesNames}`);
}

function getGames(data) {
	const { game_indices } = data;
	const games = game_indices.map((game) => game.version.name).join(', ');
	console.log(`Games: ${games}`);
}
