/* #01 { PROGRAMMING CHALLENGES }   OPERATORS AND CONTROL STRUCTURES */
// Note: This code references Matt Frisbie's book "Professional JavaScript for Web Developers" for accurate information about operators.
// Additional tips are sourced from "JavaScript Notes for Professionals" by the StackOverflow community, available for free at GoalKicker.com.
//and https://www.typescriptlang.org/docs/

// Short for log
const log = console.log;

/*  OPERATORS  */

// Unary Operators

// Unary Plus and Minus
/* The unary plus operator converts non-numeric values to numbers, similar to the Number() function. 
Boolean values are converted to 0 (false) and 1 (true), strings are parsed, and objects call their valueOf() 
and/or toString() methods for conversion. */

let str1: string = "03";
let num1: number = +str1; // Converts to number
log(num1); // 3

let str2: string = "1.4";
let num2: number = +str2; // Converts to number
log(num1 + num2); // 4.4

let str3: string = "zaz";
let num3: number = +str3; // Converts to number (NaN)
log(num3); // NaN

let bool: boolean = true;
let numBool: number = +bool; // Converts to number
log(numBool); // 1

let f_num: number = 2.8; // Already a number
log(f_num); // 2.8

let obj = {
    valueOf() {
        return -5;
    }
};
let numObj: number = +obj; // Converts to number
log(numObj); // -5

/* The unary minus operator negates numeric values. When applied to non-numeric values, it follows the same 
conversion rules as unary plus and then negates the result. */

let g_actions: number = 50;
g_actions = -g_actions;
log(g_actions); // -50

let str_1: string = "03";
let num_1: number = +str_1; // Convert to number
num_1 = -num_1; // Negate the number
log(num1); // -3

let str_2: string = "1.4";
let num_2: number = +str_2; // Convert to number
num_2 = -num_2; // Negate the number
log(num_2); // -1.4

let str_3: string = "zaz";
let num_3: number = +str_3; // Convert to number (NaN)
num_3 = -num_3; // Negate the number (still NaN)
log(num_3); // NaN

let bool1: boolean = true;
let numBool1: number = +bool1; // Convert to number
numBool1 = -numBool1; // Negate the number
log(numBool1); // -1

let f_num1: number = 2.8; // Already a number
f_num1 = -f_num1; // Negate the number
log(f_num1); // -2.8

let obj1 = {
    valueOf() {
        return -5;
    }
};
let numObj1: number = +obj1; // Convert to number
numObj1 = -numObj1; // Negate the number
log(numObj1); // 5

// Increment/Decrement Operators
let numA: number = 10, numB: number = 5, numC: number, numD: number;
numC = numA++; // Post-increment
log(numC); // 10
log(numA); // 11
numC = ++numA; // Pre-increment
log(numC); // 12
log(numA); // 12
numD = numB--; // Post-decrement
log(numD); // 5
log(numB); // 4
numD = --numB; // Pre-decrement
log(numD); // 3
log(numB); // 3
numD++; // Increment
log(numD); // 4


// Bitwise Operators
/* Bitwise operators work with numbers at the bit level. When applied, a conversion occurs: 
the 64-bit number is converted to a 32-bit number, the operation is performed, and the result is stored back. */

// Bitwise NOT (~)
let n1: number = 25; // binary 00000000000000000000000000011001
let n2: number = ~n1; // binary 11111111111111111111111111100110
log(n2); // -26

// Bitwise AND (&)
let n3: number = 25 & 3;
log(n3); /* Logs: 1 because:
    25 = 0000 0000 0000 0000 0000 0000 0001 1001
     3 = 0000 0000 0000 0000 0000 0000 0000 0011
    ---------------------------------------------
   AND = 0000 0000 0000 0000 0000 0000 0000 0001   */



// Bitwise OR |
// A bitwise OR operation returns 1 if at least one bit is 1. It returns 0 only if both bits are 0.

n3 = 25 | 3; 
log(n3); // Logs: 27 because the comparison of both binary codes is:
                   // 25 = 0000 0000 0000 0000 0000 0000 0001 1001
                   // 3  = 0000 0000 0000 0000 0000 0000 0000 0011
                   // ---------------------------------------------
                   // OR = 0000 0000 0000 0000 0000 0000 0001 1011

