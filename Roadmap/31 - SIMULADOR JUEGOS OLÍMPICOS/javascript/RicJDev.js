//@RicJDev
//EJERCICIO
/*

* PARTE I: modelado de jugadores, simulacion de los juegos y sistema de registro de eventos

	- Se ejecuta en Node.js

*/

//Jugadores y simulador de juegos
class Player {
  constructor(name, country) {
    this.name = name
    this.country = country
  }
}

class GameSimulator {
  constructor() {
    this.players = []
  }

  add(player) {
    this.players.push(player)
  }

  play() {
    if (this.players.length >= 3) {
      this.players.sort(() => Math.random() - 0.5)

      const winners = [
        { gold: this.players[0] },
        { silver: this.players[1] },
        { bronze: this.players[2] },
      ]

      this.players.length = 0

      return winners
    } else {
      return undefined
    }
  }
}

//Registro de eventos deportivos
class Event {
  constructor(discipline) {
    this.discipline = discipline
    this.simulator = new GameSimulator()
  }
}

class EventRegister {
  constructor() {
    this.events = []
  }

  search(discipline) {
    return this.events.find((event) => event.discipline == discipline)
  }

  add(event) {
    this.events.push(event)
  }
}

/*

* PARTE II: implementacion en terminal

	- Se ha importado el modulo Readline para tener input en terminal
	- Se ha instalado Picocolors, una libreria para colorear el texto de la terminal

*/

const readline = require('readline')
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const pc = require('picocolors')

const eventRegister = new EventRegister()

//1. Registrar evento
function createEvent() {
  rl.question(pc.blue('\nIndique la disciplina del evento a registrar: '), (discipline) => {
    eventRegister.add(new Event(discipline))

    main()
  })
}

//2. Registrar participantes
function registerParticipant() {
  rl.question(pc.blue('\nIndique el evento para registrar el participante: '), (discipline) => {
    const event = eventRegister.search(discipline)

    if (event) {
      rl.question(pc.green('Indique el nombre del participante: '), (name) => {
        rl.question(pc.magenta('Indique el pais del participante: '), (country) => {
          event.simulator.add(new Player(name, country))

          main()
        })
      })
    } else {
      console.log(pc.red('Evento no registrado'))

      main()
    }
  })
}

//3. Simular evento
function simulateEvent() {
  rl.question(pc.blue('\nIndique el evento a simular: '), (discipline) => {
    const event = eventRegister.search(discipline)

    if (event) {
      let results = event.simulator.play()

      if (results) {
        console.log(results)
      } else {
        console.log(pc.red('No hay suficientes participantes'))
      }
    } else {
      console.log(pc.red('Evento no registrado'))
    }

    main()
  })
}

//TODO: 4. Generar un informe
function generateInform() {
  //...
  main()
}

//5. Salir del programa
function exit() {
  console.log(pc.red('\nSaliendo del programa...'))

  setTimeout(() => {
    console.clear()
    rl.close()
  }, 300)
}

//Menu principal
function main() {
  console.log(pc.underline('\nSIMULADOR DE JUEGOS OLIMPICOS'))

  console.log(
    pc.yellow(
      '\n1. Registrar evento\n2. Registrar participantes\n3. Simular evento\n4. Generar informes\n5. Salir del programa'
    )
  )

  const actions = new Map([
    ['1', createEvent],
    ['2', registerParticipant],
    ['3', simulateEvent],
    ['4', generateInform],
    ['5', exit],
  ])

  rl.question(pc.green('\nSeleccione una opcion (1 - 5) '), (option) => {
    const action =
      actions.get(option) ||
      function () {
        console.log(pc.red('Opcion no valida'))
        main()
      }

    action()
  })
}

main()
