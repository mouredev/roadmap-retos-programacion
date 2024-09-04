//  Basic functions
//  No parameter, no return
function noParameterFunction() {
  console.log("Hello world!");
}
noParameterFunction();

//  One parameter, no return
function oneParameterFunction(displays) {
  console.log("I have", displays, "displays in my computer");
}
oneParameterFunction(2);

//  Two parameters, no return
function twoParametersFunction(a, b) {
  console.log("The area of the rectangle is:", a * b);
}
twoParametersFunction(5, 10);

//  No parameter with return
function noParameterReturnFunction() {
  return Math.random();
}
let randomNumber = noParameterReturnFunction();
console.log("The random number is: ", randomNumber);

//  One parameter with return
function oneParameterReturnFunction(number) {
  return number * 2;
}
let doubleNumber = oneParameterReturnFunction(10);
console.log("The double of this number is:", doubleNumber);

//  Two parameters with return
function twoParametersReturnFunction(base, height) {
  return (base * height) / 2;
}
console.log("The area of the triangle is:" + twoParametersReturnFunction(4, 5));

//  Function as expression
let multiply = function (a, b) {
  return a * b;
};
console.log("The multiplication result is", multiply(1, 3));

// Arrow function
let square = (n) => n * n;
console.log("The square of the number is", square(3));

//  Function with default parameters
function greet(name, salute = "Hello!") {
  console.log(salute + " " + name);
}
greet("Mark");
greet("Jim", "Good morning");

//  Function with rest parameters
function sumAll(...allNumbers) {
  return allNumbers.reduce((acc, num) => acc + num, 0);
}
console.log("The sum of all numbers is:", sumAll(5, 3, 10, 2));

//  Function within function
function squareSum(a, b) {
  function square(x) {
    return x * x;
  }
  return square(a) + square(b);
}
console.log("The sum of both squares is:", squareSum(2, 4));

//  Function within native functions
function processText(text) {
  function countWords(str) {
    return str.split(" ").length;
  }

  let numberOfWords = countWords(text);
  return `Number of words: ${numberOfWords}`;
}

let result = processText("Hello everyone my name is Jim");
console.log(result);

//  Function with local and global variables
let message = "This is a global variable";

function showMessage() {
  let message = "This is a local variable";
  console.log(message);
}

console.log(message);
showMessage();
console.log(message);

//  Extra difficulty
function extraDifficulty(firstString, secondString) {
  let counter = 0;

  for (let i = 1; i <= 100; i++) {
    let ouput =
      (i % 3 === 0 ? firstString : "") + (i % 5 === 0 ? secondString : "") || i;
    if (ouput === i) counter++;
    console.log(ouput);
  }
  return counter;
}

extraDifficulty("First string", "Second string");
