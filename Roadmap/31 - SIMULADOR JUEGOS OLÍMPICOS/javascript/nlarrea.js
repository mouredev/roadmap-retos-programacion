/*
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
 */

const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

class Participant {
	constructor(name, country) {
		this.name = name;
		this.country = country;
	}

	equals(other) {
		if (other instanceof Participant) {
			return this.name === other.name && this.country === other.country;
		}

		return false;
	}

	hashCode(other) {
		return `${this.name} ${this.country}`.hashCode();
	}
}

class Olympics {
	constructor() {
		this.events = [];
		this.participants = {};
		this.results = {};
		this.countries = {};
	}

	addEvent() {
		rl.question('Introducir el nombre del evento:\n > ', (inputEvent) => {
			const event = inputEvent.trim();

			if (this.events.includes(event)) {
				console.log(
					`El evento '${event}' ya ha sido añadido anteriormente.`
				);
			} else {
				this.events.push(event);
				console.log(`El evento '${event}' ha sido añadido.`);
			}

			main();
		});
	}

	addParticipant() {
		if (this.events.length === 0) {
			console.log(
				'No existen eventos todavía. Espera a que haya alguno para inscribirte!'
			);
			return;
		}

		// Get participant's information
		rl.question(
			'Introduce el nombre del participante:\n > ',
			(inputName) => {
				const name = inputName.trim();

				rl.question(
					'Introduce el país del participante:\n > ',
					(inputCountry) => {
						const country = inputCountry.trim();
						const participant = new Participant(name, country);

						// Register the participant in an event
						console.log('\nMENÚ DE OPCIONES');
						console.log('----------------');
						for (const index in this.events) {
							console.log(
								`${parseInt(index) + 1}. ${
									this.events[parseInt(index)]
								}`
							);
						}
						rl.question(
							'Selecciona en qué evento deseas participar:\n > ',
							(eventChoice) => {
								const event =
									this.events[parseInt(eventChoice) - 1];

								if (!event) {
									console.log(
										`Debes introducir un número entre [1-${this.events.length}]!`
									);
								} else {
									if (
										Object.keys(
											this.participants
										).includes(event) &&
										this.participants[event].includes(
											participant
										)
									) {
										console.log(
											`El participante ${name} de ${country} ya está registrado en el evento deportivo ${event}`
										);
									} else {
										if (
											!Object.keys(
												this.participants
											).includes(event)
										) {
											this.participants[event] = [];
										}

										this.participants[event].push(
											participant
										);
										console.log(
											`El participante ${name} de ${country} se ha registrado en ${event}`
										);
									}
								}

								main();
							}
						);
					}
				);
			}
		);
	}

	simulate() {
		const randomSample = (list, quantity) => {
			const selectedItems = [];
			let listCopy = [...list];
			while (selectedItems.length < quantity) {
				// Update maxValue to match the length of the list
				let maxValue = listCopy.length;
				// Select a random index for the list -> [0, maxValue)
				const index = Math.floor(Math.random() * (maxValue - 0) + 0);
				// Remove the selected index and append that item to the selectedItems
				selectedItems.push(...listCopy.splice(index, 1));
			}
			return selectedItems;
		};

		if (this.events.length === 0) {
			console.log('Aún no hay eventos registrados');
			return;
		}

		for (const event of this.events) {
			if (
				!Object.keys(this.participants).includes(event) ||
				this.participants[event].length < 3
			) {
				console.log(
					`\nNo hay participantes suficientes para simular el evento '${event}'...`
				);
				continue;
			}

			// Get Gold, Silver and Bronze randomly
			const eventParticipants = randomSample(
				this.participants[event],
				3
			);

			const [gold, silver, bronze] = eventParticipants;
			const winners = { gold, silver, bronze };
			this.results[event] = winners;

			// Update each country's medal counter
			this.updateCountryResults(gold.country, 'gold');
			this.updateCountryResults(silver.country, 'silver');
			this.updateCountryResults(bronze.country, 'bronze');

			this.printResults(event, winners);
		}

		main();
	}

	writeSummary() {
		console.log('\nINFORME DE LOS JJOO');
		console.log('-------------------\n');

		if (!this.results) {
			console.log('No hay resultados registrados');
		} else {
			for (const event in this.results) {
				this.printResults(event, this.results[event]);
			}
		}

		if (!this.countries) {
			console.log('No hay medallas por país registradas');
		} else {
			console.log('RESULTADOS DEL EVENTO POR PAÍS:');
			for (const country in this.countries) {
				console.log(`${country}:`);
				console.log(`  ${this.countries[country].gold} Oro`);
				console.log(`  ${this.countries[country].silver} Plata`);
				console.log(`  ${this.countries[country].bronze} Bronce`);
			}
		}

		main();
	}

	updateCountryResults(country, medal) {
		if (!Object.keys(this.countries).includes(country)) {
			this.countries[country] = { gold: 0, silver: 0, bronze: 0 };
		}

		this.countries[country][medal] += 1;
	}

	printResults(event, winners) {
		console.log(`RESULTADOS DEL EVENTO:`, event);
		console.log(`Oro: ${winners.gold.name} (${winners.gold.country})`);
		console.log(
			`Plata: ${winners.silver.name} (${winners.silver.country})`
		);
		console.log(
			`Bronce: ${winners.bronze.name} (${winners.bronze.country})\n`
		);
	}
}

const jjoo = new Olympics();
function main() {
	const options = [
		'Registro de eventos',
		'Registro de participantes',
		'Simulación de eventos',
		'Creación de informes',
		'Salir del programa',
	];

	console.log('\nMENÚ DE OPCIONES');
	console.log('----------------');

	for (const index in options) {
		console.log(`${parseInt(index) + 1}. ${options[index]}`);
	}

	rl.question('Selecciona una opción:\n > ', (option) => {
		switch (option) {
			case '1':
				console.log();
				jjoo.addEvent();
				break;
			case '2':
				console.log();
				jjoo.addParticipant();
				break;
			case '3':
				console.log();
				jjoo.simulate();
				break;
			case '4':
				console.log();
				jjoo.writeSummary();
				break;
			case '5':
				console.log();
				console.log('Saliendo del programa...');
				rl.close();
				break;
			default:
				console.log(
					`Opción no válida. Introduce un valor entre [1-${options.length}]!`
				);
				main();
		}
	});
}

main();