// Bitwise XOR
// Bitwise XOR is different from bitwise OR in that it returns 1 only when exactly one bit has a value of 1 (if both bits contain 1, it returns 0).

n3 = 25 ^ 3;
log(n3); // Logs: 26 because the comparison of both binary codes is:
                   // 25 = 0000 0000 0000 0000 0000 0000 0001 1001
                   // 3  = 0000 0000 0000 0000 0000 0000 0000 0011
                   // ---------------------------------------------
                   // XOR = 0000 0000 0000 0000 0000 0000 0001 1010

// Left Shift
// The left shift is represented by two less-than signs (<<) and shifts all bits in a number to the left by the number of positions given.

let numb: number = 2; // 10 in binary code
let new_number: number = numb << 6; // 10000000 in binary code which is decimal 128
log(new_number); // 128

/* |1|         |0|       |0|       |0|       |0|        |0|       |0|      |0|
(2^7x1)  +  (2^6x0) + (2^5x0) + (2^4x0) + (2^3x0) + (2^2x0) + (2^1x0) + (2^0x0) // here ^ is a power
 128     +     0    +    0    +    0    +   0     +    0    +    0    +   0    = 128   */

// Signed Right Shift
// The signed right shift is represented by two greater-than signs (>>) and shifts all bits in a 32-bit number to the right while preserving the sign (positive or negative).

numb = 128; // 10000000 in binary code
new_number = numb >> 6; // 10 in binary code which is decimal 2
log(new_number); // 2

// Unsigned Right Shift
/* The unsigned right shift is represented by three greater-than signs (>>>) and shifts all bits in a 32-bit number to the right. 
For numbers that are positive, the effect is the same as a signed right shift. For negative numbers, unlike signed right shift, 
the empty bits get filled with zeros regardless of the sign of the number. */

numb = -64; // equal to binary 11111111111111111111111111000000
new_number = numb >>> 5; // equal to decimal 134217726
log(new_number); // 134217726
/* because the unsigned right shift treats this as a positive number, it considers the value to be
4294967232. When this value is shifted to the right by five bits, it becomes 00000111111111111111
111111111110, which is 134217726. */

/* Boolean operators */
// Logical NOT ! 
// can be used in any value. This operator always returns a Boolean value, regardless of the data type it’s used on. 
// The logical NOT operator first converts the operand to a Boolean value and then negates it.

log(!false); // true
log(!false); // true

// Using Boolean() to evaluate the truthiness of the string
log(!Boolean("shadow")); // false

log(!Boolean(0)); // true
log(!Boolean(NaN)); // true
log(!Boolean("")); // true
log(!Boolean(57344)); // false
log(!Boolean(null)); // true
log(!Boolean(undefined)); // true

//Note: Here we need to convert first to a Boolean to avoid ts(2872) error


// it can be used to transform a value into its boolean equivalent by using two NOT operators in a row

let girlname: string = 'Angy';
// name = !!girlname;
// log(name); // Logs: true

// Note: see that the first negates the
// value after converting it, the second just converts it to boolean.

// Logical AND &&
// It operates over two values and returns true if both values are true, false otherwise.
log(true && girlname); // Angy
log(false && 'Angy'); // false
log(4 < 5 && 8 > 6); // true
/* Logical AND can be used with any type of operand, not just Boolean values. When either operand is
not a primitive Boolean, logical AND does not always return a Boolean value; instead, it does one of the following:
➤ If the first operand is an object, then the second operand is always returned.
➤ If the second operand is an object, then the object is returned only if the first operand evaluates to true.
➤ If both operands are objects, then the second operand is returned.
➤ If either operand is null, then null is returned.
➤ If either operand is NaN, then NaN is returned.
➤ If either operand is undefined, then undefined is returned. */

// Logical OR ||
// It operates over two values and returns true if both or one of both values are true, false otherwise.
let empty: string = '';
log(false || empty); // Logs: <empty string>
log(girlname || empty); // Angy
log(4 >= 5 || 8 > 6); // true 

/* Just like logical AND, if either operand is not a Boolean, logical OR will not always return a Boolean value; instead, it does one of the following:
➤ If the first operand is an object, then the first operand is returned.
➤ If the first operand evaluates to false, then the second operand is returned.
➤ If both operands are objects, then the first operand is returned.
➤ If both operands are null, then null is returned.
➤ If both operands are NaN, then NaN is returned.
➤ If both operands are undefined, then undefined is returned. */

