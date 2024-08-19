//EJERCICIO
function getAbradolfLincler() {
	let url = 'https://rickandmortyapi.com/api/character/7';
	fetch(url)
	.then((response) => response.json())
	.then((data) => {
		console.log(data);
	})
	.catch((error) => console.log(error));
}

//EXTRA
const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

async function getPokeData(id) {
	let baseUrl = 'https://pokeapi.co/api/v2/pokemon/';
	let speciesUrl;
	let chainUrl;

	try {
		await fetch(`${baseUrl}/${id.toLowerCase()}`)
			.then((response) => response.json())
			.then((data) => {
				console.log(`\nName: ${data.name}`);
				console.log(`Id: ${data.id}`);
				console.log(`Weight: ${data.weight}`);
				console.log(`Height: ${data.height}`);
				console.log(`Type: ${data.types.map((type) => type.type.name)}`);
				console.log('Games: ');
				let gamesArr = data.game_indices.map((game) => game.version.name);
				gamesArr.forEach((element) => {
					console.log(`* ${element}`);
				});
				speciesUrl = data.species.url;
			});

		await fetch(speciesUrl)
			.then((response) => response.json())
			.then((data) => {
				chainUrl = data.evolution_chain.url;
			});

		await fetch(chainUrl)
			.then((response) => response.json())
			.then((data) => {
				let evolves = data.chain.evolves_to;
				let first = data.chain.species;
				let second = evolves.map((name) => name.species.name);
				let third = evolves[0].evolves_to.map((name) => name.species.name);
				console.log(`Evolution chain:\n${first.name} => ${second} => ${third}`);
			});
	} catch (err) {
		console.log(`\nHa ocurrido un error: ${err}`);
	}
}

function requestPokemon() {
	rl.question(
		'\nIngrese la ID o el nombre de su pokemon. Enter para salir\n',
		async (id) => {
			switch (id) {
				case '':
					console.log('Cerrando aplicación...');
					rl.close();
					break;
				default:
					await getPokeData(id);
					requestPokemon();
					break;
			}
		}
	);
}

requestPokemon();
