/* -- exercise */
const greet = (): void => console.log("Hello, world!");

greet();

const square = (number: number): number => number * number;

let result: number = square(5);
console.log("Square of 5:", result);

const outerFunction = (): void => {
  console.log("Outer function is executing.");
  const innerFunction = (): void => console.log("Inner function is executing.");
  innerFunction();
};

outerFunction();

let globalVariable: string = "I'm global";

function localGlobalExample(): void {
  let localVariable: string = "I'm local";
  console.log("Inside function:");
  console.log(" - Local variable:", localVariable);
  console.log(" - Global variable:", globalVariable);
}

localGlobalExample();

console.log("Outside function - Global variable:", globalVariable);

let randomNumber: number = Math.random();
console.log("Random number:", randomNumber);

/* -- extra challenge */
function printNumbersAndCount(text1: string, text2: string): number {
  let count: number = 0;

  for (let i: number = 1; i <= 100; i++) {
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

let count: number = printNumbersAndCount("Fizz", "Buzz");
console.log("Number of times text has been printed:", count);
