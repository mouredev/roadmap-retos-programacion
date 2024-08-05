//@RicJDev
//EJERCICIO
/*

* PARTE I: modelado de jugadores, simulacion de los juegos y sistema de registro de eventos

	- Se ejecuta en Node.js

*/

//Registro de eventos
class OlympicRegistry {
  constructor() {
    if (OlympicRegistry.instance) {
      return OlympicRegistry.instance
    }

    this.events = []
    this.participants = {}

    OlympicRegistry.instance = this
  }

  addEvent(event) {
    this.events.push(event)
  }

  registerParticipant(eventName, participant) {
    if (!this.participants[eventName]) {
      this.participants[eventName] = []
    }

    this.participants[eventName].push(participant)
  }

  getParticipants(eventName) {
    return this.participants[eventName] || []
  }
}

//Modelado de eventos
class Event {
  constructor(name) {
    this.name = name
    this.medals = []
  }

  assignMedals() {
    const participants = OlympicRegistry.instance.getParticipants(this.name)

    if (participants.length < 3) {
      console.log('Se requieren al menos tres participantes')

      return
    }

    const medalTypes = ['Gold', 'Silver', 'Bronze']

    for (let i = 0; i < 3; i++) {
      const randomIndex = Math.floor(Math.random() * participants.length)

      this.medals.push({
        participant: participants[randomIndex],
        medal: medalTypes[i],
      })

      participants.splice(randomIndex, 1)
    }
  }
}

//Ranking de medallas
class MedalRanking {
  constructor() {
    this.rankings = {}
  }

  addMedal(country, medal) {
    if (!this.rankings[country]) {
      this.rankings[country] = {
        Gold: 0,
        Silver: 0,
        Bronze: 0,
      }

      this.rankings[country][medal]++
    }
  }

  displayRankings() {
    console.log('Medallas por pais')

    for (const country in this.rankings) {
      console.log(' ')
      console.log(country.toUpperCase())
      console.log(`Gold: ${this.rankings[country].Gold}`)
      console.log(`Silver: ${this.rankings[country].Silver}`)
      console.log(`Bronze: ${this.rankings[country].Bronze}`)
    }
  }
}

//Modelado de jugadores
class Participant {
  constructor(name, country) {
    this.name = name
    this.country = country
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

const registry = new OlympicRegistry()
const ranking = new MedalRanking()

//1. Registrar evento
function createEvent() {
  rl.question(pc.blue('\nIndique la disciplina del evento a registrar: '), (eventName) => {
    registry.addEvent(new Event(eventName))

    main()
  })
}

//2. Registrar participantes
function registerParticipant() {
  rl.question(pc.blue('\nIndique el evento para registrar el participante: '), (eventName) => {
    rl.question(pc.green('Indique el nombre del participante: '), (name) => {
      rl.question(pc.magenta('Indique el pais del participante: '), (country) => {
        registry.registerParticipant(eventName, new Participant(name, country))

        main()
      })
    })
  })
}

//3. Simular evento
function simulateEvent() {
  rl.question(pc.blue('\nIndique el evento a simular: '), (eventName) => {
    const event = registry.events.find((event) => event.name === eventName)

    event.assignMedals()

    event.medals.forEach(({ participant, medal }) => {
      ranking.addMedal(participant.country, medal)
    })

    main()
  })
}

//Mostrar medallas
function generateInform() {
  ranking.displayRankings()
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
