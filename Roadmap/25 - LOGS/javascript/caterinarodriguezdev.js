/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
 */

console.log("Mensaje general 💚");
console.error("Mensaje de error 🔴");
console.warn("Mensaje de alerta 🚩");
console.info("Mensaje informativo ℹ️");
console.debug("Mensaje de depuración");
console.trace("Mensaje detallado sobre la ejecución del programa 🔢");

console.group("Lista de mensajes");
console.log("M1");
console.log("M2");
console.log("M3");
console.groupEnd();

console.time("tiempoEjecucion");
console.timeEnd("tiempoEjecucion");

console.log("-----------------DIFICULTAD EXTRA-------------");

const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

let tareas = [];

const gestorTareas = () => {
  console.log(`Menú:
        1. Añadir tarea
        2. Eliminar tarea
        3. Listar tareas\n`);

  rl.question(
    "Bienvenido al gestor de tareas, elija una opción -> ",
    (resp) => {
      switch (resp) {
        case "1":
          rl.question("\n¿Qué tarea quieres añadir? -> ", (resp) => {
            tareas.push(resp);
            console.log("Añadiendo tarea: ", resp);
            gestorTareas();
          });
          break;
        case "2":
          rl.question("\n¿Qué tarea deseas eliminar? -> ", (resp) => {
            console.log("\n");
            tareas = tareas.filter((tarea) => tarea !== resp);
            console.log("Se ha eliminado la tarea: ", resp);
            gestorTareas();
          });
          break;
        case "3":
          tareas.forEach((tarea) => console.log(`- ${tarea}\n`));
          gestorTareas();
          break;
        default:
          console.log("\nElija una opción disponible");
          gestorTareas();
      }
    }
  );
};

gestorTareas();
