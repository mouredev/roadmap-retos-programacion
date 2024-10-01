// Ejemplo de una clase en JavaScript

/**
 * Clase Persona que representa a una persona con nombre y edad.
 */
class Persona {
    // Constructor
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Métodos getter y setter
    getNombre() {
        return this.nombre;
    }

    setNombre(nombre) {
        this.nombre = nombre;
    }

    getEdad() {
        return this.edad;
    }

    setEdad(edad) {
        this.edad = edad;
    }

    // Método para imprimir los datos de la persona
    imprimirDatos() {
        console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
    }
}

/**
 * Clase Pila que implementa una estructura de datos de tipo pila (LIFO).
 */
class Pila {
    constructor() {
        this.elementos = [];
    }

    push(elemento) {
        this.elementos.push(elemento);
    }

    pop() {
        if (this.elementos.length === 0) {
            return "La pila está vacía";
        }
        return this.elementos.pop();
    }

    size() {
        return this.elementos.length;
    }

    imprimirContenido() {
        console.log("Contenido de la pila:", this.elementos);
    }
}

/**
 * Clase Cola que implementa una estructura de datos de tipo cola (FIFO).
 */
class Cola {
    constructor() {
        this.elementos = [];
    }

    enqueue(elemento) {
        this.elementos.push(elemento);
    }

    dequeue() {
        if (this.elementos.length === 0) {
            return "La cola está vacía";
        }
        return this.elementos.shift();
    }

    size() {
        return this.elementos.length;
    }

    imprimirContenido() {
        console.log("Contenido de la cola:", this.elementos);
    }
}

// Pruebas de las implementaciones
function main() {
    // Prueba de la clase Persona
    const persona = new Persona("Juan", 30);
    persona.imprimirDatos();
    persona.setEdad(31);
    persona.imprimirDatos();

    // Prueba de la Pila
    const pila = new Pila();
    pila.push(1);
    pila.push(2);
    pila.push(3);
    pila.imprimirContenido();
    console.log("Elemento extraído de la pila:", pila.pop());
    pila.imprimirContenido();

    // Prueba de la Cola
    const cola = new Cola();
    cola.enqueue("A");
    cola.enqueue("B");
    cola.enqueue("C");
    cola.imprimirContenido();
    console.log("Elemento extraído de la cola:", cola.dequeue());
    cola.imprimirContenido();
}

main();