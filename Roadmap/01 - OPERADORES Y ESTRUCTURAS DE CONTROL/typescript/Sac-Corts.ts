// Arithmetic Operators
let c: number = 10;
let b: number = 5;
console.log("Addition:", c + b);
console.log("Subtraction:", c - b);
console.log("Multiplication:", c * b);
console.log("Division:", c / b);
console.log("Modulus:", c % b);
console.log("Exponentiation:", c ** b);

// Logical Operators
let isTrue: boolean = true;
let isFalse: boolean = false;
console.log("AND (&&):", isTrue && isFalse);
console.log("OR (||):", isTrue || isFalse);
console.log("NOT (!):", !isTrue);

// Comparison Operators
console.log("Equal (==):", c == b);
console.log("Not equal (!=):", c != b);
console.log("Strict equal (===):", c === b);
console.log("Strict not equal (!==):", c !== b);
console.log("Greater than (>):", c > b);
console.log("Less than (<):", c < b);
console.log("Greater than or equal (>=):", c >= b);
console.log("Less than or equal (<=):", c <= b);

// Assignment Operators
let x: number = 10;
x += 5;
console.log("x after x += 5:", x);
x -= 3;
console.log("x after x -= 5:", x);
x *= 2;
console.log("x after x *= 2:", x);
x /= 4;
console.log("x after x /= 4:", x);
x **= 2;
console.log("x after x **= 2:", x);
x %= 2;
console.log("x after x %= 2:", x);

// Bitwise Operators
let bitA: number = 5; // Binary: 0101
let bitB: number = 3; // Binary: 0011
console.log("Bitwise AND(&):", bitA & bitB);
console.log("Bitwise OR(|):", bitA | bitB);
console.log("Bitwise XOR(^):", bitA ^ bitB);
console.log("Bitwise NOT(~):", ~bitA);
console.log("Left shift(<<):", bitA << 1);
console.log("Right shift(>>):", bitA >> 1);

// Control Structures //
// If-else statement
if (c > b) {
    console.log("c is greater than b");
} else {
    console.log("c is not greater than b");
}

// Ternary Operator
let max = c > b ? c : b;
console.log("Max value:", max);

// Switch-case statement
let day: number = 2;
switch(day) {
    case 1: 
        console.log("It's Monday");
        break;
    case 2:
        console.log("It's Tuesday");
        break;
    case 3:
        console.log("It's Wednesday");
        break;
}

// While loop
let _count: number = 0;
while (_count < 3) {
    console.log("While loop count:", _count);
    _count++;
}

// For loop
for (let i = 0; i < 3; i++) {
    console.log("For loop iteration:", i);
}

// Do-while loop
let doCount: number = 0;
do {
    console.log("Do-while loop count:", doCount);
    doCount++;
} while (doCount < 3);

// Try-catch (Exception Handling)
try {
    let result = c / 0;
    if (!isFinite(result)) {
        throw new Error("Cannot divide by zero");
    }
} catch (error) {
    if (error instanceof Error) {
        console.log(error.message);
    }
} finally {
    console.log("Finally block executed");
}

// *** Extra Exercise *** //

for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i % 3 !== 0 && i !== 16) {
        console.log(i);
    }
}