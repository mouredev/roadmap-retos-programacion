//Stack

/*Modalidad con
Array*/

class Stack_Array {
  constructor() {
    this.stack = [];
  }
  push(element) {//Se agrega un nuevo elemento al final de la pila.
    this.stack.push(element);
    return this.stack;
  }
  pop() {//Se elimina el ultimo elemento de la pila.
    return this.stack.pop();
  }
  peak() {//Retorna el ultimo valor de la pila.
    return this.stack[this.stack.length - 1];
  }
  size() {
    return this.stack.length;
  }
  print() {
    console.log(this.stack);
  }
}
const stackArray = new Stack_Array();
console.log(stackArray.size());
console.log(stackArray.push("Pedro"));
console.log(stackArray.push("María"));
console.log(stackArray.size());
stackArray.print();
console.log(stackArray.peak());
console.log(stackArray.pop());
console.log(stackArray.peak());

/*Modalidad con
Object*/

class Stack_Obect {
  constructor() {
    this.stack = {};
    this.count = 0;
  }
  push(element) {
    this.stack[this.count] = element;
    this.count++;
    return this.stack;
  }
  pop() {
    this.count--;
    const element = this.stack[this.count];
    delete this.stack[this.count];
    return element;
  }
  peak() {
    return this.stack[this.count - 1];
  }
  size() {
    return this.count;
  }
  print() {
    console.log(this.stack);
  }
}
const stackObject = new Stack_Obect();
console.log(stackObject.size());
console.log(stackObject.push("Liliana"));//Se agrega el primer elemento a la pila.
console.log(stackObject.size());
console.log(stackObject.peak());//Retorna el ultimo elemento de la pila.
console.log(stackObject.push("Luisa"));
console.log(stackObject.size());
stackObject.print();
console.log(stackObject.peak());
console.log(stackObject.pop());//Elimina el último elemento de la pila.
stackObject.print();

//Queue

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
  peak() {
    return this.queue[0]
  }
  size() {
    return this.queue.length;
  }
  isEmpty() {
    return this.queue.length === 0;
  }
  print() {
    console.log(this.queue);
  }
}
const queue = new Queue();
console.log(queue.isEmpty());
console.log(queue.enqueue("Luis"));
console.log(queue.enqueue("María"));
console.log(queue.enqueue("Lysa"));
queue.print();
console.log(queue.dequeue());
queue.print();