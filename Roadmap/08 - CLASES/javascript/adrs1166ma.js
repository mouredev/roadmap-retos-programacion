/*
EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.

DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido.
*/

// 🔥 Clase básica
class Persona {
    constructor(nombre, edad, ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    imprimirDatos() {
        console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}, Ciudad: ${this.ciudad}`);
    }
}

// Instancia
const persona1 = new Persona("Anderson", 20, "Lima");
persona1.imprimirDatos(); // Nombre: Anderson, Edad: 20, Ciudad: Lima

// Modificar los atributos
persona1.nombre = "Adrs";
persona1.edad = 21;
persona1.imprimirDatos(); // Nombre: Adrs, Edad: 21, Ciudad: Lima

// 🔥 EXTRA - Pila y Cola

// Clase Pila (Stack - LIFO)
class Pila {
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

    // Retornar el número de elementos
    size() {
        return this.items.length;
    }

    // Mostrar el contenido de la pila
    print() {
        console.log(this.items.toString()||'La pila está vacía');
    }
}

const pila = new Pila();
console.log('*************** Clase Pila (Stack - LIFO) ********************')
pila.print(); // La pila está vacía
pila.push("A");
pila.push("B");
pila.push("C");
pila.print(); // A,B,C
console.log("Tamaño:", pila.size()); // Tamaño: 3
console.log("Eliminado:", pila.pop()); // Eliminado: C
pila.print(); // A,B


// Clase Cola (Queue - FIFO)
class Cola {
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
    
    // Retornar el número de elementos
    size() {
        return this.items.length;
    }

    // Imprimir el contenido de la cola
    print() {
        console.log(this.items.toString() || "La cola está vacía");
    }
}


const cola = new Cola();
console.log('*************** Clase Cola (Queue - FIFO) ********************')
cola.print(); // La cola está vacía
cola.enqueue("A");
cola.enqueue("B");
cola.enqueue("D");
cola.print(); // A,B,D
console.log("Tamaño:", cola.size()); // Tamaño: 3
console.log("Eliminado:", cola.dequeue()); // Eliminado: A
cola.print(); // B,D