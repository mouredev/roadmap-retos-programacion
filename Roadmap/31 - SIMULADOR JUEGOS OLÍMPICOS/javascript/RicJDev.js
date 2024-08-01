/*

	Se ejecuta en Node.js

	- Se ha importado el modulo Readline
	- Se ha instalado Picocolors, una libreria para colorear el texto de la terminal

	@RicJDev

*/

const readline = require('readline')
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})

const pc = require('picocolors')

//EJERCICIO
class Participant {
	constructor(name, country) {
		this.name = name
		this.country = country
	}
}

class Event {
	constructor(discipline) {
		this.discipline = discipline
	}
}

class EventRegister {
	events = []

	search(discipline) {
		this.events.find((event) => event.discipline === discipline)
	}

	addEvent(discipline) {
		let event = new Event(discipline)
		event.status = 'unfinished'

		this.events.push(event)
	}J
}

class GameSimulator {
	constructor() {
		this.players = []
	}

	addPlayer(player) {
		this.players.push(player)
	}

	simulateGame() {
		if (this.players.length >= 3) {
			this.players.sort(() => Math.random() - 0.5)

			this.players[0].medal = 'gold'
			this.players[1].medal = 'silver'
			this.players[2].medal = 'bronze'

			return this.players
		}
	}
}

//Menu
function createEvent() {
	rl.question(pc.blue('\nIndique la disciplina del evento a registrar: '), (discipline) => {
		main()
	})
}

function registerParticipant() {
	rl.question(pc.green('\nIndique el evento para registrar el participante: '), (discipline) => {
		rl.question(pc.green('Indique el nombre del participante: '), (name) => {
			rl.question(pc.green('Indique el pais del participante: '), (country) => {
				main()
			})
		})
	})
}

function simulateEvent() {
	rl.question(pc.blue('\nIndique el evento a simular: '), (discipline) => {
		main()
	})
}

function generateInform() {
	//...
	main()
}

function exit() {
	console.log(pc.green('\nSaliendo del programa...'))

	setTimeout(() => {
		console.clear()
		rl.close()
	}, 300)
}

//Menu de opciones
function main() {
	console.log(pc.underline('\nSIMULADOR DE JUEGOS OLIMPICOS'))

	const actions = new Map([
		['1', createEvent],
		['2', registerParticipant],
		['3', simulateEvent],
		['4', generateInform],
		['5', exit],
	])

	console.log(
		pc.yellow(
			'\n1. Registrar evento\n2. Registrar participantes\n3. Simular evento\n4. Generar informes\n5. Salir del programa'
		)
	)

	rl.question(pc.green('\nSeleccione una opcion (1 - 5) '), (option) => {
		const method = actions.get(option) || main
		method()
	})
}

rl.close()
