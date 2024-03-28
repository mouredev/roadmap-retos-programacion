class Stack<T> {
    private items: T[];

    constructor() {
        this.items = [];
    }

    push(element: T): void {
        this.items.push(element);
    }

    pop(): T | undefined {
        return this.items.pop();
    }

    peek(): T | undefined {
        return this.items[this.items.length - 1];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }
}

class Queue<T> {
    private items: T[];

    constructor() {
        this.items = [];
    }

    enqueue(element: T): void {
        this.items.push(element);
    }

    dequeue(): T | undefined {
        return this.items.shift();
    }

    peek(): T | undefined {
        return this.items[0];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }
}

// Ejemplo de uso
const stack = new Stack<number>();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.pop()); // 3
console.log(stack.peek()); // 2
console.log(stack.size()); // 2

const queue = new Queue<string>();
queue.enqueue("documento1");
queue.enqueue("documento2");
queue.enqueue("documento3");
console.log(queue.dequeue()); // documento1
console.log(queue.peek()); // documento2
console.log(queue.size()); // 2


//
const browserStack = new Stack<string>();
let currentPage = "";

function navigateTo(url: string): void {
    browserStack.push(currentPage);
    currentPage = url;
    console.log(`Navegando a ${url}`);
}

function goBack(): void {
    const previousPage = browserStack.pop();
    if (previousPage) {
        currentPage = previousPage;
        console.log(`Volviendo a ${currentPage}`);
    } else {
        console.log("No hay páginas anteriores");
    }
}

function goForward(): void {
    const nextPage = browserStack.pop();
    if (nextPage) {
        browserStack.push(currentPage);
        currentPage = nextPage;
        console.log(`Avanzando a ${currentPage}`);
    } else {
        console.log("No hay páginas siguientes");
    }
}

// Ejemplo de uso
navigateTo("google.com");
navigateTo("facebook.com");
goBack(); // Volviendo a google.com
goForward(); // Avanzando a facebook.com
