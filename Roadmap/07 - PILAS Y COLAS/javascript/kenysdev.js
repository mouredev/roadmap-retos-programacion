/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#07 PILAS Y COLAS
---------------------------------------
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo Forward/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar Forward o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "Forward", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
*/

// ________________________________________________________
// Pilas (Stack - LIFO):
// - Estructura de datos que sigue el principio LIFO (Last In, First Out).
// - El último elemento agregado es el primero en ser retirado.

class Stack {
  constructor() {
      this.elements = [];
  }

  // Total de elementos
  get length() {
      return this.elements.length;
  }

  // Verificar si la pila está vacía
  isEmpty() {
      return this.length === 0;
  }

  // Agregar un elemento
  push(item) {
      this.elements.push(item);
  }

  // Agregar múltiples elementos
  pushBatch(items) {
      this.elements.push(...items);
  }

  // Eliminar y obtener el elemento superior
  pop() {
      return this.isEmpty() ? null : this.elements.pop();
  }

  // Obtener el elemento superior sin eliminarlo
  peek() {
      return this.isEmpty() ? null : this.elements[this.elements.length - 1];
  }

  // Obtener la pila como tupla
  toArray() {
      return [...this.elements].reverse();
  }

  // Vaciar la pila
  clear() {
      this.elements = [];
  }
}

// ________________________________________________________
// Ejercicio: Historial de navegación

const MsgNav = `
  Historial de navegación:
  -------------------------------------------------
  Usar: "<" para página anterior.
        ">" para página Forward.
        "h" Ver historial completo.
        "x" para salir.
  Escribir web para agregar:
  -------------------------------------------------`;

function NavHistory() {
  const BackHistory = new Stack();
  const forwardHistory = new Stack();
  const history = new Stack();
  history.push("Inicio");

  const ShowHistory = () => {
      console.log(MsgNav);
      ShowStatus(history.peek());
      SelectAction();
  };

  const ShowStatus = (url) => {
      console.log(`(${BackHistory.length}) <- Atrás <- [Actual: ${url}] -> Forward -> (${forwardHistory.length})`);
  };

  const Back = () => {
      if (!BackHistory.isEmpty()) {
          forwardHistory.push(history.pop());
          history.push(BackHistory.pop());
          ShowStatus(history.peek());
      } else {
          console.log("No hay página previa.");
      }
      SelectAction();
  };

  const Forward = () => {
      if (!forwardHistory.isEmpty()) {
          BackHistory.push(history.pop());
          history.push(forwardHistory.pop());
          ShowStatus(history.peek());
      } else {
          console.log("No hay página siguiente.");
      }
      SelectAction();
  };

  const NewWeb = (url) => {
      BackHistory.push(history.peek());
      forwardHistory.clear();
      history.push(url);
      ShowStatus(history.peek());
      SelectAction();
  };

  const PrintHistory = () => {
      const historial = history.toArray();
      console.log(historial.length ? historial.join(" -> ") : "Historial vacío.");
      SelectAction();
  };

  const SelectAction = () => {
      console.log("____________");
      rl.question("Acción: ", (option) => {
          switch (option) {
              case "<":
                  Back();
                  break;
              case ">":
                  Forward();
                  break;
              case "h":
                  PrintHistory();
                  break;
              case "x":
                  rl.close;
                  main();
                  return;
              default:
                  NewWeb(option);
          }
      });
  };

  ShowHistory();
}

// ________________________________________________________
// Colas (Queue - FIFO):
// - Estructura de datos que sigue el principio FIFO (First In, First Out).
// - El primer elemento agregado es el primero en ser retirado.
class Queue {
  constructor() {
      this.elements = [];
  }

  // Total de elementos
  get length() {
      return this.elements.length;
  }

  // Verificar si la cola está vacía
  isEmpty() {
      return this.length === 0;
  }

  // Agregar un elemento
  enqueue(item) {
      this.elements.push(item);
  }

  // Agregar múltiples elementos
  enqueueAll(items) {
      this.elements.push(...items);
  }

  // Eliminar y devolver el primer elemento
  dequeue() {
      return this.isEmpty() ? null : this.elements.shift();
  }

  // Obtener el primer elemento sin eliminarlo
  peek() {
      return this.isEmpty() ? null : this.elements[0];
  }

  // Obtener la cola como tupla
  toArray() {
      return [...this.elements];
  }

  // Vaciar la cola
  clear() {
      this.elements = [];
  }
}

// ________________________________________________________
// Ejercicio: Simulador de impresora

const mensajeImpresora = `
  ------------------------------------------------
  Usar: "p" Imprimir.
        "l" Ver documentos pendientes.
        "x" para salir.
  Escribir nombre de documento para enviar a cola:
  ------------------------------------------------`;

function QueuePrinter() {
  const docQueue = new Queue();
  docQueue.enqueueAll(["a.pdf", "b.txt", "c.docx"]);

  const PrintDoc = () => {
      if (!docQueue.isEmpty()) {
          console.log(`${docQueue.dequeue()} -> ha sido impreso.`);
          console.log(`${docQueue.length} -> archivos faltantes.`);
      } else {
          console.log("No hay archivos.");
      }
      SelectAction();
  };

  const DocPending = () => {
      const documentos = docQueue.toArray();
      console.log(documentos.length ? documentos.join(", ") : "No hay archivos.");
      SelectAction();
  };

  const AddDoc = (doc) => {
      docQueue.enqueue(doc);
      console.log("Archivo agregado a la cola de impresión.");
      SelectAction();
  };

  const SelectAction = () => {
      console.log("____________");
      rl.question("Acción: ", (option) => {
          switch (option) {
              case "p":
                  PrintDoc();
                  break;
              case "l":
                  DocPending();
                  break;
              case "x":
                  rl.close;
                  main();
                  return
              default:
                  AddDoc(option);
          }
      });
  };

  console.log(mensajeImpresora);
  SelectAction();
}

// ________________________________________________________
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const MenuHome = `
  ----------------------------------
  Usar: "1" para simulador de navegador.
        "2" para simulador de impresora.
        "Otra tecla" para salir.
  ----------------------------------`;

function main() {
  console.log(MenuHome);
  rl.question("Seleccionar: ", (option) => {
      switch (option) {
          case "1":
              NavHistory();
              break;
          case "2":
              QueuePrinter();
              break;
          default:
              console.log("Adiós");
              rl.close();
              process.exit();
      }
  });
}

main();
