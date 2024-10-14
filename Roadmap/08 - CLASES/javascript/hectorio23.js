// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

/*******************************************
 * CLASE WebPage
 *******************************************/

class WebPage {
    constructor(title, index) {
        this.title = title;
        this.index = index;
    }

    getInfo() {
        console.log(`<Object WebPage - ${this.title} at ${this}`);
    }
}

/*******************************************
 * CLASE Queue
 *******************************************/

class Queue {
    constructor() {
        this.next = null;
        this.last = null;
        this.size = 0;
        this.page = null;
    }

    push(webPage) {
        const tmp = new Queue();
        tmp.page = webPage;
        if (this.size === 0) {
            this.next = tmp;
            this.last = tmp;
        } else {
            this.last.next = tmp;
            this.last = tmp;
        }
        this.size++;
    }

    pop() {
        if (this.size === 0) return null;
        const aux = this.next;
        this.next = aux.next;
        this.size--;
        if (this.size === 0) {
            this.last = null;
        }
        return aux.page;
    }
}

/*******************************************
 * CLASE Stack
 *******************************************/

class Stack {
    constructor() {
        this.next = null;
        this.garbage = null; // experimental
        this.size = 0;
        this.page = null;
    }

    push(webPage) {
        const tmp = new Stack();
        tmp.page = webPage;
        tmp.next = this.next;
        this.next = tmp;
        this.size++;
    }

    pop() {
        if (this.size === 0) return null;
        const aux = this.next;
        this.next = aux.next;
        this.size--;
        return aux.page;
    }
}

/*******************************************
 * CLASE Persona
 *******************************************/

class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    info() {
        console.log(`Nombre: ${this.nombre}`);
        console.log(`Edad: ${this.edad}`);
    }

    setNombre(nuevoNombre) {
        this.nombre = nuevoNombre;
    }

    setEdad(nuevaEdad) {
        this.edad = nuevaEdad;
    }
}

/*******************************************
 * PROGRAMA PRINCIPAL
 *******************************************/

// Crear una instancia de Persona
const persona = new Persona("Juan", 30);

// Imprimir los atributos
console.log("Datos de la persona:");
persona.info();

// Modificar los atributos
persona.setNombre("María");
persona.setEdad(25);

// Imprimir los atributos actualizados
console.log("\nDatos de la persona actualizados:");
persona.info();

// Crear objetos WebPage para usar en Stack y Queue
const p1 = new WebPage("index", 1);
const p2 = new WebPage("index", 2);
const p3 = new WebPage("index", 3);

// Crear una instancia de Queue
const queue = new Queue();

// Agregar elementos a Queue
queue.push(p1);
queue.push(p2);
queue.push(p3);

console.log(`\nNúmero de elementos en Queue: ${queue.size}`);
queue.pop();
queue.pop();
queue.pop();
console.log(`Número de elementos en Queue después de eliminar: ${queue.size}`);

// Crear una instancia de Stack
const stack = new Stack();

// Agregar elementos a Stack
stack.push(p1);
stack.push(p2);
stack.push(p3);

console.log(`\nNúmero de elementos en Stack: ${stack.size}`);
stack.pop();
stack.pop();
stack.pop();
console.log(`Número de elementos en Stack después de eliminar: ${stack.size}`);
