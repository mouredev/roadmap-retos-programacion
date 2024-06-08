// STACK
let stack = [];

stack.push("persona1");
stack.push("persona2");

console.log(stack);

stack.pop();
console.log(stack);

// QUEUE
let queue = [];

queue.push("persona3");
queue.push("persona4");

console.log(queue);

queue.shift();
console.log(queue);

// EJERCICIO
stacks = [];

function navigation() {
  let action = prompt("Introduzca la acción a realizar: ");

  if (action == "salir") {
    console.log("Saliendo del sistema");
  } else if (action == "Adelante") {
    pass;
  } else if (action == "Atras") {
    if (stacks.length > 0) {
      console.log("Regresando a la página anterior");
      stacks.pop();
    }
  } else {
    stacks.push(action);
  }

  if (stacks.length > 0) {
    console.log("Página actual: " + stacks[stacks.length - 1]);
  } else {
    console.log("Pagina de inicio");
  }
}

navigation();

// EJERCICIO
function shared_printed() {
  let queue = [];

  while (true) {
    let action = prompt("Añade un documento o selecciona imprimir/salir: ");

    if (action == "salir") {
      console.log("Apagando impresora");
      break;
    } else if (action == "imprimir") {
      if (queue.length > 0) {
        console.log("Imprimiendo: " + queue.pop());
      } else {
        console.log("No hay archivos para imprimir");
      }
    } else {
      queue.push(action);
      console.log("Documento añadido a la cola de impresión");
    }
  }
}

shared_printed();
