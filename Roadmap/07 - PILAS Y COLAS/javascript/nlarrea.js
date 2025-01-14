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


// Stack - LIFO

const stack = [];

// Add item
stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);
console.log(stack);  // [1, 2, 3, 4]

// Remove item
stack.length = stack.length - 1;
console.log(stack);  // [1, 2, 3]

stack.pop();
console.log(stack); // [1, 2]


// Queue - FIFO

let queue = [];

// Add item
queue.push(1);
queue.push(2);
queue.push(3);
queue.push(4);
console.log(queue);  // [1, 2, 3, 4]

// Remove item
queue.splice(0, 1);
console.log(queue);  // [2, 3, 4]

queue = queue.slice(1);  // queue can't be a constant to use this
console.log(queue);  // [3, 4]

queue.shift();
console.log(queue);  // [4]


/*
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 */


const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


const history = [];
let pointer = -1;

function webNavigation() {
    const showMenu = () => {
        console.log('\nType one of the following:');
        console.log(' - The web page you want to visit');
        console.log(' - Back (to go to the previous page)');
        console.log(' - Next (to go to the next page)');
        console.log(' - Exit');
    };

    showMenu();
    
    rl.question('Where do you want to go?\n> ', (action) => {
        if (action && action.trim().toLowerCase() === 'exit') {
            rl.close();
            return;
        } else if (action && action.trim().toLowerCase() === 'next') {
            if (pointer !== history.length - 1) {
                pointer++;
            }
            console.log(`\nYou are in: ${history[pointer]}`);
        } else if (action && action.trim().toLowerCase() === 'back') {
            pointer--;
            if (pointer < 0) {
                pointer = -1;
                console.log('\nYou are in home page');
            } else {
                console.log(`\nYou are in: ${history[pointer]}`);
            }
        } else if (action) {
            history.push(action);
            pointer = history.length - 1;
            console.log(`\nYou are in: ${history[pointer]}`);
        }

        webNavigation();
    });
}

webNavigation();


/*
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */


const printerQueue = [];

function printer() {
    const showMenu = () => {
        console.log('\nPrinter options:');
        console.log(' - Type a document name to add it to the queue');
        console.log(' - Type "print" to print the first item');
        console.log(' - Exit');
    };

    const showQueue = () => {
        console.log('\nPrinter Queue:');

        if (printerQueue.length > 0) {
            for (let doc of printerQueue) {
                console.log(` - ${doc}`);
            }
        } else {
            console.log('The Queue is empty.');
        }
    };

    showMenu();
    rl.question('Type a document name or "print" to print the first item:\n> ', (action) => {
        if (action && action.trim().toLowerCase() === 'exit') {
            rl.close();
            return;
        } else if (action && action.trim().toLowerCase() === 'print') {
            if (printerQueue.length > 0) {
                let printingDoc = printerQueue.shift();
                console.log(`Printing: ${printingDoc}`);
            } else {
                console.log('There are no documents to print.');
            }
        } else if (action) {
            printerQueue.push(action);
        }

        showQueue();
        printer();
    });
}

printer();