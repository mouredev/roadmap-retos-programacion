class Programmer {
  constructor(name, age, language) {
    this.name = name;
    this.age = age;
    this.language = language;
  }
  printInfo() {
    console.log(
      `Name: ${this.name} | Age: ${this.age} | Language: ${this.language}`
    );
  }
}

const my_programmer = new Programmer("Glitzypanic", 25, "JavaScript");
my_programmer.printInfo();

// EJERCICIO
class Stack {
  constructor() {
    this.stack = [];
  }
  push(item) {
    this.stack.push(item);
  }
  pop() {
    if (this.count() == 0) {
      return null;
    }
    return this.stack.pop();
  }
  count() {
    return this.stack.length;
  }
  print() {
    for (let i = this.stack.length - 1; i >= 0; i--) {
      console.log(this.stack[i]);
    }
  }
}

const my_stack = new Stack();
my_stack.push("Jose");
my_stack.push("Daniel");
my_stack.push("Farias");
my_stack.push("Cordova");
my_stack.push("Glitzypanic");
console.log(my_stack.count());
my_stack.print();
my_stack.pop();
my_stack.pop();
console.log(my_stack.count());
console.log(my_stack.pop());
my_stack.print();

// EJERCICIO 2
class Queue {
  constructor() {
    this.Queue = [];
  }
  push(item) {
    this.Queue.push(item);
  }
  shift() {
    if (this.Queue.length == 0) {
      return null;
    }
    return this.Queue.shift();
  }
  count() {
    return this.Queue.length;
  }
  print() {
    for (let i = 0; i < this.Queue.length; i++) {
      console.log(this.Queue[i]);
    }
  }
}

const my_queue = new Queue();
my_queue.push("Tamara");
my_queue.push("Francisca");
my_queue.push("Nuñez");
my_queue.push("Rodriguez");
my_queue.count();
my_queue.print();
console.log(my_queue.shift());
console.log(my_queue.count());
my_queue.shift();
console.log(my_queue.count());
console.log(my_queue.shift());
