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

// 🔥 Implementación de pilas y colas

// Pila (Stack - LIFO)
/*
Una pila es una estructura de datos que sigue el principio LIFO 
(Last In, First Out).
Los elementos se añaden y se eliminan desde la parte superior de la pila.
*/
class Stack {
    constructor() { this.items = [] }

    // Añadir un elemento a la pila
    push(element) { this.items.push(element) }

    // Eliminar el último elemento añadido
    pop() {
        return this.isEmpty() ? 'La pila está vacía' : this.items.pop()
    }

    // Ver el último elemento sin eliminarlo
    peek() {
        return this.isEmpty() ? 'La pila está vacía' : this.items[this.items.length - 1]
    }

    // Verificar si la pila está vacía
    isEmpty() {
        return this.items.length === 0;
    }

    // Mostrar el contenido de la pila
    print() {
        console.log(this.items.toString()||'La pila está vacía');
    }
}

const stack = new Stack();
stack.print(); // La pila está vacía
stack.push("A");
stack.push("B");
stack.push("C");
stack.print(); // C,B,A
console.log(stack.pop()); // C
console.log(stack.peek()); // B



// Cola (Queue - FIFO)
/*
Una cola es una estructura de datos que sigue el principio FIFO 
(First In, First Out). 
Los elementos se añaden al final de la cola y se eliminan desde el frente.
*/

class Queue {
    constructor() { this.items = [] }

    // Añadir un elemento a la cola
    enqueue(element) { this.items.push(element) }

    // Eliminar el primer elemento añadido
    dequeue() {
        return this.isEmpty() ? 'La cola está vacía' : this.items.shift()
    }

    // Ver el primer elemento sin eliminarlo
    front() {
        return this.isEmpty() ? 'La cola está vacía' : this.items[0]
    }

    // Verificar si la cola está vacía
    isEmpty() {
        return this.items.length === 0;
    }

    // Mostrar el contenido de la cola
    print() {
        console.log(this.items.toString()||'La cola está vacía' );
    }
}

const queue = new Queue();
queue.print(); // La cola está vacía
queue.enqueue("A");
queue.enqueue("B");
queue.enqueue("C");
queue.print(); // A,B,C
console.log(queue.dequeue()); // A
console.log(queue.front()); // B


// 🔥 Extra

// 1. Navegador web
class Navegador {
    constructor() {
        this.backStack = new Stack()
        this.forwardStack = new Stack()
        this.actualPage = null;
    }

    // Visitar una nueva página
    visitar(pagina) {
        this.actualPage !== null && this.backStack.push(this.actualPage); // Guardar la página actual en el historial
        this.actualPage = pagina;
        this.forwardStack = new Stack(); // Limpiar el historial hacia adelante
        console.log(`Visitando: ${pagina}`);
    }

    // Retroceder a la página anterior
    atras() {
        if (!this.backStack.isEmpty()) {
            this.forwardStack.push(this.actualPage); // Guardar la página actual en el historial hacia adelante
            this.actualPage = this.backStack.pop(); // Retroceder
            console.log(`Retrocediendo a: ${this.actualPage}`);
        } else {
            console.log("No hay más páginas hacia atrás.");
        }
    }

    // Avanzar a la siguiente página
    adelante() {
        if (!this.forwardStack.isEmpty()) {
            this.backStack.push(this.actualPage); // Guardar la página actual en el historial hacia atrás
            this.actualPage = this.forwardStack.pop(); // Avanzar
            console.log(`Avanzando a: ${this.actualPage}`);
        } else {
            console.log("No hay más páginas hacia adelante.");
        }
    }
}

// Ejemplo de uso
const navegador = new Navegador();
navegador.visitar("https://www.google.com");
navegador.visitar("https://www.facebook.com");
navegador.visitar("https://www.youtube.com");
navegador.atras(); // Retrocediendo a https://www.facebook.com
navegador.adelante(); // Avanzando a https://www.youtube.com
navegador.atras(); // Retrocediendo a https://www.facebook.com
navegador.visitar("https://www.twitter.com"); // Visita https://www.twitter.com
navegador.adelante(); // No hay más páginas hacia adelante



// 2. Impresora
class Impresora {
    constructor() {
        this.documentos = new Queue(); // Cola de documentos
    }

    // Agregar un documento a la cola
    agregarDocumento(documento) {
        this.documentos.enqueue(documento);
        console.log(`Documento agregado: ${documento}`);
    }

    // Imprimir un documento
    imprimir() {
        if (!this.documentos.isEmpty()) {
            const documento = this.documentos.dequeue();
            console.log(`Imprimiendo: ${documento}`);
        } else {
            console.log("No hay documentos en la cola.");
        }
    }
}

const impresora = new Impresora();
impresora.agregarDocumento("versiculos.pdf");
impresora.agregarDocumento("libro.pptx");
impresora.imprimir(); // Imprime versiculos.pdf
impresora.imprimir(); // Imprime libro.pptx
impresora.imprimir(); // No hay más documentos