/*
  EJERCICIO:

  @RicJDev
*/

// Primero modelamos las preguntas y el cuestionario

class Question {
  constructor(title) {
    this.title = title
    this.options = { A: null, B: null, C: null, D: null }
  }

  addOption(letter, option) {
    if (Object.keys(this.options).includes(letter.toUpperCase())) {
      if (this.options[letter] === option) {
        throw new Error('You cannot repeat options.')
      }

      this.options[letter] = option
    } else {
      throw new Error(`Options avalaible: A, B, C or D. Cannot set '${letter}' option.`)
    }
  }
}

class Questionary {
  constructor() {
    this.questions = {}
  }

  addQuestion(id, title) {
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

questionary.addQuestion(1, '¿Qué parte de un sitio web te llama más la atención?')
questionary.addQuestion(
  2,
  'Si tuvieras que elegir entre crear una nueva aplicación móvil o diseñar una base de datos, ¿cuál preferirías?'
)
questionary.addQuestion(3, '¿Qué te resulta más fácil de entender?')
questionary.addQuestion(4, '¿Qué tipo de problemas te gusta resolver?')
questionary.addQuestion(5, '¿Qué herramienta te resulta más interesante?')
questionary.addQuestion(6, '¿Qué te gustaría hacer en tu tiempo libre?')
questionary.addQuestion(7, '¿Qué tipo de proyectos te motivan más?')
questionary.addQuestion(8, '¿Qué habilidad consideras más importante para un desarrollador?')
questionary.addQuestion(9, '¿Qué tipo de equipo te gustaría formar parte?')
questionary.addQuestion(10, '¿Qué te gustaría lograr a largo plazo en tu carrera?')

// Almacenamos las respuestas separadas por "casas" y las asignamos según las opciones

const houses = {
  frontend: {
    1: 'El diseño visual y la interfaz de usuario.',
    2: 'Crear una aplicación móvil con una interfaz intuitiva.',
    3: 'Diagramas de flujo y diseños visuales.',
    4: 'Problemas relacionados con la estética y la experiencia del usuario.',
    5: 'Photoshop o Figma.',
    6: 'Diseñar interfaces de usuario para diferentes aplicaciones.',
    7: 'Proyectos que tienen un impacto visual y estético.',
    8: 'La creatividad y el sentido del diseño.',
    9: 'Un equipo de diseño y UX.',
    10: 'Crear productos digitales con una interfaz de usuario excepcional.',
  },

  backend: {
    1: 'La lógica detrás de cómo funciona el sitio y cómo se conectan las diferentes partes.',
    2: 'Diseñar una base de datos eficiente para almacenar grandes cantidades de información.',
    3: 'Código y algoritmos.',
    4: 'Problemas lógicos y de optimización.',
    5: 'Python o Java.',
    6: 'Desarrollar videojuegos o aplicaciones web.',
    7: 'Proyectos que requieren resolver problemas complejos y optimizar el rendimiento.',
    8: 'La capacidad de resolver problemas y pensar de forma lógica.',
    9: 'Un equipo de desarrollo backend.',
    10: 'Desarrollar aplicaciones escalables y eficientes.',
  },

  mobile: {
    1: 'Cómo se ve y funciona la aplicación en un teléfono móvil.',
    2: 'Ambas opciones me parecen igualmente interesantes.',
    3: 'Prototipos y maquetas.',
    4: 'Problemas relacionados con la portabilidad y la compatibilidad en diferentes dispositivos.',
    5: 'XCode o Android Studio.',
    6: 'Crear aplicaciones móviles para diferentes plataformas.',
    7: 'Proyectos que pueden ser utilizados por muchas personas en sus dispositivos móviles.',
    8: 'La adaptabilidad y la capacidad de aprender nuevas tecnologías.',
    9: 'Un equipo de desarrollo móvil.',
    10: 'Crear aplicaciones móviles que cambien la forma en que las personas interactúan con el mundo.',
  },

  data: {
    1: 'Los datos que se recolectan y cómo se utilizan para mejorar el sitio.',
    2: 'Ninguna de las opciones me llama la atención.',
    3: 'Gráficos y estadísticas.',
    4: 'Problemas relacionados con la extracción de información útil de grandes conjuntos de datos.',
    5: 'SQL o Tableau.',
    6: 'Analizar datos y crear visualizaciones.',
    7: 'Proyectos que utilizan datos para tomar decisiones informadas.',
    8: 'La capacidad de analizar datos y extraer insights.',
    9: 'Un equipo de ciencia de datos.',
    10: 'Utilizar datos para resolver problemas del mundo real y tomar decisiones estratégicas.',
  },
}

for (const id in questionary.questions) {
  questionary.addOption(id, 'A', houses.frontend[id])
  questionary.addOption(id, 'B', houses.backend[id])
  questionary.addOption(id, 'C', houses.mobile[id])
  questionary.addOption(id, 'D', houses.data[id])
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

// * Aquí empieza la magia *

const results = { A: 0, B: 0, C: 0, D: 0 }

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

// Mostramos los resultados del cuestionario y finaliza el programa

let winner = Object.keys(results).reduce((previous, current) => {
  if (results[current] > results[previous]) {
    previous = current
  }

  return previous
})

const tieValues = Object.keys(results).filter((same) => results[winner] === results[same])

if (tieValues.length > 1) winner = tieValues[Math.floor(Math.random() * tieValues.length)]

console.clear()
console.log(
  `\nQuerido ${pc.bold(name)}, ¡el cuestionario ha terminado!\nEstos son los resultados:\n`
)

const messages = {
  A: `Tu casa será el desarrollo ${pc.blue('Frontend')}.`,
  B: `Tu casa será el desarrollo ${pc.blue('Backend')}.`,
  C: `Tu casa será el desarrollo ${pc.blue('Mobile')}.`,
  D: `Tu casa será el análisis de ${pc.blue('Data')}.`,
}

const resultMessage = messages[winner] || pc.red('Ha ocurrido algún error inesperado.')

console.log(resultMessage)

if (tieValues.length > 1) {
  console.log('\nFue una decisión difícil debido a que hubo empate en algunas preguntas.')
}

console.log(' ')
console.log(`Total de respuestas ${pc.green('A')}: ${pc.yellow(results.A)}.`)
console.log(`Total de respuestas ${pc.green('B')}: ${pc.yellow(results.B)}.`)
console.log(`Total de respuestas ${pc.green('C')}: ${pc.yellow(results.C)}.`)
console.log(`Total de respuestas ${pc.green('D')}: ${pc.yellow(results.D)}.`)
