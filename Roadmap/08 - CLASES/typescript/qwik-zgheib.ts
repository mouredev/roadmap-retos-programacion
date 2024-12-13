/* -- exercise */
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  printDetails(): void {
    console.log(`Name: ${this.name}, Age: ${this.age}`);
  }

  setDetails(name: string, age: number): void {
    this.name = name;
    this.age = age;
  }
}

let person = new Person("Abdul Rahman", 22);
person.printDetails();
person.setDetails("Ahmed Khedr", 20);
person.printDetails();

/* -- extra challenge */
class Stack<T> {
  private items: T[];

  constructor() {
    this.items = [];
  }

  push(element: T): void {
    this.items.push(element);
  }

  pop(): T | string {
    if (this.isEmpty()) {
      return "Stack is empty";
    }
    return this.items.pop() as T;
  }

  size(): number {
    return this.items.length;
  }

  print(): void {
    console.log("Stack:", this.items.toString());
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }
}

let stack = new Stack<number>();
stack.push(10);
stack.push(20);
stack.push(30);
stack.print();
console.log("Popped:", stack.pop());
stack.print();
console.log("Size:", stack.size());

class Queue<T> {
  private items: T[];

  constructor() {
    this.items = [];
  }

  enqueue(element: T): void {
    this.items.push(element);
  }

  dequeue(): T | string {
    if (this.isEmpty()) {
      return "Queue is empty";
    }
    return this.items.shift() as T;
  }

  size(): number {
    return this.items.length;
  }

  print(): void {
    console.log("Queue:", this.items.toString());
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }
}

let queue = new Queue<number>();
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.print();
console.log("Dequeued:", queue.dequeue());
queue.print();
console.log("Size:", queue.size());
