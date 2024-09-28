/*
    * EJERCICIO:
    * Implementa los mecanismos de introducción y recuperación de elementos propios de las
    * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
    * o lista (dependiendo de las posibilidades de tu lenguaje).
*/
// Pilas
class Stack {
    constructor() {
      this.stack = [];
    }
    
    push( element ) {
      this.stack.push( element );
      return this.stack;
    }
    
    pop() {
      return this.stack.pop();
    }
    
    peek() {
      return this.stack[this.stack.length - 1];
    }
    
    size() {
      return this.stack.length;
    }
  
    print() {
      console.log(this.stack);
    }
  }
  
  const stack = new Stack();
  console.log(stack.size()); // 0
  console.log(stack.push('John Cena')); // ['John Cena']
  console.log(stack.push('The Rock')); // ['John Cena', 'The Rock']
  console.log(stack.size()); // 2
  stack.print(); // ['John Cena', 'The Rock]
  console.log(stack.peek()); // 'The Rock'
  console.log(stack.pop()); // 'The Rock'
  console.log(stack.peek()); // John Cena

  // Cola
  class Queue {
    constructor() {
      this.queue = [];
    }
  
    enqueue(element) {
      this.queue.push(element);
      return this.queue;
    }
  
    dequeue() {
      return this.queue.shift();
    }
  
    peek() {
      return this.queue[0];
    }
  
    size() {
      return this.queue.length;
    }
  
    isEmpty() {
      return this.queue.length === 0;
    }
  
    print() {
      return this.queue;
    }
  }
  
  const queue = new Queue();
  console.log(queue.enqueue('The Rock')); // ['The Rock']
  console.log(queue.enqueue('John Cena')); // ['The Rock', 'John Cena']
  console.log(queue.enqueue('Stone Cold Steve Austin')); // ['The Rock', 'John Cena', 'Stone Cold Steve Austin']
  console.log(queue.dequeue()); // 'The Rock'
  console.log(queue.peek()); // 'John Cena'
  console.log(queue.isEmpty()); // false
  console.log(queue.print()); // ['John Cena', 'Stone Cold Steve Austin']
/*
 * DIFICULTAD EXTRA (opcional):
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