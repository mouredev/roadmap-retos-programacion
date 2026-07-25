// Exercise // 
// Function whitout parameters or return value
function noParameters() {
    console.log("This function has no parameters or return value.");
}

noParameters();

// Function with one parameter
function oneParameter(param) {
    console.log("The received parameter is: " + param);
}

oneParameter("Hello World");

// Function with multiple parameters
function multipleParameters(param1, param2) {
    console.log("The received parameters are: " + param1 + " and " + param2);
}

multipleParameters('Hello', 'World');

// Function with return value
function addition(a, b) {
    return console.log(a + b);
}

addition(4, 10);

// Nested functions
function outerFunction() {
    console.log("This is the outer function");
    function innerFunction() {
        console.log("This is the inner function");
    }
    innerFunction();
}

outerFunction();

// Using built-in functions
function exampleMath() {
    console.log("The absolute value of -5 is: " + Math.abs(-5));
}

exampleMath();

// Local and global variables
var globalVar = "I am a global variable";

function variableScope() {
    var localVar = "I am a local variable";
    console.log(globalVar);
    console.log(localVar);
}

variableScope();
console.log(globalVar);
// The following line will throw an error because 'localVar' is not defined in the global scope
// console.log(localVar);

// Extra Exercise // 

function oneHundred(param1, param2) {
    let counter = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(param1, param2);
        } else if (i % 3 === 0) {
            console.log(param1);
        } else if (i % 5 === 0) {
            console.log(param2);
        } else {
            console.log(i);
            counter++;
        }
    }
    return counter;
}

const counter = oneHundred('Fizz', 'Buzz');
console.log("Count of numbers printed: " + counter);
