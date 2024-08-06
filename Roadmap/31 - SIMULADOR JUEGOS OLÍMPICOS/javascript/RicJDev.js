//@RicJDev
//EJERCICIO
class OlympicRegistry {
  constructor() {
    if (OlympicRegistry.instance) {
      return OlympicRegistry.instance
    }

    this.events = []
    this.participants = {}

    OlympicRegistry.instance = this
  }

  addEvent(eventName) {
    this.events.push(eventName)

    console.log(`${eventName} ha sido registrado!`)
  }

  registerParticipant(eventName, participant) {
    if (this.events.includes(eventName)) {
      if (!this.participants[eventName]) {
        this.participants[eventName] = []
      }

      this.participants[eventName].push(participant)

      console.log(`Participante registrado en el evento ${eventName}!`)
    } else {
      console.log('Evento no registrado')
    }
  }

  getParticipants(eventName) {
    return this.participants[eventName] || []
  }
}

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
    for (const country in this.rankings) {
      console.log(' ')
      console.log(country.toUpperCase())
      console.log(`Gold: ${this.rankings[country].Gold}`)
      console.log(`Silver: ${this.rankings[country].Silver}`)
      console.log(`Bronze: ${this.rankings[country].Bronze}`)
    }
  }
}

class Participant {
  constructor(name, country) {
    this.name = name
    this.country = country
  }
}

/*

  * IMPLEMENTACION EN LA TERMINAL

	- Se ejecuta en Node.js
	- Se ha importado el modulo Readline para tener input en terminal
  - Se ha instalado Picocolors, una libreria para colorear el texto en la terminal

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
function registerEvent() {
  rl.question('\nIndique el nnombre del evento a registrar: ', (eventName) => {
    registry.addEvent(eventName)

    main()
  })
}

//2. Registrar participantes
function registerParticipant() {
  rl.question('\nIndique el nombre del participante: ', (name) => {
    rl.question('Indique el pais del participante: ', (country) => {
      if (registry.events.length > 0) {
        console.log('\nEstos son los eventos displibles: ')

        for (let i = 0; i < registry.events.length; i++) {
          console.log(`${i + 1}. ${registry.events[i]}`)
        }

        rl.question('\nElija un evento para registrar al participante: ', (eventIndex) => {
          const index = parseInt(eventIndex) - 1

          if (registry.events[index]) {
            registry.registerParticipant(registry.events[index], new Participant(name, country))
          } else {
            console.log(pc.red('Elija una opcion valida'))
          }

          main()
        })
      } else {
        console.log(pc.red('Debe registrar al menos un evento'))
        main()
      }
    })
  })
}

//3. Simular evento
function simulateEvent() {
  if (registry.events.length > 0) {
    console.log('\nEstos son los eventos displibles: ')

    for (let i = 0; i < registry.events.length; i++) {
      console.log(`${i + 1}. ${registry.events[i]}`)
    }

    rl.question('\nIndique el evento a simular: ', (eventIndex) => {
      const index = parseInt(eventIndex) - 1

      if (registry.events[index]) {
        const event = new Event(registry.events[index])

        event.assignMedals()

        for (const element of event.medals) {
          ranking.addMedal(element.participant.country, element.medal)
        }
      } else {
        console.log(pc.red('\nEvento no registrado'))
      }

      main()
    })
  } else {
    console.log(pc.red('Debe registrar al menos un evento'))
    main()
  }
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
    '\n1. Registrar evento\n2. Registrar participantes\n3. Simular evento\n4. Generar informes\n5. Salir del programa'
  )

  const actions = new Map([
    ['1', registerEvent],
    ['2', registerParticipant],
    ['3', simulateEvent],
    ['4', generateInform],
    ['5', exit],
  ])

  rl.question('\nSeleccione una opcion (1 - 5) ', (option) => {
    const action =
      actions.get(option) ||
      function () {
        console.log('Opcion no valida')
        main()
      }

    action()
  })
}

main()
