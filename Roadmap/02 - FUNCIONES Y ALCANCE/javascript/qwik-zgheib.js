/* -- exercise */
const greet = () => console.log("Hello, world!");

greet();

const square = (number) => number * number;

let result = square(5);
console.log("Square of 5:", result);

const outerFunction = () => {
  console.log("Outer function is executing.");
  const innerFunction = () => console.log("Inner function is executing.");
  innerFunction();
};

outerFunction();

let globalVariable = "I'm global";

function localGlobalExample() {
  let localVariable = "I'm local";
  console.log("Inside function:");
  console.log(" - Local variable:", localVariable);
  console.log(" - Global variable:", globalVariable);
}

localGlobalExample();

console.log("Outside function - Global variable:", globalVariable);

let randomNumber = Math.random();
console.log("Random number:", randomNumber);

/* -- extrta challenge */
function printNumbersAndCount(text1, text2) {
  let count = 0;

  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(text1 + text2);
      count++;
    } else if (i % 3 === 0) {
      console.log(text1);
      count++;
    } else if (i % 5 === 0) {
      console.log(text2);
      count++;
    } else console.log(i);
  }

  return count;
}

let count = printNumbersAndCount("Fizz", "Buzz");
console.log("Number of times text has been printed:", count);
