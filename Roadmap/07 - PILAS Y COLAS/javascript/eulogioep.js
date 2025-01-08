const readline = require('readline');

// Implementación de la Pila (Stack - LIFO)
class Stack {
    constructor() {
        this.items = [];
    }

    // Método para añadir un elemento a la pila
    push(element) {
        this.items.push(element);
    }

    // Método para quitar un elemento de la pila
    pop() {
        if (this.isEmpty()) {
            console.log("Error: Pila vacía");
            return null;
        }
        return this.items.pop();
    }

    // Método para verificar si la pila está vacía
    isEmpty() {
        return this.items.length === 0;
    }

    // Método para obtener el elemento en la cima de la pila sin quitarlo
    peek() {
        if (this.isEmpty()) {
            console.log("Error: Pila vacía");
            return null;
        }
        return this.items[this.items.length - 1];
    }
}

// Implementación de la Cola (Queue - FIFO)
class Queue {
    constructor() {
        this.items = [];
    }

    // Método para añadir un elemento a la cola
    enqueue(element) {
        this.items.push(element);
    }

    // Método para quitar un elemento de la cola
    dequeue() {
        if (this.isEmpty()) {
            console.log("Error: Cola vacía");
            return null;
        }
        return this.items.shift();
    }

    // Método para verificar si la cola está vacía
    isEmpty() {
        return this.items.length === 0;
    }

    // Método para obtener el primer elemento de la cola sin quitarlo
    peek() {
        if (this.isEmpty()) {
            console.log("Error: Cola vacía");
            return null;
        }
        return this.items[0];
    }
}

// Función para el simulador de navegador web
function webBrowserSimulator() {
    const backStack = new Stack();
    const forwardStack = new Stack();
    let currentPage = "";

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Simulador de navegador web (escribe 'salir' para terminar):");

    function askForAction() {
        rl.question("Ingresa una acción o nombre de página web: ", (input) => {
            input = input.trim().toLowerCase();

            if (input === 'salir') {
                rl.close();
                printerSimulator();
            } else if (input === 'atrás') {
                if (!backStack.isEmpty()) {
                    forwardStack.push(currentPage);
                    currentPage = backStack.pop();
                    console.log("Página actual:", currentPage);
                } else {
                    console.log("No hay páginas anteriores");
                }
            } else if (input === 'adelante') {
                if (!forwardStack.isEmpty()) {
                    backStack.push(currentPage);
                    currentPage = forwardStack.pop();
                    console.log("Página actual:", currentPage);
                } else {
                    console.log("No hay páginas siguientes");
                }
            } else {
                if (currentPage) {
                    backStack.push(currentPage);
                }
                forwardStack = new Stack();  // Limpia la pila de adelante
                currentPage = input;
                console.log("Página actual:", currentPage);
            }

            askForAction();
        });
    }

    askForAction();
}

// Función para el simulador de impresora compartida
function printerSimulator() {
    const printQueue = new Queue();

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("\nSimulador de impresora compartida (escribe 'salir' para terminar):");

    function askForDocument() {
        rl.question("Ingresa un nombre de documento o 'imprimir': ", (input) => {
            input = input.trim().toLowerCase();

            if (input === 'salir') {
                rl.close();
                return;
            } else if (input === 'imprimir') {
                const document = printQueue.dequeue();
                if (document) {
                    console.log("Imprimiendo:", document);
                }
            } else {
                printQueue.enqueue(input);
                console.log("Documento añadido a la cola:", input);
            }

            askForDocument();
        });
    }

    askForDocument();
}

// Iniciar el simulador de navegador web
webBrowserSimulator();