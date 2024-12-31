/*
 * EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 * 
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado 
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *   
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
*/

const readlinePromises = require("readline/promises");
const fs = require('fs');
const rl = readlinePromises.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputs = ["Meta", "Cantidad", "Unidades", "Plazo"];
const months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
let purposes = [];
let monthCounter = 1;
let results = 'Planificación de objetivos - 2025\n';

(async () => {
  for (let objectiveIndex = 0; objectiveIndex < 2; objectiveIndex++) {
    let objectiveNumber = objectiveIndex + 1;

    purposes.push({});

    console.log(`\nObjetivo #${objectiveNumber}\n`);

    for (let index = 0; index < inputs.length; index++) {
      const input = await rl.question(`${inputs[index]}: `);

      purposes[objectiveIndex][inputs[index]] = input;
    }
  }

  purposes.forEach(function(key) {
    key["Cantidad"] = parseInt(key["Cantidad"]);
    key["Plazo"] = parseInt(key["Plazo"]);
  });

  for (let month = 0; month < months.length; month++) {
    results = results + `\n${months[month]}:\n`;

    purposes.forEach((purpose, index) => {
      let goalNumber = index + 1;
      let goal = purpose["Meta"];
      let units = purpose["Unidades"];
      let total = purpose["Cantidad"];
      let deadLine = purpose["Plazo"];
      let unitsPerMonth = purpose["Cantidad"] / purpose["Plazo"];

      if (monthCounter <= deadLine) {
        results = results + `[] ${goalNumber}. ${goal} (${unitsPerMonth} ${units}/mes). Total: ${total}.\n`;
      }
    });

    monthCounter++;
  }

  fs.writeFile('objetivos-2025.txt', results, 'utf8', (error) => {
    if (error) {
      console.error('Ocurrió un error al intentar exportar el archivo: ', error);

      return;
    }

    console.log('El archivo fue creado exitosamente.');
  });

  rl.close();
})();
