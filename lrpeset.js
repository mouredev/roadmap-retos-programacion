//  Initialize variables
console.log("**   Initialize variables:   **");

let a = 1;
let b = 2;

console.log("let a = " + a);
console.log("let b = " + b);

//  Arithmetic operators
console.log("**   Arithmetic operators:   **");

let addition = a + b;
let increment = a++;
let substraction = a - b;
let decrement = a --;
let multiplication = a * b;
let division = a / b;
let remainder = a % b;
let exponentiation = a ** b;

console.log("Addition operator: ", addition);
console.log("Increment operator: ", increment);
console.log("Substraction operator: ", substraction);
console.log("Decrement operator: ", decrement);
console.log("Multiplication operator: ", multiplication);
console.log("Division operator: ", division);
console.log("Remainder operator: ", remainder);
console.log("Exponentiation operator: ", exponentiation);

// Assignment operators
console.log("**   Assignment operators:   **");

let additionAssignment = a += b;
let substractionAssignment = a -= b;
let multiplicationAssignment = a *= b;
let divisionAssignment = a /= b;
let remainderAssignment = a %= b;
let exponentiationAssignment = a **= b

console.log("Addition assignment: ", additionAssignment);
console.log("Substraction assignment: ", substractionAssignment);
console.log("Multiplication assignment: ", multiplicationAssignment);
console.log("Division assignment: ", divisionAssignment);
console.log("Remainder assignment: ", remainderAssignment);
console.log("Exponentiation Assignment: ", exponentiationAssignment);

//  Comparison operators
console.log("**   Comparison operators:   **");

let equality = a == 1;
let strictEquality = a === 1;
let inequality = a != 1;
let strictInequality = a !== 1;
let graterThan = a > b;
let graterThanOrEqual = a >= b;
let lessThan = a < b;
lessThanOrEqual = a <= b;

console.log("Equality operator: ", equality);
console.log("Strict equality operator: ", equality);
console.log("Inequality operator: ", inequality);
console.log("Strict inequality operator: ", inequality);
console.log("Greater than operator: ", graterThan);
console.log("Greater than or equal operator: ", graterThanOrEqual);
console.log("Less than operator: ", lessThan);
console.log("Less than or equal operator: ", lessThanOrEqual);

//  Logical operators
console.log("**   Logical operators:   **");

let and = true && true;
let andAssignment = true;
andAssignment &&= true;
let or = true || false;
let orAssignment = true;
orAssignment ||= false;
let not = !false;

console.log("AND operator: ", and);
console.log("AND assignment operator: ", andAssignment);
console.log("OR operator: ", or);
console.log("OR assignment operator: ", orAssignment);
console.log("NOT operator: ", not);

//  Control structures examples
console.log("**   Example of control structures:   **")

//  Conditional statements
//  if
let c = 10;
let d = 20;

if (c < d) {
  console.log("c is less than d");
} else if (c < d) {
  console.log("c is greater than d");
} else {
  console.log("c is equal to d");
}

//  switch
let day = 1;

switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  case 5:
    console.log("Friday");
    break;
  case 6:
    console.log("Saturday");
    break;
  case 7:
    console.log("Sunday");
    break;
}

//  Loops
//  for
let countdown = 10;

for (i = 0; countdown > i; countdown--) {
  console.log(countdown, "seconds left to launch!");
}

//  while
let count = 1;

while (count <= 5) {
  console.log("Count is: ", count);
  count++;
}

//  do...while
let carOnSale = 3;

do {
  console.log(carOnSale, "last units available!");
  carOnSale--;
} while (carOnSale > 0);

//  for...in
const obj = { a: 1, b: 2, c: 3 };

for (let key in obj) {
  console.log(key, ":", obj[key]);
}

//  for...of
const array = [1, 2, 3];

for (let value of array) {
  console.log("Value:", value);
}

//  Flow control
//  break and continue
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    console.log("Interruption on i loop:", i);
    break;
  }
  if (i % 2 === 0) {
    continue;
  }
  console.log(i);
}

//  return
function sum(a, b) {
  if (a < 0 || b < 0) {
    return "Numbers must be positives";
  }
  return a + b;
}

//  try...catch...finally and throw
function divide(a, b) {
    if (b === 0) {
        throw new Error("Can't divide by 0");
    }
    return a / b;
}

try {
    let result = divide(10, 0);
    console.log("Result:", result);
} catch (error) {
    console.error("Error:", error.message);
} finally {
    console.log("Operation complete.");
}

// Extra difficulty
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}