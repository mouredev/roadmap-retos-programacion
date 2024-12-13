// Ejemplo de una clase en TypeScript

/**
 * Clase Persona que representa a una persona con nombre y edad.
 */
class Persona {
    private nombre: string;
    private edad: number;

    constructor(nombre: string, edad: number) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Métodos getter y setter
    getNombre(): string {
        return this.nombre;
    }

    setNombre(nombre: string): void {
        this.nombre = nombre;
    }

    getEdad(): number {
        return this.edad;
    }

    setEdad(edad: number): void {
        this.edad = edad;
    }

    // Método para imprimir los datos de la persona
    imprimirDatos(): void {
        console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
    }
}

/**
 * Clase Pila que implementa una estructura de datos de tipo pila (LIFO).
 */
class Pila<T> {
    private elementos: T[];

    constructor() {
        this.elementos = [];
    }

    push(elemento: T): void {
        this.elementos.push(elemento);
    }

    pop(): T | undefined {
        return this.elementos.pop();
    }

    size(): number {
        return this.elementos.length;
    }

    imprimirContenido(): void {
        console.log("Contenido de la pila:", this.elementos);
    }
}

/**
 * Clase Cola que implementa una estructura de datos de tipo cola (FIFO).
 */
class Cola<T> {
    private elementos: T[];

    constructor() {
        this.elementos = [];
    }

    enqueue(elemento: T): void {
        this.elementos.push(elemento);
    }

    dequeue(): T | undefined {
        return this.elementos.shift();
    }

    size(): number {
        return this.elementos.length;
    }

    imprimirContenido(): void {
        console.log("Contenido de la cola:", this.elementos);
    }
}

// Función principal para probar las implementaciones
function main(): void {
    // Prueba de la clase Persona
    const persona = new Persona("Juan", 30);
    persona.imprimirDatos();
    persona.setEdad(31);
    persona.imprimirDatos();

    // Prueba de la Pila
    const pila = new Pila<number>();
    pila.push(1);
    pila.push(2);
    pila.push(3);
    pila.imprimirContenido();
    console.log("Elemento extraído de la pila:", pila.pop());
    pila.imprimirContenido();

    // Prueba de la Cola
    const cola = new Cola<string>();
    cola.enqueue("A");
    cola.enqueue("B");
    cola.enqueue("C");
    cola.imprimirContenido();
    console.log("Elemento extraído de la cola:", cola.dequeue());
    cola.imprimirContenido();
}

// Ejecutar la función principal
main();