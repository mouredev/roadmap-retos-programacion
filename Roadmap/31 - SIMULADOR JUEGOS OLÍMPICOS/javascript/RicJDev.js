//@RicJDev
//EJERCICIO
/*

* PARTE I: modelado de jugadores, simulacion de los juegos y sistema de registro de eventos

	- Se ejecuta en Node.js

*/

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

      this.players[0].medal = 'gold'
      this.players[1].medal = 'silver'
      this.players[2].medal = 'bronze'

      return this.players
    }
  }
}

class Event {
  constructor(discipline) {
    this.discipline = discipline
    this.simulator = new GameSimulator()
  }
}

class EventRegister {
  events = []

  search(discipline) {
    let result = this.events.find((event) => event.discipline == discipline)

    return result
  }

  add(event) {
    event.status = 'unfinished'
    this.events.push(event)
  }

  finish(event) {
    let result = this.search(event)
    result.status = 'finished'
  }
}

class InformService {
  constructor() {
    this.data = []
  }

  add(data) {
    this.data.push(data)
  }

  display() {
    console.log(this.data)
  }
}

/*

* PARTE II: implementacion de la parte I en la terminal

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
const informService = new InformService()

//Funciones del menu
function createEvent() {
  rl.question(pc.blue('\nIndique la disciplina del evento a registrar: '), (discipline) => {
    eventRegister.add(new Event(discipline))

    main()
  })
}

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

function simulateEvent() {
  rl.question(pc.blue('\nIndique el evento a simular: '), (discipline) => {
    const event = eventRegister.search(discipline)

    if (event) {
      let results = event.simulator.play()
      informService.add(results)
    } else {
      console.log(pc.red('Evento no registrado'))
    }

    main()
  })
}

function generateInform() {
  informService.display()
  main()
}

function exit() {
  console.log(pc.red('\nSaliendo del programa...'))

  setTimeout(() => {
    console.clear()
    rl.close()
  }, 300)
}

//Menu de opciones
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
