// Arithmetic Operators
console.log("Arithmetic Operators")
let x = 100
console.log("+ Addition:", x + 50)
console.log("- Subtraction:", x - 50)
console.log("* Multiplication:", x * 50)
console.log("** Exponentiation:", x ** 2)
console.log("/ Division:", x / 50)
console.log("% Modulus:", 1 % 2)
console.log("++ Increment:", x++)
console.log("-- Decrementing:", x--)

// Assignment Operators
console.log("\nAssignment Operators")
console.log("= Assignment: x = ", x)
x += 1
console.log("+= Addition assignment: x += ", x)
x -= 1
console.log("-= Substraction Assignment: x -= ", x)
x *= 2
console.log("*= Multiplication Assignment: x *= ", x)
x /= 3
console.log("/= Division Assignment: x /= ", x)
x %= 2
console.log("%= Modulus Assignment: x %= ", x)
x **= 2
console.log("**= Exponentiation Assignment: x **= ", x)

// Shift Assignment Operators
console.log('\nShift Assignment Operators')
x = 5
x <<= 2
console.log('<<= left shift assignment:', x)
x = 5
x >>= 2
console.log('>>= right shift assignment:', x)

// Bitwise Assignment Operators
console.log('\nBitwise Assignment Operators')
x = 5
x &= 3
console.log('&= Bitwise AND assignment:', x)
x = 5
x ^= 3
console.log('^= Bitwise XOR:', x)
x = 5
x |= 3
console.log('|= Bitwise OR assignment:', x)

// Logical Assignment Operators
console.log('\nLogical Assignment Operators')
x = 1
x &&= 2
console.log('&&= Logical AND assignment', x)
x = 1
x ||= 2
console.log('||= Logical OR assignment', x)
x = 1
x ??= 2
console.log('??= Nullish coalescing assignment', x)

// Comparison Operators
console.log('\nComparision Operators')
console.log('== equal to:', 2 == '2')
console.log('=== equal value and equal type:', 2 === '2')
console.log('!=	not equal:', 2 != "3")
console.log('!==	not equal value or not equal type:', 2 !== 3)
console.log('> greater than:', 2 > 1)
console.log('< less than:', 2 < 1)
console.log('>=	greater than or equal to:', 2 >= 2)
console.log('<=	less than or equal to:', 2 <= 2)

// Logical Operators
console.log('\nLogical Operators')
x = 6
console.log('&& and operator:', x > 1 && x < 8)
console.log('|| or operator:', x > 1 || x > 8)
console.log('! not operator:', !(6 == 6))

// Miscellaneous Operators
console.log('\nMiscellaneous Operators')
let voteable = (7 < 18) ? "Too young" : "Old enough"
console.log('?: Ternary operator:', voteable)
let name = null;
let text = "missing";
let result = name ?? text;
console.log('?? The Nullish Coalescing Operator', result)
const car = {
  type: "Fiat",
  model: "500",
  color: "white"
};
let namecar = car?.namecar;
console.log('? The Optional Chaining Operator', namecar)

// CONTROL STRUCTURES
console.log('\nif Statement')
if (7 < 18) {
  console.log("Good day")
}

console.log('\nelse Statement')
if (19 < 18) {
  console.log("Good day")
} else {
  console.log("Good evening")
}

console.log('\nelse if Statement')
if (1 < 10) {
  console.log("Good morning")
} else if (time < 20) {
  console.log("Good day")
} else {
  console.log("Good evening")
}

console.log('\nSwitch Statement')
switch (new Date().getDay()) {
  case 0:
    console.log("Sunday")
    break;
  case 1:
    console.log("Monday")
    break;
  case 2:
    console.log("Tuesday")
    break;
  case 3:
    console.log("Wednesday")
    break;
  case 4:
    console.log("Thursday")
    break;
  case 5:
    console.log("Friday")
    break;
  case 6:
    console.log("Saturday")
}

console.log('\nfor loop')
const cars = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];

let texto = "";
for (let i = 0; i < cars.length; i++) {
  texto += cars[i] + "\n";
}
console.log(texto)

console.log('\nfor in loop')
const person = {
  fname: "John",
  lname: "Doe",
  age: 25
};
let textPerson = "";
for (let x in person) {
  textPerson += person[x] + " "
}
console.log(textPerson)

console.log('\nFor Of Loop Statement')
const cars1 = ["BMW", "Volvo", "Mini"];
let textCars = "";
for (let x of cars1) {
  textCars += x + " "
}
console.log(textCars)

console.log('\nWhile Loop')
let i = 0
while (i < 10) {
  text += "The number is " + i;
  i++;
  console.log(i)
}

// Exceptions(try, catch, finally and throw)
console.log('\ntry and catch')
try {
  nonExistentFunction()
} catch (error) {
  console.log("Something went wrong.")
}

console.log('\ntry and finally')

function doIt() {
  try {
    return console.log('1')
  } finally {
    return console.log('2')
  }
}
doIt();

console.log('\ntry, catch and throw')

function getRectArea(width, height) {
  if (isNaN(width) || isNaN(height)) {
    throw new Error('Parameter is not a number!');
  }
}

try {
  getRectArea(3, 'A');
} catch (e) {
  console.error(e);
}

// Challenge. Print numbers between 10 and 55(included), even and odd but not print 16 and multiple of 3.
console.log('\nChallenge')
for (let n = 0; n <= 55; n++) {
  if (n >= 10 && n % 2 == 0 && n != 16 && !(n % 3 == 0) || n == 55) {
    console.log(n)
  }
}