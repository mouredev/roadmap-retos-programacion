const readline = require('node:readline')
const { stdin: input, stdout: output } = require('node:process')
const rl = readline.createInterface({ input, output })

class OlympicsGames {
  constructor() {
    this.events = []
    this.participants = []
    this.points = []
    this.countriesRanking = {}
  }

  registerEvents() {
    rl.question('Ingresa el nombre del evento: ', (nameOfEvent) => {
      const eventName = nameOfEvent.trim().toLowerCase()
      if (this.events.includes(eventName)) {
        console.log('El evento ya está registrado')
      } else {
        this.events.push(eventName)
        console.log('Evento registrado con éxito')
      }
      program()
    })
  }

  registerParticipants() {
    rl.question('Ingresa el nombre del participante: ', (nameOfParticipant) => {
      rl.question('Ingresa el nombre del país: ', (countryOfParticipant) => {
        if (this.events.length <= 0) {
          console.log('No hay eventos disponibles')
          program()
        } else {
          this.events.map((item, index) => {
            console.log(`${index}.${item}`)
          })
          rl.question('Ingresa un el indice del evento a inscribir: ', (eventUserRegister) => {
            const participantName = nameOfParticipant.trim().toLowerCase()
            const participantCountry = countryOfParticipant.trim().toLowerCase()
            const eventOfParticipant = parseInt(eventUserRegister)
            const existingParticipant = this.participants.find((item) => item.name === participantName)
            if (existingParticipant) {
              console.log('El participante ya está registrado')
            } else {
              this.participants.push({
                name: participantName,
                country: participantCountry,
                event: this.events[eventOfParticipant]
              })
              console.log('Participante registrado con éxito')
            }
            console.log(this.participants)
            program()
          })
        }
      })
    })
  }

  updateCountryMedals(country, medalType) {
    if (!this.countriesRanking[country]) {
      this.countriesRanking[country] = { gold: 0, silver: 0, bronze: 0 }
    }
    this.countriesRanking[country][medalType]++
  }

  displayCountryRanking() {
    const sortedCountries = Object.entries(this.countriesRanking)
      .sort((a, b) => {
        const [countryA, medalsA] = a
        const [countryB, medalsB] = b
        if (medalsB.gold !== medalsA.gold) return medalsB.gold - medalsA.gold
        if (medalsB.silver !== medalsA.silver) return medalsB.silver - medalsA.silver
        return medalsB.bronze - medalsA.bronze
      })

    console.log('Ranking de países:')
    sortedCountries.forEach(([country, medals], index) => {
      console.log(
        `${index + 1}. ${country} - 🥇 ${medals.gold}, 🥈 ${medals.silver}, 🥉 ${medals.bronze}`
      )
    })
  }

  eventsSimulator() {
    rl.question('Ingrese el nombre del evento a simular: ', (nameOfEvent) => {
      const tableOfPoints = []
      for (let participant of this.participants) {
        if (
          participant.event === nameOfEvent.trim().toLocaleLowerCase() &&
          this.participants.length >= 3
        ) {
          const nameOfParticipant = participant.name
          const country = participant.country
          let points = Math.round(Math.random() * 11)
          tableOfPoints.push({
            participantName: nameOfParticipant,
            country,
            points,
          })
        } else {
          console.log('No hay suficientes participantes para este evento')
          program()
        }
      }

      this.points = tableOfPoints.sort((a, b) => b.points - a.points)
      if (this.points.length >= 3) {
        console.log('Podio de ganadores')
        console.log(`🥇 ${this.points[0].country} ${this.points[0].participantName} ${this.points[0].points} puntos`)
        this.updateCountryMedals(this.points[0].country, 'gold')

        console.log(`🥈 ${this.points[1].country} ${this.points[1].participantName} ${this.points[1].points} puntos`)
        this.updateCountryMedals(this.points[1].country, 'silver')

        console.log(`🥉 ${this.points[2].country} ${this.points[2].participantName} ${this.points[2].points} puntos`)
        this.updateCountryMedals(this.points[2].country, 'bronze')
      }
      program()
    })
  }

  finalReport() {
    console.log('Reporte final de medallas:')
    this.displayCountryRanking()
    program()
  }
}

console.log('¡JJOO de París 2024!')
const newOlympicsGames = new OlympicsGames()

function program() {
  console.log('1. Registrar eventos')
  console.log('2. Registrar participantes')
  console.log('3. Simular eventos')
  console.log('4. Reporte final')
  console.log('0. Salir')

  rl.question('Ingresa una opción: ', (response) => {
    switch (response) {
      case '1':
        newOlympicsGames.registerEvents()
        break
      case '2':
        newOlympicsGames.registerParticipants()
        break
      case '3':
        newOlympicsGames.eventsSimulator()
        break
      case '4':
        newOlympicsGames.finalReport()
        break
      case '0':
        rl.close()
        break
      default:
        console.log('Opción inválida')
        program()
        break
    }
  })
}

program()