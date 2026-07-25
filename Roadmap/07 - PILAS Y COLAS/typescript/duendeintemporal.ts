/* #07 { Retosparaprogramadores } Pilas y Colas  */
//I use GPT & Deepseekto generate accurate comments and also as a reference.

  //shorthand for console.log()
  let log = console.log;

//The array structure can be useful in JavaScript as in Typescript to simulate stacks and queues.

/* A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. You can think of it like a stack of plates: you add plates to the top and also remove them from the top.
Key Operations:

    Push: Add an element to the top of the stack.
    Pop: Remove the element from the top of the stack.
    Peek/Top: Retrieve the top element without removing it.
    IsEmpty: Check if the stack is empty.
 */

  //Pila(Stack)
  let stack: number[] = [1,2,3,4];
  
  //view the contents of a stack
  log('view stack: ', stack); // view stack: [ 1, 2, 3, 4 ]

  //add an element to the stack
  stack.push(5);
  log('add an element: ', stack); // add an element: [ 1, 2, 3, 4, 5 ] 

  //get the size of the stack
  log('size: ', stack.length); // size:  5

  //get the last value of the stack
  log('last value of the stack: ', stack[stack.length - 1]); // last value of the stack:  5

  //remove the last value from the stack and print its value
 log('delete and return the last value: ', stack.pop()); // delete and return the last value:  5

 //empty the stack
 stack = [];
 log('empty the stack: ', stack); // empty the stack: []

 /* we can also enclosed in a function or a class for better organization and reusability */
 interface IStack<T> {
    push(element: T): void;
    pop(): T | undefined;
    peek(): T | undefined;
    empty(): T[];
    isEmpty(): boolean;
    size(): number;
    getItems(): T[];
}

class Stack<T> implements IStack<T> {
    private items: T[];
    
    constructor(initialItems: T[] = []) {
        this.items = Array.isArray(initialItems) ? initialItems : [];
    }   
    
    getItems(): T[] {
        return [...this.items];
    }

    push(element: T): void {
        this.items.push(element);
    }

    pop(): T | null {
        if (this.isEmpty()) {
            console.error("Stack is empty. Cannot pop an element.");

            return null;
        }
        const item = this.items.pop();
        return item !== undefined ? item : null;
    }

    peek(): T | undefined {
        if (this.isEmpty()) {
            console.error("Stack is empty. Cannot peek.");

            return undefined;
        }
        return this.items[this.items.length - 1];
    }

    empty(): T[] {
        return this.items = [];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }
}

// Test code starts here
function testStack() {
    const stack2 = new Stack<number>([55, 76, 98, 100]);
    log('Initial stack2:', stack2.getItems());

    stack2.push(32);
    log('After pushing 32:', stack2.getItems());

    log('Peek:', stack2.peek());

    log('Pop:', stack2.pop());
    log('After popping:', stack2.getItems());

    log('Pop all elements:');
    while (!stack2.isEmpty()) {
        log('Popped:', stack2.pop());
    }

    log('Final stack2:', stack2.getItems());
    log('Pop from empty stack2:', stack2.pop());
}

// Run the test
testStack();
/*
Initial stack2: [ 55, 76, 98, 100 ] 
After pushing 32: [ 55, 76, 98, 100, 32 ]
Peek: 32
Pop: 32
After popping: [ 55, 76, 98, 100 ]
Pop all elements:
Popped: 100
Popped: 98
Popped: 76
Popped: 55
Final stack2: []
Stack is empty. Cannot pop an element.
Pop from empty stack2: null
*/

 //Cola(Queue)

 /* A queue is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed. You can think of it like a line of people waiting for service: the first person in line is the first to be served.
Key Operations:

    Enqueue: Add an element to the end of the queue.
    Dequeue: Remove the element from the front of the queue.
    Front/Peek: Retrieve the front element without removing it.
    IsEmpty: Check if the queue is empty.
 */

  let queue: number[] = [8, 5, 4, 2, 1];

  //view the contents of a queue
  log('view queue: ', queue); // view queue: [ 8, 5, 4, 2, 1 ]

  //add elements to the queue
  queue.push(7);
  log('add an element: ', queue); // add an element: [ 8, 5, 4, 2, 1, 7 ]

  //get the size of the queue
  log('size: ', queue.length); // size:  6

  //get the first value of the queue
  log('first value: ', queue[0]); // first value:  8

  //remove the first value from the queue and print its value
  log('delete and return the first value ', queue.shift()); // delete and return the first value  8

  //empty the queue
  queue = [];
  log('empty the queue: ', queue); // empty the queue: [] 

 /* we can also enclosed in a function or a class for better organization and reusability */
 interface IQueue<T> {
    enqueue(element: T): void;
    dequeue(): T | undefined;
    peek(): T | undefined;
    empty(): T[];
    isEmpty(): boolean;
    size(): number;
    getItems(): T[];
}

class Queue<T> implements IQueue<T> {
    private items: T[];

    constructor(initialItems: T[] = []) {
        this.items = Array.isArray(initialItems) ? initialItems : [];
    }

    getItems(): T[] {
        return [...this.items];
    }

    enqueue(element: T): void {
        this.items.push(element);
    }

    dequeue(): T | undefined {
        if (this.isEmpty()) {
            console.error("Queue is empty. Cannot dequeue an element.");
            return undefined;
        }
        return this.items.shift();
    }


    peek(): T | undefined {
        if (this.isEmpty()) {
            console.error("Queue is empty. Cannot peek.");
            return undefined;
        }
        return this.items[0];
    }

