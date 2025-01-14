/* -- exercise */
/* stack - LIFO */
class Stack<T> {
  private items: T[];

  constructor() {
    this.items = [];
  }

  push(element: T): void {
    this.items.push(element);
  }

  pop(): T | null {
    if (this.isEmpty()) {
      return null;
    }
    return this.items.pop() as T;
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }

  peek(): T | null {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.items.length - 1];
  }

  size(): number {
    return this.items.length;
  }

  print(): void {
    console.log(this.items.toString());
  }
}

let stack = new Stack<number>();
stack.push(10);
stack.push(20);
stack.push(30);
stack.print();
console.log(stack.pop() !== null ? "Popped" : "Stack is empty");
stack.print();
console.log(stack.peek() !== null ? "Peeked" : "Stack is empty");

/* queue - FIFO */
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

  isEmpty(): boolean {
    return this.items.length === 0;
  }

  front(): T | string {
    if (this.isEmpty()) {
      return "Queue is empty";
    }
    return this.items[0];
  }

  size(): number {
    return this.items.length;
  }

  printQueue(): void {
    console.log("Queue:", this.items.toString());
  }
}

let queue = new Queue<number>();
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.printQueue();
console.log(queue.dequeue());
queue.printQueue();
console.log(queue.front());

/* -- extra challenge */
class Browser {
  private backStack: Stack<string>;
  private forwardStack: Stack<string>;
  private currentPage: string | null;

  constructor() {
    this.backStack = new Stack<string>();
    this.forwardStack = new Stack<string>();
    this.currentPage = null;
  }

  navigate(page: string): void {
    if (this.currentPage !== null) this.backStack.push(this.currentPage);

    this.currentPage = page;
    this.forwardStack = new Stack<string>();
    console.log("Navigated to:", this.currentPage);
  }

  back(): void {
    if (this.backStack.isEmpty()) {
      console.log("No pages to go back to.");
      return;
    }
    this.forwardStack.push(this.currentPage as string);
    this.currentPage = this.backStack.pop() as string;
    console.log("Went back to:", this.currentPage);
  }

  forward(): void {
    if (this.forwardStack.isEmpty()) {
      console.log("No pages to go forward to.");
      return;
    }
    this.backStack.push(this.currentPage as string);
    this.currentPage = this.forwardStack.pop() as string;
    console.log("Went forward to:", this.currentPage);
  }
}

let browser = new Browser();
browser.navigate("page1.com");
browser.navigate("page2.com");
browser.navigate("page3.com");
browser.back();
browser.back();
browser.forward();
browser.navigate("page4.com");
browser.forward();

class Printer {
  private queue: Queue<string>;

  constructor() {
    this.queue = new Queue<string>();
  }

  addDocument(document: string): void {
    this.queue.enqueue(document);
    console.log("Added document:", document);
  }

  printDocument(): void {
    const document = this.queue.dequeue();
    if (document !== "Queue is empty") console.log("Printing document:", document);
    else console.log(document);
  }
}

let printer = new Printer();
printer.addDocument("doc1.pdf");
printer.addDocument("doc2.pdf");
printer.addDocument("doc3.pdf");
printer.printDocument();
printer.printDocument();
printer.printDocument();
printer.printDocument();
