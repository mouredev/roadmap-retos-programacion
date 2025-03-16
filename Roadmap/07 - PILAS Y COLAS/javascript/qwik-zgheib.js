/* -- exercise */
/* stack - LIFO */
class Stack {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element);
  }

  pop() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items.pop();
  }

  isEmpty() {
    return this.items.length === 0;
  }

  peek() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.items.length - 1];
  }

  size() {
    return this.items.length;
  }

  print() {
    console.log(this.items.toString());
  }
}

let stack = new Stack();
stack.push(10);
stack.push(20);
stack.push(30);
stack.print();
console.log(stack.pop() !== null ? "Popped" : "Stack is empty");
stack.print();
console.log(stack.peek() !== null ? "Peeked" : "Stack is empty");

/* queue - FIFO */
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

  isEmpty() {
    return this.items.length === 0;
  }

  front() {
    if (this.isEmpty()) {
      return "Queue is empty";
    }
    return this.items[0];
  }

  size() {
    return this.items.length;
  }

  printQueue() {
    console.log("Queue:", this.items.toString());
  }
}

let queue = new Queue();
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.printQueue();
console.log(queue.dequeue());
queue.printQueue();
console.log(queue.front());

/* -- extra challenge */
class Browser {
  constructor() {
    this.backStack = new Stack();
    this.forwardStack = new Stack();
    this.currentPage = null;
  }

  navigate(page) {
    if (this.currentPage !== null) this.backStack.push(this.currentPage);

    this.currentPage = page;
    this.forwardStack = new Stack();
    console.log("Navigated to:", this.currentPage);
  }

  back() {
    if (this.backStack.isEmpty()) {
      console.log("No pages to go back to.");
      return;
    }
    this.forwardStack.push(this.currentPage);
    this.currentPage = this.backStack.pop();
    console.log("Went back to:", this.currentPage);
  }

  forward() {
    if (this.forwardStack.isEmpty()) {
      console.log("No pages to go forward to.");
      return;
    }
    this.backStack.push(this.currentPage);
    this.currentPage = this.forwardStack.pop();
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
  constructor() {
    this.queue = new Queue();
  }

  addDocument(document) {
    this.queue.enqueue(document);
    console.log("Added document:", document);
  }

  printDocument() {
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
