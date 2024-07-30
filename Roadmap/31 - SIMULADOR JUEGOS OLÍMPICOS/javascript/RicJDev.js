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

//Se ejecuta en Node.js importando el módulo ReadLine
const readline = require('readline')
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})
//EJERCICIO
//Modelado de eventos
const events = []

class Event {
	constructor(discipline) {
		this.discipline = discipline
		this.participants = []

		events.push(this)
	}

	addParticipant(participant) {
		this.participants.push(participant)
	}
}

//Modelado de participantes
class Participant {
	constructor(name, country) {
		this.name = name
		this.country = country
	}
}

//Funciones del menu
function searchEvent(discipline) {
	const result = events.find((event) => event.discipline === discipline)

	return result
}

function registerParticipant() {
	rl.question('Indique el evento para registrar el participante ', (discipline) => {
		const event = searchEvent(discipline)

		rl.question('Indique el nombre del participante ', (name) => {
			rl.question('Indique el pais del participante ', (country) => {
				const participant = new Participant(name, country)
				event.addParticipant(participant)

				main()
			})
		})
	})
}

function createEvent() {
	rl.question('Indique la disciplina del evento a registrar ', (discipline) => {
		new Event(discipline)

		main()
	})
}

function simulateEvent() {
	rl.question('Indique el evento a simular ', (discipline) => {
		const event = searchEvent(discipline)

		if (event.participants.length > 3) {
			//...
		} else {
			console.log('No hay suficientes participantes para la simulacion')
		}

		main()
	})
}

function generateInform() {
	main()
}

function exit() {
	console.log('\nSaliendo del programa...')
	rl.close()
}

function display() {
	console.log('\n\nOpcion para mostrar listados solo para el desa')

	events.forEach((element) => {
		console.log(element.discipline)
		console.log(element.participants)
	})

	main()
}

//Menu de opciones
function main() {
	console.log('\nSIMULADOR DE JUEGOS OLIMPICOS')

	const actions = new Map([
		['1', createEvent],
		['2', registerParticipant],
		['3', simulateEvent],
		['4', generateInform],
		['5', exit],
		['d', display],
	])

	console.log(
		'1. Registrar evento\n2. Registrar participantes\n3. Simular evento\n4. Generar informes\n5. Salir del programa'
	)

	rl.question('Seleccione una opcion (1 - 5) ', (option) => {
		const method = actions.get(option) || main
		method()
	})
}

main()
