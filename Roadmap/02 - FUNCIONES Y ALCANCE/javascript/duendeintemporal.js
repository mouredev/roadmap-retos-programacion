/* { RETOS DE PROGRAMACIÓN }  #2 FUNCIONES Y ALCANCE */
// I use the book "Eloquent JavaScript: A Modern Introduction to Programming" by Marijn Haverbeke for concept reference.
// I also use the book "Secrets of the JavaScript Ninja" by John Resig, Bear Bibeault, and Josip Maras.
// I refer to "JavaScript Notes for Professionals" from the people of Stack Overflow. https://goalkicker.com/JavaScriptBook
// Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.


//short for console.log
let log = console.log.bind(console);

/* FUNCTIONS */
/* Functions are the bread and butter of JavaScript programming. The concept of wrapping a piece of program in a value has many uses. It gives us a way to structure larger programs, to reduce repetition, to associate names with subprograms, and to isolate these subprograms from each other. 

In JavaScript, the fundamental unit of execution is a function. We use them all the
time, to calculate something, to perform side effects such as changing the UI, to
achieve code reuse, or to make our code easier to understand. 
*/


//Functions as first-class objects
/*Functions in JavaScript possess all the capabilities of objects and are thus treated like any other object in the language. We say that functions are first-class objects, which can also be */

// Created via literals.  
function  addPad(number, width, pad = 0){
   let result = String(number); 
   while (result.length < width) {
        result = `${pad}` + result;
   }
    return result;
}


log(addPad(4, 3, '#'))// ##4
log(addPad(56, 3, '$'))// $56
log(addPad(7, 3))// 007

//note: See that we can pass default arguments as in the last example

// Assigned to variables, array entries, and properties of other objects
let square = function(n){
    return n * n;
};

let funcArray = [];
funcArray.push(square(8));// Adds a new function to an array
log(funcArray)//  [ 64 ]

let data ={ book_name:'Hackbook', }
data.some_method = function(){ console.log(`${data.book_name} is now avaible in z-lib.org, so hack the world.`) };// Assigns a new function as a property of another object
data.some_method()// Hackbook is now avaible in z-lib.org, so hack the world.


//A newly created object passed as an argument to a function

//Passed as arguments to other functions (callbacks)
function call(doSomething){
    doSomething();
}

call(()=> log('Hi roadmap coders!'))// Hi roadmap coders!

//Returned as values from functions
function returnFunc(){
    return function(str){ console.log(str) }
}

const greeting = returnFunc();
greeting('Hi there!')// Hi there!



//They can possess properties that can be dynamically created and assigned as in objects:

let callMom = function(){ log('Mommmmm!') };

callMom()// Mommmmm!
callMom.name = "Mom";
log(callMom.name)// Logs: callMom cause "name" is a inherit property of the function constructor, and is not writeble

callMom.something = 'something';
log(callMom.something)// something

log(callMom)/* Logs: 
function callMom()
    ​arguments: null
    caller: null
    length: 0
    name: "callMom"
    prototype: Object { … }
    something: "something"
    <prototype>: function () */


/* Whatever we can do with objects, we can do with functions as well. Functions are objects, just with an additional, special capability of being invokable: Functions can be called or invoked in order to perform an action. */

/*Constructor functions are functions designed to construct a new object. Within a constructor function, the keyword this refers to a newly created object which values can be assigned to. Constructor functions "return" his new object automatically. */

function Cat(name, color, sound){
    this.name = name;
    this.color = color;
    this.sound = sound;
}

//Constructor functions are invoked using the new keyword:
let psicoCat = new Cat("Psicotrogato", "Black & White", "Meaw");
log(psicoCat.color)// Black & White
psicoCat.sound = "Hey girl what's your name, what's your name?... I forgot";

/*Constructor functions also have a prototype property which points to an object whose properties are automatically inherited by all objects created with that constructor: */

Cat.prototype.speak = function(){
    log(this.sound);
}

psicoCat.speak(); // "Hey girl what's your name, what's your name?.. I forgot"


//Closure
/* The ability to treat functions as values, combined with the fact that local bindings are re-created every time a function is called, brings up  interesting possibilities */ 

const incrementer = (function(n){
    let local = n;
    return () => local++;
})(0); // Immediately invoked with an initial value of 0

console.log('incrementer value is:', incrementer()); // incrementer value is:  0
console.log('incrementer value is:', incrementer()); // incrementer value is:  1
console.log('incrementer value is:', incrementer()); // incrementer value is:  2

//in the previus example we use an IIFE(Inmediatly Invoked Function Expression) to create a clousure, but we can achive the same with regular functions

 function square_v2(n){
    return ()=> n * n;
}

const pow64 = square_v2(64);
const pow78 = square_v2(78);

