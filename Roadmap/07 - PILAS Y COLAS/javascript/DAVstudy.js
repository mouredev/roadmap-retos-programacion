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

let myStack = [];

// stack  Last In, First Out (LIFO)

myStack.push(1)
myStack.push(2)
myStack.push(3)

console.log(myStack);
myStack.pop()
console.log(myStack);

// queue First In, FirstOut (FIFO)

let myQueue = []

myQueue.push(1)
myQueue.push(2)
myQueue.push(3)

console.log(myQueue);
myQueue.shift()
console.log(myQueue)


/*
* Navegacion Adelante y Atras
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.
*/

const browser = {
    currentWeb : '',
    backHistory : [],
    fowardHistory : [],
    addHistory : function (str) { 
        if (this.backHistory.length === 0 && this.currentWeb === '') {
            this.currentWeb = str
            return this.currentWeb
        }
        this.backHistory.push(this.currentWeb)
        this.currentWeb = str
        return this.currentWeb
    },
    backforward : function () {
        // Si existe una pagina actual y si la pila aun tiene un elemento que no sea igual al actual, quiere decir que podemos volver atras
        if (this.currentWeb !== '' && this.checkHistory(this.backHistory)) {
            this.fowardHistory.push(this.currentWeb) // Quitamos de la cola la pagina actual y la guardamos en la pila fowardsHistory
            this.currentWeb = this.backHistory.pop() // Actualizamos la pagina actual y la retornamos
            return this.currentWeb
        }
        return 'No hay historial'
    },
    forward : function () {
       // Si existe una pagina actual y si la pila aun tiene un elemento que no sea igual al actual, quiere decir que podemos ir hacia delante
        if (this.currentWeb !== '' && this.checkHistory(this.fowardHistory)) {
            this.backHistory.push(this.currentWeb) // Almacenamos la pagina actual en la pila backforward
            this.currentWeb = this.fowardHistory.pop() // obtenemos la nueva pagina actual de la pila foward y se quita de fowardHistory
            return this.currentWeb
        }
        return 'No hay historial'

    },
    checkHistory : (stack) => stack.length === 0 ? false : true
}


const readline = require("readline");
const read = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const menu = () => {
    read.question(
        `browser: `,
        (option = (option) => {
        switch (option) {
            case "adelante":
                console.log(browser.forward())
                console.log('Pagina actual: ' + browser.currentWeb);
                menu()
                break;
            case "atras":
                console.log(browser.backforward())
                console.log('Pagina actual: ' + browser.currentWeb);
                menu()
                break;
            default:
                browser.addHistory(option)
                console.log('Pagina actual: ' + browser.currentWeb);
                menu()
                break;
        }
        })
    );
}

//menu()

/*
* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
*/

const printer = {
    queue : [],
    addDocument : function (str) {this.queue.push(str)},
    printDocument : function () {return this.queue.length === 0 ? 'No hay documentos en cola' : this.queue.shift()}
}


const menuPrinter = () => {
    read.question(
        `Impresora, esperando nueva instruccion: `,
        (option = (option) => {
        switch (option) {
            case "imprimir":
                console.log(printer.printDocument())
                menuPrinter()
                break;
            default:
                printer.addDocument(option)
                console.log(printer.queue)
                menuPrinter()
                break;
        }
        })
    );
}

//menuPrinter()