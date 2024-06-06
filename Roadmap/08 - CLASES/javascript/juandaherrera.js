/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */

class Persona {
    constructor(firstName, lastName, birthDate) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthDate = new Date(birthDate); // birthDate debe ser una cadena en formato 'YYYY-MM-DD'
    }

    get age() {
        const today = new Date();
        let age = today.getFullYear() - this.birthDate.getFullYear();
        const m = today.getMonth() - this.birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < this.birthDate.getDate())) {
            age--;
        }
        return age;
    }

    describe() {
        console.log(
            `${this.firstName} ${this.lastName} tiene ${this.age} años`
        );
    }
}

const juanDavid = new Persona("Juan David", "Herrera", "1999-12-05");
juanDavid.describe();

/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */

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