log(pow64())// 4096
log(pow78())// 6084


// Arrow Functions ()=>{ }
const factor = (n)=>{
    if(n == 1) return 1;
    return n * factor(n - 1);
}

log(factor(8))// 40320

//Note: here factor is a recursive function too. It means that it's a function that calls it self.

//Arrow function allow us to abreviate the expresion when they have only one parameter or a single expression

const square_v3 = n => n * n;
log(square_v3(4))// 16
//note we omit the curly braces, the return and also the parentesis


//Note 2: is important to have in mind that arrows function doesn't have their own 'this' context

const obj = {
    value: 'Rutadeprogramacion Exercice #2.',

    advertisement: function(){
        log(this.value); // Rutadeprogramacion Exercice #2
        setTimeout(() => {
            alert(`${this.value} Please open the Browser Developer Tools.`);
        }, 1000);
    }
};

obj.advertisement()// Alert: Rutadeprogramacion Exercice #2. Please open the Browser Developer Tools. and Logs in console: Rutadeprogramacion Exercice #2.

/* Note: Because arrows function doesn't have `this`, the 'this' points to obj. If we had used a regular function instead of the arrow function inside the setTimeout, it would have alert undefined or throw a reference error. */ 

//So we have
/* Function Declarations: A function declaration defines a named function. It is hoisted, meaning it can be called before it is defined in the code. */

function substract(n, m){
    return n - m;
}

log(substract(8, 4))// 4

/* Function Expressions: A function expression defines a function as part of a larger expression. It can be anonymous or named and is not hoisted. */

const multiply = function(n, m){
    return n * m;
};

log(multiply(8, 9))// 72

const add = function add(a, b){
    return a + b;
}// can share the name for the bindding word & the named function

log(add(3, 3))// 6

/* Arrow Functions:  Introduced in ES6, arrow functions provide a more concise syntax for writing functions. They do not have their own this, which makes them useful in certain contexts. */


const divide = (n, m) =>  n / m ;

log(divide(543, 56))// 9.696428571428571

/* Anonymous Functions: These are functions that do not have a name. They are often used in callbacks or as arguments to other functions. */

window.addEventListener('load', function(){
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #2.';
    title.style.setProperty('font-size', '3.5vmax')
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    log( 'This is an anonymous function')// this will be logged at the end cause the nature of window event
});

let sayHi = function(){
    console.log('Hi');
}

sayHi()// Hi

/* Named functions differ from the anonymous functions in multiple scenarios:
When you are debugging, the name of the function will appear in the error/stack trace
Named functions are hoisted while anonymous functions are not
Named functions and anonymous functions behave differently when handling recursion
Depending on ECMAScript version, named and anonymous functions may treat the function name property
differently */

/* Immediately Invoked Function Expressions (IIFE): An IIFE is a function that is executed immediately after it is defined. It is often used to create a new scope and avoid scope pollution. */

let iife = (function(){
    console.log("This another example of IIFE functions");//this will be logged
})();


/* Higher-Order Functions: These are functions that take other functions as arguments or return functions as their result. They are commonly used in functional programming. */

//in example if we have sum
function sum(numbers){
    let total = 0;
    for(let i = 0; i < numbers.length; i++ ){
        total += numbers[i];
    }
    return total;
}

//and range 
function range(n, m){
    let result = [];
    for(let i = n; i <= m; i++){
        result.push(i);
    }
    return result;
}

//them we can just
log(sum(range(1, 100)))// 5050

/* Generator Functions: Introduced in ES6, generator functions can pause and resume execution. They are defined using the function * syntax and use the yield keyword. */

function *IdGenerator() {
    let id = 0;
    while(true){
        yield addPad(++id, 5) ;
    }
}

const idIterator = IdGenerator();

log(idIterator.next().value)// 00001
log(idIterator.next().value)// 00002


/* Async Functions: Async functions are a way to work with asynchronous code. They return a promise and can use the await keyword to pause execution until a promise is resolved. */

//Note: you will need a extention to allow CORS(Cross Origin Resource Sharing) to avoid the console warning

const getLoremIpsum = numberOfParagraphs => {
    return fetch(`https://baconipsum.com/api/?type=meat-and-filler&paras=${numberOfParagraphs}`)
        .then(response => response.json())
        .then(loremIpsumTextArray => {
           return loremIpsumTextArray;
        })
        .catch(error => {
            showError(error);
        });
};

const showError = error => console.log(error);



    async function logParagraphs() {
        const result = await getLoremIpsum(2);
        console.log(result);
    }

