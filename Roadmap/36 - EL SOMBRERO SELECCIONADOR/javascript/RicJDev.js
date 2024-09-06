/*
  EJERCICIO:

  @RicJDev
*/

// Primero modelamos las preguntas y el cuestionario

class Question {
  constructor(title) {
    this.title = title
    this.options = {
      A: null,
      B: null,
      C: null,
      D: null,
    }
  }

  addOption(letter, option) {
    if (Object.keys(this.options).includes(letter.toUpperCase())) {
      if (this.options[letter] === option) {
        throw new Error('You cannot repeat options.')
      }

      this.options[letter] = option
    } else {
      throw new Error('You cannot access an option that does not exist.')
    }
  }
}

class Questionary {
  constructor() {
    this.questions = {}
  }

  addQuestion(title) {
    const id = Object.keys(this.questions).length + 1
    this.questions[id] = new Question(title)
  }

  addOption(id, letter, option) {
    if (this.questions[id]) {
      const question = this.questions[id]

      question.addOption(letter, option)
    }
  }
}

// Creamos el cuestionario

const questionary = new Questionary()

questionary.addQuestion('¿Qué parte de un sitio web te llama más la atención?')
questionary.addQuestion(
  'Si tuvieras que elegir entre crear una nueva aplicación móvil o diseñar una base de datos, ¿cuál preferirías?'
)
questionary.addQuestion('¿Qué te resulta más fácil de entender?')
questionary.addQuestion('¿Qué tipo de problemas te gusta resolver?')
questionary.addQuestion('¿Qué herramienta te resulta más interesante?')
questionary.addQuestion('¿Qué te gustaría hacer en tu tiempo libre?')
questionary.addQuestion('¿Qué tipo de proyectos te motivan más?')
questionary.addQuestion('¿Qué habilidad consideras más importante para un desarrollador?')
questionary.addQuestion('¿Qué tipo de equipo te gustaría formar parte?')
questionary.addQuestion('¿Qué te gustaría lograr a largo plazo en tu carrera?')

// Almacenamos las respuestas separadas por "casas" y las asignamos según las opciones

const frontendHouse = [
  'El diseño visual y la interfaz de usuario.',
  'Crear una aplicación móvil con una interfaz intuitiva.',
  'Diagramas de flujo y diseños visuales.',
  'Problemas relacionados con la estética y la experiencia del usuario.',
  'Photoshop o Figma.',
  'Diseñar interfaces de usuario para diferentes aplicaciones.',
  'Proyectos que tienen un impacto visual y estético.',
  'La creatividad y el sentido del diseño.',
  'Un equipo de diseño y UX.',
  'Crear productos digitales con una interfaz de usuario excepcional.',
]

const backendHouse = [
  'La lógica detrás de cómo funciona el sitio y cómo se conectan las diferentes partes.',
  'Diseñar una base de datos eficiente para almacenar grandes cantidades de información.',
  'Código y algoritmos.',
  'Problemas lógicos y de optimización.',
  'Python o Java.',
  'Desarrollar videojuegos o aplicaciones web.',
  'Proyectos que requieren resolver problemas complejos y optimizar el rendimiento.',
  'La capacidad de resolver problemas y pensar de forma lógica.',
  'Un equipo de desarrollo backend.',
  'Desarrollar aplicaciones escalables y eficientes.',
]

const mobileHouse = [
  'Cómo se ve y funciona la aplicación en un teléfono móvil.',
  'Ambas opciones me parecen igualmente interesantes.',
  'Prototipos y maquetas.',
  'Problemas relacionados con la portabilidad y la compatibilidad en diferentes dispositivos.',
  'XCode o Android Studio.',
  'Crear aplicaciones móviles para diferentes plataformas.',
  'Proyectos que pueden ser utilizados por muchas personas en sus dispositivos móviles.',
  'La adaptabilidad y la capacidad de aprender nuevas tecnologías.',
  'Un equipo de desarrollo móvil.',
  'Crear aplicaciones móviles que cambien la forma en que las personas interactúan con el mundo.',
]

