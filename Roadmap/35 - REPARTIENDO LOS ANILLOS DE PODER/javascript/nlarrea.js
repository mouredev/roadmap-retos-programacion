/**
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */

const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

function isEven(number) {
	return number % 2 === 0;
}

function isPrime(number) {
	if (number < 2) {
		return false;
	}

	const range = Array.from('x'.repeat(number - 2), (_, i) => 2 + i);
	for (const n of range) {
		if (number % parseInt(n) === 0) {
			return false;
		}
	}

	return true;
}

function oddNumbers(number) {
	const range = Array.from('x'.repeat(number - 1), (_, i) => 1 + i);
	return range.filter((n) => !isEven(n));
}

function evenNumbers(number) {
	const range = Array.from('x'.repeat(number - 1), (_, i) => 1 + i);
	return range.filter((n) => isEven(n));
}

function combineOptions(totalRings) {
	const solution = [];

	// Give one ring to Sauron
	totalRings--;

	// Get possible values for the rest of the races
	for (const man of evenNumbers(totalRings)) {
		for (const elf of oddNumbers(totalRings)) {
			const dwarf = totalRings - elf - man;
			if (dwarf > 0 && isPrime(dwarf)) {
				solution.push({
					elfos: elf,
					enanos: dwarf,
					hombres: man,
					sauron: 1,
				});
			}
		}
	}

	return solution;
}

function printResult(results) {
	if (results.length === 0) {
		console.log('No se ha encontrado ninguna solución.');
		return;
	}

	let counter = 1;
	while (results.length > 0) {
		const result = results.shift();

		console.log(`\nSOLUCIÓN ${counter}:`);
		for (const race in result) {
			console.log(
				`${race[0].toUpperCase() + race.slice(1)}: ${result[race]}`
			);
		}
		counter++;
	}
}

function run() {
	rl.question(
		'Introduce la cantidad de anillos a repartir:\n > ',
		(rings) => {
			const totalRings = parseInt(rings, 10);

			const results = combineOptions(totalRings);
			printResult(results);

			rl.close();
		}
	);
}

run();
