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

const readline = require('readline')
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})

//EJERCICIO
//Modelado de participantes
class Participant {
	constructor(name, country) {
		this.name = name
		this.country = country
	}
}

//Modelado de eventos
class Event {
	constructor(discipline) {
		this.discipline = discipline
	}

	participants = []

	addParticipant(participant) {
		this.participants.push(participant)
	}
}

//Menu de opciones
function main() {
	console.log('\nSIMULADOR DE JUEGOS OLIMPICOS')
	console.log(
		'1. Registrar evento\n2. Registrar participantes\n3. Simular evento\n4. Generar informes\n5. Salir del programa'
	)
	rl.question('Seleccione una opcion ', (answer) => {
		if (answer == '5') {
			rl.close()
		} else {
			main()
		}
	})
}

main()