// Note: Both AND and OR are short-circuit operators, which means sometimes only the first operator is evaluated.

// Multiplicative Operators
/* There are three multiplicative operators in ECMAScript: multiply, divide, and modulus. 
These operators work similarly to their counterparts in languages such as Java, C, and Perl, 
but they also include automatic type conversions when dealing with non-numeric values. */

// Multiply Operator *
let number: number = 4 * Number('8'); // Explicitly convert the string to a number
log(number); // Logs: 32

// Alternatively, you can use the unary plus operator
let number_2: number = 4 * +'8'; // Using unary plus to convert the string to a number
log(number_2); // Logs: 32




// Divide Operator /
number = 10 / 5;
log(number); // Logs: 2
number = 4 / 40;
log(number); // Logs: 0.1 

// Modulus (remainder) Operator %
number = 41 % 5;
log(number); // Logs: 1

// Exponentiation Operator **
number = 4 ** 2;
log(number); // Logs: 16
// same as
log(Math.pow(4, 2)); // 16

// Add Operator +
number = 76 + 78;
log(number); // 154
log('76' + '78'); // 7678, on strings performs as a concatenator

let bigNumb = BigInt(767867686876876) + BigInt(6757575755);
log(bigNumb); // 767874444452631n

// Subtract -
number = 48 - 3;
log(number); // 45

// Note: These operators have a particular behavior in some cases when used with Infinity, 0, NaN, or non-numeric values; you should search if you want more information.

/* Relational Operators */
/* The less-than (<), greater-than (>), less-than-or-equal-to (<=), and greater-than-or-equal-to (>=) 
relational operators perform comparisons between values in the same way that you learned in math class. */
let computation: boolean = 76 < 4;
log(computation); // false
computation = 87 > 32;
log(computation); // true
computation = 43 <= 43;
log(computation); // true
computation = 44 >= 85;
log(computation); // false


//In TypeScript, when comparing values, it's important to ensure that the types are compatible to avoid unexpected behavior.
let user: { name: string } = {
    name: 'Clavin & Hobbes'
};

// Comparing user object with a number
log(user.name <= '4'); // false, comparing string to string

// Comparing strings
log("43" < "8"); // true, because string comparison is lexicographical
log(Number("43") < 8); // false, converting "43" to a number for comparison


log('DeepState' < 'real people'); // true, not only because there are more real people, but when we talk about strings, the upper characters have lower codes than the regular ones
log('DeepState'.toLowerCase() < 'real people'.toLocaleLowerCase()); // true again ... well ummm sometimes we win 

/* As with other operators in ECMAScript, there are some conversions and other oddities that happen
when using different data types. They are as follows:
➤ If the operands are numbers, perform a numeric comparison.
➤ If the operands are strings, compare the character codes of each corresponding character in
the string.
➤ If one operand is a number, convert the other operand to a number and perform a numeric
comparison.
➤ If an operand is an object, call valueOf() and use its result to perform the comparison
according to the previous rules. If valueOf() is not available, call toString() and use that
value according to the previous rules.
➤ If an operand is a Boolean, convert it to a number and perform the comparison. */

// Equality operators
// Determining whether two variables are equivalent is one of the most important operations in programming.

// Equal or Equality Operator ==
log(2 == Number('2')); // true

// Deep comparison, also compares types. Identically equal or Strict Equality Operator ===
log(2 === Number('2')); // true, explicitly converting '2' to a number
//Note: if we were using Javascript and avoiding to using the Number() build-in structure, the result were be diferent because types are diferent

// Not-equal or Inequality Operator !=
log(2 != Number('2')); // false

// Deep comparison, also compares types. Identically not-equal or Strict Inequality Operator !==
log(2 !== Number('2')); // false, explicitly converting '2' to a number. Same observation that the about deep comparation


/* When performing conversions, the equal and not-equal operators follow these basic rules:
➤ If an operand is a Boolean value, convert it into a numeric value before checking for
equality. A value of false converts to 0, whereas a value of true converts to 1.
➤ If one operand is a string and the other is a number, attempt to convert the string into a
number before checking for equality.
➤ If one of the operands is an object and the other is not, the valueOf() method is called on
the object to retrieve a primitive value to compare according to the previous rules.

The operators also follow these rules when making comparisons:
➤ Values of null and undefined are equal.
➤ Values of null and undefined cannot be converted into any other values for
equality checking.
➤ If either operand is NaN, the equal operator returns false and the not-equal operator
returns true. Important note: even if both operands are NaN, the equal operator returns
false because, by rule, NaN is not equal to NaN.
➤ If both operands are objects, then they are compared to see if they are the same object. If
both operands point to the same object, then the equal operator returns true. Otherwise,
the two are not equal. */