logParagraphs();  // Logs: Array [ "T-bone ham hock enim, ipsum frankfurter tri-tip consequat.  Reprehenderit ut occaecat elit in, qui ea flank chuck porchetta chicken bacon ham hock kielbasa hamburger.  Pork chop commodo strip steak mollit filet mignon andouille velit tempor fatback ea.  Capicola laboris beef ribs in chuck, et jerky swine exercitation ribeye ullamco in turkey.  Turkey dolor ball tip proident pariatur corned beef, chislic jerky leberkas fugiat doner.  Chuck laboris pork do, ut esse sed in drumstick deserunt ribeye voluptate tail reprehenderit.  Beef aliquip sint fugiat pork belly pig reprehenderit nisi corned beef chicken dolore ad proident non.", "Spare ribs officia irure, est brisket ham prosciutto.  Do proident consectetur, capicola ad bacon non pancetta magna aute.  Pork loin ribeye chuck doner, duis beef ribs ut ham hock adipisicing sed turkey boudin buffalo rump pancetta.  Deserunt ham pork chop short loin tail." ] or something similar

// Functions that takes multiple arguments / the Rest parameter ...
// Some times we don't know how many arguments we will recive, we can use the rest parameter in those cases

const total = (...numbers)=> {
    return numbers.reduce((total, num) => total + num, 0);
}

log('Total: ',total(10, 256, 345, 465, 87, 432))// Total: 1595

/* CLOUSURES AND SCOPES */

// Scope:  A scope refers to the visibility of identifiers in certain parts of a program. 
/* Closure: A closure allows a function to access and manipulate variables that are external to that
function. Closures allow a function to access all the variables, as well as other functions, that are in scope when the function itself is defined. */
/* Hoisting is a mechanism which moves all variable and function declarations to the top of their scope. However, variable assignments still happen where they originally were. */

/* When using an anonymous function, the function can only be called after the line of declaration, whereas a named function can be called before declaration. Consider */

// This will works cause doSoemthing is a Named Function and JavaScript hoists function declarations to the top of their containing scope.
log(doSomething());

function doSomething(){
    console.log("I'm here coding, and I'm amazed at all we can learn by following this roadmap.")
}

// This will throw an error because an anonymous function cannot be called before its declaration.
// log(doAnotherthing())

let anotherthing = function(){
    console.log('never log this...')
}

let friend = 'Asterix';

function showClosure(){
    log(friend)// Asterix in scope
    let anotherFriend = 'Obelix';
    function innerClosure(){
        let anotherOne = 'Idefix'
        log(anotherFriend)// Obelix in scope
        log(friend)// Asterix in scope
        log(anotherOne)// Idefix in scope
     }
     //log(anotherOne)// throw an Error: anotherOne is not defined, is not in scope
  innerClosure();
}

showClosure();
//log(anotherFriend)// Throw an Error: anotherFriend is not defined, is not in scope


/* Closures lets us do some interesting things, such as defining "private" variables that are visible only to a specific function or set of functions. A contrived (but popular) example: */


const  makeCounter = ()=> {
    var counter = 0;
    return {
              value: function() {
                        return counter;
              },
              increment: function() {
                           counter++;
              },
              restart: function() {
                          counter = 0;
              }
           };
}

let counter1 = makeCounter();
let counter2 = makeCounter();
counter2.increment();
counter2.increment();
log(counter1.value())// 0
log(counter2.value())// 2
counter2.restart();
log(counter2.value)// 0

// Note: When makeCounter() is called, a snapshot of the context of that function is saved.
// Note2: Closures are also used to prevent global namespace pollution, often through the use of immediately-invoked function expressions.

// Apply and Call
function speak() {
    let sentences = Array.prototype.slice.call(arguments);
    let tell = '';
    sentences.forEach(word => tell += word + ' ' );
    console.log(this.name+": "+ tell);
}

let person = { name: "Niko" };
    speak.apply(person, ["I", "will", "go", "through", "this", "roadmap", "until", "the", "end" ]); // I will go throght this roadmap to the end
    speak.call(person, "But", "first", "I", "need", "some", "exercice"); // But first I need some exercice

/* Notice that apply allows you to pass an Array or the arguments object (array-like) as the list of arguments, whereas, call needs you to pass each argument separately. */

/* As we see in the previus obj.adverstiment() example in line 155: When using arrow functions this takes the value from the enclosing execution context's this (that is, this in arrow functions has lexical scope rather than the usual dynamic scope). In global code (code that doesn't belong to any
function) it would be the global object. And it keeps that way, even if you invoke the function declared with the arrow notation from any of the others methods here described. */

/* The bind method of every function allows you to create new version of that function with the context strictly bound to a specific object. It is especially useful to force a function to be called as a method of an object. */

let person2 = { name: 'Anna' };

function sayHiLady() {
    log(`Hi ${this.name}`);
}

hiAnna = sayHiLady.bind(person2);
hiAnna()// Hi Anna

