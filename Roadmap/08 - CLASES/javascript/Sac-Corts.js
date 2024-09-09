// Exercise
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`); 
        }
}

isaac = new Person('Isaac', 22);
isaac.greet();

isaac.name = 'Isaac Cortés';
isaac.age = 23;
isaac.greet();

// Extra Exercise //
class Stack {
    constructor() {
        this.array = [];
    }

    push(item) {
        this.array.push(item);
    }

    pop() {
        if (this.isEmpty()) {
            return "Stack is empty.";
        }
        return this.array.pop();
    }  

    peek() {
        if (this.isEmpty()) {
            return "Stack is empty.";
        }
        return this.array[this.array.length - 1];
    }

    isEmpty() {
        return this.array.length === 0;
    }

    size() {
        return this.array.length;
    }
}

const stack = new Stack();
stack.push('Karina');
stack.push('Isaac');
stack.push('Danna');
console.log(stack.peek());
console.log(stack.pop());
console.log(stack.isEmpty());
console.log(stack.size());


class Queue{
    constructor() {
        this.array = [];
    }

    enqueue(item) {
        this.array.push(item);
    } 

    dequeue() {
        if (this.isEmpty()) {
            return "Queue is empty."
        }
        return this.array.shift();
    }

    front() {
        if (this.isEmpty()) {
            return "Queue is empty."
        }
        return this.array[0];
    }

    isEmpty() {
        return this.array.length === 0;
    }

    size() {
        return this.array.length;
    }
}

const queue = new Queue();
queue.enqueue('Marco');
queue.enqueue('Ceci');
queue.enqueue('Jenni');
console.log(queue.front());
console.log(queue.dequeue());
console.log(queue.isEmpty());
console.log(queue.size());




