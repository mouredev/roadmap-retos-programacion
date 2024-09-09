const readline = require("readline")

const preguntas = [
  {
    pregunta: "¿Qué parte de un proyecto disfrutas más?",
    opciones: [
      {
        respuesta: "Crear interfaces interactivas y atractivas",
        casa: "Frontend",
      },
      {
        respuesta: "Diseñar la estructura de datos y las bases de datos",
        casa: "Backend",
      },
      {
        respuesta: "Desarrollar aplicaciones móviles",
        casa: "Mobile",
      },
      {
        respuesta: "Implementar sistemas de seguridad y control de acceso",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Cuál es tu lenguaje de programación favorito?",
    opciones: [
      {
        respuesta: "JavaScript",
        casa: "Frontend",
      },
      {
        respuesta: "Python",
        casa: "Backend",
      },
      {
        respuesta: "Swift",
        casa: "Mobile",
      },
      {
        respuesta: "R",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Qué herramienta te resulta más útil en tu trabajo diario?",
    opciones: [
      {
        respuesta: "Visual Studio Code",
        casa: "Frontend",
      },
      {
        respuesta: "Git y GitHub",
        casa: "Backend",
      },
      {
        respuesta: "Docker y Kubernetes",
        casa: "Mobile",
      },
      {
        respuesta: "Jupyter Notebooks",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Cómo prefieres gestionar tus proyectos?",
    opciones: [
      {
        respuesta: "Utilizando versiones de control",
        casa: "Frontend",
      },
      {
        respuesta: "Utilizando un herramienta de planeamiento",
        casa: "Backend",
      },
      {
        respuesta: "Utilizando un herramienta de gestión de proyectos",
        casa: "Mobile",
      },
      {
        respuesta: "Utilizando un herramienta de planificación",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Qué parte de la depuración de código disfrutas más?",
    opciones: [
      {
        respuesta: "Encontrar errores visuales en las interfaces",
        casa: "Frontend",
      },
      {
        respuesta: "Corregir problemas de rendimiento en el servidor",
        casa: "Backend",
      },
      {
        respuesta: "Desarrollar nuevas características y funciones",
        casa: "Mobile",
      },
      {
        respuesta: "Optimizar algoritmos de procesamiento de datos",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Cuál sería tu rol ideal en un equipo de desarrollo?",
    opciones: [
      {
        respuesta: "Desarrollador/Diseñador Frontend",
        casa: "Frontend",
      },
      {
        respuesta: "Arquitecto de Soluciones Backend",
        casa: "Backend",
      },
      {
        respuesta: "Desarrollador de Aplicaciones Móviles",
        casa: "Mobile",
      },
      {
        respuesta: "Científico de Datos",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Cómo prefieres aprender nuevas tecnologías?",
    opciones: [
      {
        respuesta:
          "Experimentando con nuevas librerías y frameworks de frontend",
        casa: "Frontend",
      },
      {
        respuesta:
          "Trabajando con nuevas tecnologías de servidores y bases de datos",
        casa: "Backend",
      },
      {
        respuesta: "Explorando nuevas plataformas de desarrollo móvil",
        casa: "Mobile",
      },
      {
        respuesta:
          "Analizando nuevos algoritmos y técnicas de procesamiento de datos",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Qué tipo de proyectos te motivan más?",
    opciones: [
      {
        respuesta: "Crear interfaces web interactivas y atractivas",
        casa: "Frontend",
      },
      {
        respuesta: "Desarrollar sistemas robustos y escalables en la nube",
        casa: "Backend",
      },
      {
        respuesta:
          "Desarrollar aplicaciones móviles con excelente experiencia de usuario",
        casa: "Mobile",
      },
      {
        respuesta: "Proyectos de análisis y visualización de datos",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Qué tecnología te gustaría dominar en el futuro?",
    opciones: [
      {
        respuesta: "WebAssembly y animaciones avanzadas en la web",
        casa: "Frontend",
      },
      {
        respuesta: "Inteligencia Artificial y Machine Learning en servidores",
        casa: "Backend",
      },
      {
        respuesta: "Realidad aumentada en aplicaciones móviles",
        casa: "Mobile",
      },
      {
        respuesta: "Big Data y análisis de grandes volúmenes de información",
        casa: "Data",
      },
    ],
  },
  {
    pregunta: "¿Cómo te gusta colaborar en un equipo?",
    opciones: [
      {
        respuesta: "Diseñando y mejorando la experiencia de usuario",
        casa: "Frontend",
      },
      {
        respuesta: "Integrando servicios y APIs en el backend",
        casa: "Backend",
      },
      {
        respuesta: "Asegurando la mejor experiencia en aplicaciones móviles",
        casa: "Mobile",
      },
      {
        respuesta: "Proporcionando análisis detallados a partir de los datos",
        casa: "Data",
      },
    ],
  },
]

const puntosCasas = {
  Frontend: 0,
  Backend: 0,
  Mobile: 0,
  Data: 0,
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})
const prompt = (query) => new Promise((resolve) => rl.question(query, resolve))

// When done reading prompt, exit program
rl.on("close", () => process.exit(0))
