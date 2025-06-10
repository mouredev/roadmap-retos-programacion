/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
*/

// "+++++++++ EJERCICIO +++++++++"
console.log("+++++++++ PILA +++++++++");
var names = ["Peter", "Felicia"];

console.log("La pila inicial:");
console.log(names);
console.log("Se agregan dos elementos:");
names.push("MJ");
names.push("Gwen");
console.log(names);
names.pop();
console.log(`Se elimina el último elemento:`);
console.log(names);

console.log("\n+++++++++ COLA +++++++++");
var numbers = [7, 19, 15];

console.log("La cola inicial:");
console.log(numbers);
numbers.push(2018);
numbers.push(2019);
console.log("Se agregan dos nuevos elementos:");
console.log(numbers);
numbers.shift();
console.log("Se elimina el primer elemento:");
console.log(numbers);

// +++++++++ DIFICULTAD EXTRA +++++++++
console.log("\n+++++++++ CONTROLES DEL NAVEGADOR WEB +++++++++");
var pages = [];

function previousPage() {
  if (pages.length > 0) {
    pages.pop();
  }
    
  if (pages.length >= 1) {
    alert(`Navegaste a la página anterior: ${pages[pages.length - 1]}`);
  } else {
    alert("No existe página para retroceder.");
  }
}

function nextPage() {
  alert("No fue posible construir la funcionalidad de navegación adelante con los principios de una pila.");
}

function addPage() {
  pages.push(controls);
  alert(`Navegando a la página web "${controls}"`);
}

while (controls !== "Salir") {
  var controls = prompt("Elige la opción para navegar: \n[Escribe el nombre de la página] | Atrás | Adelante | Salir");

  switch (controls) {
    case "Atrás":
      previousPage();
      break;

    case "Adelante":
      nextPage();
      break;

    case "Salir":
      alert("Cerrando el navegador...");
      break;

    default:
      addPage();
      break;
  }
}

console.log("\n+++++++++ IMPRESORA +++++++++");
var documents = [];

function printDocument() {
  if (documents.length > 0) {
    var printDocument = documents.shift();
    alert(`El documento "${printDocument}" fue impreso.`);
  } else {
    alert("No hay documentos en la cola.");
  }
}

function sendDocument() {
  documents.push(instruction);
  alert(`El documento "${documents[documents.length -1]}" se envió a la cola.`);
}

while (instruction !== "Salir") {
  var instruction = prompt("Escribe la acción que debe realizar la impresora: \n[Escribe el nombre del documento a enviar] | Imprimir | Salir");

  switch (instruction) {
    case "Imprimir":
      printDocument();
      break;

    case "Salir":
      alert("Apagando la impresora...");
      break;

    default:
      sendDocument();
      break;
  }
}
