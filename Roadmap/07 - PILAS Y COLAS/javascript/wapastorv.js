/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista en javascript.
 */

// Implementación de una pila (stack - LIFO)
/*function Stack() {
    // Atributos
    this.stack = [];
    
    // Añadir un elemento a la pila
    this.push = function (element) {
        this.stack.push(element);
    }

    // Eliminar un elemento de la pila
    this.pop = function () {
        return this.stack.pop();
    }

    // Devolver el elemento que está en la cima de la pila
    this.peek = function () {
        return this.stack[this.stack.length - 1];
    }

    // Devolver si la pila está vacía
    this.isEmpty = function () {
        return this.stack.length === 0;
    }
    
    // Devolver el tamaño de la pila
    this.size = function () {
        return this.stack.length;
    }
    
    // Imprimir la pila
    this.print = function () {
        console.log(this.stack);
    }
    
    //  Limpiar la pila
    this.clear = function () {
        this.stack = [];
    }


}

// Implementación de una cola (queue - FIFO)
function Queue() {
    // Atributos de la cola (queue) 
    this.queue = [];

    // Métodos de la cola (queue) 
    this.enqueue = function (element) {
        // Añadir un elemento a la cola
        this.queue.push(element);
    }

    // Eliminar un elemento de la cola
    this.dequeue = function () {
        return this.queue.shift();
    }

    // Devolver el primer elemento de la cola
    this.front = function () {
        return this.queue[0];
    }

    // Devolver si la cola está vacía
    this.isEmpty = function () {
        return this.queue.length === 0;
    }

    // Devolver el tamaño de la cola
    this.size = function () {
        return this.queue.length;
    }

    // Imprimir la cola
    this.print = function () {
        console.log(this.queue);
    }
    
    // Limpiar la cola
    this.clear = function () {
        this.queue = [];
    }
}
 
// Pruebas pila
var stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.print();
console.log(stack.pop());
console.log(stack.peek());
console.log(stack.isEmpty());
console.log(stack.size());
stack.print();
stack.clear();
stack.print();

// Pruebas cola
var queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
queue.print();
console.log(queue.dequeue());
console.log(queue.front());
console.log(queue.isEmpty());
console.log(queue.size());
queue.print();
queue.clear();
queue.print();/*

/* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 */
/*const readline = require("readline");

class Browser {
    constructor() {
        this.historyStack = []; // Pila para el historial hacia atrás
        this.forwardStack = []; // Pila para el historial hacia adelante
        this.currentPage = null; // Página actual
    }

    navigateTo(page) {
        if (this.currentPage) {
            this.historyStack.push(this.currentPage);
        }
        this.currentPage = page;
        this.forwardStack = [];
        console.log(`Navegando a: ${this.currentPage}`);
    }

    goBack() {
        if (this.historyStack.length === 0) {
            console.log("No hay más páginas hacia atrás.");
            return;
        }
        this.forwardStack.push(this.currentPage);
        this.currentPage = this.historyStack.pop();
        console.log(`Retrocediendo a: ${this.currentPage}`);
    }

    goForward() {
        if (this.forwardStack.length === 0) {
            console.log("No hay más páginas hacia adelante.");
            return;
        }
        this.historyStack.push(this.currentPage);
        this.currentPage = this.forwardStack.pop();
        console.log(`Avanzando a: ${this.currentPage}`);
    }

    printStatus() {
        console.log(`Página actual: ${this.currentPage || "Ninguna"}`);
        console.log(`Historial atrás: [${this.historyStack.join(", ")}]`);
        console.log(`Historial adelante: [${this.forwardStack.join(", ")}]`);
    }
}

// Configuración del intérprete
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const browser = new Browser();

function showMenu() {
    console.log("\nAcciones disponibles:");
    console.log("1. Navegar a una página (escribe el nombre de la página).");
    console.log("2. Ir atrás (escribe 'atrás').");
    console.log("3. Ir adelante (escribe 'adelante').");
    console.log("4. Mostrar estado (escribe 'estado').");
    console.log("5. Salir (escribe 'salir').\n");
}

function processInput(input) {
    input = input.trim().toLowerCase();

    if (input === "salir") {
        console.log("¡Adiós!");
        rl.close();
        return;
    }

    if (input === "atrás") {
        browser.goBack();
    } else if (input === "adelante") {
        browser.goForward();
    } else if (input === "estado") {
        browser.printStatus();
    } else if (input) {
        browser.navigateTo(input);
    } else {
        console.log("Entrada no válida.");
    }

    startInteraction(); // Volvemos a mostrar el menú
}

function startInteraction() {
    showMenu();
    rl.question("¿Qué deseas hacer? ", processInput);
}

// Iniciar la interacción
console.log("¡Bienvenido al navegador interactivo!");
startInteraction();*/

/*DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

/*class Impresora {
    constructor(){
      this.queue = new Queue();
    }
    //Añadir un documento a la cola
    addDocument(document){
      this.queue.enqueue(document);
      console.log(`Documento añadido: ${document}`);
    }
    //Imprimir un documento
    printDocument(){
      if(this.queue.isEmpty()){
        console.log("No hay documentos para imprimir.");
        return;
      }
      const document = this.queue.dequeue();
      console.log(`Imprimiendo documento: ${document}`);
    }
    //Mostrar el estado actual
    printStatus(){
      console.log(`Documentos en cola: [${this.queue.queue.join(", ")}]`);
    }
}

const impresora = new Impresora();
impresora.addDocument("Documento1");
impresora.addDocument("Documento2");
impresora.addDocument("Documento3");
impresora.printStatus();
impresora.printDocument();
impresora.printStatus();
impresora.printDocument();*/

const readline = require("readline");
class PrinterQueue {
    constructor() {
        this.queue = []; // Cola para los documentos
    }

    addDocument(document) {
        this.queue.push(document);
        console.log(`Documento "${document}" añadido a la cola.`);
    }

    printDocument() {
        if (this.queue.length === 0) {
            console.log("No hay documentos en la cola para imprimir.");
        } else {
            const document = this.queue.shift();
            console.log(`Imprimiendo: "${document}"`);
        }
    }

    showQueue() {
        if (this.queue.length === 0) {
            console.log("La cola de impresión está vacía.");
        } else {
            console.log(`Documentos en la cola: [${this.queue.join(", ")}]`);
        }
    }
}

// Configuración del intérprete
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const printer = new PrinterQueue();

function showMenu() {
    console.log("\nAcciones disponibles:");
    console.log("1. Añadir un documento (escribe el nombre del documento).");
    console.log("2. Imprimir un documento (escribe 'imprimir').");
    console.log("3. Ver la cola de impresión (escribe 'cola').");
    console.log("4. Salir (escribe 'salir').\n");
}

function processInput(input) {
    input = input.trim().toLowerCase();

    if (input === "salir") {
        console.log("Cerrando impresora. ¡Adiós!");
        rl.close();
        return;
    }

    if (input === "imprimir") {
        printer.printDocument();
    } else if (input === "cola") {
        printer.showQueue();
    } else if (input) {
        printer.addDocument(input);
    } else {
        console.log("Entrada no válida.");
    }

    startInteraction(); // Volvemos a mostrar el menú
}

function startInteraction() {
    showMenu();
    rl.question("¿Qué deseas hacer? ", processInput);
}

// Iniciar la interacción
console.log("¡Bienvenido a la impresora compartida!");
startInteraction();

