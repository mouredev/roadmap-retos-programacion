/**
 * @author: Kronstadt-Lambda
 * @version: 1.0
 */

// Initializations
let array = [1, 2, 3, 4, 5];
let author = "Kronstadt-Lambda";

// function whitout return and parameters
function helloTeam() {
    console.log("Hello roadmap-retos-programacion!");
}
helloTeam();

// function whit one parameter whitout return
function helloName(name) {
    console.log("Hello " + name + "!");
}
helloName("Kronstadt-Lambda");

// function whit many parameters whitout return
function sumFactors(a, b, c, d) {
    console.log("The sum of the factors is: " + (a + b + c + d));
}
sumFactors(1, 2, 3, 4);

// Function that accepts any number of parameters and don't have return
function sumFactors2(...args) {
    let sum = 0;
    for (let i = 0; i < args.length; i++) {
        sum += args[i];
    }
    console.log("The sum of the factors is: " + sum);
}
sumFactors2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
sumFactors2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20);

// Function whitout parameters and whit return
function getNameDay() {
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const today = new Date();
    return days[today.getDay()];
}
console.log("Today is " + getNameDay());

// Function whit one parameter and whit return
function getSquare(n) {
    return n * n;
}
console.log("The square of 5 is: " + getSquare(5));

// Function whit many parameters and whit return
function getAverage(a, b, c, d) {
    return (a + b + c + d) / 4;
}
console.log("The average is: " + getAverage(1, 2, 3, 4));

// Function that accepts any number of parameters and have return
function getAverage2(...args) {
    let sum = 0;
    for (let i = 0; i < args.length; i++) {
        sum += args[i];
    }
    return sum / args.length;
}
console.log("The average is: " + getAverage2(1, 2, 3, 4, 5, 6));
console.log("The average is: " + getAverage2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));

// Function whit optional parameters and whit return
function multiplication(a, b = 1) {
    return a * b;
}
console.log("The multiplication of 5 is: " + multiplication(5));
console.log("The multiplication of 5 x 2 is: " + multiplication(5, 2));

// Function inside a function
function dotProduct(...args) {
    let sum = 0;
    function squareFactors(n) { 
        return n * n;
    }
    for (let i = 0; i < args.length; i++) {
        sum += squareFactors(args[i]);
    }
    return sum**0.5;
}
console.log("The sum of the square factors is: " + dotProduct(1, 2, 3, 4, 5));

// Functions pre-stablished
// parseInt
console.log(typeof parseInt("10")); // number
// push, pop, shift, unshift
array.push(6);
console.log(array); // [1, 2, 3, 4, 5, 6]
array.pop();
console.log(array); // [1, 2, 3, 4, 5]
array.shift();
console.log(array); // [2, 3, 4, 5]
array.unshift(1);
console.log(array); // [1, 2, 3, 4, 5]
// toUpperCase, toLowerCase
console.log(author.toUpperCase()); // KRONSTADT-LAMBDA
console.log(author.toLowerCase()); // kronstadt-lambda

// Local and global variables
let global = "World";
function greetings() {
    let local = "Hello ";
    console.log(local + global + "!"); // access to local and global variables
}
greetings();
try {
    console.log(local); // This line throws an error
} catch (error) {
    console.error("Error: variable" + error.message); // Catch the error and show a message
}

/**
 * Extra exercise
 * Create a function that takes two string parameters and returns a number.
 * - The function prints all numbers from 1 to 100. Considering that:
 * - If the number is a multiple of 3, it displays the string of the first parameter.
 * - If the number is a multiple of 5, it displays the string of the second parameter.
 * - If the number is a multiple of 3 and 5, it displays the two strings of text concatenated.
 * - The function returns the number of times the number has been printed instead of the texts.
 */

function printNumbers(text1, text2) {
    let count = 0;
    for (let i = 1; i <= 100; i++) {
        switch (true) {
            case i % 3 === 0 && i % 5 === 0:
                console.log(text1," and ", text2);
                break;
            case i % 3 === 0:
                console.log(text1);
                break;
            case i % 5 === 0:
                console.log(text2);
                break;
            default:
                console.log(i);
                count++;
                break;
        }
    }
    return count;
}
console.log("The number of times the NUMBER has been printed is: " + printNumbers("multiple of three", "multiple of five"));
