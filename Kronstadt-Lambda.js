/**
 * @author: Kronstadt-Lambda
 * @version: 1.0
 */

// Initialize variables
let float_a = 2.0;
let float_b = 2.0;
let bit_a = 0b00000101;
let bit_b = 0b00000110;
const day = "Wendesday";
let edad = 1;
let isBool;
const person = { name: "Jhon", age: 30 };
const numbers = [1, 2, 3];

/**
 * Operators in JavaScript
 */
// Arithmetic operators
console.log("Addition:", float_a + float_b);
console.log("Subtraction:", float_a - float_b);
console.log("Multiplication:", float_a * float_b);
console.log("Division:", float_a / float_b);
console.log("Exponentiation:", float_a ** float_b);
console.log("Modulus:", float_a % float_b);
console.log("Pre-Increment:", ++float_a);
console.log("Pre-Decrement:", --float_a);
console.log("Post-increment:", float_a++);
console.log("Post-decrement:", float_a--);

// Assignment operators
console.log("Simple Assignment:", float_a = float_b);
console.log("Addition Assignment:", float_a += float_b);
console.log("Subtraction Assignment:", float_a -= float_b);
console.log("Multiplication Assignment:", float_a *= float_b);
console.log("Division Assignment:", float_a /= float_b);
console.log("Exponentiation Assignment:", float_a **= float_b);
console.log("Modulus Assignment:", float_a %= float_b);
console.log("Bitwise AND Assignment:", bit_a &= bit_b);
console.log("Bitwise OR Assignment:", bit_a |= bit_b);
console.log("Bitwise XOR Assignment:", bit_a ^= bit_b);
console.log("Left Shift Assignment:", bit_a <<= bit_b);
console.log("Right Shift Assignment:", bit_a >>= bit_b);

// Comparison operators
console.log("Equal to:", float_a == float_b);
console.log("Not equal to:", float_a != float_b);
console.log("Strict equal (value and type) to:", float_a === float_b);
console.log("Strict not equal (value and type) to:", float_a !== float_b);
console.log("Greater than:", float_a > float_b);
console.log("Less than:", float_a < float_b);
console.log("Greater than or equal to:", float_a >= float_b);
console.log("Less than or equal to:", float_a <= float_b);

// Logical operators
console.log("Logical AND:", true && false);
console.log("Logical OR:", true || false);
console.log("Logical NOT:", !true);

// Bitwise operators
console.log("Bitwise AND:", bit_a & bit_b);
console.log("Bitwise OR:", bit_a | bit_b);
console.log("Bitwise XOR:", bit_a ^ bit_b);
console.log("Bitwise NOT:", ~bit_a);
console.log("Left Shift:", bit_a << 1);
console.log("Right Shift:", bit_a >> 1);
console.log("Zero-fill Right Shift:", bit_a >>> 1);

// Identity operators
console.log("Equal value and type:", float_a === float_b);
console.log("Not equal value or not equal type:", float_a !== float_b);

// Membership operators
console.log("Is in:", 'name' in person); // Verify if the property exists in the object
console.log("Is not in:", 'lastname' in person); // Verify if the property does not exist in the object
console.log("Is in:", numbers.includes(2)); // Verify if the value exists in the array

/**
 * Control structures in JavaScript
 */
// If, if-else, else statement
if (float_a === float_b) {
  console.log("The numbers are equal.");
} else if (float_a > float_b) {
  console.log("float_a is greater than float_b.");
} else {
  console.log("float_a is less than float_b.");
}
// Switch statement
switch (day) {
    case "Monday":
        console.log("Today is Monday.");
        break; // Exit the switch statement to avoid executing the next cases
    case "Tuesday":
        console.log("Today is Tuesday.");
        break; // Exit the switch statement to avoid executing the next cases
    case "Wednesday":
        console.log("Today is Wednesday.");
        break; // Exit the switch statement to avoid executing the next cases
    case "Thursday":
        console.log("Today is Thursday.");
        break; // Exit the switch statement to avoid executing the next cases
    case "Friday":
        console.log("Today is Friday.");
        break; // Exit the switch statement to avoid executing the next cases
    default: // If no case matches
        console.log("It's the weekend.");
        break; // Exit the switch statement to avoid executing the next cases
}
// For loop
for (let i = 10; i >= 0; i--) {
    console.log("The loop end in ...", i);
}
// While loop
while (edad < 18) {
    console.log("I am ", edad, " years old.");
    edad++;
}
// Do-while loop
do {
    isBool = false;
    console.log("At least one execution.");
} while (isBool);
// For-in loop: Usefull for objects
for (let key in person) {
    console.log(key, ":", person[key]);
}
// For-of loop: Usefull for arrays
for (let number of numbers) {
    console.log("Number:", number);
}
// Break statement
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        console.log("Break at:", i);
        break; // Exit the loop
    }
    console.log("i = :", i);
}
// Continue statement
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        console.log("Continue (skip) at:", i);
        continue; // Skip the current iteration
    }
    console.log("Cube of", i, "is", i ** 3);
}
// Label statement: Exit an outer loop
outerloop: for (let i = 0; i < 5; i++) {
    console.log("Outerloop:", i);
    innerloop: for (let j = 0; j < 5; j++) {
        if (j === 3) {
            break outerloop; // Exit the outer loop
        }
        console.log("Innerloop:", j);
    }
}
// Return statement: Exit a function
function add(a, b) {
  return a + b;
}
// try-catch-finally statement: Handle exceptions
try {
  console.log(numbers[3]);
} catch (error) {
  console.error("An error occurred:", error);
} finally {
  console.log("Finally block.");
}

/**
 * Extra exercises
 * Create a program that prints to the console all numbers between 10 and 55 (inclusive), even, and that are neither 16 nor multiples of 3
 */

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log("The solution is: ", i);
    }
}