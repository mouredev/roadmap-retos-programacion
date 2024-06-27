/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
*/

console.log("+++++++++ EJERCICIO +++++++++");
class Greeting {
  constructor(name, occupation) {
    this.name = name;
    this.occupation = occupation;
  }

  message() {
    return `Hello, my name is ${this.name} and I'm a ${this.occupation}!`
  }
}

let hello = new Greeting("Samus", "Bounty Hunter");
console.log(hello.message());
console.log("Modificación de los parámetros e impresión del resultado:");
hello.name = "Peter";
hello.occupation = "Photographer";
console.log(hello.message());

console.log("\n+++++++++ DIFICULTAD EXTRA: PILA +++++++++");
class MyStack {
  constructor() {
    this.stackArray = [];
  }

  add(element) {
    this.stackArray.push(element);
    const pushedElement = this.stackArray[this.stackArray.length - 1];
    console.log(`Se agregó el elemento "${pushedElement}" a la pila.`);
  }

  remove() {
    const poppedElement = this.stackArray.pop();
    console.log(`Se eliminó el elemento "${poppedElement}" de la Pila.`);
  }

  length() {
    console.log(`Hay ${this.stackArray.length} elementos en la pila:`);
  }

  show() {
    console.log(this.stackArray);
  }
}

let stack = new MyStack();

stack.add("La Historia de un Cowboy");
stack.add("Plexo Solar");
stack.add("Espera");
stack.length()
stack.show();
stack.remove();
stack.length()
stack.show();

console.log("\n+++++++++ DIFICULTAD EXTRA: COLA +++++++++");
class MyQueue {
  constructor() {
    this.queueArray = [];
  }

  add(element) {
    this.queueArray.push(element);
    const pushedElement = this.queueArray[this.queueArray.length - 1];

    console.log(`El elemento "${pushedElement}" se agregó a la fila.`);
  }

  remove() {
    const shiftedElement = this.queueArray.shift();

    console.log(`El elemento "${shiftedElement}" se desplazó de la fila.`);
  }

  length() {
    const queueLength = this.queueArray.length;
    console.log(`La fila contiene ${queueLength} elementos:`);
  }

  show() {
    console.log(this.queueArray);
  }
}

let queue = new MyQueue();

queue.add("Alfredo");
queue.add("Diego");
queue.add("Raúl");
queue.length();
queue.show();
queue.remove();
queue.length();
queue.show();
