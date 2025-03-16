/**
 * Clase Persona
 */

// Implementación del inicializador
class Persona {
  nombre: string; // Atributo de la clase
  edad: number; // Atributo de la clase
  lenguajes: string[]; // Atributo de la clase

  constructor(nombre: string, edad: number, lenguajes: string[]) {
    // Inicializador de la clase
    this.nombre = nombre; // Asignación del valor al atributo
    this.edad = edad; // Asignación del valor al atributo
    this.lenguajes = lenguajes; // Asignación del valor al atributo
  }

  imprimir() {
    // Función que imprime los datos de la persona
    console.log(
      "Hola, mi nombre es " +
        this.nombre +
        ", tengo " +
        this.edad +
        " y conozco los lenguajes: " +
        this.lenguajes
    );
  }
}

let persona1 = new Persona("Anthony", 26, ["TS", "Py", "C"]); // Creación y establecimiento de parámetros
persona1.imprimir(); // Impresión de los datos

// Ejercicio extra: Implementación de Pila y Cola (LIFO y FIFO)
// Clase Pila (Last In, First Out)
class Pila {
  arreglo: any[];

  constructor() {
    this.arreglo = [];
  }

  // Métodos de la Pila
  apilar(elemento: any) {
    this.arreglo.push(elemento);
  }

  // Método desapilar
  desapilar(): any {
    if (this.arreglo.length === 0) {
      throw new Error("La pila está vacía");
      return null;
    }
    return this.arreglo.pop();
  }

  // Método contar
  contar(): number {
    return this.arreglo.length;
  }

  // Método imprimir
  imprimir() {
    console.log("Contenido de la pila:");
    for (let i = this.arreglo.length - 1; i >= 0; i--) {
      console.log(this.arreglo[i]);
    }
  }
}

let pila = new Pila(); // Creación de la pila
pila.apilar("Hola");
pila.apilar("Mundo");
pila.contar(); // Impresión del número de elementos en la pila
pila.imprimir(); // Impresión del contenido de la pila

// Clase Cola (First In, First Out)
class Cola {
  arreglo: any[];

  constructor() {
    this.arreglo = [];
  }

  // Métodos de la Cola
  // Metodo encolar
  encolar(elemento: any) {
    this.arreglo.push(elemento);
  }

  // Método desencolar
  desencolar(): any {
    if (this.arreglo.length === 0) {
      throw new Error("La cola esta vacia");
    }
    return this.arreglo.pop(0);
  }

  // Método contar
  contar(): number {
    return this.arreglo.length;
  }

  // Método imprimir para mostrar los elementos de la cola
  imprimir() {
    console.log("Contenido de la cola:");
    for (let i = 0; i < this.arreglo.length; i++) {
      console.log(this.arreglo[i]);
    }
  }
}

let cola = new Cola(); // Creación de la cola
cola.encolar("Hola");
cola.encolar("Mundo");
cola.contar(); // Impresión del número de elementos en la cola
cola.imprimir(); // Imprimimos la cola
cola.desencolar(); // Eliminación del primer elemento en la cola
cola.imprimir(); // Imprimimos la cola
