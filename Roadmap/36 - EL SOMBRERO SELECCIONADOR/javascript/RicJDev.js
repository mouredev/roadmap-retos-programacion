/*
  TODO: Estas preguntas fueron generadas por IA. Recordar revisarlas

  LISTADO DE PREGUNTAS

  1. ¿Qué parte de un sitio web te llama más la atención?

   - A) El diseño visual y la interfaz de usuario.
   - B) La lógica detrás de cómo funciona el sitio y cómo se conectan las diferentes partes.
   - C) Cómo se ve y funciona la aplicación en un teléfono móvil.
   - D) Los datos que se recolectan y cómo se utilizan para mejorar el sitio.

  2. Si tuvieras que elegir entre crear una nueva aplicación móvil o diseñar una base de datos, ¿cuál preferirías?

   - A) Crear una aplicación móvil con una interfaz intuitiva.
   - B) Diseñar una base de datos eficiente para almacenar grandes cantidades de información.
   - C) Ambas opciones me parecen igualmente interesantes.
   - D) Ninguna de las opciones me llama la atención.

  3. ¿Qué te resulta más fácil de entender?

   - A) Diagramas de flujo y diseños visuales.
   - B) Código y algoritmos.
   - C) Prototipos y maquetas.
   - D) Gráficos y estadísticas.

  4. ¿Qué tipo de problemas te gusta resolver?

   - A) Problemas relacionados con la estética y la experiencia del usuario.
   - B) Problemas lógicos y de optimización.
   - C) Problemas relacionados con la portabilidad y la compatibilidad en diferentes dispositivos.
   - D) Problemas relacionados con la extracción de información útil de grandes conjuntos de datos.

  5. ¿Qué herramienta te resulta más interesante?

   - A) Photoshop o Figma.
   - B) Python o Java.
   - XCode o Android Studio.
   - D) SQL o Tableau.

  6. ¿Qué te gustaría hacer en tu tiempo libre?

   - A) Diseñar interfaces de usuario para diferentes aplicaciones.
   - B) Desarrollar videojuegos o aplicaciones web.
   - C) Crear aplicaciones móviles para diferentes plataformas.
   - D) Analizar datos y crear visualizaciones.

  7. ¿Qué tipo de proyectos te motivan más?

   - A) Proyectos que tienen un impacto visual y estético.
   - B) Proyectos que requieren resolver problemas complejos y optimizar el rendimiento.
   - C) Proyectos que pueden ser utilizados por muchas personas en sus dispositivos móviles.
   - D) Proyectos que utilizan datos para tomar decisiones informadas.

  8. ¿Qué habilidad consideras más importante para un desarrollador?

   - A) La creatividad y el sentido del diseño.
   - B) La capacidad de resolver problemas y pensar de forma lógica.
   - C) La adaptabilidad y la capacidad de aprender nuevas tecnologías.
   - D) La capacidad de analizar datos y extraer insights.

  9. ¿Qué tipo de equipo te gustaría formar parte?

   - A) Un equipo de diseño y UX.
   - B) Un equipo de desarrollo backend.
   - C) Un equipo de desarrollo móvil.
   - D) Un equipo de ciencia de datos.

  10. ¿Qué te gustaría lograr a largo plazo en tu carrera?

    - A) Crear productos digitales con una interfaz de usuario excepcional.
    - B) Desarrollar aplicaciones escalables y eficientes.
    - C) Crear aplicaciones móviles que cambien la forma en que las personas interactúan con el mundo.
    - D) Utilizar datos para resolver problemas del mundo real y tomar decisiones estratégicas.

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
      console.log(`Se han llenado todas las opciones. No se pudo agregar "${option}"`)
    }
  }

  editOption(letter, newOption) {
    if (Object.keys(this.options).includes(letter)) {
      this.options[letter] = newOption
    } else {
      console.log('Esta intentando acceder a una opcion inexistente')
    }
  }
}

class Questionary {
  constructor() {
    this.questions = {}
  }

  addQuestion(question) {
    const id = Object.keys(this.questions).length + 1

    this.questions[id] = question
    question.id = id
  }

  printAllQuestions() {
    for (const id in this.questions) {
      const currentQuestion = this.questions[id]

      console.log(`\n${id}. ${currentQuestion.title}\n`)

      for (const letter in currentQuestion.options) {
        console.log(` - ${letter}. ${currentQuestion.options[letter]}`)
      }
    }
  }
}

const q1 = new Question('¿Qué parte de un sitio web te llama más la atención?')

q1.addOption('El diseño visual y la interfaz de usuario.')
q1.addOption('La lógica detrás de cómo funciona el sitio y cómo se conectan las diferentes partes.')
q1.addOption('Cómo se ve y funciona la aplicación en un teléfono móvil.')
q1.addOption('Los datos que se recolectan y cómo se utilizan para mejorar el sitio.')
q1.addOption('Cómo se ha estructurado y maquetado el contenido.')

const myQuestionary = new Questionary()

myQuestionary.addQuestion(q1)
myQuestionary.printAllQuestions()
