//@RicJDev

//Se ha instalado Picocolors, un libreria para colorear texto en terminal (https://www.npmjs.com/package/picocolors)
import pc from 'picocolors'

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
  }

  registerParticipant(eventName, participant) {
    if (this.events.includes(eventName)) {
      if (!this.participants[eventName]) {
        this.participants[eventName] = []
      }

      this.participants[eventName].push(participant)
    } else {
      console.log(pc.red('Evento no registrado'))
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
      console.log(pc.red('Se requieren al menos tres participantes'))

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
    if (Object.keys(this.rankings).length > 0) {
      for (const country in this.rankings) {
        console.log(' ')
        console.log(country.toUpperCase())
        console.log(`Gold: ${this.rankings[country].Gold}`)
        console.log(`Silver: ${this.rankings[country].Silver}`)
        console.log(`Bronze: ${this.rankings[country].Bronze}`)
      }
    } else {
      console.log(pc.red('No se ha asignado medallas a ningún país'))
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

  - Se ejecuta en Node.js, importando el modulo Readline (https://nodejs.org/api/readline.html)

*/

import * as readline from 'node:readline'

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const registry = new OlympicRegistry()
const ranking = new MedalRanking()

//1. Registrar evento
function registerEvent() {
  rl.question(pc.blue('\nIndique el nombre del evento a registrar: '), (eventName) => {
    registry.addEvent(eventName)

    console.log(`${pc.green(eventName)} ha sido registrado!`)

    main()
  })
}

//2. Registrar participantes
function registerParticipant() {
  rl.question('\nIndique el nombre del participante: ', (name) => {
    rl.question('Indique el país del participante: ', (country) => {
      if (registry.events.length > 0) {
        console.log('\nEstos son los eventos registrados: ')

        for (let i = 0; i < registry.events.length; i++) {
          console.log(`${i + 1}. ${registry.events[i]}`)
        }

        rl.question(pc.blue('\nElija un evento para registrar al participante: '), (eventIndex) => {
          const index = parseInt(eventIndex) - 1

          if (registry.events[index]) {
            registry.registerParticipant(registry.events[index], new Participant(name, country))

            console.log(
              `${pc.green(name)} ha sido registrado en ${pc.green(registry.events[index])}!`
            )
          } else {
            console.log(pc.red('Elija una opción válida'))
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
    console.log('\nEstos son los eventos disponibles: ')

    for (let i = 0; i < registry.events.length; i++) {
      console.log(`${i + 1}. ${registry.events[i]}`)
    }

    rl.question(pc.blue('\nIndique el evento a simular: '), (eventIndex) => {
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

  rl.question(pc.yellow('\nSeleccione una opción (1 - 5) '), (option) => {
    const action =
      actions.get(option) ||
      function () {
        console.log(pc.red('Elija una opción válida'))
        main()
      }

    action()
  })
}

main()
