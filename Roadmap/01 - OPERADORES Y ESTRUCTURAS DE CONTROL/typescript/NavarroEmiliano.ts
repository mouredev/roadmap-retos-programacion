/* =============Arithmetic operators ============= */
let num1: number = 10;
let num2: number = 5;

//Addition operator
let sum: number = num1 + num2; // 15

//Subtraction operator
let difference: number = num1 - num2; // 5

//Multiplication operator
let product: number = num1 * num2; // 50

//Division operator
let quotient: number = num1 / num2; // 2

//Modulus operator
let remainder: number = num1 % num2; // 0

//Exponentiation operator
let power: number = num1 ** num2; // 100000

//Increment operator
let postIncrement: number = num1++; // Returns the value of num1 (10), then increments num1 by 1 (11)
let preIncrement: number = ++num1; // Increments num1 by 1 (12), then returns the value of num1 (12)

//Decrement operator
let postDecrement: number = num1--; // Returns the value of num1 (12), then decrements num1 by 1 (11)
let preDecrement: number = --num1; // Decrements num1 by 1 (10), then returns the value of num1 (10)

//Unary plus operator
let unaryPlus: number = +num1; // Try to convert num1 to a number if possible, otherwise returns NaN

//Unary minus operator
let unaryMinus: number = -num1; // Try to convert num1 to a number if possible, then negates it finally returns the value or NaN

/* =============Logical operators ============= */
let isTrue: boolean = true;
let isFalse: boolean = false;

// Logical AND operator (&&)
// The logical AND operator (&&) evaluates operands from left to right.
// 1. If both operands are true, it returns true.
// 2. If any operand is false, it returns false.
// 3. If the first operand is falsy, it returns that value without evaluating the second operand (short-circuit).
// 4. If the first operand is truthy, it returns the value of the second operand.

// Behavior with boolean values:
let andResult1: boolean = true && true; // true
let andResult2: boolean = true && false; // false
let andResult3: boolean = false && true; // false
let andResult4: boolean = false && false; // false

// Short-circuit evaluation and non-boolean values:
let andShortCircuit1: any = 0 && 'hello'; // 0 (falsy, short-circuits)
let andShortCircuit2: any = 1 && 'hello'; // "hello"
let andShortCircuit3: any = 'hello' && 0; // 0
let andShortCircuit4: any = null && undefined; // null (falsy, short-circuits)

// Truthy and falsy values:
// Falsy: false, 0, -0, 0n, "", null, undefined, NaN
// Truthy: Everything else, including "0", "false", [], {}, function(){}

// Type coercion:
let andCoercion1: any = '5' && 2; // 2 (string "5" is truthy)
let andCoercion2: any = [] && 'hello'; // "hello" (empty array is truthy)

// In this specific case:
let andResult: boolean = isTrue && isFalse; // false (because isFalse is false)

// Note: When used with boolean operands, && always returns a boolean.
// When used with non-boolean operands, it may return a non-boolean value.

//Logical OR operator
let orResult: boolean = isTrue || isFalse; // true

// Logical OR operator (||)
// The logical OR operator (||) evaluates operands from left to right.
// 1. If either operand is true, it returns true.
// 2. If both operands are false, it returns false.
// 3. If the first operand is truthy, it returns that value without evaluating the second operand (short-circuit).
// 4. If the first operand is falsy, it returns the value of the second operand.

// Behavior with boolean values:
let orResult1: boolean = true || true; // true
let orResult2: boolean = true || false; // true
let orResult3: boolean = false || true; // true
let orResult4: boolean = false || false; // false

// Short-circuit evaluation and non-boolean values:
let orShortCircuit1: any = 1 || 'hello'; // 1 (truthy, short-circuits)
let orShortCircuit2: any = 0 || 'hello'; // "hello"
let orShortCircuit3: any = 'hello' || 0; // "hello" (truthy, short-circuits)
let orShortCircuit4: any = null || undefined; // undefined

// Truthy and falsy values:
// Falsy: false, 0, -0, 0n, "", null, undefined, NaN
// Truthy: Everything else, including "0", "false", [], {}, function(){}

// Type coercion:
let orCoercion1: any = '' || 2; // 2 (empty string is falsy)
let orCoercion2: any = [] || 'hello'; // [] (empty array is truthy, short-circuits)

// In this specific case:
let orResultFinal: boolean = isTrue || isFalse; // true (because isTrue is true)

// Note: When used with boolean operands, || always returns a boolean.
// When used with non-boolean operands, it may return a non-boolean value.

//Logical NOT operator
let notResult: boolean = !isTrue; // false

//Logical NOT operator (!)
// The logical NOT operator (!) converts its operand to a boolean value and returns the opposite value.
// 1. If the operand is truthy, it returns false.
// 2. If the operand is falsy, it returns true.

/* ============= Comparison operators ============= */

// num1 = 10; num2 = 5;
let comparison1: boolean = num1 == num2; // false -- returns true if the values are the same
let comparison2: boolean = num1 != num2; // true -- returns true if the values are not the same
let comparison3: boolean = num1 === num2; // false -- returns true if the values are the same and of the same type
let comparison4: boolean = num1 !== num2; // true -- returns true if the values are not the same or of different type
let comparison5: boolean = num1 > num2; // true -- returns true if num1 is greater than num2
let comparison6: boolean = num1 < num2; // false -- returns true if num1 is less than num2
let comparison7: boolean = num1 >= num2; // true -- returns true if num1 is greater than or equal to num2
let comparison8: boolean = num1 <= num2; // false -- returns true if num1 is less than or equal to num2

/* ============= Assignment operators ============= */

// Assignment operators