// in Javascript we can do something like: log(NaN !== NaN); // true
// NaN is not equal to itself
const isNotEqual: boolean = Object.is(NaN, NaN); // false
log(!isNotEqual); // true, because NaN is not equal to itself
//Note: We use the above structure to avoid ts(2845) error

// in Javascript we can do something like: log(true === 1); // false
// Comparing boolean true with number 1
const isTrueEqualToOne: boolean = (true as unknown as number) === 1; // true
log(isTrueEqualToOne); // true
//Note: We use the above structure to avoid ts(2367)

log(null == undefined); // true
log(null === undefined); // false

// Conditional Operator (condition) ? true : false;
/* This basically allows a conditional assignment to a variable depending on the evaluation of the
boolean_expression. If it’s true, then true_value is assigned to the variable; if it’s false, then
false_value is assigned to the variable. */

let login: string = (user.name == 'Nixon') ? `Successful login, Welcome ${user.name}` : "Sorry we don't have any user with that name";
log(login); // Sorry we don't have any user with that name

// Assignment Operators

let a: string = 'a';
a = a + a;
log(a); // aa

number = 8;

/* Compound assignment is done with one of the multiplicative, additive, or bitwise–shift operators
followed by an equal sign (=). These assignments are designed as shorthand for such common situations as: */

number *= number;
log(number); // 64

number -= 4;
log(number); // 60

/* Compound-assignment operators exist for each of the major mathematical operations and a few
others as well. They are as follows:
➤ Multiply/assign (*=)
➤ Divide/assign (/=)
➤ Modulus/assign (%=)
➤ Add/assign (+=)
➤ Subtract/assign (-=)
➤ Left shift/assign (<<=)
➤ Signed right shift/assign (>>=)
➤ Unsigned right shift/assign (>>>=)
These operators are designed specifically as shorthand ways of achieving operations. They do not
represent any performance improvement. */

// Membership Operators
// The in operator
let Crows: { description: string; age: number } = {
    description: "Mutant fat man lives beyond the margins of the known universe...",
    age: 600,
};

log('description' in Crows); // true
log('location' in Crows
); // false

// instanceof operator

class User {
    name: string;
    age: number;
    email: string;

    constructor(name: string, age: number, email: string) {
        this.name = name;
        this.age = age;
        this.email = email;
    }

    greeting(): string {
        return `Hi ${this.name}. Welcome to Roadmap Exercise #01.`;
    }
}

// Example usage of the User class
const userInstance = new User('Alice', 16, 'aliceinchain@gronch.com');
log(userInstance.greeting()); // Hi Alice. Welcome to Roadmap Exercise #01.

// Create a new User instance
const niko_zen = new User('Niko', 41, 'duendeintemporal@hotmail.com');
log(niko_zen.greeting()); // 'Hi Niko. Welcome to Roadmap Exercise #01'

// Check instance types
log(niko_zen instanceof User); // true
log(niko_zen instanceof Object); // true
// Function to check if a value is a Number object
function isNumberObject(value: any): value is Number {
    return value instanceof Number;
}
log(isNumberObject(4)); // false, because 4 is a primitive value
//Note: if we do: log(4 instanceof Number) like in Javascript it throw ts(2358) error

let four = new Number(4);
log(four instanceof Number); // true

// Type Operators
// Using instanceof and typeof
log(typeof true); // boolean
log(typeof NaN); // number
log(typeof niko_zen); // object 

// Destructuring Operations and Spread Operator
// For arrays
let books: string[] = ['Dune', 'Shibumi', 'El Maestro de Esgrima', 'El Perfume'];
let books2: string[] = ['Eloquent JavaScript', 'You Don’t Know JS ES6 Beyond', 'Linux Command Line An Admin Beginners Guide', 'Learn Bash the Hard Way', 'Programming Algorithms', 'MATLAB Notes for Professionals'];
const mix_books = [...books, ...books2];
const [frank_herbert, trevanian] = books;
log(trevanian); // Logs: Shibumi

