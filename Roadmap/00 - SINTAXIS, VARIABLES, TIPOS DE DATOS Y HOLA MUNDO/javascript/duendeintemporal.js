//It seems to me that there is no official language page, however I leave two reference links
//The first to a documentation of language as such: https://lenguajejs.com/
/*The second is an ECMAScript documentation, the standard set for the language: https://262.ecma-international.org/12.0/ Note: There is a more current specification: https://ecma-international.org/publications-and-standards/standards/ecma-262/ */

// One-line comments 
/* Comments
                of
                     many lines */

var num; /* It declares a variable, is deprecated as its scope definition gives way to potential errors. Has a defined scope at the function level */


let lang; /* It is most commonly used and has a defined scope at the block level.
Unlike the var keyword, when declaring variables using let in the global context, variables will not
attach to the window object as they do with var. */

const MIN_VA=0; /* Like the previous one, it has a scope defined in block, but it declares a constant and must be initialized at some value. By convention, capital letters are usually used */


// Primitive Types or Primitive Values

let hello='Hi Girl!'; // string type
console.log(`String type: ${hello}`);

let x_coord=100; // number type
console.log('Number type: ', num);

let bool=true; // boolean type
console.log('Boolean type: ', bool);

let stack=[0,1,2,3,4,5,6]; // array type
console.log('Array type: ', stack);

let obj={
    name:'Niko',
    age:41,
    profession: 'Writer & Web Developer',

  // method
    greetings: function(){
        console.log(`Hello I am ${this.name} and it's a pleasure to start and share this roadmap with you`) }
} // object type
console.log('Object type: ', obj);
obj.greetings();

let obj2=null; // null type
/* Representing the absence of a value helps to handle situations where a value is not available or has not been intentionally defined. */
console.log('Null type: ', obj2);

let obj3; // undefined type
/* undefined is a value that indicates that a variable has been declared but not initialized. */
console.log('Undefined type: ', obj3);

let syn=Symbol('syn'); // symbol type
console.log('Symbol type: ', syn);// Symbol can't be converted to string
/* Symbols can be used to prevent object collisions, such as to create hidden non-enumerable properties on objects or private methods in a class */

let amount=BigInt(3783787487877877887)*BigInt(2); //bigint type
console.log(`BigInt type: ${amount}`);
/* Using BigInt is especially useful in situations where accuracy is required in calculations with large integers, such as in financial or crypto applications. */


/* Typeof is an operator that we can use to figure out a type or make type comparisons */
console.log('Type of syn:', typeof syn);
console.log('Is amount of bigint type:', (typeof amount == "bigint"));

// short for console.log()
let log=console.log.bind(console);

// mapping to a previously declared variable
lang='JavaScript';

//print in console
log(`Hello, ${lang}`);