    empty(): T[] {
        return this.items = [];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }
}

const queue2 = new Queue<number>([45, 32, 16]); 
log('Initial queue2:', queue2.getItems()); //  [45, 32, 16]

queue2.enqueue(77);
log('After enqueueing 4:', queue2.getItems()); //  [45, 32, 16, 77]

log('Peek:', queue2.peek()); //  45

log('Dequeue:', queue2.dequeue()); //  45
log('After dequeueing:', queue2.getItems()); //  [32, 16, 77]

log('Dequeue all elements:'); // Dequeue all elements:
while (!queue2.isEmpty()) {
    log('Dequeued:', queue2.dequeue());
} // or we can just empty the queue queue2.empty()
/*
Dequeued: 32
Dequeued: 16
Dequeued: 77
*/

log('Final queue2:', queue2.getItems()); //  []
log('Dequeue from empty queue2:', queue2.dequeue()); // Queue is empty. Cannot dequeue an element. & null
// Dequeue from empty queue2: undefined

  //Additional exercises: 
  /* #1 Simulate the behavior of the back and forward buttons in a browser. */

  // Custom document interface to avoid conflicts with built-in Document
interface FileDocument {
    name: string;
    content: string;
}

let documentsQueue: FileDocument[] = [
    { name: 'Tratado de Tantra.txt', content: 'Here comes the content of Tratado de Tantra.' },
    { name: 'Nada Sagrado.doc', content: 'Here comes the content of Nada Sagrado.' },
    { name: 'El Blanco Invisible.pdf', content: 'Here comes the content of El Blanco Invisible.' }
];

function printQueue(arr: FileDocument[]): void {
    if(arr.length === 0) {
        log('There no element to print in the queue!');
        return;
    }
    while (arr.length > 0) {
        const doc = arr.shift();
        if (doc) {
            log('Printing document:', doc.name);
            log('Content:', doc.content);
        }
    }
    log('There no more element to print in the queue!');
}

printQueue(documentsQueue);/* Printing document: Tratado de Tantra.txt 
Content: Here comes the content of Tratado de Tantra. 
Printing document: Nada Sagrado.doc 
Content: Here comes the content of Nada Sagrado. 
Printing document: El Blanco Invisible.pdf 
Content: Here comes the content of El Blanco Invisible. 
There no more element to print in the queue! */

/* To read and print the contents of documents in JavaScript, you would typically need to use a file reading mechanism. However, JavaScript running in a browser environment does not have direct access to the file system for security reasons. Instead, you can simulate reading the contents of the documents by using predefined content or by using the File API if you're working with file inputs. */

// Browser history types
interface BrowserState {
    urlStack: string[];
    currentIndex: number;
}

class BrowserHistory {
    private state: BrowserState = {
        urlStack: [],
        currentIndex: -1
    };

    private back(): void {
        if (this.state.currentIndex > 0) {
            this.state.currentIndex--;
            const previousUrl = this.state.urlStack[this.state.currentIndex];
            log('Location: ', previousUrl);
            // window.location = previousUrl;
        } else {
            log("There are no more pages back..");
        }
    }

    private forward(): void {
        if (this.state.currentIndex < this.state.urlStack.length - 1) {
            this.state.currentIndex++;
            const nextUrl = this.state.urlStack[this.state.currentIndex];
            log('Location: ', nextUrl);
            // window.location = nextUrl;
        } else {
            log("There are no more pages forward.");
        }
    }

    public browseWeb(url: string | null = null): void {
        if (!url) return;

        if (url !== 'back' && url !== 'forward') {
            if (this.state.currentIndex < this.state.urlStack.length - 1) {
                this.state.urlStack = this.state.urlStack.slice(0, this.state.currentIndex + 1);
            }
            this.state.urlStack.push(url);
            this.state.currentIndex++;
            log('Location: ', url);
        } else if (url === 'back') {
            this.back();
        } else if (url === 'forward') {
            this.forward();
        }
    }
}

// DOM manipulation types and interface
interface StyleProperties {
    background?: string;
    'text-align'?: string;
    'font-size'?: string;
    color?: string;
    'line-height'?: string;
}

class DOMManager {
    private body: HTMLBodyElement | null;
    private title: HTMLHeadingElement;

    constructor() {
        this.body = document.querySelector('body');
        this.title = document.createElement('h1');
    }

    private setStyles(element: HTMLElement, styles: StyleProperties): void {
        Object.entries(styles).forEach(([property, value]) => {
            element.style.setProperty(property, value);
        });
    }

    public initializePage(): void {
        if (!this.body) return;

        const bodyStyles: StyleProperties = {
            'background': '#000',
            'text-align': 'center'
        };

        const titleStyles: StyleProperties = {
            'font-size': '3.5vmax',
            'color': '#fff',
            'line-height': '100vh'
        };

        this.setStyles(this.body, bodyStyles);
        this.setStyles(this.title, titleStyles);

        this.title.textContent = 'Retosparaprogramadores #7.';
        this.body.appendChild(this.title);
    }
}


    
    log('Retosparaprogramadores #7'); // Retosparaprogramadores #7

    // Test browser history
    const browser = new BrowserHistory();
    browser.browseWeb('www.lectura_prospectiva.net');
    browser.browseWeb('www.test.web');
    browser.browseWeb('back');
    browser.browseWeb('forward');

    /*  
Location:  www.lectura_prospectiva.net
Location:  www.test.web
Location:  www.lectura_prospectiva.net
Location:  www.test.web
*/
