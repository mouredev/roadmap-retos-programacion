/* #08 CLASES */
//bibliography reference
//Secrets of the JavaScript Ninja (John Resig, Bear Bibeault, Josip Maras) (z-lib.org)
//Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
//JavaScript Notes for Professionals (GoalKicker.com) (Z-Library)
//Python para todos (Raúl Gonzáles Duque)
//GPT

/*                                        **Classes and Objects**

To understand this paradigm, we first need to comprehend what a class is and what an object is. An object is an entity that groups related state and functionality. The state of the object is defined through variables called attributes, while the functionality is modeled through functions known as the object's methods.

An example of an object could be a car, which would have attributes such as the brand, the number of doors, or the type of fuel, and methods such as start and stop. Alternatively, it could be any other combination of attributes and methods relevant to our program.

A class, on the other hand, is nothing more than a generic template from which to instantiate objects; a template that defines what attributes and methods the objects of that class will have. */



//Short for console.log()
let log = console.log.bind(console);

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #8.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #8. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #8'); 
});

/* A class can be composed of the class’s constructor method, instance methods, getters, setters, and
static class methods. None of these are explicitly required; an empty class definition is valid syntax.
By default, everything inside a class definition executes in strict mode. */

/* The fundamental part of most classes is its constructor, which sets up each instance's initial state and handles any
parameters that were passed when calling new. */

/* Similar to the function type, there are two primary ways of defining a class: class declarations and
class expressions. Both use the class keyword and curly braces:
// class declaration
class Person {}
// class expression
const Animal = class {}; */

/* Note: even though ES6 has introduced the class keyword, under the
hood we’re still dealing with good old prototypes; classes are syntactic sugar designed
to make our lives a bit easier when mimicking classes in JavaScript.  */


class User {
    constructor(name, nickname, email) {
        this.name = name;
        this.nickname = nickname;
        this.email = email;
    }

    greeting() {
        log(`Hi ${this.nickname}. Welcome to this Roadmap for Developers!`)
    }

    getEmail() {
       if(this.email != undefined) {
            return this.email;
       } else {
            log('no email set yet!');
            return null;
       } 
    }

    getName() {
        if(this.name != undefined) {
            return this.name;
       } else {
            log('no name set yet!');
            return null;
       } 
    }

    getNickname() {
        if(this.nickname != undefined) {
            return this.nickname;
       } else {
            log('no nickname set yet!')
            return null;
       } 
    }

    setName(name) {
       if(name) this.name = name;
    }

    setEmail(email) {
       if(email) this.email = email;
    }

    setNickname(nickname) {
       if(nickname) this.nickname = nickname;
    }
    
    userInfo() {
        log(`User name: ${this.name || 'not set'}, User nickname: ${this.nickname || 'not set'}, User email: ${this.email || 'not set'}`);
    }
}

let user1 = new User('Niko Zen', 'duendeintemporal', 'duendeintemporal@hotmail.com');
user1.greeting(); // Hi duendeintemporal. Wellcome to this Roadmap for Developers!

user1.userInfo(); // user name: Niko Zen, user nickname: duendeintemporal, user email: duendeintemporal@hotmail.com 

user1.setNickname('psicotrogato');

log(user1.getNickname()); // psicotrogato

/* There is no formal class type in the ECMAScript specification, and in many ways ECMAScript classes
behave like special functions. Once declared, the class identifier identifies as a function when checked with the typeof operator: */

log(typeof User); // function

/* As with function constructors, you can use the instanceof operator to test if the constructor prototype appears in the prototype chain of an instance: */

log(user1 instanceof User); // true

/*  Class Inheritance
Inheritance works just like it does in other object-oriented languages: methods defined on the superclass are accessible in the extending subclass. */

class Log {
    constructor() {
        this.logger = console.log;
        this.errorLog = console.error;
    }

    log(msj) {
       (msj)? this.logger(msj) : this.errorLog('you should provide a msj');
    }
}
// When you extend a class in JavaScript, you must call super() in the constructor of the subclass before you can use this.

class Greeting extends Log {
    constructor(msj) {
        super();
        this.msj = msj;
    }
}

let sayHiPeople = new Greeting('Hi everybody. Welcome to the most wierd and lonly place in the cyberspace...');

sayHiPeople.log(); // Hi everybody. Welcome to the most wierd and lonly place in the cyberspace...

/*  Static Methods
Static methods and properties are defined on the class/constructor itself, not on instance objects. These are specified in a class definition by using the static keyword   */

class ElectroCat {
    static catSay() {
        return 'Miauu';
    }
    
    static get catThink() {
        return "Let's see if there's some lovely gircat over there";
    } 
}

log(ElectroCat.catSay()); // Miauu
log(ElectroCat.catThink); // Let's see if there's some lovely gircat over there

// We can see that static properties are not defined on object instances:

const mishu = new ElectroCat();
//log(mishu.catSay()); // undefined OR throw an error
//log(mishu.catThink); // undefined or throw an error

// However, they are defined on subclasses:

class PoetCat extends ElectroCat {}
log(PoetCat.catSay()); // Miauu
log(PoetCat.catThink); // Let's see if there's some lovely gircat over there

/* Getters and setters allow you to define custom behaviour for reading and writing a given property on your class. To the user, they appear the same as any typical property. However, internally a custom function you provide is used to determine the value when the property is accessed (the getter), and to perform any necessary changes when the property is assigned (the setter).
In a class definition, a getter is written like a no-argument method prefixed by the get keyword. A setter is similar, except that it accepts one argument (the new value being assigned) and the set keyword is used instead. */

const h_method = Symbol('Hidden method');

//We use private properties in JavaScript classes to avoid infinite recursion in getters and setters by referencing the private property instead of the public property.
class GopiElectronica {
    constructor(name) {
        this._name = name; 
    }

    set name(name) {
        this._name = name; 
    }

    get name() {
        return this._name; 
    }

    // You can also create dynamic methods or use symbols or JavaScript expressions as keys 
    [h_method]() {
        return 'I will hack you boy';
    }
}

const Nicky = new GopiElectronica('Nicky');
log(Nicky.name); // Nicky
Nicky.name = 'Samantha';
log(Nicky.name); // Samantha
log(Nicky[h_method]()); // I will hack you boy
log(Object.keys(Nicky)); // [] - will not show the symbol method
log(Reflect.ownKeys(Nicky)); // Shows all keys including symbol keys





/* Tips: (relevant info) 
Classes are first-class citizens in JavaScript, meaning they can be passed around as you would any
other object or function reference:
// Classes may be defined anywhere a function would, such as inside an array:
let classList = [
    class {
        constructor(id) {
             this.id_ = id;
             console.log('instance ${this.id_}');
        }
    }
];

function createInstance(classDefinition, id) {
    return new classDefinition(id);
}

let foo = createInstance(classList[0], 3141); // instance 3141 */


/* Similar to an immediately invoked function expression, a class can also be immediately instantiated:
// Because it is a class expression, the class name is optional
let p = new class Foo {
    constructor(x) {
        console.log(x);
    }
}('bar'); // bar

console.log(p); // Foo {} */


//Aditional Exercises

//QUEUE

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
log('Dequeue from empty queue2:', queue2.dequeue()); //Logs error: Queue is empty. Cannot dequeue an element. & Dequeue from empty queue2: null

//STACK

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
log('Pop from empty stack2:', stack2.pop()); // Logs error: Stack is empty. Cannot pop an element. & Pop from empty stack2: null
