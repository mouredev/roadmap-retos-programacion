/* Pilas (Stacks - LIFO) */

class Pila {
  constructor() {
    this.elementos = [];
  }

  push(elementos) {
    this.elementos.push(elemento);
  }

  pop() {
    if (this.isEmpty()) {
      return null;
    }
    return this.elementos.pop();
  }

  isEmpty() {
    return this.elementos.length === 0;
  }
}

// Ejemplo de uso
let pila = new Pila();
pila.push(1);
pila.push(2);
pila.push(3);

console.log(pila.pop());
console.log(pila.peek());
console.log(pila.isEmpty());

/* Colas (Queues - FIFO) */

class Cola {
  constructor() {
    this.elementos = [];
  }

  enqueue(elemento) {
    this.elementos.push(elemento);
  }

  dequeue() {
    if (this.isEmpty()) {
      return null;
    }
    return this.elementos.shift();
  }

  peek() {
    if (this.isEmpty()) {
      return null;
    }
    return this.elementos[0];
  }

  isEmpty() {
    return this.elementos.length === 0;
  }
}

// Ejemplo de uso
let cola = new Cola();
cola.enqueue(1);
cola.enqueue(2);
cola.enqueue(3);

console.log(cola.dequeue());
console.log(cola.peek());
console.log(cola.isEmpty());
