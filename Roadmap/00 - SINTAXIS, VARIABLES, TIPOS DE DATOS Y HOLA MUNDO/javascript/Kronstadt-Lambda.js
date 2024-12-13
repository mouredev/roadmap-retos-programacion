// https://developer.mozilla.org/en-US/docs/Web/JavaScript

// * Syntax to create comments in JavaScript
// Single line comments like this
/* Multi-line comments
like this */
/**
 * Documentation comments
 * like this
 * @author Kronstadt
 */

// * Syntax to manage punctuation in JavaScript
// ; (semicolon) is used to separate statements. It is optional in JavaScript but it is a good practice to use it.
// , (comma) is used to separate items in a arrays, elements in objects and parameters in functions.
// . (dot) is used to access properties and methods of objects.
// : (colon) is used to separate keys and values in objects. Too, it is used in ternary operator.
// () (parentheses) are used to define parameters in functions, to group expressions and to call functions.
// [] (brackets) are used to define arrays, to access elements in arrays and objects.
// {} (braces) are used to define objects and blocks of code like in loops and conditionals.
// "" (double quotes) and '' (simple quotes) are used to define strings.
// `` (backticks) are used to define template literals.

// * Variables and constants in JavaScript
let variable_string = 'value'; // Declares a variable with a value
let variable_number = 1; // Declares a variable with a number
let variable_boolean = true; // Declares a variable with a boolean
let variable_array = [1, 2, 3]; // Declares a variable with an array
let variable_object = { key: 'value' }; // Declares a variable with an object
let variable_undefined; // Declares a variable without a value

const constant_string = 'value'; // Declares a constant with a value
const constant_array = [1, 2, 3]; // Declares a constant with an array
const constant_object = { key: 'value' }; // Declares a constant with an object
const constant_undefined = undefined; // Declares a constant with a value of undefined
// Note: It does not define a constant value. IT DEFINES A CONSTANT REFERENCE TO A VALUE.
// Note: var is an old way to declare variables in JavaScript. It is not recommended to use it.

// Best practices:
// 1. Always declare variables
// 2. Always use const if the value should not be changed
// 3. Always use const if the type should not be changed (Arrays and Objects)
// 4. Only use let if you can't use const
// 5. Only use var if you MUST support old browsers.

// * Primitive data types in JavaScript
// String: Represents a sequence of characters.
const string = 'Hello, World!';
// Number: Represents a number.
const number = 42;
// BigInt: Represents a number that can store big integers with arbitrary precision.
const bigInt = 9007199254740991n;
// Boolean: Represents a logical entity and can have two values: true or false.
const boolean = true;
// Symbol: Represents a unique values and inmutable data type that may be used as an identifier for object properties.
const symbol = Symbol('description');
// Undefined: Represents an undefined value. This means that the variable has not been assigned a value.
let undefinedValue; 
// Null: Represents an intentional absence of any object value.
const nullValue = null;

console.log("A string:", string, ", typeof:", typeof string);
console.log("A number:", number, ", typeof:", typeof number);
console.log("A BigInt:", bigInt, ", typeof:", typeof bigInt);
console.log("A boolean:", boolean, ", typeof:", typeof boolean);
console.log("A symbol:", symbol, ", typeof:", typeof symbol);
console.log("An undefined value:", undefinedValue, ", typeof:", typeof undefinedValue);
console.log("A null value:", nullValue, ", typeof:", typeof nullValue); // Note: typeof null returns 'object'.

// * Print a greeting
const language = "JavaScript";
console.log(`Hello, ${language}!`);

// Style guide:
/*
1. Nomenclature:
- Use camelCase for variables and functions.
- Use PascalCase for classes.
- Use UPPERCASE for constants.
2. Indentation:
- Use 2 spaces for indentation.
3. Comentaries:
- Use // above the code to comment.
- Use /* to comment a block of code.
- Use /** JSDoc comments to document functions, methods and classes.
4. Code organization:
- Group `imports` at the top of the file.
- Group `constants` next.
- Group `variables` next.
- Group `functions` next.
- Group `classes` next.
*/
