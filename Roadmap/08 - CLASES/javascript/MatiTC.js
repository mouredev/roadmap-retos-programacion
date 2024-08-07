/*
 * EJERCICIO:
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 *
 */

// Definición de la clase Persona
class Persona {
  // Inicializado (constructor :  es un método especial para crear e inicializar un objeto)
  constructor(nombre, edad) {
    this.nombre = nombre; // Atributo nombre
    this.edad = edad; // Atributo edad
  }

  // Función para imprimir los atributos
  imprimirInformacion() {
    console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
  }
  // Función para modificar los atributos
  modificarNombre(nombre) {
    this.nombre = nombre;
  }
  // Función para modificar los atributos
  modificarEdad(edad) {
    this.edad = edad;
  }
}
// Creación de una instancia de la clase Persona
const persona1 = new Persona('Matias', 24);
// Llamada a la función para imprimir los atributos
persona1.imprimirInformacion(); // Salida esperada: Nombre: Matias, Edad: 24
// Llamada a la funcion para modificar(edad)
persona1.modificarEdad(25);
persona1.imprimirInformacion(); // Salida esperada: Nombre: Matias, Edad: 25

//<---Dificultad extra--->
//<---Pila/stacks--->
// Definición de la clase Pila
class Pila {
  // Atributos
  // Constructor de la clase
  constructor() {
    this.items = []; // Array para almacenar los elementos de la pila
  }
  //Funciones
  // Método para agregar un elemento a la pila
  push(elemento) {
    this.items.push(elemento);
  }
  // Método para eliminar y devolver el último elemento de la pila
  pop() {
    if (this.items.length === 0) {
      return 'La pila está vacía'; // Si la pila está vacía, se devuelve un mensaje
    }
    return this.items.pop(); // Se elimina y devuelve el último elemento de la pila
  }
  // Método para obtener el tamaño de la pila
  size() {
    return this.items.length; // Se devuelve el tamaño de la pila
  }
  // Método para vaciar la pila
  clear() {
    this.items = []; // Se vacía la pila
  }
}

// Ejemplo de uso de la clase Pila
const pruebaPila = new Pila(); // Creamos una nueva instancia de la clase Pila
pruebaPila.push(1); // Agregamos el elemento 1 a la pila
pruebaPila.push(2); // Agregamos el elemento 2 a la pila
pruebaPila.push(3); // Agregamos el elemento 3 a la pila
console.log('Elementos de la pila:', pruebaPila.items); // Mostramos los elementos de la pila
console.log('Tamaño de la pila:', pruebaPila.size()); // Mostramos el tamaño de la pila
console.log('Se saca con pop:', pruebaPila.pop()); // Desapilamos un elemento de la pila
console.log('Elementos de la pila después del pop:', pruebaPila.items); //

//<---Cola--->
// Definición de la clase Cola
class Cola {
  // Constructor de la clase
  constructor() {
    this.items = []; // Array para almacenar los elementos de la cola
  }
  // Método para agregar un elemento a la cola
  enqueue(elemento) {
    this.items.push(elemento); // Agrega el elemento al final de la cola
  }
  // Método para eliminar y devolver el primer elemento de la cola
  dequeue() {
    if (this.items.length === 0) {
      return 'La cola está vacía'; // Si la cola está vacía, se devuelve un mensaje
    }
    return this.items.shift(); // Elimina y devuelve el primer elemento de la cola
  }
  // Método para obtener el tamaño de la cola
  size() {
    return this.items.length; // Devuelve el tamaño de la cola
  }
  // Método para vaciar la cola
  clear() {
    this.items = []; // Vacía la cola
  }
}
// Ejemplo de uso de la clase Cola
const cola = new Cola(); // Creamos una nueva instancia de la clase Cola
cola.enqueue('a'); // Agregamos el elemento "a" a la cola
cola.enqueue('b'); // Agregamos el elemento "b" a la cola
cola.enqueue('C'); // Agregamos el elemento "b" a la cola
console.log('Elementos de la cola:', cola.items); // Mostramos los elementos de la cola
console.log('Tamaño de la cola:', cola.size()); // Mostramos el tamaño de la cola
console.log('Se desencola:', cola.dequeue()); // Desencolamos un elemento de la cola
console.log('Elementos de la cola después de desencolar:', cola.items); // Mostramos los elementos de la cola después de desencolar
