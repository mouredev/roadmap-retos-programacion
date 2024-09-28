

//⚡⚡  CONCEPTO DE CLASE ==================

class Programmer {

    name;
    age;
    language;

    constructor( name,age,language){
        this.name = name;
        this.age = age;
        this.language = language;
    }

    printProperties(){
        console.log(`Name: ${this.name} Age: ${this.age} Language: ${this.language} `);
    }
};

//* Instancia
const programmer1 = new Programmer( 'Artic','34','Javascript' );
// Imprimir Instancia
console.log( programmer1 );
// Imprimir método
programmer1.printProperties();
//Modificar propiedades
programmer1.name = 'Biancho';
programmer1.age = 35;
programmer1.language = 'Java';
//Imprimir propiedades modificadas
programmer1.printProperties();



//  DIFICULTAD EXTRA (opcional):
//  Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
//  en el ejercicio número 7 de la ruta de estudio)

//  - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
//    retornar el número de elementos e imprimir todo su contenido.


//⚡  Clase para representar una Pila =====

class Stack {

    constructor() {
        this.items = [];
    }
    // Método para añadir un elemento a la pila
    push(element) {
        this.items.push(element);
    }
    // Método para eliminar el último elemento de la pila
    pop() {
        if (this.items.length === 0) {
            return "La pila está vacía";
        }
        return this.items.pop();
    }
    // Método para retornar el número de elementos en la pila
    size() {
        return this.items.length;
    }
    // Método para imprimir todo el contenido de la pila
    print() {
        console.log("Contenido de la Pila:", this.items);
    }
};


// ⚡ Clase para representar una Cola =====
class Queue {

    constructor() {
        this.items = [];
    }
    // Método para añadir un elemento a la cola
    enqueue(element) {
        this.items.push(element);
    }
    // Método para eliminar el primer elemento de la cola
    dequeue() {
        if (this.items.length === 0) {
            return "La cola está vacía";
        }
        return this.items.shift();
    }
    // Método para retornar el número de elementos en la cola
    size() {
        return this.items.length;
    }
    // Método para imprimir todo el contenido de la cola
    print() {
        console.log("Contenido de la Cola:", this.items);
    }
};

// Instancia Stack
const stack = new Stack();
stack.push(10);
stack.push(20);
stack.push(30);
stack.print();
console.log( "Elemento eliminado de la Pila:", stack.pop() );
console.log( "Tamaño de la Pila:", stack.size() );

//Instancia Queue
const queue = new Queue();
queue.enqueue("A");
queue.enqueue("B");
queue.enqueue("C");
queue.print();
console.log( "Elemento eliminado de la Cola:", queue.dequeue() );
console.log( "Tamaño de la Cola:", queue.size() );




//⚡⚡ Resolucion Moure =========================================================

// Stack (LIFO)
class Stack {
    constructor() {
        this.stack = [];
    }

    push(item) {
        this.stack.push(item);
    }

    pop() {
        if (this.count() === 0) {
            return null;
        }
        return this.stack.pop();
    }

    count() {
        return this.stack.length;
    }

    print() {
        for (let i = this.stack.length - 1; i >= 0; i--) {
            console.log(this.stack[i]);
        }
    }
}

// Example for Stack
const myStack = new Stack();
myStack.push("A");
myStack.push("B");
myStack.push("C");
console.log(myStack.count());
myStack.print();
myStack.pop();
console.log(myStack.count());
console.log(myStack.pop());
console.log(myStack.pop());
console.log(myStack.pop());
console.log(myStack.pop());
console.log(myStack.pop());
console.log(myStack.count());

// Queue (FIFO)
class Queue {
    constructor() {
        this.queue = [];
    }

    enqueue(item) {
        this.queue.push(item);
    }

    dequeue() {
        if (this.count() === 0) {
            return null;
        }
        return this.queue.shift();
    }

    count() {
        return this.queue.length;
    }

    print() {
        for (let i = 0; i < this.queue.length; i++) {
            console.log(this.queue[i]);
        }
    }
}

// Example for Queue
const myQueue = new Queue();
myQueue.enqueue("A");
myQueue.enqueue("B");
myQueue.enqueue("C");
console.log(myQueue.count());
myQueue.print();
myQueue.dequeue();
console.log(myQueue.count());
console.log(myQueue.dequeue());
console.log(myQueue.dequeue());
console.log(myQueue.dequeue());
console.log(myQueue.dequeue());
console.log(myQueue.dequeue());
console.log(myQueue.count());
