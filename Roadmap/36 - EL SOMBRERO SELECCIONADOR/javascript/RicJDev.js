// Modelado de preguntas y cuestionario

class Question {
  constructor(title, id = 0) {
    this.id = id
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
      console.log(`Se han llenado todas las opciones. No se pudo agregar "${option}"`)
    }
  }

  editOption(letter, newOption) {
    if (this.options[letter]) {
      this.options[letter] = newOption
    } else {
      console.log('Está intentando acceder a una opción inexistente')
    }
  }
}

class Questionary {
  constructor() {
    this.questions = {}
  }

  addQuestion(id, question) {
    if (this.questions[id]) {
      console.log('Esta pregunta ya existe en el cuestionario.')
    } else {
      this.questions[id] = question
      question.id = id
    }
  }

  printQuestion(id) {
    const question = this.questions[id]

    for (const letter in question.options) {
        console.log(` - ${letter}. ${question.options[letter] || 'Opción vacía'}`)
    }
  }

  printAllQuestions() {
    for (const id in this.questions) {
      const currentQuestion = this.questions[id]

      console.log(`\n${id}. ${currentQuestion.title}\n`)
      this.printQuestion(id)
    }
  }
}

// Implementamos las clases para crear el cuestionario

const questionary = new Questionary()

questionary.addQuestion(1, new Question('¿Qué parte de un sitio web te llama más la atención?'))

questionary.questions[1].addOption('El diseño visual y la interfaz de usuario.')
questionary.questions[1].addOption(
  'La lógica detrás de cómo funciona el sitio y cómo se conectan las diferentes partes.'
)
questionary.questions[1].addOption('Cómo se ve y funciona la aplicación en un teléfono móvil.')
questionary.questions[1].addOption(
  'Los datos que se recolectan y cómo se utilizan para mejorar el sitio.'
)

questionary.addQuestion(
  2,
  new Question(
    'Si tuvieras que elegir entre crear una nueva aplicación móvil o diseñar una base de datos, ¿cuál preferirías?'
  )
)
questionary.questions[2].addOption('Crear una aplicación móvil con una interfaz intuitiva.')
questionary.questions[2].addOption(
  'Diseñar una base de datos eficiente para almacenar grandes cantidades de información.'
)
questionary.questions[2].addOption('Ambas opciones me parecen igualmente interesantes.')
questionary.questions[2].addOption('Ninguna de las opciones me llama la atención.')

questionary.addQuestion(3, new Question('¿Qué te resulta más fácil de entender?'))
questionary.questions[3].addOption('Diagramas de flujo y diseños visuales.')
questionary.questions[3].addOption('Código y algoritmos.')
questionary.questions[3].addOption('Prototipos y maquetas.')
questionary.questions[3].addOption('Gráficos y estadísticas.')

questionary.addQuestion(4, new Question('¿Qué tipo de problemas te gusta resolver?'))
questionary.questions[4].addOption(
  'Problemas relacionados con la estética y la experiencia del usuario.'
)
questionary.questions[4].addOption('Problemas lógicos y de optimización.')
questionary.questions[4].addOption(
  'Problemas relacionados con la portabilidad y la compatibilidad en diferentes dispositivos.'
)
questionary.questions[4].addOption(
  'D',
  'Problemas relacionados con la extracción de información útil de grandes conjuntos de datos.'
)

questionary.addQuestion(5, new Question('¿Qué herramienta te resulta más interesante?'))
questionary.questions[5].addOption('Photoshop o Figma.')
questionary.questions[5].addOption('Python o Java.')
questionary.questions[5].addOption('XCode o Android Studio.')
questionary.questions[5].addOption('SQL o Tableau.')

questionary.addQuestion(6, new Question('¿Qué te gustaría hacer en tu tiempo libre?'))
questionary.questions[6].addOption('Diseñar interfaces de usuario para diferentes aplicaciones.')
questionary.questions[6].addOption('Desarrollar videojuegos o aplicaciones web.')
questionary.questions[6].addOption('Crear aplicaciones móviles para diferentes plataformas.')
questionary.questions[6].addOption('Analizar datos y crear visualizaciones.')

questionary.addQuestion(7, new Question('¿Qué tipo de proyectos te motivan más?'))
questionary.questions[7].addOption('Proyectos que tienen un impacto visual y estético.')
questionary.questions[7].addOption(
  'Proyectos que requieren resolver problemas complejos y optimizar el rendimiento.'
)
questionary.questions[7].addOption(
  'Proyectos que pueden ser utilizados por muchas personas en sus dispositivos móviles.'
)
questionary.questions[7].addOption('Proyectos que utilizan datos para tomar decisiones informadas.')

questionary.addQuestion(
  8,
  new Question('¿Qué habilidad consideras más importante para un desarrollador?')
)
questionary.questions[8].addOption('La creatividad y el sentido del diseño.')
questionary.questions[8].addOption('La capacidad de resolver problemas y pensar de forma lógica.')
questionary.questions[8].addOption(
  'La adaptabilidad y la capacidad de aprender nuevas tecnologías.'
)
questionary.questions[8].addOption('La capacidad de analizar datos y extraer insights.')

questionary.addQuestion(9, new Question('¿Qué tipo de equipo te gustaría formar parte?'))
questionary.questions[9].addOption('Un equipo de diseño y UX.')
questionary.questions[9].addOption('Un equipo de desarrollo backend.')
questionary.questions[9].addOption('Un equipo de desarrollo móvil.')
questionary.questions[9].addOption('Un equipo de ciencia de datos.')

questionary.addQuestion(10, new Question('¿Qué te gustaría lograr a largo plazo en tu carrera?'))
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