const dataHouse = [
  'Los datos que se recolectan y cómo se utilizan para mejorar el sitio.',
  'Ninguna de las opciones me llama la atención.',
  'Gráficos y estadísticas.',
  'Problemas relacionados con la extracción de información útil de grandes conjuntos de datos.',
  'SQL o Tableau.',
  'Analizar datos y crear visualizaciones.',
  'Proyectos que utilizan datos para tomar decisiones informadas.',
  'La capacidad de analizar datos y extraer insights.',
  'Un equipo de ciencia de datos.',
  'Utilizar datos para resolver problemas del mundo real y tomar decisiones estratégicas.',
]

for (const id in questionary.questions) {
  questionary.addOption(id, 'A', frontendHouse[id - 1])
  questionary.addOption(id, 'B', backendHouse[id - 1])
  questionary.addOption(id, 'C', mobileHouse[id - 1])
  questionary.addOption(id, 'D', dataHouse[id - 1])
}

/*
  * Creamos la "app" en la terminal *

- Se ejecuta en Node.js, importando el módulo Readline/promises para tener input por terminal (https://nodejs.org/api/readline.html)
- Se ha instalado Picocolors, un librería para colorear texto en la terminal (https://www.npmjs.com/package/picocolors)

*/

import * as readline from 'readline/promises'
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

import pc from 'picocolors'

// Hacemos un sitema básico para manejar los resultados

const results = {
  A: 0,
  B: 0,
  C: 0,
  D: 0,
}

function getWinnerLetter() {
  let winner = 'A'

  for (const letter in results) {
    if (results[letter] > results[winner]) {
      winner = letter
    }
  }

  const sameValues = Object.keys(results).filter((key) => {
    return results[winner] === results[key]
  })

  if (sameValues.length > 1) {
    const randomIndex = Math.floor(Math.random() * sameValues.length)

    return { letter: sameValues[randomIndex], isTie: true }
  }

  return { letter: winner, isTie: false }
}

// * Aquí empieza la magia *

console.clear()

const name = await rl.question('\nDime tu nombre, querido alumno. ')

for (const id in questionary.questions) {
  const question = questionary.questions[id]

  let message = '¡Descubre a cuál casa perteneces!'
  let answer = ''

  while (!Object.keys(question.options).includes(answer.toUpperCase())) {
    console.clear()
    console.log(`\nBienvenido seas, ${pc.bold(name)}. ${message}`)
    console.log(`\n${pc.blue(id)}. ${question.title}\n`)

    for (const letter in question.options) {
      console.log(` - ${pc.green(letter)}. ${question.options[letter] || 'Opción vacía.'}`)
    }

    answer = await rl.question('\nIndica la opción de tu preferencia. ')

    message = pc.yellow('Elije una opción válida, por favor.')
  }

  results[answer.toUpperCase()]++
}

rl.close()

// Mostramos los resultados del cuestionario y aquí finaliza el programa

console.clear()
console.log(
  `\nQuerido ${pc.bold(name)}, ¡el cuestionario ha terminado!\nEstos son los resultados:\n`
)

const conditions = {
  A: `Tu casa será el desarrollo ${pc.blue('Frontend')}.`,
  B: `Tu casa será el desarrollo ${pc.blue('Backend')}.`,
  C: `Tu casa será el desarrollo ${pc.blue('Mobile')}.`,
  D: `Tu casa será el análisis de ${pc.blue('Data')}.`,
}

const { letter, isTie } = getWinnerLetter()

const resultMessage = conditions[letter] || pc.red('Ha ocurrido algun error inesperado.')

console.log(resultMessage)

if (isTie) {
  console.log('\nFue una decisión difícil debido a que hubo empate en algunas preguntas.')
}

console.log(' ')
console.log(`Total de respuestas ${pc.green('A')}: ${pc.yellow(results.A)}.`)
console.log(`Total de respuestas ${pc.green('B')}: ${pc.yellow(results.B)}.`)
console.log(`Total de respuestas ${pc.green('C')}: ${pc.yellow(results.C)}.`)
console.log(`Total de respuestas ${pc.green('D')}: ${pc.yellow(results.D)}.`)
