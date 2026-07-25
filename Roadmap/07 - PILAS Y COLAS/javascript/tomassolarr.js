/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */
 class Stack{
    constructor(){
        this.array=[];
    }
    push(elemento){
        this.array.push(elemento);
    } 
    pop(){
        return this.array.pop();
    }
    mostrar(){
        return this.array
    }
 }
    
 const pila = new Stack();

pila.push(1)
pila.push(2)
pila.push(3)

console.log(pila.mostrar())
console.log(pila.pop());
console.log(pila.mostrar());

class Queue {

  constructor() {
    this.items = [];
  }

  enqueue(elemento) {
    this.items.push(elemento);
  }

  dequeue() {
    return this.items.shift();
  }

  mostrar() {
    return this.items;
  }
}

const cola = new Queue();

cola.enqueue(1);
cola.enqueue(2);
cola.enqueue(3);

console.log(cola.mostrar());
console.log(cola.dequeue());
console.log(cola.mostrar());

/* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */