class Person {
    name: string;
    age: number;
    job: string;

    constructor(name: string, age: number, job: string) {
        this.name = name;
        this.age = age;
        this.job = job;
    }

    printDetails(): void {
        console.log(`Name: ${this.name}`);
        console.log(`Age: ${this.age}`);
        console.log(`Job: ${this.job}`);
    }
}

let person1 = new Person("Isaac", 22, "Backend Developer");
person1.printDetails();

person1.name = "Yusuke";
person1.age = 14;
person1.job = "Fighter";
person1.printDetails();

// *** Extra Exercise *** //

// Stack
class Stack<T> {
    private elements: T[] = [];

    push(element: T): void {
        this.elements.push(element);
    }

    pop(): T | undefined {
        return this.elements.pop();
    }

    size(): number {
        return this.elements.length;
    }

    print(): void {
        console.log("Stack: ", this.elements);
    }
}

let stack = new Stack<number>();
stack.push(10);
stack.push(11);
console.log(stack.print());
console.log(stack.pop());
console.log(stack.size());

// Queue
class Queue<T> {
    private elements: T[] = [];

    enqueue(element: T): void {
        this.elements.push(element);
    }

    dequeue(): T | undefined {
        return this.elements.shift();
    }

    size(): number {
        return this.elements.length;
    }

    print(): void {
        console.log("Queue: ", this.elements);
    }
}

let queue = new Queue<string>();
queue.enqueue("A");
queue.enqueue("B");
console.log(queue.print());
console.log(queue.dequeue());
console.log(queue.size());
