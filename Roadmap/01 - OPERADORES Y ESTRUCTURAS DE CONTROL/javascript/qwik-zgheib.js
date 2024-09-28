// -- exercise
// Arithmetic operators
let a = 10;
let b = 5;
let sum = a + b;
let difference = a - b;
let product = a * b;
let quotient = a / b;
let remainder = a % b;

console.log("Arithmetic Operators:");
console.log("Sum:", sum);
console.log("Difference:", difference);
console.log("Product:", product);
console.log("Quotient:", quotient);
console.log("Remainder:", remainder);

// Logical operators
let x = true;
let y = false;
let andResult = x && y;
let orResult = x || y;
let notResult = !x;

console.log("\nLogical Operators:");
console.log("AND:", andResult);
console.log("OR:", orResult);
console.log("NOT:", notResult);

// Comparison operators
let num1 = 10;
let num2 = 20;
let isEqual = num1 === num2;
let isNotEqual = num1 !== num2;
let greaterThan = num1 > num2;
let lessThan = num1 < num2;
let greaterThanOrEqual = num1 >= num2;
let lessThanOrEqual = num1 <= num2;

console.log("\nComparison Operators:");
console.log("Is Equal:", isEqual);
console.log("Is Not Equal:", isNotEqual);
console.log("Greater Than:", greaterThan);
console.log("Less Than:", lessThan);
console.log("Greater Than or Equal:", greaterThanOrEqual);
console.log("Less Than or Equal:", lessThanOrEqual);

// Assignment operators
let assignedValue = 30;
assignedValue += 5;
console.log("\nAssignment Operator:");
console.log("Assigned Value:", assignedValue);

// Identity operators
let obj1 = {};
let obj2 = {};
let obj3 = obj1;
let identityCheck1 = obj1 === obj2;
let identityCheck2 = obj1 === obj3;

console.log("\nIdentity Operators:");
console.log("Identity Check 1:", identityCheck1);
console.log("Identity Check 2:", identityCheck2);

// Membership operators
let array = [1, 2, 3];
let isInArray = 2 in array;

console.log("\nMembership Operator:");
console.log("Is 2 in Array?", isInArray);

// Bitwise operators
let bitwiseAnd = 5 & 1;
let bitwiseOr = 5 | 1;
let bitwiseXor = 5 ^ 1;
let bitwiseNot = ~5;
let leftShift = 5 << 1;
let rightShift = 5 >> 1;
let zeroFillRightShift = 5 >>> 1;

console.log("\nBitwise Operators:");
console.log("Bitwise AND:", bitwiseAnd);
console.log("Bitwise OR:", bitwiseOr);
console.log("Bitwise XOR:", bitwiseXor);
console.log("Bitwise NOT:", bitwiseNot);
console.log("Left Shift:", leftShift);
console.log("Right Shift:", rightShift);
console.log("Zero-fill Right Shift:", zeroFillRightShift);

// Conditional structures
let condition = true;

if (condition) {
  console.log("Condition is true.");
} else {
  console.log("Condition is false.");
}

// ---------------------------------------------
// Iterative structure -- extra challenge
console.log("\nIterative Structure:");
for (let i = 10; i <= 55; i++) {
  if (i !== 16 && i % 3 !== 0 && i % 2 === 0) {
    console.log(i);
  }
}
// ---------------------------------------------

// Exception handling structure
console.log("\nException Handling Structure:");
try {
  throw new Error("Example error");
} catch (error) {
  console.error(error);
}
