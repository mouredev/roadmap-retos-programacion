// Exercise //

// Arithmetic Operators
let addition = 5 + 3;
console.log("Addition: 5 + 3 = ", addition);

let subtraction = 10 - 5;
console.log("Subtraction: 10 - 5 = ", subtraction);

let multiplication = 10 * 5;
console.log("Multiplication: 10 * 5 = ", multiplication);

let division = 100 / 5;
console.log("Division: 10 / 5 = ", division);

let _module = 8 % 2;
console.log("Module: 8 % 2 = ", _module);

let power = 4 ** 2;
console.log("Power: 4 ** 2 = ", power);

// Assignment Operators
let a = 10;

a += 2;
console.log("Addition assignment +=: ", a);

a -= 2;
console.log("Subtraction assignment -=: ", a);

a *= 4;
console.log("Multiplication assignment *=: ", a);

a /= 2;
console.log("Division assignment /=: ", a);

a %= 2;
console.log("Remainder assignment %=: ", a);

a **= 2;
console.log("Exponentiation assignment **=: ", a);

// Comparison Operators
console.log("Equality == : ", 5 == "5");
console.log("Strict equality == : ", 5 === "5");
console.log("Inequality != : ", 5 != "5");
console.log("Strict inequality !== : ", 5 !== "5");
console.log("Greater than > : ", 10 > 5);
console.log("Less than < : ", 10 < 5);
console.log("Greater than or equal >= : ", 5 >= 7);
console.log("Less than or equal <= : ", 5 <= 7);

// Logical Operators
console.log("Logical AND (&&):", true && false);
console.log("Logical OR (||):", true || false);
console.log("Logical NOT (!):", !false);

// Identity Operators
let obj1 = { name: "Isaac" };
let obj2 = { name: "Isaac" };
let obj3 = obj1;
console.log("Identity (===):", obj1 === obj2);
console.log("Identity (===):", obj1 === obj3);

// Membership Operators
let array = [1, 2, 3, 4, 5];
console.log("Membership (in):", 3 in array);
console.log("Membership (includes):", array.includes(3));

let obj = { name: "Bob", age: 25 };
console.log("Membership (in):", "name" in obj);
console.log("Membership (in):", "height" in obj);

// Bits Operators
console.log("Bitwise AND (&):", 5 & 1); // 101 & 001 = 001 (1)
console.log("Bitwise OR (|):", 5 | 1); // 101 | 001 = 101 (5)
console.log("Bitwise XOR (^):", 5 ^ 1); // 101 ^ 001 = 100 (4)
console.log("Bitwise NOT (~):", ~5); // ~101 = 010 (complemento)
console.log("Bitwise Left Shift (<<):", 5 << 1); // 101 << 1 = 1010 (10)
console.log("Bitwise Right Shift (>>):", 5 >> 1); // 101 >> 1 = 010 (2)
console.log("Bitwise Zero-fill Right Shift (>>>):", 5 >>> 1); // 101 >>> 1 = 010 (2)

// Control Structures //

// Conditionals
let num = 10;
if (num > 0) {
    console.log("The number is positive");
} else if (num < 0) {
    console.log('The number is negative');
} else {
    console.log('The number is cero');
}

switch (num) {
    case 1:
        console.log('The number is 1');
        break;
    case 10:
        console.log('The numer is 10')
        break;
        default:
            console.log('The number is not 1 or 10');
}

// Iterative
for (let i = 0; i < 5; i++) {
    console.log('For loop, i = ', i);
}

let count = 0;
while (count < 5) {
    console.log('While loop, i = ', count);
    count++;
}

let index = 0;
do {
    console.log('Do loop, index = ', index);
    index++;
} while (index < 5);

let arrayForOf = ['a', 'b', 'c'];
for (let item of arrayForOf) {
    console.log('For-of loop, item = ', item);
}

let objForIn = { name: 'Alice', age: 25};
for (let key in objForIn) {
    console.log('For-in loop, key = ', key, ', value = ', objForIn[key]);
}

// Exceptions 
try {
    let result = 10 / 0;
    console.log('Result: ', result);
    throw new Error('This is a custom exception');
} catch (error) {
    console.log('An exception was caught: ', error.message);
} finally {
    console.log('This block is always executed');
}

// Extra Exercise // 

for (let i = 10; i <= 55 ; i++) {
    if (i % 2 === 0 && i % 3 !== 0 && i !== 16) {
        console.log(i);
    }
}