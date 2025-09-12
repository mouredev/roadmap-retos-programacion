/*
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
 *
 */


/* Soluciones */


class Persona {
  // Inicializador
  constructor(nombre, apellido, edad) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
  }

  // Función para imprimir los atributos
  imprimirInfo() {
    console.log(`Nombre: ${this.nombre}`);
    console.log(`Apellido: ${this.apellido}`);
    console.log(`Edad: ${this.edad}`);
  }
}

// Creación de una instancia de la clase
const persona1 = new Persona("Juan", "Pérez", 30);

// Modificación de los atributos
persona1.nombre = "Daniel";
persona1.apellido = "Corbo";
persona1.edad = 24;

// Impresión de los atributos
persona1.imprimirInfo();


/* Extra - Opcional */


class Pila {
  constructor() {
    this.pila = [];
  }

  apilar(elemento) {
    this.pila.push(elemento);
  }

  desapilar() {
    if (this.estaVacia()) {
      return "La pila está vacía";
    }
    return this.pila.pop();
  }

  estaVacia() {
    return this.pila.length === 0;
  }

  imprimirElementos() {
    if (this.estaVacia()) {
      return "La pila está vacía";
    }
    let resultado = "Elementos:\n";
    this.pila.forEach((elemento, index) => {
      resultado += `Elemento ${index}: ${elemento}\n`;
    });
    return resultado;
  }
}

class Cola {
  constructor() {
    this.cola = [];
  }

  encolar(elemento) {
    this.cola.push(elemento);
  }

  desencolar() {
    if (this.estaVacia()) {
      return "La cola está vacía";
    }
    return this.cola.shift();
  }

  estaVacia() {
    return this.cola.length === 0;
  }

  imprimirElementos() {
    if (this.estaVacia()) {
      return "La cola está vacía";
    }
    let resultado = "Elementos:\n";
    this.cola.forEach((elemento, index) => {
      resultado += `Elemento ${index}: ${elemento}\n`;
    });
    return resultado;
  }
}

// Ejemplo de uso

const miPila = new Pila();

miPila.apilar("Hola");
miPila.apilar("Mundo");
miPila.apilar("!");

console.log(miPila.imprimirElementos());
/* Salida: 
Elementos:
Elemento 0: Hola
Elemento 1: Mundo
Elemento 2: ! */
console.log(`Primer elemento: ${miPila.desapilar()}`); // Salida: !
console.log(`Segundo elemento: ${miPila.desapilar()}`); // Salida: Mundo
console.log(`¿Pila vacía?: ${miPila.estaVacia()}`); // Salida: false
console.log(`Último elemento: ${miPila.desapilar()}`); // Salida: Hola
console.log(`¿Pila vacía?: ${miPila.estaVacia()}`); // Salida: true

const miCola = new Cola();

miCola.encolar("Primero");
miCola.encolar("Segundo");
miCola.encolar("Tercero");

console.log(miCola.imprimirElementos());
/* Salida: 
Elementos:
Elemento 0: Primero
Elemento 1: Segundo
Elemento 2: Tercero */
console.log(`Primer elemento: ${miCola.desencolar()}`); // Salida: Primero
console.log(`Segundo elemento: ${miCola.desencolar()}`); // Salida: Segundo
console.log(`¿Cola vacía?: ${miCola.estaVacia()}`); // Salida: false
console.log(`Último elemento: ${miCola.desencolar()}`); // Salida: Tercero
console.log(`¿Cola vacía?: ${miCola.estaVacia()}`); // Salida: true
