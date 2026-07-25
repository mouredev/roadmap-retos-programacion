/*
Arithmetic operators
These operators are used to perform mathematical operations
between variables and/or values.
*/

/*
let a = 10;
let b = 2;

console.log(a + b); // 12 (Sum)
console.log(a - b); // 8 (Substraction)
console.log(a * b); // 20 (Multiplication)
console.log(a / b); // 5 (Division)
console.log(a % b); // 0 (Module: remainder of the division)
console.log(a ** b); // 100 (Elevar a una potencia - Raise to a power)
*/

/*
Assignment Operators
Assignment operators are used to assign values ​​to variables.
*/

/*
let a = 10;
a += 2; // is equal to a = a + 2
console.log(a); // 12

let b = 10;
b -= 2; // is equal to b = b - 2
console.log(b) // 8

let c = 10;
c *= 2; // is equal to c = c * 2
console.log(c); // 20

let d = 10;
d /= 2; // is equal to d = d / 2
console.log(d) // 5

let e = 10
e %= 2; // is equal to e = e % 2
console.log(e) // 0
*/

/*
Comparison Operators
Comparison operators are used to compare two values.

In TypeScript, the operators == and === are used for equality comparison,
but there is an important difference between them.

The == operator checks values ​​for equality, but allows automatic type conversion.
This means that if two values ​​of different types are compared that can be considered equivalent, == will return true. For example,
2 == "2" will return true, even though the first is a number and the second is a string.

In contrast, the === operator checks both the equality of values ​​and the type.
It does not allow type conversion, so if you compare two values ​​of different
types, === will return false, even if the values ​​are equivalent from a type conversion
standpoint. For example, 2 === "2" will return false, because
one is a number and the other is a text string.
*/

/*
let a = 10;
let b = 2;

console.log(a == b); // Equality (compares values, allows type conversion)
console.log(a === b); // Strict equality (compares values ​​and types)
console.log(a != b); // Different (compares values, allows type conversion)
console.log(a !== b); // Strict Different (compares values ​​and types)
console.log(a > b); // Mayor que
console.log(a < b); // Less than
console.log(a >= b); // Greater than or equal to
console.log(a <= b); // Less than or equal to
*/

/*
Logical Operators
Logical operators are used to combine conditions
*/

/*
let a = true;
let b = false;

console.log(a && b); // false (AND: true if all conditions are true)
console.log(a || b); // true (OR: true at least if one condition is true)
console.log(!a); // false (NOT: reverses the condition)
*/

/*
Bitwise Operators
Bitwise operators operate at the bit level of numbers.
*/

/*
let a = 5; // in binary 0101
let b = 3; // in binary 0011

console.log(a & b); // 1, in binary 0001
console.log(a | b); // 7, in binary 0111
console.log(a ^ b); // 6, in binary 0110
console.log(~a); // -6, It is the two's complement
console.log(a << 1); // 10, moves to the left 1 bit
console.log(a >> 1); // 2, moves to the right 1 bit

*/

/*
Conditional (ternary) operator
This operator is used to assign a value to a variable based on a
condition.
*/

/*
let age : number = 18;
let canDrive: string = age ? 'Yes' : 'No';
console.log(canDrive); //Yes
*/

/*
typeof operator
This operator is used to obtain the type of a variable or a value.
*/

/*
let a = 10;
console.log(typeof a); // number
*/

/*
instanceof operator
Used to check if an object is an instance of a specific class
*/

/*
class Person{
    constructor(public name: string) {}
}

const jhon = new Person('Jhon');

console.log(jhon instanceof Person); // true
console.log(jhon instanceof Object); // true (since all classes inherit from Object)
console.log(jhon instanceof Array); // false
*/

/*
Property Access Operators
TypeScript supports property access operators
*/

// Access with point (.)

/*

class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

const person = new Person("Jhon", 30);

console.log(person.name); // "Jhon"
console.log(person.age); // 30

*/

