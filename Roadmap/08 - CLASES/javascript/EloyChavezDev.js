/* 
EJERCICIO:
 *Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
*/

// Clase básica con inicializador, atributos y función de impresión:
class Persona {
    constructor(nombre, edad) {
      this.nombre = nombre;
      this.edad = edad;
    }
  
    imprimir() {
      console.log(`Nombre: ${this.nombre}`);
      console.log(`Edad: ${this.edad}`);
    }
  }
  
  // Creación de una instancia de la clase
  const persona1 = new Persona("Juan", 25);
  
  // Modificación de los atributos
  persona1.nombre = "María";
  persona1.edad = 30;
  
  // Impresión de los atributos
  persona1.imprimir();


  //Dificultad Extra: Implementación de Pila y Cola
  class Pila {
    constructor() {
      this.pila = [];
    }
  
    // Añadir un elemento
    push(elemento) {
      this.pila.push(elemento);
    }
  
    // Sacar un elemento
    pop() {
      return this.pila.pop();
    }
  
    // Ver el último elemento sin sacarlo
    peek() {
      return this.pila[this.pila.length - 1];
    }
  
    // Ver si la pila está vacía
    estaVacia() {
      return this.pila.length === 0;
    }
  
    // Imprimir la pila
    imprimir() {
      console.log("Pila:");
      for (const elemento of this.pila) {
        console.log(elemento);
      }
    }
  }
  
  // Ejemplo de uso
  const pila = new Pila();
  pila.push("Elemento 1");
  pila.push("Elemento 2");
  pila.push("Elemento 3");
  
  pila.imprimir();
  
  pila.pop();
  
  pila.imprimir();

  //Clase Cola:
  class Cola {
    constructor() {
      this.cola = [];
    }
  
    // Añadir un elemento
    enqueue(elemento) {
      this.cola.push(elemento);
    }
  
    // Sacar un elemento
    dequeue() {
      return this.cola.shift();
    }
  
    // Ver el primer elemento sin sacarlo
    peek() {
      return this.cola[0];
    }
  
    // Ver si la cola está vacía
    estaVacia() {
      return this.cola.length === 0;
    }
  
    // Imprimir la cola
    imprimir() {
      console.log("Cola:");
      for (const elemento of this.cola) {
        console.log(elemento);
      }
    }
  }
  
  // Ejemplo de uso
  const cola = new Cola();
  cola.enqueue("Elemento 1");
  cola.enqueue("Elemento 2");
  cola.enqueue("Elemento 3");
  
  cola.imprimir();
  
  cola.dequeue();
  
  cola.imprimir();