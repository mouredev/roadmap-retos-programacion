// Stack
class Stack<T> {
    private items: T[] = [];

    push(element: T): void {
        this.items.push(element);
    }

    pop(): T | undefined {
        if (this.items.length === 0) {
            console.log("Stack is empty");
            return undefined;
        }
        return this.items.pop();
    }

    peek(): T | undefined {
        if (this.items.length === 0) {
            console.log("Stack is empty");
            return undefined;
        }
        return this.items[this.items.length - 1];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }

    clear(): void {
        this.items = [];
    }
}

const stack = new Stack<number>();
stack.push(10);
stack.push(20);
console.log(stack.peek());
console.log(stack.pop());
console.log(stack.isEmpty());
console.log(stack.size());
console.log(stack.clear());


// Queue
class Queue<T> {
    private items: T[] = [];

    enqueue(element: T): void {
        this.items.push(element);
    }

    dequeue(): T | undefined {
        if (this.items.length === 0) {
            console.log("Queue is empty");
            return undefined;
        }
        return this.items.shift();
    }

    front(): T | undefined {
        if (this.items.length === 0) {
            console.log("Queue is empty");
            return undefined;
        }
        return this.items[0];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }

    clear(): void {
        this.items = [];
    }
}

const queue = new Queue<number>();
queue.enqueue(10);
queue.enqueue(20);
console.log(queue.front());
console.log(queue.dequeue());
console.log(queue.isEmpty());
console.log(queue.size());
console.log(queue.clear());

// *** Extra Exercise *** //

// Browser History
class BrowserNavigation {
    private backStack: string[] = [];
    private forwardStack: string[] = [];
    private currentPage: string | null = null;

    navigateTo(page: string): void {
        if (this.currentPage) {
            this.backStack.push(this.currentPage);
        }
        this.currentPage = page;
        this.forwardStack = [];
        console.log(`Navigate to: ${this.currentPage}`);
    }

    goBack(): void {
        if (this.backStack.length === 0) {
            console.log("There are not pages back");
            return;
        }
        if (this.currentPage) {
            this.forwardStack.push(this.currentPage);
        }
        this.currentPage = this.backStack.pop() || null;
        console.log(`Going back to: ${this.currentPage}`);
    }

    goForward(): void {
        if (this.forwardStack.length === 0) {
            console.log("There are not pages forward");
            return;
        }
        if (this.currentPage) {
            this.backStack.push(this.currentPage);
        }
        this.currentPage = this.forwardStack.pop() || null;
        console.log(`Moving forward: ${this.currentPage}`);
    }
}

const browser = new BrowserNavigation();

function simulateNavigation(action: string): void {
    if (action === 'back') {
        browser.goBack();
    } else if (action === "forward") {
        browser.goForward();
    } else {
        browser.navigateTo(action);
    }
}

simulateNavigation("google.com");
simulateNavigation("github.com");
simulateNavigation("stackoverflow.com");
simulateNavigation("back");
simulateNavigation("back");
simulateNavigation("forward");
simulateNavigation("youtube.com");
simulateNavigation("back");
simulateNavigation("forward");

// Printer
class PrinterQueue {
    private queue: string[] = [];

    addDocument(document: string): void {
        this.queue.push(document);
        console.log(`Document "${document}" added to queue`);
    }

    printDocument(): void {
        if (this.queue.length === 0) {
            console.log("There are not documents in the queue");
            return;
        }
        const nextDocument = this.queue.shift();
        console.log(`Printing: ${nextDocument}`);
    }

    isEmpty(): boolean {
        return this.queue.length === 0;
    }
}

const printer = new PrinterQueue();

function simulatePrinter(action: string): void {
    if (action === "print") {
        printer.printDocument();
    } else {
        printer.addDocument(action);
    }
}

simulatePrinter("document1.pdf");
simulatePrinter("document2.pdf");
simulatePrinter("print");
simulatePrinter("document3.docx");
simulatePrinter("print");
simulatePrinter("print");
simulatePrinter("print");