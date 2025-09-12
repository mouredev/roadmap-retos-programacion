
// Stacks (Pilas)
class Stack {
  constructor() {
    this.stack = []
  }

  push(element) {
    this.stack.push(element)
  }

  pop() {
    if (this.isEmpty()) return "La pila esta vacia";
    return this.stack.pop()
  }

  // Devuelve el ultimo elemento de la pila sin eliminarlo
  peek() {
    return this.stack[this.stack.length - 1]
  }

  isEmpty() {
    return this.stack.length === 0;
  }

  // Devuelve el tamaño del stack
  size() {
    return this.stack.length;
}

// Devuelve una representación en cadena del stack
print() {
  return this.stack.toString();
}

}

const stack = new Stack();

stack.push("Javascript"); 
stack.push("Python");
stack.push("C#");

console.log(stack.print());
console.log(stack.pop()) // Elimina el ultimo elemento de la lista
console.log(stack.peek()); // Ultimo elemento de la lista
console.log(stack.size());
console.log(stack.isEmpty());
console.log(stack.print());

// Queue (Colas)

class Queue {
  constructor() {
    this.queue = []
  }

  // Agregar un elemento a la cola
  enqueue(element) {
    this.queue.push(element)
  }

  // Eliminar elemento de la cola
 dequeue() {
  if (this.isEmpty()) return "La cola esta vacia";
  return this.queue.shift()
 }

 // Devuelve el primer elemento de la cola sin eliminarlo
 front() {
  if (this.isEmpty()) return "La cola esta vacia";
  return this.queue[0];
 }

 // Verificar si la cola esta vacia
 isEmpty() {
  return this.queue.length === 0;
 }

 // Devuelve el tamaño de la cola
 size() {
  return this.items.length;
}

// Devuelve la cola
 print() {
  return this.queue.toString();
 }

 }

const queue = new Queue();
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

console.log(queue.print()) // Imprime la cola
console.log(queue.dequeue()) // Eliminar el primer elemento de la cola
console.log(queue.front()) // Muestra el primer elemento de la cola sin eliminarlo
console.log(queue.isEmpty()) // Revisa si la cola esta vacia
console.log(queue.print()) // Imprime la cola con los ultimos cambios

// DIFICULTAD EXTRA

let webs = []

const readLine = require('readline');
const { PassThrough } = require('stream');
const rl = readLine.createInterface({
  input: process.stdin,
  output: process.stdout
});

function menu() {
  rl.question('\nAgrega una url o navega utilizando adelante/atras o "salir" para terminar el programa ', (accion) => {
    if(accion){
      navegacion(accion);
    } else {
      console.log('Debes introducir algo')
      menu();
    }
  })
}



let navegacion = accion => {
 
  if(accion.toLowerCase() === "adelante") {
    console.log('No existen urls adelante de la que estas')
    menu()
  } else if (accion.toLowerCase() === "atras") {
    if(webs.length === 0) {
      console.log('No existen urls actualmente puedes empezar agregando una tu')
      menu()
    } else {
      webs.pop()
    }
  } else if(accion.toLowerCase() === "salir") {
    console.log('Saliendo...')
    rl.close()
    return;
  } else {
    webs.push(accion)
    console.log(webs)
  }
  console.log(`Haz navegado a ${webs[webs.length - 1]}`)
  menu()
}

//menu()

// Impresora

let cola = []

function menuImpresora() {
  rl.question('Agrega un documento o selecciona imprimir/salir: ', (accion) =>{
    if(accion) {
      impresora(accion)
    } else {
      console.log('Debes introducir algo')
    }
  })
}

let impresora = accion => {

  if(accion.toLowerCase() === 'imprimir') {
    if(cola.length === 0) {
      console.log('No hay elementos para imprimir')
    } else {
      console.log('Imprimiendo: ', cola.shift())
    }
  } else if(accion.toLowerCase() === 'salir') {
    console.log('Saliendo...')
    rl.close()
    return;
  } else {
    cola.push(accion);
  }
  console.log('Cola de impresion: ', cola)
  menuImpresora()
}
  
menuImpresora()
 