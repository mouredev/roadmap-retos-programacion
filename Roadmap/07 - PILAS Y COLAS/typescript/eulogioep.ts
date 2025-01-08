import * as readline from 'readline';

// Implementación de la Pila (Stack - LIFO)
class Stack<T> {
    private items: T[] = [];

    // Método para añadir un elemento a la pila
    push(element: T): void {
        this.items.push(element);
    }

    // Método para quitar un elemento de la pila
    pop(): T | undefined {
        if (this.isEmpty()) {
            console.log("Error: Pila vacía");
            return undefined;
        }
        return this.items.pop();
    }

    // Método para verificar si la pila está vacía
    isEmpty(): boolean {
        return this.items.length === 0;
    }

    // Método para obtener el elemento en la cima de la pila sin quitarlo
    peek(): T | undefined {
        if (this.isEmpty()) {
            console.log("Error: Pila vacía");
            return undefined;
        }
        return this.items[this.items.length - 1];
    }
}

// Implementación de la Cola (Queue - FIFO)
class Queue<T> {
    private items: T[] = [];

    // Método para añadir un elemento a la cola
    enqueue(element: T): void {
        this.items.push(element);
    }

    // Método para quitar un elemento de la cola
    dequeue(): T | undefined {
        if (this.isEmpty()) {
            console.log("Error: Cola vacía");
            return undefined;
        }
        return this.items.shift();
    }

    // Método para verificar si la cola está vacía
    isEmpty(): boolean {
        return this.items.length === 0;
    }

    // Método para obtener el primer elemento de la cola sin quitarlo
    peek(): T | undefined {
        if (this.isEmpty()) {
            console.log("Error: Cola vacía");
            return undefined;
        }
        return this.items[0];
    }
}

// Función para el simulador de navegador web
function webBrowserSimulator(): Promise<void> {
    const backStack = new Stack<string>();
    const forwardStack = new Stack<string>();
    let currentPage = "";

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Simulador de navegador web (escribe 'salir' para terminar):");

    function askForAction(): Promise<void> {
        return new Promise((resolve) => {
            rl.question("Ingresa una acción o nombre de página web: ", (input: string) => {
                input = input.trim().toLowerCase();

                if (input === 'salir') {
                    rl.close();
                    resolve();
                } else if (input === 'atrás') {
                    if (!backStack.isEmpty()) {
                        forwardStack.push(currentPage);
                        currentPage = backStack.pop() || "";
                        console.log("Página actual:", currentPage);
                    } else {
                        console.log("No hay páginas anteriores");
                    }
                } else if (input === 'adelante') {
                    if (!forwardStack.isEmpty()) {
                        backStack.push(currentPage);
                        currentPage = forwardStack.pop() || "";
                        console.log("Página actual:", currentPage);
                    } else {
                        console.log("No hay páginas siguientes");
                    }
                } else {
                    if (currentPage) {
                        backStack.push(currentPage);
                    }
                    forwardStack = new Stack<string>();  // Limpia la pila de adelante
                    currentPage = input;
                    console.log("Página actual:", currentPage);
                }

                askForAction().then(resolve);
            });
        });
    }

    return askForAction();
}

// Función para el simulador de impresora compartida
function printerSimulator(): Promise<void> {
    const printQueue = new Queue<string>();

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("\nSimulador de impresora compartida (escribe 'salir' para terminar):");

    function askForDocument(): Promise<void> {
        return new Promise((resolve) => {
            rl.question("Ingresa un nombre de documento o 'imprimir': ", (input: string) => {
                input = input.trim().toLowerCase();

                if (input === 'salir') {
                    rl.close();
                    resolve();
                } else if (input === 'imprimir') {
                    const document = printQueue.dequeue();
                    if (document) {
                        console.log("Imprimiendo:", document);
                    }
                } else {
                    printQueue.enqueue(input);
                    console.log("Documento añadido a la cola:", input);
                }

                askForDocument().then(resolve);
            });
        });
    }

    return askForDocument();
}

// Función principal asíncrona para ejecutar los simuladores
async function main() {
    await webBrowserSimulator();
    await printerSimulator();
}

// Ejecutar la función principal
main();