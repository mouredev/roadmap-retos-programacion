/* #07 Pilas y Colas  */
//I use GPT to generate accurate comments and also as a reference.

  //shorthand for console.log()
  let log = console.log.bind(console);

//The array structure can be useful in JavaScript to simulate stacks and queues.

/* A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. You can think of it like a stack of plates: you add plates to the top and also remove them from the top.
Key Operations:

    Push: Add an element to the top of the stack.
    Pop: Remove the element from the top of the stack.
    Peek/Top: Retrieve the top element without removing it.
    IsEmpty: Check if the stack is empty.
 */

  //Pila(Stack)
  let stack = [1,2,3,4];
  
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

 class Stack {
    constructor(initialItems = []) {
            this.items = Array.isArray(initialItems) ? initialItems : [];
    }

    push(element) {
        this.items.push(element);
    }

    pop() {
        if (this.isEmpty()) {
            console.error("Stack is empty. Cannot pop an element.");
            return null; 
        }
        return this.items.pop();
    }

    peek() {
        if (this.isEmpty()) {
            console.error("Stack is empty. Cannot peek.");
            return null; 
        }
        return this.items[this.items.length - 1];
    }

    empty() {
        return this.items = [];
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length;
    }
}

const stack2 = new Stack([55, 76, 98, 100]); 
log('Initial stack2:', stack2.items); // [55, 76, 98, 100]

stack2.push(32);
log('After pushing 32:', stack2.items); // [55, 76, 98, 100, 32]

log('Peek:', stack2.peek()); // 32

log('Pop:', stack2.pop()); // 32
log('After popping:', stack2.items); // [55, 76, 98, 100]

log('Pop all elements:');
while (!stack2.isEmpty()) {
    log('Popped:', stack2.pop());
} // or we can just empty the stack stack2.empty() 

log('Final stack2:', stack2.items); // []
log('Pop from empty stack2:', stack2.pop()); // Stack is empty. Cannot pop an element. & null


 //Cola(Queue)

 /* A queue is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed. You can think of it like a line of people waiting for service: the first person in line is the first to be served.
Key Operations:

    Enqueue: Add an element to the end of the queue.
    Dequeue: Remove the element from the front of the queue.
    Front/Peek: Retrieve the front element without removing it.
    IsEmpty: Check if the queue is empty.
 */

  let queue = [8,5,4,2,1];

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

 class Queue {
    constructor(initialItems = []) {
         this.items = Array.isArray(initialItems) ? initialItems : [];
    }

    enqueue(element) {
        this.items.push(element); 
    }

    dequeue() {
        if (this.isEmpty()) {
            console.error("Queue is empty. Cannot dequeue an element.");
            return null;
        }
        return this.items.shift();
    }

    peek() {
        if (this.isEmpty()) {
            console.error("Queue is empty. Cannot peek.");
            return null;
        }
        return this.items[0];
    }
    empty() {
        return this.items = [];
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length; 
    }
}

const queue2 = new Queue([45, 32, 16]); 
log('Initial queue2:', queue2.items); //  [45, 32, 16]

queue2.enqueue(77);
log('After enqueueing 4:', queue2.items); //  [45, 32, 16, 77]

log('Peek:', queue2.peek()); //  45

log('Dequeue:', queue2.dequeue()); //  45
log('After dequeueing:', queue2.items); //  [32, 16, 77]

log('Dequeue all elements:');
while (!queue2.isEmpty()) {
    log('Dequeued:', queue2.dequeue());
} // or we can just empty the queue queue2.empty()

log('Final queue2:', queue2.items); //  []
log('Dequeue from empty queue2:', queue2.dequeue()); // Queue is empty. Cannot dequeue an element. & null


  //Additional exercises: 
  /* #1 Simulate the behavior of the back and forward buttons in a browser. */

  let documentsQueue = [
    { name: 'Tratado de Tantra.txt', content: 'Here comes the content of Tratado de Tantra.' },
    { name: 'Nada Sagrado.doc', content: 'Here comes the content of Nada Sagrado.' },
    { name: 'El Blanco Invisible.pdf', content: 'Here comes the content of El Blanco Invisible.' }
];

function printQueue(arr){
    if(arr.length == 0){
        log('There no element to print in the queue!')
        return;
    }
        while (arr.length > 0) {
            const document = arr.shift(); // Get the first document
            log('Printing document:', document.name);
            log('Content:', document.content);
       }
    log('There no more element to print in the queue!')
}

printQueue(documentsQueue);/* Printing document: Tratado de Tantra.txt 
Content: Here comes the content of Tratado de Tantra. 
Printing document: Nada Sagrado.doc 
Content: Here comes the content of Nada Sagrado. 
Printing document: El Blanco Invisible.pdf 
Content: Here comes the content of El Blanco Invisible. 
There no more element to print in the queue! */

/* To read and print the contents of documents in JavaScript, you would typically need to use a file reading mechanism. However, JavaScript running in a browser environment does not have direct access to the file system for security reasons. Instead, you can simulate reading the contents of the documents by using predefined content or by using the File API if you're working with file inputs. */

let urlStack = [];
let currentIndex = -1; // To keep track of the current position.

function browseWeb(str = prompt('Enter a URL or the word "forward" or "back" to navigate in the browsing history.')) {
    const back = () => {
        if (currentIndex > 0) {
            currentIndex--;
            const previousUrl = urlStack[currentIndex];
            log('Location: ', previousUrl);
            // window.location = previousUrl; // Navigate to the previous URL.
        } else {
            log("There are no more pages back..");
        }
    };

    const forward = () => {
        if (currentIndex < urlStack.length - 1) {
            currentIndex++;
            const nextUrl = urlStack[currentIndex];
            log('Location: ', nextUrl);
            // window.location = nextUrl; // Navigate to the next URL.
        } else {
            log("There are no more pages forward.");
        }
    };

    if (str !== 'back' && str !== 'forward') {
        if (currentIndex < urlStack.length - 1) {
            urlStack = urlStack.slice(0, currentIndex + 1); // Clear forward if navigation has occurred.
        } // the standard behavior of a web browser's navigation history,
        urlStack.push(str);
        currentIndex++;
        // window.location = str; // Navigate to the new URL.
        log('Location: ', str);
    } else if (str === 'back') {
        back();
    } else if (str === 'forward') {
        forward();
    }
}


browseWeb('www.lectura_prospectiva.net'); // Location:  www.lectura_prospectiva.net
browseWeb('www.test.web'); // Location:  www.test.web
browseWeb('back'); // www.lectura_prospectiva.net           
browseWeb('forward'); // www.test.web


window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #7.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #7. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #7'); 
});