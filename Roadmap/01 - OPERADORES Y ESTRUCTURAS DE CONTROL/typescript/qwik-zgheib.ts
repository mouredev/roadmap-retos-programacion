// -- exercise
// Arithmetic operators
let a: number = 10;
let b: number = 5;
let sum: number = a + b;
let difference: number = a - b;
let product: number = a * b;
let quotient: number = a / b;
let remainder: number = a % b;

console.log("Arithmetic Operators:");
console.log("Sum:", sum);
console.log("Difference:", difference);
console.log("Product:", product);
console.log("Quotient:", quotient);
console.log("Remainder:", remainder);

// Logical operators
let x: boolean = true;
let y: boolean = false;
let andResult: boolean = x && y;
let orResult: boolean = x || y;
let notResult: boolean = !x;

console.log("\nLogical Operators:");
console.log("AND:", andResult);
console.log("OR:", orResult);
console.log("NOT:", notResult);

// Comparison operators
let num1: number = 10;
let num2: number = 20;
let isEqual: boolean = num1 === num2;
let isNotEqual: boolean = num1 !== num2;
let greaterThan: boolean = num1 > num2;
let lessThan: boolean = num1 < num2;
let greaterThanOrEqual: boolean = num1 >= num2;
let lessThanOrEqual: boolean = num1 <= num2;

console.log("\nComparison Operators:");
console.log("Is Equal:", isEqual);
console.log("Is Not Equal:", isNotEqual);
console.log("Greater Than:", greaterThan);
console.log("Less Than:", lessThan);
console.log("Greater Than or Equal:", greaterThanOrEqual);
console.log("Less Than or Equal:", lessThanOrEqual);

// Assignment operators
let assignedValue: number = 30;
assignedValue += 5;
console.log("\nAssignment Operator:");
console.log("Assigned Value:", assignedValue);

// Identity operators
let obj1: object = {};
let obj2: object = {};
let obj3: object = obj1;
let identityCheck1: boolean = obj1 === obj2;
let identityCheck2: boolean = obj1 === obj3;

console.log("\nIdentity Operators:");
console.log("Identity Check 1:", identityCheck1);
console.log("Identity Check 2:", identityCheck2);

// Membership operators
let array: number[] = [1, 2, 3];
let isInArray: boolean = array.includes(2);

console.log("\nMembership Operator:");
console.log("Is 2 in Array?", isInArray);

// Bitwise operators
let bitwiseAnd: number = 5 & 1;
let bitwiseOr: number = 5 | 1;
let bitwiseXor: number = 5 ^ 1;
let bitwiseNot: number = ~5;
let leftShift: number = 5 << 1;
let rightShift: number = 5 >> 1;
let zeroFillRightShift: number = 5 >>> 1;

console.log("\nBitwise Operators:");
console.log("Bitwise AND:", bitwiseAnd);
console.log("Bitwise OR:", bitwiseOr);
console.log("Bitwise XOR:", bitwiseXor);
console.log("Bitwise NOT:", bitwiseNot);
console.log("Left Shift:", leftShift);
console.log("Right Shift:", rightShift);
console.log("Zero-fill Right Shift:", zeroFillRightShift);

// Conditional structures
let condition: boolean = true;

if (condition) {
  console.log("Condition is true.");
} else {
  console.log("Condition is false.");
}

// ---------------------------------------------
// Iterative structure -- extra challenge
console.log("\nIterative Structure:");
for (let i: number = 10; i <= 55; i++) {
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
