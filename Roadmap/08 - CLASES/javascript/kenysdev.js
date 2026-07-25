/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#08 CLASES
---------------------------------------
* EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
*/

// ________________________________________________________
class Employee {
    // Atributos de clase
    static baseSalary = 25000;
    static vacationDays = 15;

    // Constructor
    constructor(name, hireDate) {
        this.name = name;
        this.hireDate = hireDate;
    }

    // Métodos de instancia
    edit(name, hireDate) {
        this.name = name;
        this.hireDate = hireDate;
    }

    println() {
        console.log(`Name: ${this.name} - Hire date: ${this.hireDate}`);
    }
}

// Crear objeto
const employeeInstance = new Employee("Ben", "2024-02-01");

// Acceder a los atributos
console.log(`
Name:          ${employeeInstance.name}
Hire date:     ${employeeInstance.hireDate}
Base salary:   ${Employee.baseSalary}
Vacation days: ${Employee.vacationDays}
`);

// Utilizar métodos
employeeInstance.edit("Ben edit", "2024-03-01");
employeeInstance.println();

// ________________________________________________________
// DIFICULTAD EXTRA
// __________________________
// Clase Stack (Pila - LIFO):
class Stack {
    constructor() {
        this.elements = [];
    }

    get length() { // Total elementos
        return this.elements.length;
    }

    isEmpty() { // Es vacía
        return this.length === 0;
    }

    push(item) { // Agregar elemento
        this.elements.push(item);
    }

    pushBatch(items) { // Agregar múltiples
        this.elements.push(...items);
    }

    popGet() { // Eliminar y obtener
        return this.isEmpty() ? null : this.elements.pop();
    }

    getTop() { // Obtener sin eliminar
        return this.isEmpty() ? null : this.elements[this.elements.length - 1];
    }

    toArray() { // Retornar pila como tupla
        return [...this.elements].reverse();
    }

    clear() { // Vaciar pila
        this.elements = [];
    }
}

// __________________________
// Clase Queue (Cola - FIFO):
class Queue {
    constructor() {
        this.elements = [];
    }

    get length() { // Total elementos
        return this.elements.length;
    }

    isEmpty() { // Es vacía
        return this.length === 0;
    }

    enqueue(item) { // Agregar elemento
        this.elements.push(item);
    }

    enqueueAll(items) { // Agregar múltiples
        this.elements.push(...items);
    }

    dequeue() { // Eliminar y devolver
        return this.isEmpty() ? null : this.elements.shift();
    }

    peek() { // Obtener sin eliminar
        return this.isEmpty() ? null : this.elements[0];
    }

    toArray() { // Retornar cola como tupla
        return [...this.elements];
    }

    clear() { // Vaciar cola
        this.elements = [];
    }
}

// __________________________
console.log("\nUso de pila:");
const mystack = new Stack();
mystack.push("Zoe");
mystack.pushBatch(["Ben", "Dan"]);
if (!mystack.isEmpty()) {
    console.log(mystack.popGet());
}
console.log(`Número de elementos: ${mystack.length}`);
for (const name of mystack.toArray()) {
    console.log(name);
}

// __________________________
console.log("\nUso de cola:");
const myqueue = new Queue();
myqueue.enqueue("Zoe");
myqueue.enqueueAll(["Ben", "Dan"]);
if (!myqueue.isEmpty()) {
    console.log(myqueue.dequeue());
}
console.log(`Número de elementos: ${myqueue.length}`);
for (const name of myqueue.toArray()) {
    console.log(name);
}
