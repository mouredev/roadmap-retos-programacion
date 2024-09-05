/*
  EJERCICIO:

  @RicJDev
*/

// Modelado de preguntas y cuestionario

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

  addOption(option) {
    const isSomeNull = Object.values(this.options).some((option) => option === null)

    if (isSomeNull) {
      const voidOption = Object.keys(this.options).find((option) => this.options[option] === null)
      this.options[voidOption] = option
    } else {
      console.warn(`Se han llenado todas las opciones. No se pudo agregar "${option}"`)
    }
  }

  editOption(letter, newOption) {
    if (this.options[letter]) {
      this.options[letter] = newOption
    } else {
      console.warn('Está intentando acceder a una opción inexistente')
    }
  }
}

class Questionary {
  constructor() {
    this.questions = {}
    this.results = {
      A: 0,
      B: 0,
      C: 0,
      D: 0,
    }
  }

  addQuestion(title) {
    const id = this.questionsCount + 1
    this.questions[id] = new Question(title)
  }

  getWinnerLetter() {
    let result = 'A'

    for (const letter in this.results) {
      if (this.results[letter] > this.results[result]) {
        result = letter
      }
    }

    const equals = Object.keys(this.results).filter((key) => {
      return this.results[result] === this.results[key]
    })

    if (equals.length > 1) {
      const randomIndex = Math.floor(Math.random() * equals.length)

      return { letter: equals[randomIndex], wasRandomized: true }
    }

    return { letter: result, wasRandomized: false }
  }

  get questionsCount() {
    return Object.keys(this.questions).length
  }
}

// Implementamos las clases para crear el cuestionario

const questionary = new Questionary()

questionary.addQuestion('¿Qué parte de un sitio web te llama más la atención?')

questionary.questions[1].addOption('El diseño visual y la interfaz de usuario.')
questionary.questions[1].addOption(
  'La lógica detrás de cómo funciona el sitio y cómo se conectan las diferentes partes.'
)
questionary.questions[1].addOption('Cómo se ve y funciona la aplicación en un teléfono móvil.')
questionary.questions[1].addOption(
  'Los datos que se recolectan y cómo se utilizan para mejorar el sitio.'
)

questionary.addQuestion(
  'Si tuvieras que elegir entre crear una nueva aplicación móvil o diseñar una base de datos, ¿cuál preferirías?'
)

questionary.questions[2].addOption('Crear una aplicación móvil con una interfaz intuitiva.')
questionary.questions[2].addOption(
  'Diseñar una base de datos eficiente para almacenar grandes cantidades de información.'
)
questionary.questions[2].addOption('Ambas opciones me parecen igualmente interesantes.')
questionary.questions[2].addOption('Ninguna de las opciones me llama la atención.')

questionary.addQuestion('¿Qué te resulta más fácil de entender?')
questionary.questions[3].addOption('Diagramas de flujo y diseños visuales.')
questionary.questions[3].addOption('Código y algoritmos.')
questionary.questions[3].addOption('Prototipos y maquetas.')
questionary.questions[3].addOption('Gráficos y estadísticas.')

questionary.addQuestion('¿Qué tipo de problemas te gusta resolver?')
questionary.questions[4].addOption(
  'Problemas relacionados con la estética y la experiencia del usuario.'
)
questionary.questions[4].addOption('Problemas lógicos y de optimización.')
questionary.questions[4].addOption(
  'Problemas relacionados con la portabilidad y la compatibilidad en diferentes dispositivos.'
)
questionary.questions[4].addOption(
  'Problemas relacionados con la extracción de información útil de grandes conjuntos de datos.'
)

questionary.addQuestion('¿Qué herramienta te resulta más interesante?')
questionary.questions[5].addOption('Photoshop o Figma.')
questionary.questions[5].addOption('Python o Java.')
questionary.questions[5].addOption('XCode o Android Studio.')
questionary.questions[5].addOption('SQL o Tableau.')

questionary.addQuestion('¿Qué te gustaría hacer en tu tiempo libre?')
questionary.questions[6].addOption('Diseñar interfaces de usuario para diferentes aplicaciones.')
questionary.questions[6].addOption('Desarrollar videojuegos o aplicaciones web.')
questionary.questions[6].addOption('Crear aplicaciones móviles para diferentes plataformas.')
questionary.questions[6].addOption('Analizar datos y crear visualizaciones.')