/*
Access with brackets (corchetes)

This operator is useful when the property name is dynamic (i.e., it is
located in a variable) or when the property name is not a valid identifier (for
example, it has spaces or special characters).
*/


/*
const person = {
  name: "Jhon",
  age: 30,
  "full name": "Jhon Pérez"
};

const property = "age";

console.log(person["name"]); // "Jhon"
console.log(person["full name"]); // "Jhon Pérez"
console.log(person[property]); // 30
*/

/*

Optional chaining operator (?.)

The optional chaining operator was introduced in TypeScript 3.7 and allows you to safely access
the properties of an object without raising an error if the object is null
or undefined. If the property does not exist or the object is null or undefined, instead of
raising an error, undefined is returned.

interface Person {
    name?: string;
    address?: {
      street?: string;
    };
  }
  
  const person: Person = {};
  
  console.log(person.name?.toUpperCase()); // undefined
  console.log(person.address?.street?.toUpperCase()); // undefined

*/

/*
Nullish chaining operator (??)

Although not a property access operator in the strict sense, the ?? operator
can be combined with other access operators to handle cases where a property
may be null or undefined. It returns the value on the right only if the value on the
left is null or undefined.


interface Person {
  name?: string | null;
}

const person: Person = { name: null };

console.log(person.name ?? "Unknown name"); // "Unknown name"

*/

/*
Function Call Operator ()
This operator is used to call a function.


function myFunction() {
    console.log('¡Hello World!');
  }
  
  myFunction();  // '¡Hello World!'
  

  function sum(a: number, b: number): number {
    return a + b;
  }
  
  console.log(sum(3, 4));  // 7
  
*/

/*
New Instance Operator new
The new operator in TypeScript (and JavaScript) is used to create a new instance
of a class. When this operator is used, the class constructor is called, which
initializes a new object with the properties and methods defined in the class.



class Person {
    name: string;
    age: number;
  
    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  
    greet() {
      return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
  }
  
  const person1 = new Person("Jhon", 30);
  console.log(person1.greet());  // "Hello, my name is Jhon and I am 30 years old."
  

*/

/*

1. Conditional Control Structures
They are used to execute code
depending on a condition.

let age: number = 18;

if (age >= 18) {
  console.log("You are of legal age.");
} else {
  console.log("You are a minor")
}


let day: number = 3;

switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  default:
    console.log("Another day");
}


2. Loop Control Structures (Iterative)
They are used to repeat a series of instructions.



for (let i = 0; i < 5; i++) {
  console.log(i);
}


let counter: number = 0; 

while (counter < 5) {
  console.log(counter);
  counter++;
}

let num: number = 0;

do {
  console.log(num);
  num++;
} while (num < 5);

// for...of (to iterate over arrays, strings, etc.)

let numbers: number[] = [1, 2, 3, 4];

for (let num of numbers) {
  console.log(num);
}



// for in... to iterate over properties of an object

let person = { name: "Jhon", age: 25 };

for (let key in person) {
  console.log(`${key}: ${person[key as keyof typeof person]}`);
}


3. Jump Control Structures
They allow the normal flow of
execution to be modified.

break (breaks out of a loop o switch)

for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break; // loop ends
  }
  console.log(i);
}

continue (skip the current iteration and go to the next one)

for (let i = 0; i < 5; i++) {
  if (i === 2) {
    continue; // Jump this iteration
  }
  console.log(i);
}

return (exits a function and returns a value)

function sum(a: number, b: number): number {
  return a + b; // Ends the function and returns a result


// throw (throws an error)

function validateAge(age: number) {
  if (age < 18) {
    throw new Error("You must be legal of age.");
  }
  return "Access allowed";
}

try {
  console.log(validateAge(19)); // change the number to test
} catch (error) {
  console.error(error.message);
}


*/

for (let i = 10; i < 55; i++) {
  if (i % 2 == 0 && i != 16 && i % 3 != 0)
  console.log(i);
}
