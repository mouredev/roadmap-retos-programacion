/* { retosparaprogramadores }  #2 FUNCIONES Y ALCANCE */
// I use the book "Eloquent JavaScript: A Modern Introduction to Programming" by Marijn Haverbeke for concept reference.
// I also use the book "Secrets of the JavaScript Ninja" by John Resig, Bear Bibeault, and Josip Maras.
// I refer to "JavaScript Notes for Professionals" from the people of Stack Overflow. https://goalkicker.com/JavaScriptBook
// Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.
//https://www.typescriptlang.org/docs/

// Short for log
const log = console.log;


/* FUNCTIONS */
/* Functions are fundamental in TypeScript and JavaScript programming. They allow us to structure larger programs, reduce repetition, 
   associate names with subprograms, and isolate these subprograms from each other. 
   Functions can be used to calculate values, perform side effects, achieve code reuse, and enhance code readability. */

// Functions as first-class objects
/* Functions in TypeScript are treated as first-class objects, meaning they can be assigned to variables, 
   passed as arguments, and returned from other functions. */

// Created via literals.
function addPad(number: number, width: number, pad: number | string = 0): string {
    let result = String(number);
    while (result.length < width) {
        result = `${pad}` + result;
    }
    return result;
}

log(addPad(4, 3, '#')); // ##4
log(addPad(56, 3, '$')); // $56
log(addPad(7, 3)); // 007

// Note: Default arguments can be passed as shown in the last example.

// Assigned to variables, array entries, and properties of other objects
const square = (n: number): number => n * n;

const funcArray: number[] = [];
funcArray.push(square(8)); // Adds a new function to an array
log(funcArray); // [64]

const data: { book_name: string; some_method?: () => void } = { book_name: 'Hackbook' };
data.some_method = function () {
    console.log(`${data.book_name} is now available in z-lib.org, so hack the world.`);
}; // Assigns a new function as a property of another object
data.some_method(); // Hackbook is now available in z-lib.org, so hack the world.

// A newly created object passed as an argument to a function

// Passed as arguments to other functions (callbacks)
function call(doSomething: () => void): void {
    doSomething();
}

call(() => log('Hi roadmap coders!')); // Hi roadmap coders!

// Returned as values from functions
function returnFunc(): (str: string) => void {
    return function (str: string) { console.log(str); };
}

const greeting = returnFunc();
greeting('Hi there!'); // Hi there!

// Functions can possess properties that can be dynamically created and assigned like objects:
const callMom = function () { log('Mommmmm!'); };

callMom(); // Mommmmm!
callMom.name = "Mom";
log(callMom.name); // Logs: callMom because "name" is an inherited property of the function constructor and is not writable

callMom.something = 'something';
log(callMom.something); // something

log(callMom); /* Logs: 
[Function: callMom] { something: 'something' } */

/* Functions are objects with the special capability of being invokable. */

// Constructor functions are functions designed to construct a new object.
function Cat(this: any, name: string, color: string, sound: string) {
    this.name = name;
    this.color = color;
    this.sound = sound;
}

// Constructor functions are invoked using the new keyword:
const psicoCat = new Cat("Psicotrogato", "Black & White", "Meaw");
log(psicoCat.color); // Black & White
psicoCat.sound = "Hey girl what's your name, what's your name?... I forgot";

// Constructor functions also have a prototype property which points to an object whose properties are automatically inherited by all objects created with that constructor:
Cat.prototype.speak = function () {
    log(this.sound);
};

psicoCat.speak(); // "Hey girl what's your name, what's your name?.. I forgot"

// Closure
/* The ability to treat functions as values, combined with the fact that local bindings are recreated every time a function is called, 
   leads to interesting possibilities. */

const incrementer = (function (n: number) {
    let local = n;
    return () => local++;
})(0); // Immediately invoked with an initial value of 0

console.log('incrementer value is:', incrementer()); // incrementer value is: 0
console.log('incrementer value is:', incrementer()); // incrementer value is: 1
console.log('incrementer value is:', incrementer()); // incrementer value is: 2

// In the previous example, we used an IIFE (Immediately Invoked Function Expression) to create a closure, 
// but we can achieve the same with regular functions.
function square_v2(n: number): () => number {
    return () => n * n;
}

const pow64 = square_v2(64);
const pow78 = square_v2(78);

log(pow64()); // 4096
log(pow78()); // 6084

// Arrow Functions
const factor = (n: number): number => {
    if (n === 1) return 1;
    return n * factor(n - 1);
};

log(factor(8)); // 40320

// Note: The factor function is recursive, meaning it calls itself.

// Arrow functions allow us to abbreviate expressions when they have only one parameter or a single expression.
const square_v3 = (n: number): number => n * n;
log(square_v3(4)); // 16
// Note: We omit the curly braces, the return statement, and also the parentheses.

