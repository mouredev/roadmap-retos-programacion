// Exercise // 
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

    peek() {
        if (this.isEmpty()) {
            return "Stack is empty";
        }
        return this.items[this.items.length - 1];
    }

    isEmpty() {
        return this.items.length === 0;
        }

    size() {
        return this.items.length;
    }   
}

const stack = new Stack();
stack.push(11);
stack.push(7);
stack.push(21);
console.log(stack.peek());
console.log(stack.pop());
console.log(stack.size());
console.log(stack.isEmpty());

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

    front() {
        if (this.isEmpty()) {
            return "Queue is empty";
        }
        return this.items[0];
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length;
    }
}

const queue = new Queue();
queue.enqueue(11);
queue.enqueue(7);
queue.enqueue(21);
console.log(queue.front());
console.log(queue.dequeue());
console.log(queue.size());
console.log(queue.isEmpty());

// Extra Exercise //

// Browser History
const readline = require('readline');

class BrowserHistory {
    constructor() {
        this.record = [];
        this.forward = [];
    }
    
    navigateTo(page) {
        this.record.push(page);
        this.forward.length = 0;
        console.log(`Current page: ${page}`);
    }

    goBack() {
        if (this.record.length > 1) {
            const lastPage = this.record.pop();
            this.forward.push(lastPage);
            console.log(`Current page: ${this.record[this.record.length - 1]}`);
        } else {
            console.log("There are no more pages");
        }
    }

    goForward() {
        if (this.forward.length) {
            const nextPage = this.forward.pop();
            this.record.push(nextPage);
            console.log(`Current page: ${nextPage}`)
        } else {
            console.log("There are no more pages");
        }
    }
}

// Printer
class Printer {
    constructor() {
        this.queue = [];
    }

    addDocument(document) {
        this.queue.push(document);
    }

    printDocument() {
        if (this.queue.length > 0) {
            const print = this.queue.shift();
            console.log(`Printing ${print} | Remaining queue: ${this.queue}`);
        } else {
            console.log("There are no prints at the moment.");
        }
    }
}

const myHistory = new BrowserHistory();
const myPrinter = new Printer();

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Functions to control the browser history and the printer
function historyControl() {
    rl.question("Enter a page or 'backward'/'forward' ('exit' to finish): ", (command) => {
        command = command.toLowerCase();
        if (command === 'backward') {
            myHistory.goBack();
        } else if (command === 'forward') {
            myHistory.goForward();
        } else if (command === 'hexit') {
            console.log("Exiting the browser...");
            printerControl();
            return;
        } else {
            myHistory.navigateTo(command);
        }
    
        historyControl();
    });
}


function printerControl() {
    rl.question("Enter a document or 'print' (if you want to print a document in the queue): ", (command) => {
        command = command.toLowerCase();
        if (command === 'print') {
            myPrinter.printDocument();
        } else if (command === 'pexit') {
            console.log("Turning off the printer...");
            rl.close();
        } else {
            myPrinter.addDocument(command);
            console.log(`Print queue: ${myPrinter.queue}`);
        }

        printerControl();
    });
}

historyControl();   