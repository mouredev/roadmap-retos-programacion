/*
  EJERCICIO:
  Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
  de programación de Hogwarts para magos y brujas del código.
  En ella, su famoso sombrero seleccionador ayuda a los programadores
  a encontrar su camino...
  Desarrolla un programa que simule el comportamiento del sombrero.
  Requisitos:
  1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
  2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
     (Puedes elegir las que quieras)
  Acciones:
  1. Crea un programa que solicite el nombre del alumno y realice 10
     preguntas, con cuatro posibles respuestas cada una.
  2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
  3. Una vez finalizado, el sombrero indica el nombre del alumno 
     y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
     pero indicándole al alumno que la decisión ha sido complicada).
*/

let userName = "";
let frontEndHouse = 0;
let backEndHouse = 0;
let mobileHouse = 0;
let dataScienceHouse = 0;
const questions = [
  "1. ¿Qué prefieres jugar?: \na) Super Metroid \nb) Ajedrez \nc) Pokémon Go \nd) Sudoku",
  "2. ¿Con qué actividad te identificas más?: \na) Dibujar \nb) Doblar la ropa \nc) Editar fotos en el teléfono \nd) Acomodar la despensa",
  "3. ¿Dónde te gusta más escuchar música?: \na) Audífonos  \nb) Mini componente \nc) Bocina portatil \nd) Donde sea pero Hi-Res",
  "4. ¿Qué superhéroe es tu favorito?: \na) Spider-Man \nb) Superman \nc) Flash \nd) Doctor Strange",
  "5. Si volvieras a cursar una materia, ¿cuál sería?: \na) Biología \nb) Cálculo diferencial e integral \nc) Física \nd) Probabilidad y estadística",
  "6. Si te regalaran un dispositivo electrónico, ¿cuál elegirías?: \na) MacBook \nb) PC \nc) Smartphone \nd) Raspberry Pi",
  "7. ¿Qué recurso utilizarías para administrar tus finanzas?: \na) Aplicación de escritorio \nb) Papel y lápiz \nc) Aplicación móvil \nd) Hoja de cálculo",
  "8. ¿Qué te llama más la atención en un sitio web?: \na) La apariencia \nb) Las validaciones en un formulario \nc) La adaptación a medidas pequeñas \nd) La información que muestra",
  "9. ¿Qué lenguaje de programación es tu favorito?: \na) JavaScript \nb) Python \nc) Swift \nd) SQL",
  "10. ¿Con qué persona te sientes más identificado?: \na) Miguel Durán \nb) Héctor de León \nc) Brais Moure \nd) Rafa Gonzalez Gouveia",
];

userName = prompt("Por favor, ingresa tu nombre:");

for (let index = 0; index < questions.length; index++) {
  let quiz = prompt(questions[index]);

  switch (quiz.toLowerCase()) {
    case "a":
      frontEndHouse += 4;
      break;

    case "b":
      backEndHouse += 4;
      break;

    case "c":
      mobileHouse += 4;
      break;

    case "d":
      dataScienceHouse += 4;
      break;

    default:
      alert("Por favor, selecciona una opción válida.");

      index--;
      break;
  }
}

let allHouses = {
  "Front-end": frontEndHouse,
  "Back-end": backEndHouse,
  "Mobile": mobileHouse,
  "Data Science": dataScienceHouse,
};
let houseNames = Object.keys(allHouses);
let higherScore = Math.max.apply(null, houseNames.map((houseScore) => allHouses[houseScore]));
let chosenHouse = houseNames.reduce((house, score) => {
  if (allHouses[score] === higherScore) {
    house.push(score);
  }

  return house;
}, []);
let randomSelection = Math.round(Math.random() * (chosenHouse.length - 1) + 1) - 1;

if (chosenHouse.length > 1) {
  console.log(`${userName}, la decisión ha sido complicada, pero pertenecerás a la casa de ${chosenHouse[randomSelection]}.`);
} else {
  console.log(`${userName}, pertenecerás a la casa de ${chosenHouse[0]}.`);
}
