// ** EJERCICIO

// Implementación de una Pila (Stack - LIFO)

class Stack {
    constructor() {
        this.items = [];
        this.forwardStack = [] // Array secundaria
    }

    push(element) {
        this.items.push(element); // Agrega el elemento al final de la lista
    }

    pop() {
        if (this.isEmpty()) {
            return "La pila está vacía";
        }
        return this.items.pop(); // Elimina y devuelve el último elemento de la lista
    }

    peek() {
        if (this.isEmpty()) {
            return "La pila está vacía";
        }
        return this.items[this.items.length - 1]; // Devuelve el último elemento sin eliminarlo
    }

    isEmpty() {
        return this.items.length === 0; // Comprueba si la lista está vacía
    }

    size() {
        return this.items.length; // Devuelve el tamaño de la lista
    }

    clear() {
        this.items = []; // Vacía la lista
    }

    print() {
        console.log(this.items.toString()); // Imprime los elementos de la lista
    }

    pushForward(element) {
        this.forwardStack.push(element); // Añade elementos al forwardStack que son usados para almacenar
    }

    popForward() {
        if (this.forwardStack.length === 0) { 
            return "Forward stack is empty";
        }
        return this.forwardStack.pop(); // Elimina y devuelve el último elemento del forwardStack
    }

    peekForward() {
        if (this.forwardStack.length === 0) { 
            return "Forward stack is empty";
        }
        return this.forwardStack[this.forwardStack.length - 1]; // Devuelve el último elemento del forwardStack sin eliminarlo
    }

    isEmptyForward() {
        return this.forwardStack.length === 0; // Comprueba si la lista está vacía
    }
}

let pila = new Stack()
pila.push(10) // Añade 10
pila.push(20) // Añade 20
pila.push(30) // Añade 30
pila.pop() // Devuelve y elimina 30
pila.peek() // Devuelve 20 sin eliminarlo
// pila.print() // Imprime 10,20

// Implementación de una Cola (Queue - FIFO)

class Queue {
    constructor() {
        this.items = [];
    }

    enqueue(element) {
        this.items.push(element); // Agrega el elemento al final de la lista
    }

    dequeue() {
        if (this.isEmpty()) {
            return "La cola está vacía";
        }
        return this.items.shift(); // Elimina y devuelve el primer elemento de la lista
    }

    front() {
        if (this.isEmpty()) {
            return "La cola está vacía";
        }
        return this.items[0]; // Devuelve el primer elemento sin eliminarlo
    }

    isEmpty() {
        return this.items.length === 0; // Comprueba si la lista está vacía
    }

    size() {
        return this.items.length; // Devuelve el tamaño de la lista
    }

    clear() {
        this.items = []; // Vacía la lista
    }

    print() {
        console.log(this.items.toString()); // Imprime los elementos de la lista
    }
}

// Ejemplo de uso:
let cola = new Queue();
cola.enqueue(10); // Añade 10
cola.enqueue(20); // Añade 20
cola.enqueue(30); // Añade 30
cola.dequeue() // Devuelve y elimina 10
cola.front() // Devuelve 20 sin eliminarlo
// cola.print(); // Imprime 20,30

// ** DIFICULTAD EXTRA (navegador Web) ** ---------------------------------------------------------------------------------------------------------------------------------------------

let navegadorWebPila = new Stack();
// navegadorWebPila.push(10); // Añade 10
// navegadorWebPila.push(20); // Añade 20
// navegadorWebPila.push(30); // Añade 30
// console.log(navegadorWebPila.pop()); // Devuelve y elimina 30
// console.log(navegadorWebPila.peek()); // Devuelve 20 sin eliminarlo
// navegadorWebPila.print(); // Imprime 10,20

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let textoInicio = false

// navegadorWeb()

function navegadorWeb(){
    if (!textoInicio) {
        readline.question('Bienvenido al búscador.\nPodrá retroceder con el comando [atrás]\nPodrá volver hacia delante con el comando [adelante]\nPodrá ir a una nueva página introduciendo una búsqueda.\nPara empezar, introduzca la página a la que quiere viajar: ', (respuesta) => {
            navegadorWebPregunta(respuesta)
        });
        textoInicio = true
    } else {
        readline.question('', (respuesta) => {
            navegadorWebPregunta(respuesta)
        });
    }
}


function navegadorWebPregunta(respuesta){
    if (respuesta !== 'atrás' && respuesta !== 'adelante' && respuesta !== '') {
        navegadorWebPila.push(respuesta);
        console.log(`Usted se encuentra en: ${navegadorWebPila.peek()}\nLa ruta de páginas es la siguiente: `)
        navegadorWebPila.print()
        navegadorWeb(respuesta);
    } else if (respuesta === 'atrás') {
        if (!navegadorWebPila.isEmpty()){
            let atras = navegadorWebPila.pop();
            navegadorWebPila.pushForward(atras);
            if (!navegadorWebPila.isEmpty()) {
                console.log(`Usted ha vuelto a: ${navegadorWebPila.peek()}`);
            } else {
                console.log("No hay más páginas en el historial.");
            }
        } else {
            console.log('No hay más páginas hacia atrás');
        }
        navegadorWeb();
    } else if (respuesta === 'adelante') {
        if (!navegadorWebPila.isEmptyForward()) {
            let adelante = navegadorWebPila.popForward()
            navegadorWebPila.push(adelante);
            console.log(`Usted ha avanzado a: ${adelante}`);
        } else {
            console.log('No hay más páginas hacia adelante');
        }
        navegadorWeb();
    } else {
        console.log(`Por favor, introduzca un texto.`)
        navegadorWeb()
    }
}

// ** DIFICULTAD EXTRA (impresora) ** ---------------------------------------------------------------------------------------------------------------------------------------------

let impresora = new Queue();

imprimirImpresora()

function imprimirImpresora(){
    if (!textoInicio) {
        readline.question('Bienvenido a la impresora.\nPodrá imprimir el primer elemento de la cola con el comando [imprimir]\nPodrá adjuntar un documento escribiendo el nombre del documento.\nPara empezar, introduzca el nombre del primer documento: ', (respuesta) => {
            imprimirImpresoraAccion(respuesta)
        });
        textoInicio = true
    } else {
        readline.question('', (respuesta) => {
            imprimirImpresoraAccion(respuesta)
        });
    }
}

function imprimirImpresoraAccion(respuesta){
    if (respuesta !== 'imprimir' && respuesta !== ''){
        console.log(`Se ha añadido: ${respuesta}.\nLos documentos que quedan son: `)
        impresora.enqueue(respuesta)
        impresora.print()
        imprimirImpresora()
    } else if (respuesta === 'imprimir') {
        if (!impresora.isEmpty()){
            console.log(`Se está imprimiento: ${impresora.dequeue()}.\nLos documentos que quedan son: `)
            impresora.print()
            imprimirImpresora()
        } else {
            console.log('No hay elementos que imprimir')
            imprimirImpresora()
        }
    } else {
        console.log('Por favor, introduzca un texto:')
        imprimirImpresora()
    }
}