// Note 2: It's important to remember that arrow functions do not have their 
// The following code is commented to avoid conflicts in Node.js environments. 
// If you transpile it to JavaScript, it will run fine in a browser.
//own 'this' context.
// const obj = {
//     value: 'Rutadeprogramacion Exercice #2.',
//     advertisement: function () {
//         log(this.value); // Rutadeprogramacion Exercice #2
//         setTimeout(() => {
//             alert(`${this.value} Please open the Browser Developer Tools.`);
//         }, 1000);
//     }
// };

//obj.advertisement(); // Alert: Rutadeprogramacion Exercice #2. Please open the Browser Developer Tools. and Logs in console: Rutadeprogramacion Exercice #2.

/* Note: Because arrow functions don't have `this`, the 'this' points to obj. 
   If we had used a regular function instead of the arrow function inside the setTimeout, 
   it would have alerted undefined or thrown a reference error. */

// Function Declarations: A function declaration defines a named function. It is hoisted, meaning it can be called before it is defined in the code.
function subtract(n: number, m: number): number {
    return n - m;
}

log(subtract(8, 4)); // 4

// Function Expressions: A function expression defines a function as part of a larger expression. 
// It can be anonymous or named and is not hoisted.
const multiply = function (n: number, m: number): number {
    return n * m;
};

log(multiply(8, 9)); // 72

const add = function add(a: number, b: number): number {
    return a + b;
}; // Can share the name for the binding word & the named function

log(add(3, 3)); // 6

// Arrow Functions: Introduced in ES6, arrow functions provide a more concise syntax for writing functions. 
const divide = (n: number, m: number): number => n / m;

log(divide(543, 56)); // 9.696428571428571

// Anonymous Functions: These are functions that do not have a name. 
// They are often used in callbacks or as arguments to other functions.
// The following code is commented to avoid conflicts in Node.js environments. 
// If you transpile it to JavaScript, it will run fine in a browser.
// window.addEventListener('load', function () {
//     const body = document.querySelector('body') as HTMLBodyElement;
//     const title = document.createElement('h1');

//     body.style.setProperty('background', '#000');
//     body.style.setProperty('text-align', 'center');

//     title.textContent = 'Retosparaprogramadores #2.';
//     title.style.setProperty('font-size', '3.5vmax');
//     title.style.setProperty('color', '#fff');
//     title.style.setProperty('line-height', '100vh');

//     body.appendChild(title);

//     log('This is an anonymous function'); // This will be logged at the end due to the nature of the window event
// });

let sayHi = function () {
    console.log('Hi');
};

sayHi(); // Hi

/* Named functions differ from anonymous functions in multiple scenarios:
   - When debugging, the name of the function will appear in the error/stack trace.
   - Named functions are hoisted while anonymous functions are not.
   - Named functions and anonymous functions behave differently when handling recursion.
   - Depending on the ECMAScript version, named and anonymous functions may treat the function name property differently. */

// Immediately Invoked Function Expressions (IIFE): An IIFE is a function that is executed immediately after it is defined. 
// It is often used to create a new scope and avoid scope pollution.
let iife = (function () {
    console.log("This is another example of IIFE functions"); // This will be logged
})();

/* Higher-Order Functions: These are functions that take other functions as arguments or return functions as their result. 
   They are commonly used in functional programming. */

// Example of a sum function
function sum(numbers: number[]): number {
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total;
}

// Example of a range function
function range(n: number, m: number): number[] {
    let result: number[] = [];
    for (let i = n; i <= m; i++) {
        result.push(i);
    }
    return result;
}

// Using the sum and range functions together
log(sum(range(1, 100))); // 5050

/* Generator Functions: Introduced in ES6, generator functions can pause and resume execution. 
   They are defined using the function * syntax and use the yield keyword. */
function* IdGenerator() {
    let id = 0;
    while (true) {
        yield addPad(++id, 5);
    }
}

const idIterator = IdGenerator();

log(idIterator.next().value); // 00001
log(idIterator.next().value); // 00002

/* Async Functions: Async functions are a way to work with asynchronous code. 
   They return a promise and can use the await keyword to pause execution until a promise is resolved. */

// Note: You may need an extension to allow CORS (Cross-Origin Resource Sharing) to avoid console warnings.
const getLoremIpsum = (numberOfParagraphs: number): Promise<string[]> => {
    return fetch(`https://baconipsum.com/api/?type=meat-and-filler&paras=${numberOfParagraphs}`)
        .then(response => response.json())
        .then(loremIpsumTextArray => {
            return loremIpsumTextArray;
        })
        .catch(error => {
            showError(error);
        });
};

const showError = (error: any): void => console.log(error);

async function logParagraphs(): Promise<void> {
    const result = await getLoremIpsum(2);
    console.log(result);
}

logParagraphs(); // Logs: Array of paragraphs or similar content