questionary.addQuestion('¿Qué tipo de proyectos te motivan más?')
questionary.questions[7].addOption('Proyectos que tienen un impacto visual y estético.')
questionary.questions[7].addOption(
  'Proyectos que requieren resolver problemas complejos y optimizar el rendimiento.'
)
questionary.questions[7].addOption(
  'Proyectos que pueden ser utilizados por muchas personas en sus dispositivos móviles.'
)
questionary.questions[7].addOption('Proyectos que utilizan datos para tomar decisiones informadas.')

questionary.addQuestion('¿Qué habilidad consideras más importante para un desarrollador?')

questionary.questions[8].addOption('La creatividad y el sentido del diseño.')
questionary.questions[8].addOption('La capacidad de resolver problemas y pensar de forma lógica.')
questionary.questions[8].addOption(
  'La adaptabilidad y la capacidad de aprender nuevas tecnologías.'
)
questionary.questions[8].addOption('La capacidad de analizar datos y extraer insights.')

questionary.addQuestion('¿Qué tipo de equipo te gustaría formar parte?')
questionary.questions[9].addOption('Un equipo de diseño y UX.')
questionary.questions[9].addOption('Un equipo de desarrollo backend.')
questionary.questions[9].addOption('Un equipo de desarrollo móvil.')
questionary.questions[9].addOption('Un equipo de ciencia de datos.')

questionary.addQuestion('¿Qué te gustaría lograr a largo plazo en tu carrera?')
questionary.questions[10].addOption(
  'Crear productos digitales con una interfaz de usuario excepcional.'
)
questionary.questions[10].addOption('Desarrollar aplicaciones escalables y eficientes.')
questionary.questions[10].addOption(
  'Crear aplicaciones móviles que cambien la forma en que las personas interactúan con el mundo.'
)
questionary.questions[10].addOption(
  'Utilizar datos para resolver problemas del mundo real y tomar decisiones estratégicas.'
)

/*
  * Creando la "app" en la terminal *

- Se ejecuta en Node.js, importando el módulo Readline/promises (https://nodejs.org/api/readline.html)
- Se ha instalado Picocolors, un librería para colorear texto en la terminal (https://www.npmjs.com/package/picocolors)

*/

import * as readline from 'readline/promises'
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

import pc from 'picocolors'

console.clear()

const name = await rl.question('\nDime tu nombre, querido alumno. ')

for (const id in questionary.questions) {
  const question = questionary.questions[id]

  let message = pc.gray('¡Descubre a cuál casa perteneces!')
  let answer = ''

  while (!Object.keys(question.options).includes(answer.toUpperCase())) {
    console.clear()
    console.log(`\nBienvenido seas, ${pc.bold(name)}. ${message}`)

    console.log(`\n${pc.blue(id)}. ${question.title}\n`)

    for (const letter in question.options) {
      console.log(` - ${pc.green(letter)}. ${question.options[letter] || 'Opción vacía'}`)
    }

    answer = await rl.question(pc.gray('\nIndica la opción de tu preferencia. '))

    message = pc.yellow('Elije una opción válida, por favor.')
  }

  questionary.results[answer.toUpperCase()]++
}

// Mostrando los resultados del cuestionario

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

const { letter, wasRandomized } = questionary.getWinnerLetter()

const resultMessage = conditions[letter] || pc.red('Ha ocurrido algun error inesperado')

console.log(resultMessage)

if (wasRandomized) {
  console.log('\nFue una decisión difícil debido a que hubo empate en algunas preguntas')
}

console.log(' ')
console.log(`Total de respuestas ${pc.green('A')}: ${pc.yellow(questionary.results.A)}.`)
console.log(`Total de respuestas ${pc.green('B')}: ${pc.yellow(questionary.results.B)}.`)
console.log(`Total de respuestas ${pc.green('C')}: ${pc.yellow(questionary.results.C)}.`)
console.log(`Total de respuestas ${pc.green('B')}: ${pc.yellow(questionary.results.D)}. `)

rl.close()
