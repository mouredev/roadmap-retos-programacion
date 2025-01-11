/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */

// Pilas (Stacks - LIFO)  (Last In, First Out)
const pilaDias = ["lunes", "martes", "miercoles", "jueves", "viernes"];
//console.log(pilaDias);

pilaDias.push("sabado");
//console.log(pilaDias);

pilaDias.pop();
//console.log(pilaDias);

// Colas (Queues - FIFO)  (First In, First Out)
const colaDias = ["lunes", "martes", "miercoles", "jueves", "viernes"];

colaDias.push("sabado");
//console.log(colaDias);

colaDias.shift();
//console.log(colaDias);

/*
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

const readline = require("readline");
const { log } = require("util");
const { url } = require("inspector");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let paginaActual = [];

const atras = "atras";
const siguiente = "siguiente";

function preguntar() {
  rl.question("Ingrese una opcion atras o siguiente: ", (input) => {
    const url = input;
    if (input === atras && paginaActual.length == []) {
      console.log("Primero debes ingresar un url");
      preguntar();
    } else if (input === siguiente) {
      rl.question("ingrese un url: ", (input) => {
        const url = input;
        console.log(`Página actual: ${url}`);
        paginaActual.push(url);
        console.log(paginaActual);
        preguntar();
      });
    } else if (input === siguiente && paginaActual.length != []) {
      console.log("Hola");
    } else if (input !== atras && input !== siguiente) {
      console.log("Opción inválida");
      preguntar();
    }
  });
}

preguntar();

/* rl.question("Ingrese un url: ", (input) => {
  const url = input;
  console.log(`Página actual: ${url}`);
  paginaAdelante.push(url);
  console.log(paginaAdelante);
}); */