let x: number = 10;
x += 5; // x = x + 5; // Adds 5 to x and assigns the result to x
x -= 3; // x = x - 3; // Subtracts 3 from x and assigns the result to x
x *= 2; // x = x * 2; // Multiplies x by 2 and assigns the result to x
x /= 4; // x = x / 4; // Divides x by 4 and assigns the result to x
x %= 3; // x = x % 3; // Calculates the remainder when x is divided by 3 and assigns it to x
x **= 2; // x = x ** 2; // Raises x to the power of 2 and assigns the result to x

let y: number = 5;
y <<= 1; // y = y << 1; // Left shifts y by 1 bit and assigns the result to y
y >>= 1; // y = y >> 1; // Right shifts y by 1 bit and assigns the result to y
y >>>= 1; // y = y >>> 1; // Unsigned right shifts y by 1 bit and assigns the result to y

let z: number = 7;
z &= 3; // z = z & 3; // Performs bitwise AND on z and 3, assigns the result to z
z |= 4; // z = z | 4; // Performs bitwise OR on z and 4, assigns the result to z
z ^= 2; // z = z ^ 2; // Performs bitwise XOR on z and 2, assigns the result to z

let str: string = 'Hello';
str += ' World'; // str = str + " World"; // Concatenates " World" to str and assigns the result to str

/* ============= Belonging operators ============= */

// in operator (for objects and arrays)
let person = { name: 'John', age: 30 };
let car = ['Toyota', 'Honda', 'Ford'];

console.log('name' in person); // true
console.log('color' in person); // false
console.log(0 in car); // true (0 is a valid index)
console.log(3 in car); // false (index 3 doesn't exist)

// instanceof operator (for objects)
class Animal {}
class Dog extends Animal {}

let myDog = new Dog();

console.log(myDog instanceof Dog); // true
console.log(myDog instanceof Animal); // true
console.log(myDog instanceof Object); // true

// Array.includes() method (for arrays)
let fruits = ['apple', 'banana', 'orange'];

console.log(fruits.includes('banana')); // true
console.log(fruits.includes('grape')); // false

// Object.hasOwnProperty() method (for objects)
let book = { title: 'TypeScript Guide', pages: 200 };

console.log(book.hasOwnProperty('title')); // true
console.log(book.hasOwnProperty('author')); // false

// String.includes() method (for strings)
let sentence = 'The quick brown fox jumps over the lazy dog';

console.log(sentence.includes('fox')); // true
console.log(sentence.includes('cat')); // false

/* ============= Bitwise operators ============= */

// Bitwise AND (&)
// Performs a bitwise AND operation on each pair of bits
let a: number = 5; // 0101 in binary
let b: number = 3; // 0011 in binary
console.log(a & b); // 0001 in binary, outputs 1

// Bitwise OR (|)
// Performs a bitwise OR operation on each pair of bits
console.log(a | b); // 0111 in binary, outputs 7

// Bitwise XOR (^)
// Performs a bitwise XOR operation on each pair of bits
console.log(a ^ b); // 0110 in binary, outputs 6

// Bitwise NOT (~)
// Inverts all the bits in a single number
console.log(~a); // 1010 in binary, outputs -6 (due to two's complement)

// Left shift (<<)
// Shifts the bits of the first operand left by the number of places specified in the second operand
console.log(a << 1); // 1010 in binary, outputs 10

// Sign-propagating right shift (>>)
// Shifts the bits of the first operand right by the number of places specified in the second operand
console.log(a >> 1); // 0010 in binary, outputs 2

// Zero-fill right shift (>>>)
// Shifts the bits of the first operand right by the number of places specified in the second operand, and shifts in zeros from the left
let c: number = -5; // 11111111111111111111111111111011 in binary (32-bit)
console.log(c >>> 1); // 01111111111111111111111111111101 in binary, outputs 2147483645

/* ============= Control structures ============= */
//if statement
if (2 > 1) {
  console.log('2 is greater than 1');
}

//if else statement
if (10 > 5) {
  console.log('10 is greater than 5');
} else {
  console.log('x is equal to 5');
}

//if else if statement

if (10 > 5) {
  console.log('10 is greater than 5');
} else if (10 < 5) {
  console.log('10 is less than 5');
} else {
  console.log('10 is equal to 5');
}

//switch statement
let day: number = 3;

switch (day) {
  case 1:
    console.log('Monday');
    break;
  case 2:
    console.log('Tuesday');
    break;
}

//iterative statement
for (let i: number = 0; i < 10; i++) {
  console.log(i);
}

//while statement
let i: number = 0;
while (i < 10) {
  console.log(i);
  i++;
}

//do while statement
let j: number = 0;
do {
  console.log(j);
  j++;
} while (j < 10);

//for of statement
let colors: string[] = ['red', 'green', 'blue'];

for (let color of colors) {
  console.log(color);
}

//for in statement
let student: { name: string; age: number } = { name: 'John', age: 30 };

for (let key in student) {
  console.log(key);
}

// exception handling
try {
  throw new Error('This is a test error');
} catch (error) {
  console.log(error);
}

// finally statement
try {
  throw new Error('This is a test error');
} catch (error) {
  console.log(error);
} finally {
  console.log('This is the finally block');
}

// throw statement
//throw new Error('This is a test error');

/* ============= Optional Programming ============= */

let myNumber: number = 10;

while (myNumber <= 55 ) {
  const isMultipleOfThree: boolean = myNumber % 3 === 0;
  const isPair: boolean = myNumber % 2 === 0;
  const notSixteen: boolean = myNumber !== 16;

  if(!isMultipleOfThree && notSixteen && isPair){
    console.log(myNumber);
  }
  myNumber++; 
}

// Output array: [10, 14, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52]





