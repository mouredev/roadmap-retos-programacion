// Pilas
class Stack {
    constructor(stack = []) {
    this.stack = stack;
    }

    push(value) {
    this.stack.push(value);
    }

    pop() {
    this.stack.pop();
    }

    toString() {
    return this.stack.toString();
    }
}

let myStack = new Stack([1, 2, 3, 4, 5]);
console.log(myStack.toString());

// Inserción
myStack.push(6);
console.log(myStack.toString());

// Eliminación
myStack.pop();
console.log(myStack.toString());

console.log("---------------------------------");

// Colas
class Queue {
constructor(queue = []) {
    this.queue = queue;
}

enqueue(value) {
    this.queue.push(value);
}

dequeue() {
    this.queue.shift();
}

toString() {
    return this.queue.toString();
}
}

let myQueue = new Queue([1, 2, 3, 4, 5]);
console.log(myQueue.toString());

// Inserción
myQueue.enqueue(6);
console.log(myQueue.toString());

// Eliminación
myQueue.dequeue();
console.log(myQueue.toString());

// Ambas
myQueue.enqueue(7);
myQueue.dequeue();
myQueue.dequeue();
myQueue.dequeue();
myQueue.enqueue(8);
myQueue.dequeue();
myQueue.enqueue(9);
console.log(myQueue.toString());

console.log("---------------------------------");

class Web extends Stack {
constructor(stack = []) {
    super(stack);
    this.lastIndexSelection = 0;
}

forward() {
    if (this.lastIndexSelection + 1 > this.stack.length - 1) {
    this.lastIndexSelection = 0;
    return this.stack[this.lastIndexSelection];
    }
    this.lastIndexSelection += 1;
    return this.stack[this.lastIndexSelection];
}

back() {
    if (this.lastIndexSelection - 1 < 0) {
    this.lastIndexSelection = this.stack.length - 1;
    return this.stack[this.lastIndexSelection];
    }
    this.lastIndexSelection -= 1;
    return this.stack[this.lastIndexSelection];
}
}

// Ejemplo de uso de la clase Web
let myWeb = new Web(["Index", "About me", "Education", "Courses"]);
console.log(myWeb.toString());

console.log("Web: 1");
console.log("Impresora: 2");

let program = prompt("Qué programa quieres probar? ");

if (program === "1") {
console.log("------------ Web -------------");
console.log("Opciones:");
console.log("adelante -> siguiente página");
console.log("atras -> página anterior");
console.log("web -> todas las páginas");
console.log("exit -> salir");
console.log("cualquier string -> nueva página")

while (true) {
    let option = prompt("Opción: ").toLowerCase();
    switch (option) {
    case "adelante":
        console.log("Página actual: ", myWeb.forward());
        break;
    case "atras":
        console.log("Página actual: ", myWeb.back());
        break;
    case "web":
        console.log(myWeb.toString());
        break;
    case "exit":
        break;
    default:
        myWeb.push(option);
    }
    if (option === "exit") break;
}
}

console.log("---------------------------------");

if (program === "2") {
let documents = new Queue(["Hoja de vida", "Trabajo literatura", "Carta presentación"]);
    
console.log("------------ Impresora -------------");
console.log("Opciones:");
console.log("imprimir -> imprime el siguiente documento");
console.log("all -> todas las impresiones pendientes");
console.log("exit -> salir");
console.log("cualquier string -> nuevo documento")

while (true) {
    let option = prompt("Opción: ").toLowerCase();
    switch (option) {
    case "imprimir":
        if (documents.queue.length > 0) {
        console.log("Imprimiendo: ", documents.queue[0]);
        documents.dequeue();
        } else {
        console.log("No hay documentos para imprimir.");
        }
        break;
    case "all":
        console.log(documents.toString());
        break;
    case "exit":
        break;
    default:
        documents.enqueue(option);
    }
    if (option === "exit") break;
}
}
