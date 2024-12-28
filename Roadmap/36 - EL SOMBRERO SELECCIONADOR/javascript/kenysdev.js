/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
# 36 EL SOMBRERO SELECCIONADOR
-------------------------------------------------------
* EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno 
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada).
*/
// ________________________________________________________

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const getInput = (prompt) => {
  return new Promise((resolve) => {
    rl.question(prompt, (input) => {
      resolve(input.trim());
    });
  });
};

const HOUSES = ["Frontend", "Backend", "Mobile", "Data"];

const QUESTIONS = [
  "¿Qué te atrae más?",
  "¿Qué superhéroe de la programación te gustaría ser?",
  "En un proyecto de software, ¿qué rol te emociona más?",
  "Si tu código fuera una obra de arte, ¿qué estilo tendría?",
  "¿Qué animal de programación serías?",
  "En una hackathon, ¿qué tipo de proyecto propondrías?",
  "Si tu carrera en tech fuera una película, ¿de qué género sería?",
  "¿Qué herramienta de programación no puede faltar en tu caja de herramientas digital?",
  "Si pudieras resolver un gran problema en tech, ¿cuál elegirías?",
  "¿Qué tipo de equipo prefieres?",
];

const ANSWERS = [
  ["Crear experiencias visuales.", "Solucionar problemas de funcionamiento.", "Innovar en dispositivos portátiles.", "Descubrir tendencias ocultas."],
  ["Diseñador de Interfaces, creando experiencias asombrosas", "Arquitecto de Sistemas, construyendo estructuras robustas", "Mago de Apps, conjurando soluciones móviles", "Explorador de Datos, descubriendo tesoros ocultos"],
  ["Director de UX, orquestando la sinfonía visual", "Ingeniero de Backend, dominando la lógica del servidor", "Desarrollador de Apps, llevando la potencia al bolsillo", "Científico de Datos, descifrando los secretos de la información"],
  ["Minimalismo elegante, como una landing page perfecta", "Arquitectura compleja, como un sistema distribuido", "Diseño adaptativo, fluyendo en diferentes dispositivos", "Visualización de datos, pintando historias con números"],
  ["Un camaleón, adaptándome a diferentes frameworks", "Un pulpo, manejando múltiples servicios a la vez", "Un colibrí, ágil y siempre en movimiento", "Una lechuza, analizando datos con sabiduría"],
  ["Una web app que revolucione la experiencia del usuario", "Un sistema de IA que optimice procesos backend", "Una app móvil que cambie la forma de interactuar con el mundo", "Un proyecto de big data que prediga tendencias futuras"],
  ["Comedia romántica con JavaScript y CSS", "Thriller de ciencia ficción con microservicios", "Aventura de acción en el mundo de las apps", "Documental profundo sobre el universo de los datos"],
  ["Un editor de código con plugins para diseño visual", "Una robusta suite de testing y depuración", "Un emulador multi-dispositivo de última generación", "Una plataforma de análisis de datos en tiempo real"],
  ["Hacer que la accesibilidad web sea universal", "Crear una arquitectura de software autorreparable", "Desarrollar una plataforma de AR/VR para educación móvil", "Construir un modelo de IA ético y transparente"],
  ["Creativos enfocados en diseño.", "Técnicos que construyen sistemas.", "Especialistas en aplicaciones móviles.", "Expertos en datos y análisis."],
];

class SortingHat {
  constructor(name) {
    this.name = name;
    this.scores = HOUSES.reduce((acc, house) => {
      acc[house] = 0;
      return acc;
    }, {});
  }

  async askQuestion(qNum, question, answers) {
    console.log(`\n#${qNum}: ${question}`);
    answers.forEach((answer, index) => {
      console.log(`${index + 1}) ${answer}`);
    });

    while (true) {
      const input = await getInput("Elige tu respuesta (1-4): ");
      const choice = parseInt(input, 10) - 1;

      if (!isNaN(choice) && choice >= 0 && choice < HOUSES.length) {
        this.scores[HOUSES[choice]] += 1;
        break;
      } else {
        console.log("Por favor, elige un número entre 1 y 4.");
      }
    }
  }

  selectHouse() {
    const maxScore = Math.max(...Object.values(this.scores));
    const topHouses = Object.keys(this.scores).filter(
      (house) => this.scores[house] === maxScore
    );

    if (topHouses.length > 1) {
      console.log("\nLa decisión ha sido complicada.");
      return topHouses[Math.floor(Math.random() * topHouses.length)];
    }

    return topHouses[0];
  }
}

const main = async () => {
  console.log("EL SOMBRERO SELECCIONADOR");
  const name = await getInput("¿Cuál es tu nombre? : ");
  const hat = new SortingHat(name);

  for (let i = 0; i < QUESTIONS.length; i++) {
    await hat.askQuestion(i + 1, QUESTIONS[i], ANSWERS[i]);
  }

  const selectedHouse = hat.selectHouse();
  console.log(`\n'${name}' pertenecerá a la casa '${selectedHouse}'\n`);
  rl.close();
};

main();
