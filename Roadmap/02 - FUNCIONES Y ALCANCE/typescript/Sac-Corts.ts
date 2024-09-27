// Function with no parameters and no return
function greet(): void {
    console.log("Hello, welcome to TypeScript!");
}

// Function with one parameter and no return
function greetUser(name: string): void {
    console.log(`Hello, ${name}!`);
}

// Function with multiple parameters and no return
function addNumbers(a: number, b: number): void {
    console.log(`The sum of ${a} and ${b} is ${a + b}`);
}

// Function with one parameter and a return value
function square(num: number): number {
    return num * num;
}

// Function with multiple parameters and a return value
function multiplyNumbers(a: number, b: number): number {
    return a * b;
}

// Nested Functions 
function outerFunction(): void {
    console.log("This is the outer function");

    // Inner function
    function innerFunction(): void {
        console.log("This is the inner function");
    }

    innerFunction();
}

// Built-in Functions
function calculateCircleArea(radius: number): number {
    return Math.PI * Math.pow(radius, 2);
} 

// Testing local and global variables
// Global variable
let globalVar = "I'm a global variable";

function testVariableScope(): void {
    // Local variable
    let localVar = "I'm a local variable";

    console.log(globalVar);
    console.log(localVar);

    globalVar = "Global variable modified inside the function";
}

greet(); // Function without parameters and no return
greetUser("Isaac"); // Function with one parameter and no return
addNumbers(5, 7); // Function with multiple parameters and no return
console.log(`Square of 4 is: ${square(4)}`); // Function with one parameter and return value
console.log(`Multiplication of 3 and 6 is: ${multiplyNumbers(3, 6)}`); // Function with multiple parameters and return value

outerFunction(); // Calls outer and inner function

console.log(`Area of circle with radius 5 is: ${calculateCircleArea(5)}`); // Uses Math functions

testVariableScope();
console.log(globalVar);
// console.log(localVar); Error: localVar is not defined outside the function


// *** Extra Exercise *** //
function printNumbersWithText(string1: string, string2: string): number  {
    let counter = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(string1 + string2);
        } else if (i % 3 === 0) {
            console.log(string1);
        } else if (i % 5 === 0) {
            console.log(string2);
        } else {
            console.log(i);
            counter++;
        }
    }
    return counter;
}

const times = printNumbersWithText("Fizz", "Buzz");
console.log(`The number was printed ${times} times`);
