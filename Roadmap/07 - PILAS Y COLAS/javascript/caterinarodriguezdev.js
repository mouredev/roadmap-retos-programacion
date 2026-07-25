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

console.log('---------------------PILA---------------------');

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
}

const pila = new Stack([10, 20, 30]); 

pila.push(40);
pila.push(50);
pila.pop();

console.log(pila.peek());
console.log(pila.size());


console.log('---------------------COLA---------------------');

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
}

const cola = new Queue([11, 22, 33]);
console.log(cola);
cola.dequeue();
cola.enqueue(1);
console.log(cola.front());

console.log('-------------- NAVEGADOR WEB --------------');

const readline = require('readline');
const rl = readline.createInterface(process.stdin, process.stdout);

let historial = new Stack([]);
let forwardStack = new Stack([]);

const navegador = () => {

    rl.question('Adelante, atrás, o introduce una web -> ', (term) => {
        switch(term) {
            case 'adelante':
                goForward();
                break;
            case 'atras':
                goBack();
                break;
            default:
                navigate(term);
        }
    });

}

const navigate = (term) => {
    historial.push(term);
    console.log('Going to -> ', term);
    forwardStack = new Stack([]);
    entryPoint();
}

const goBack = () => {
    forwardStack.push(historial.peek())
    historial.pop();
    console.log('Going back to -> ', historial.peek());
    entryPoint();
}

const goForward = () => {
    console.log('Going forward to ->', forwardStack.peek());
    historial.push(forwardStack.peek());
    entryPoint();
}

// * DIFICULTAD EXTRA (opcional):
// * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
// *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
// *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
// *   interpretan como nombres de documentos.

console.log('-------------- IMPRESORA --------------');

let colaImpresion = new Queue([]);

const imprimir = () => {

    rl.question('Imprime o añade un documento -> ', (term) => {

        switch (term) {
            case 'imprimir':
                console.log('Imprimiendo documento: ', colaImpresion.dequeue());
                imprimir();
                break;
            default:
                console.log('Documento añadido: ', term);
                colaImpresion.enqueue(term);
                imprimir();
                break;
        }
    })
}

const entryPoint = () => {

    rl.question('¿Qué programa desea ejecutar? -> ', (term) => {
        switch (term) {
            case 'Navegador':
                navegador();
                break;
            case 'Impresora':
                imprimir();
                break;
        }
    })
}

entryPoint();