// For objects
const { email } = niko_zen;
log(email); // duendeintemporal@hotmail.com

const niko_zen_settings = {
    mode: 'dark',
    avatar: 'moebius.svg',
    interfaz: 'compact',
};

const niko_zen_data = { ...niko_zen, ...niko_zen_settings };
log(niko_zen_data); // Logs both objects niko_zen instance and niko_zen_settings
/*
 {
  name: 'Niko',
  age: 41,
  email: 'duendeintemporal@hotmail.com',
  mode: 'dark',
  avatar: 'moebius.svg',
  interfaz: 'compact'
} */

function showUser({ name, age, email }: { name: string; age: number; email: string }) {
    log(`User name: ${name}, age: ${age}, email: ${email}`);
}

showUser(niko_zen); // Logs: User name: Niko, age: 41, email: duendeintemporal@hotmail.com

// Assign default values in destructuring
interface Config {
    font: string;
    mode?: string; // mode is optional
}

const config: Config = { font: 'monospace' };

const { font, mode = 'dark' } = config; // Default value for mode is 'dark'

//Note:  In TypeScript, if you are not explicitly defining types for the variables in the destructuring assignment, you can simply write the code without type annotations. In this case we create the Config interface to avoid ts(2339) error

log(font, mode); // monospace dark

// Exchange values between variables using destructuring
let ninja1 = 'Hiroshi';
let ninja2 = 'Neko';
let ninja3 = 'Kage';

[ninja1, ninja2, ninja3] = [ninja2, ninja3, ninja1];
log(ninja1); // Neko

// Copy objects or arrays without modifying the original
const shinobi = {
    skills: ['fast', 'quick', 'precise', 'lethal', 'computational thinking'],
    location: 'not found',
};

const trix = { ...shinobi };
trix.location = 'Bangkok, Thailand';

log(shinobi.location); // not found
log(trix.location); // Bangkok, Thailand

// Use spread operator to pass array elements as arguments in functions
const nums = [1, 3, 4, 5, 6];
log(Math.max(...nums)); // logs: 6

// Create a function to calculate the average
const calculateAverage = (...numbers: number[]) => {
    const total = numbers.reduce((sum, num) => sum + num, 0);
    return total / numbers.length;
};

// Call the function with multiple arguments
const average = calculateAverage(90, 76, 45, 23, 67);
log(average); // 60.2

// Convert a string into an array of its individual characters
let maximum = 'in a society that has abolished every kind of adventure, the only adventure that remains is abolishing the society';
let maxim_arr = [...maximum];
log(maxim_arr); // Logs the array of characters
/* [
  'i', 'n', ' ', 'a', ' ', 's', 'o', 'c', 'i', 'e', 't', 'y',
  ' ', 't', 'h', 'a', 't', ' ', 'h', 'a', 's', ' ', 'a', 'b',
  'o', 'l', 'i', 's', 'h', 'e', 'd', ' ', 'e', 'v', 'e', 'r',
  'y', ' ', 'k', 'i', 'n', 'd', ' ', 'o', 'f', ' ', 'a', 'd',
  'v', 'e', 'n', 't', 'u', 'r', 'e', ',', ' ', 't', 'h', 'e',
  ' ', 'o', 'n', 'l', 'y', ' ', 'a', 'd', 'v', 'e', 'n', 't',
  'u', 'r', 'e', ' ', 't', 'h', 'a', 't', ' ', 'r', 'e', 'm',
  'a', 'i', 'n', 's', ' ', 'i', 's', ' ', 'a', 'b', 'o', 'l',
  'i', 's', 'h', 'i',
  ... 14 more items */

// Comma Operator
// The comma operator allows execution of multiple operations in a single statement
let number1 = 1, number2 = 2, number3 = 3, number4: number;
log(number1, number2, number3, number4); // 1 2 3 undefined

// Using the comma operator in variable assignment
// this is valid in Javascript but in Typescript throw ts(2695) error: number = (225, 14, 40, 8, 220); // number becomes 220
//log(number); // 220
//Note: To avoid the warning TS(2695), it's best to avoid using the comma operator in this context.
// so we need to do a direct assign: 
number = 220;

// Flow Control Statements
// The if statement
if (number) {
    number += 4;
    log(number); // 224
}

// The else statement
if (number) {
    number += 4;
    log(number); // 228
} else {
    // Do something else
}

