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
 */

class Robot {

    constructor (nombre, rapidez, superPoder) {
        this.nombre = nombre ?? 'mimi';
        this.rapidez = rapidez ?? '0';
        this.superPoder = superPoder ?? 'iluminidad'
    }    

    print () {
        console.log(`>>>>>>>>>>>  Mi robot se llama ${this.nombre} con una velocidad de ${this.rapidez} y su máximo poder es ${this.superPoder}  <<<<<<<<<<<<<<<`);
    }
} 

const miRobot = new Robot();
miRobot.print();

class Stack {

    constructor (arr) {
        this.stack = arr;
    }

    push (item) {
        this.stack.push(item);
    }

    pop () {
        this.stack.pop();
    }

    peek () {
        return this.stack[this.stack.length - 1];
    }

    size () {
        return this.stack.length;
    }

    print () {
        console.log(this.stack);
    }
}

class Queue {

    constructor (arr) {
        this.queue = arr;
    }

    enqueue (item) {
        this.queue.push(item);
    }

    dequeue () {
        if (this.isEmpty()) {
            return null;
        } else {
            return this.queue.shift();
        }
    }

    isEmpty() {
        return this.queue.length === 0;
    }

    size () {
        return this.queue.length;
    }

    front () {
        if (this.isEmpty()) {
            return null;
        } else {
            return this.queue[0];
        }
    }

    print () {
        console.log(this.queue);
    }
}

const cola = new Queue([11, 22, 33]);
cola.print();

const pila = new Stack([10, 20, 30]); 
pila.print();