// Functions that take multiple arguments / the Rest parameter ...
// Sometimes we don't know how many arguments we will receive, we can use the rest parameter in those cases.
const total = (...numbers: number[]): number => {
    return numbers.reduce((total, num) => total + num, 0);
};

log('Total: ', total(10, 256, 345, 465, 87, 432)); // Total: 1595

/* CLOSURES AND SCOPES */

// Scope: A scope refers to the visibility of identifiers in certain parts of a program. 
/* Closure: A closure allows a function to access and manipulate variables that are external to that function. 
   Closures allow a function to access all the variables, as well as other functions, that are in scope when the function itself is defined. 
   Hoisting is a mechanism that moves all variable and function declarations to the top of their scope. 
   However, variable assignments still happen where they originally were. */

// This will work because doSomething is a Named Function and JavaScript hoists function declarations to the top of their containing scope.
log(doSomething()); // I'm here coding, and I'm amazed at all we can learn by following this roadmap.

function doSomething(): void {
    console.log("I'm here coding, and I'm amazed at all we can learn by following this roadmap.");
}

// This will throw an error because an anonymous function cannot be called before its declaration.
// log(doAnotherthing());

let anotherthing = function () {
    console.log('never log this...');
};

let friend = 'Asterix';

function showClosure(): void {
    log(friend); // Asterix in scope
    let anotherFriend = 'Obelix';
    function innerClosure(): void {
        let anotherOne = 'Idefix';
        log(anotherFriend); // Obelix in scope
        log(friend); // Asterix in scope
        log(anotherOne); // Idefix in scope
    }
    // log(anotherOne); // Throws an Error: anotherOne is not defined, is not in scope
    innerClosure();
}

showClosure();
// log(anotherFriend); // Throws an Error: anotherFriend is not defined, is not in scope

/* Closures let us do some interesting things, such as defining "private" variables that are visible only to a specific function or set of functions. 
   A contrived (but popular) example: */
const makeCounter = () => {
    let counter = 0;
    return {
        value: () => counter,
        increment: () => {
            counter++;
        },
        restart: () => {
            counter = 0;
        }
    };
};

let counter1 = makeCounter();
let counter2 = makeCounter();
counter2.increment();
counter2.increment();
log(counter1.value()); // 0
log(counter2.value()); // 2
counter2.restart();
log(counter2.value()); // 0

// Note: When makeCounter() is called, a snapshot of the context of that function is saved.
// Note 2: Closures are also used to prevent global namespace pollution, often through the use of immediately-invoked function expressions.
// Apply and Call
function speak(this: { name: string }, ...sentences: string[]): void {
    let tell = '';
    sentences.forEach(word => tell += word + ' ');
    console.log(this.name + ": " + tell);
}

let person = { name: "Niko" };
speak.apply(person, ["I", "will", "go", "through", "this", "roadmap", "until", "the", "end"]); // Niko: I will go through this roadmap until the end
speak.call(person, "But", "first", "I", "need", "some", "exercise"); // Niko:  But first I need some exercise

/* Notice that apply allows you to pass an Array or the arguments object (array-like) as the list of arguments, 
   whereas call requires you to pass each argument separately. */

/* As we see in the previous obj.advertisement() example: 
   When using arrow functions, 'this' takes the value from the enclosing execution context's 'this' (that is, 
   'this' in arrow functions has lexical scope rather than the usual dynamic scope). 
   In global code (code that doesn't belong to any function), it would be the global object. 
   And it keeps that way, even if you invoke the function declared with the arrow notation from any of the other methods here described. */

/* The bind method of every function allows you to create a new version of that function with the context strictly bound to a specific object. 
   It is especially useful to force a function to be called as a method of an object. */

let person2 = { name: 'Anna' };

function sayHiLady(this: { name: string }): void {
    log(`Hi ${this.name}`);
}

const hiAnna = sayHiLady.bind(person2);
hiAnna(); // Hi Anna

/*  This a possible output example for the previus  logParagraphs() async function:
[
  'Shank aliquip fugiat, cupim irure pig capicola kielbasa in mollit bresaola venison bacon aliqua.  Alcatra aliqua jowl fatback pork chop in exercitation corned beef leberkas aliquip qui chicken consequat laboris.  Swine shank porchetta tail quis in.  Chuck dolore venison, picanha id swine cupim strip steak porchetta magna ball tip excepteur hamburger mollit ex.  Picanha chislic irure strip steak sausage, in kevin ullamco.  Magna pork belly tongue meatloaf elit tempor.  Veniam meatball corned beef pork chop in.',
  'Sint ut deserunt pork loin enim doner sunt chuck qui occaecat aliqua meatloaf spare ribs exercitation.  Shank esse cupidatat, boudin cupim eiusmod tenderloin occaecat do drumstick cow ut meatball.  Aute non pig esse ea capicola landjaeger beef ad qui minim in boudin.  Shank non dolore adipisicing.  Ham hock drumstick sint landjaeger minim.  Dolor in nisi chicken sunt.'    
]  */