// ** EJERCICIO

class Cancion {
    constructor(nombre, grupo, album) {
        this.nombre = nombre
        this.grupo = grupo
        this.album = album
    }

    print() {
        console.log(`Nombre: ${this.nombre}, Grupo: ${this.grupo}, Álbum: ${this.album}`)
    }

    modNombre(nuevoNombre) {
        this.nombre = nuevoNombre
    }

    modGrupo(nuevoGrupo) {
        this.grupo = nuevoGrupo
    }

    modAlbum(nuevoAlbum) {
        this.album = nuevoAlbum
    }
}

let cancion1 = new Cancion('Verdis Duo', 'Daft Punk', 'Discovery')

cancion1.print() //'Nombre: Verdis Duo, Grupo: Daft Punk, Álbum: Discovery'

cancion1.modNombre('Them Changes')
cancion1.modAlbum('Drunk')
cancion1.modGrupo('Thundercat')

cancion1.print() //'Nombre: Them Changes, Grupo: Thundercat, Álbum: Drunk'

// ** DIFICULTAD EXTRA ** --------------------------------------------------------------------------------------------------------------------------------------------------

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