/* -- exercise */
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  printDetails() {
    console.log(`Name: ${this.name}, Age: ${this.age}`);
  }

  setDetails(name, age) {
    this.name = name;
    this.age = age;
  }
}

let person = new Person("Abdul Rahman", 22);
person.printDetails();
person.setDetails("Ahmed Khedr", 20);
person.printDetails();

/* -- extra challenge */
class Stack {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element);
  }

  pop() {
    if (this.isEmpty()) {
      return "Stack is empty";
    }
    return this.items.pop();
  }

  size() {
    return this.items.length;
  }

  print() {
    console.log("Stack:", this.items.toString());
  }

  isEmpty() {
    return this.items.length === 0;
  }
}

let stack = new Stack();
stack.push(10);
stack.push(20);
stack.push(30);
stack.print();
console.log("Popped:", stack.pop());
stack.print();
console.log("Size:", stack.size());

class Queue {
  constructor() {
    this.items = [];
  }

  enqueue(element) {
    this.items.push(element);
  }

  dequeue() {
    if (this.isEmpty()) {
      return "Queue is empty";
    }
    return this.items.shift();
  }

  size() {
    return this.items.length;
  }

  print() {
    console.log("Queue:", this.items.toString());
  }

  isEmpty() {
    return this.items.length === 0;
  }
}

let queue = new Queue();
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.print();
console.log("Dequeued:", queue.dequeue());
queue.print();
console.log("Size:", queue.size());