// The else if statement
// The else if statement
if (number > 300) {
    number += 4;
    log(number);
} else if (number > 200) {
    number += 4;
    log(number); // Logs: 232
} else {
    // Do something else
}

// The do-while statement
/* The do-while statement is a post-test loop, meaning that the escape condition is evaluated only after the code inside the loop has been executed. */
let count = 0;
do {
    log("I'm learning a lot in this roadmap for coders, even with these basic exercises");
    count++;
} while (count < 1);
// Logs: I'm learning a lot in this roadmap for coders, even with these basic exercises

// The while statement
// while (true) {
//     //Do something
//     //This creates an infinite loop as it always evaluates to true
// }

// The for statement
number = 0;
for (let i = 1; i <= 100; i++) {
    number += i;
}
log(number); // Logs: 5050

// The for-in statement
// Allows us to iterate over the properties of object elements
// Define an interface for the user
interface HideUser {
    name: string;
    age: number;
    location: string;
}

// Create a user object that adheres to the User interface
let user2: HideUser = {
    name: 'Nikita',
    age: 32,
    location: 'Not Found',
};

// Iterate over the properties of the user object
for (let key in user2) {
    if (user2.hasOwnProperty(key)) { // Check if the property belongs to the object itself
        log(key); // Logs only the property name
        log(key, user2[key as keyof HideUser]); // Logs the property and the value
        log(key, eval('user2.' + key)); // The same as before
    }
} /*  
name
name Nikita
name Nikita
age
age 32
age 32
location
location Not Found
location Not Found
 */

/* Object properties in ECMAScript are unordered, so the order in which property names are returned
in a for-in statement cannot necessarily be predicted. All enumerable properties will be returned
once, but the order may differ across browsers. */

// The for-of statement
// Designed to iterate over array elements
let oddNums = [1, 3, 5, 7, 9];

for (let num of oddNums) {
    log(num); // Logs each num
} /* 
1
3
5
7
9 */

// Using Object.entries(), Object.keys(), Object.values() to iterate over object properties
for (let [key, val] of Object.entries(user2)) {
    log(`${key}: ${val}`);
} /* 
name: Nikita
age: 32
location: Not Found */

// Label statements
outer_loop: for (let i = 0; i <= 10; i++) {
    inner_loop: for (let y = 0; y < 5; y++) {
        if ((i == 2) && (y == 4)) break outer_loop;
        if (y == 4) break inner_loop;
        log('Is there anybody out there?');
    }
} /* Logs: Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Is there anybody out there? */

// Break and continue statements
/* The break and continue statements provide stricter control over the execution of code in a loop.
The break statement exits the loop immediately, while the continue statement skips to the next iteration. */
number = 0;
while (number < 5) {
    if (number == 3) break;
    log(number);
    number++;
} // Logs: 0 1 2

number = 0;
while (number < 5) {
    if (number == 3) {
        number++;
        continue;  
    }
    log(number);
    number++;
} // Logs: 0 1 2 4

// The with Statement
/* The with statement was created for convenience when repeatedly accessing properties of a single object. 
However, it is generally discouraged in modern JavaScript and Tyscript due to potential readability and performance issues. */
// with (user) {
//     log(name); // Nikita
//     log(age); // This would throw an error because age is undefined in this context
// }
//Note: This structure is not allowed in Typescript


// The Switch Statement
switch (user.name) {
    case 'Nikita': 
        log('Welcome agent');
        break;
    case 'Calvin & Hobbes': 
        log('Bring me some cookies');
        break;
    default: 
        log('Turn off that TV'); // This will log because the second case is missing
}

// Using an expression that evaluates a string concatenation in a case
/*
let num = 25;
switch (true) {
    case num < 0:
        log("Less than 0.");
        break;
    case num >= 0 && num <= 10:
        log("Between 0 and 10.");
        break;
    case num > 10 && num <= 20:
        log("Between 10 and 20.");
        break;
    default:
        log("More than 20.");
}
*/

// Extra difficulty Exercise: Create a program that prints the even numbers from 10 to 55 inclusive,
// avoiding printing the numbers if they are equal to 16 or multiples of 3
for (let i = 10; i <= 55; i++) {
    if (i % 3 == 0 || i == 16) continue
    if (i % 2 == 0) {
        log(i); // Log the even number
    }
}

