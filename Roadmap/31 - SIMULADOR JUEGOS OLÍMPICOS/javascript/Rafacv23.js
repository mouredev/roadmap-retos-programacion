// Importa el módulo readline para pedir datos por consola
const readline = require("readline")
let playing = true // variable que sirve para decidir cuando se ha de cerrar el juego

// Crea una interfaz para leer la entrada del usuario
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

class Sports {
  constructor(name) {
    this.name = name
    this.results = [] // para guardar los resultados de los atletas en este deporte
  }

  // método para añadir los resultados de un deporte
  addResult(result) {
    this.results.push(result)
  }
}

let sports = [] // array para almacenar los deportes que el usuario cree

class Athlete {
  constructor(name, country) {
    this.name = name
    this.country = country
  }
}

class Results {
  constructor(athlete, position) {
    this.athlete = athlete
    this.position = position
  }
}

let athletes = [] // array para almacenar los atletas que el usuario cree

function createEvent() {
  console.log("Qué deporte quieres añadir a los Juegos Olímpicos?")

  rl.question("Nombre del evento: ", (name) => {
    const newSport = new Sports(name)

    sports.push(newSport) // insertamos el nuevo deporte en el array
    console.log(`El evento ${name} ha sido creado.`)

    showMenu() // retornamos al menú
  })
}

function createAthlete() {
  console.log(
    "Qué atleta quieres añadir para que participe en los Juegos Olímpicos?"
  )

  rl.question("Nombre del atleta: ", (name) => {
    rl.question("A qué país va a representar este atleta: ", (country) => {
      const newAthlete = new Athlete(name, country)

      athletes.push(newAthlete) // insertamos el nuevo atleta en el array
      console.log(
        `El atleta: ${name} del país ${country} ha sido creado correctamente`
      )
      showMenu() // retornamos al menú
    })
  })
}

// Funcion que recoje los resultados de la simulación y genera el medallero
function generateMedals() {
  let medals = {}

  sports.forEach((sport) => {
    sport.results.forEach((result) => {
      const country = result.athlete.country

      if (!medals[country]) {
        medals[country] = { oro: 0, plata: 0, bronce: 0 }
      }
      if (result.position === 1) {
        medals[country].oro += 1
      } else if (result.position === 2) {
        medals[country].plata += 1
      } else if (result.position === 3) {
        medals[country].bronce += 1
      }
    })
  })

  console.log("Medallero")

  for (const [country, medalCount] of Object.entries(medals)) {
    console.log(
      `${country}: Oro - ${medalCount.oro}, Plata - ${medalCount.plata}, Bronce - ${medalCount.bronce}`
    )
  }

  showMenu() // retornamos al menú
}

// función que simula los juegos olímpicos
function simGames() {
  console.log("Simulando los Juegos Olímpicos...")

  sports.forEach((sport) => {
    console.log(`Simulando la competición de ${sport.name}`)

    athletes.sort(() => Math.random() - 0.5)

    athletes.forEach((athlete, index) => {
      const position = index + 1
      const result = new Results(athlete, position)

      console.log(result)

      sport.addResult(result)
    })
  })

  console.log("Simulación completada, ahora vamos a generar el medallero...")

  generateMedals()
}

function showMenu() {
  console.log("Bienvenido a los Juegos Olímpicos")
  console.log(`
      1. Registro de eventos.
      2. Registro de participantes.
      3. Simulación de eventos.
      4. Creación de informes.
      5. Salir.
      `)

  rl.question("¿Qué deseas hacer? ", (opcion) => {
    switch (opcion) {
      case "1":
        createEvent()
        break
      case "2":
        createAthlete()
        break
      case "3":
        simGames()
        break
      case "4":
        playing = false
        console.log("Saliendo del juego...")
        break
      default:
        console.log("Opción no válida")
        break
    }
  })
}

showMenu()
