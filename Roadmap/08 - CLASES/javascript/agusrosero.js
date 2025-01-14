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

// EJERCICIO
class MiClase {
  constructor(name) {
    this.name = name;
  }

  get saludo() {
    return this.saludar();
  }

  saludar() {
    console.log(`Hola ${this.name}!`);
  }
}

const test = new MiClase("Hernan");
console.log(test.name);
test.saludar();

// DIFICULTAD EXTRA:
class Stack {
  constructor() {
    this.stack = [];
  }

  push(element) {
    this.stack.push(element);
    return this.stack;
  }

  pop() {
    return this.stack.pop();
  }

  len() {
    return this.stack.length;
  }

  print() {
    console.log(this.stack);
  }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.pop();
console.log(stack.len());
stack.print();

class Queue {
  constructor() {
    this.queue = [];
  }

  enqueue(element) {
    this.queue.push(element);
    return this.queue;
  }

  dequeue() {
    return this.queue.shift();
  }

  len() {
    return this.queue.length;
  }

  print() {
    return this.queue;
  }
}

const queue = new Queue();
queue.enqueue("Test1");
queue.enqueue("Test2");
queue.enqueue("Test3");
queue.dequeue();
console.log(queue.len());
console.log(queue.print());
