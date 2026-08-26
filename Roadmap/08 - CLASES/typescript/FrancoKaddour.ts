// https://www.typescriptlang.org/

// Clase básica
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  display(): void {
    console.log(`${this.name}, ${this.age} años`);
  }
}

const alice = new Person("Alice", 30);
alice.display();
alice.age = 31;
alice.display();

// Dificultad extra: clases Stack y Queue

class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }

  get count(): number {
    return this.items.length;
  }

  display(): void {
    console.log(this.items);
  }
}

class Queue<T> {
  private items: T[] = [];

  enqueue(item: T): void {
    this.items.push(item);
  }

  dequeue(): T | undefined {
    return this.items.shift();
  }

  get count(): number {
    return this.items.length;
  }

  display(): void {
    console.log(this.items);
  }
}

const stack = new Stack<number>();
stack.push(1);
stack.push(2);
stack.push(3);
stack.display();
console.log(stack.pop());
console.log(stack.count);

const queue = new Queue<string>();
queue.enqueue("a");
queue.enqueue("b");
queue.enqueue("c");
queue.display();
console.log(queue.dequeue());
console.log(queue.count);
