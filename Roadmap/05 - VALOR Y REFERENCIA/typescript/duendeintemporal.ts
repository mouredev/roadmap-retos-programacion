//#5 { Retosparaprogramadores } Valor y Referencia
// I use GPT and deepseek for translation. generate comments an also as a reference.

let log = console.log;

//Variables by Value

/*Primitive data types in JavaScript (such as number, string, boolean, null, undefined, and symbol) are assigned by value. This means that when you assign a primitive value to a variable, a copy of that value is made.*/

let a: number = 44; // a is a number (primitive type)
let b: number = a;  // b is assigned the value of a

log(a); //  44
log(b); //  44

b += 20; // Changing b does not affect a
log(a); //  44
log(b); //  64

//Variables by Reference

/*Reference data types in JavaScript (such as object, array, and function) are assigned by reference. This means that when you assign an object to a variable, you are actually assigning a reference to that object, not a copy of it.*/


let obj1: { name: string, age?: number } = { name: "Julia" }; // obj1 is an object (reference type)
let obj2: { name: string, age?: number } = obj1; // obj2 is assigned the reference of obj1

log(obj1.name); //  Julia
log(obj2.name); //  Julia

obj2.name = "Karla"; // Changing obj2 affects obj1 because they reference the same object
log(obj1.name); //  Karla
log(obj2.name); //  Karla

obj2.age = 32;
log(obj2.age)// 32
log(obj1.age)// 32

//Arrays (Reference Type) in JavaScript are also reference types.

let arr1: number[] = [7, 4, 90]; // arr1 is an array (reference type)
let arr2: number[] = arr1; // arr2 is assigned the reference of arr1

log(arr1); //  [7, 4, 90]
log(arr2); //  [7, 4, 90]

arr2.push(42); // Modifying arr2 affects arr1
log(arr1); //  [7, 4, 90, 42]
log(arr2); //  [7, 4, 90, 42]

/*    By Value: Primitive types (e.g., number, string) are copied when assigned to a new variable.
    By Reference: Reference types (e.g., object, array) are assigned by reference, meaning changes to one variable affect the other if they reference the same object. */

  /*  In JavaScript, functions are also treated as first-class objects, which means they can be assigned to variables, passed as arguments, and returned from other functions. When you assign a function to a variable, you are assigning a reference to that function, not a copy of it. Here are some examples to illustrate how functions work with reference: */
    
    //Functions Assigned by Reference
    
    //When you assign a function to a new variable, both variables point to the same function in memory.
        
    function greet(): void {
        log("Hello everybody! is time for coding...");
    }
    
    let greetCopy: Function = greet; // greetCopy is assigned the reference of greet
    
    greet();      // Hello everybody! is time for coding...
    greetCopy();  // Hello everybody! is time for coding...
    
    // Changing the function reference
    greetCopy = function(): void {
        log("This world is turning into a weird scenario with all those AIs, M2M (technology), and there are cyber attacks that can explode beepers, cell phones, and a big media that shows only a tiny fragment of reality. ");
    };
    
    greet();      // Hello everybody! is time for coding...
    greetCopy();  //This world is turning into a weird scenario with all those AIs, M2M (technology), and there are cyber attacks that can explode beepers, cell phones, and big media that shows only a tiny fragment of reality.
    
    // Passing Functions as Arguments
    
    //You can pass functions as arguments to other functions. This demonstrates that functions are treated as reference types.
    
       
    function callFunct(fn): void {
        fn();
    }
    
    function sayByeLady(): void {
        log("See you later, lady!");
    }
    
    callFunct(sayByeLady); // See you later, lady
    
    //Returning Functions from Functions
    
    //You can also return functions from other functions, which shows that functions can be created dynamically and assigned by reference.
    
        
    function saySomethingTo(greeting): Function {
        return function(name: string): void {
            log(`${greeting}, ${name}!`);
        };
    }
    
    let say: Function = saySomethingTo("Wellcome to coding lab");
    let say2: Function = saySomethingTo("Is a long way home");
    
    say("Nicky"); // Wellcome to coding lab, Nicky
    say2("Jhon");      // Is a long way home, Jhon
    
    //  Modifying Functions
    
    //Since functions are reference types, if you modify a function that is referenced by multiple variables, it will affect all references.
    
// Define a type for the function to make it reusable and explicit
type GreetingFunction = () => any;
// Note: I decide to use 'any' type for the porpouse of show a possibility of use a Immediately Invoked Function Expression (IIFE) later, but have more sanse 'void' type. 

// Original function (use `let` instead of `const` to allow reassignment)
let hiMiss: GreetingFunction = () => {
    console.log("Hello, miss. Have a beautiful day");
};

// Assign the function reference
let funcRef: GreetingFunction = hiMiss;

// Call the function reference
funcRef(); // Output: Hello, miss. Have a beautiful day

// Modify the original function
hiMiss = (): void => {
    console.log("Sometimes I feel jealous of the wind that caresses your hair, sometimes the rain....");
};

// Call the function reference again
funcRef(); // Output: Hello, miss. Have a beautiful day (still points to the original function)

// Define funcRef as a higher-order function that returns a GreetingFunction
funcRef = (): GreetingFunction => {
    return hiMiss;
};

// Call the higher-order function and then invoke the returned function
(funcRef())(); // Output: Sometimes I feel jealous of the wind that caresses your hair, sometimes the rain....

/*  In JavaScript, when you pass arguments to a function, the behavior depends on whether the argument is a primitive type (passed by value) or a reference type (passed by reference). Here’s an example that demonstrates both concepts:  */
      

// Function that takes a primitive type (passed by value)
function doSomething(value: any): void {
    value = 20; // This change does not affect the original variable
    log("Value Inside doSomething:", value); // Value Inside doSomething: 20
}

// Testing the functions
let val: string = 'something';
log("Value Before doSomething:", val); // Value Before doSomething: something
doSomething(val); // Value Inside setUserName: 20
log("After doSomething:", val); // After doSomething: something (remains unchanged)

// Function that takes an object (passed by reference)
function setUserName(obj: { name: string, age: number }, name: string) {
    obj.name = name; // This change affects the original object
    log("Value Inside setUserName:", obj.name); 
}

let user: { name: string, age: number } = { name: "Luna", age: 32 };
log("Before setUserName:", user.name); // Before setUserName: Luna
setUserName(user, 'Kia'); // Value Inside setUserName: Kia
log("After setUserName:", user.name); // After setUserName: Kia (changed)

//Note: the same apply to arrays that are reference values.

    log( 'Retosparaprogramadores #5'); // Retosparaprogramadores #5 



/* EXTRA DIFFICULTY (optional):

    Create two programs that receive two parameters (each) defined as variables previously.
    One program receives, in one case, two parameters by value, and in another case, by reference.
    These parameters are swapped between each other internally, returned, and their return values are assigned to two variables different from the originals. Then, print the value of the original variables and the new ones, checking that their values have been inverted in the second set.
    Also verify that the original values have been preserved in the first set.
 */

let user1: { name: string, age: number } = {
    name: 'Kasperle',
    age: 12
}

let user2: { name: string, age: number } = {
    name: 'Snoopy',
    age: void(0)
}

log('user1: ', user1);// user1: Object { name: "Kasperle", age: 12 }
log('user2: ', user2);// user2: Object { name: "Snoopy", age: undefined }

function changeUser(obj1: { name: string, age: number }, obj2: { name: string, age: number }): void {
   const provisional = {};
    Object.assign(provisional, obj1);// Object.assign allow a deep copy
    Object.assign(obj1, obj2);
    Object.assign(obj2, provisional);
   // return [obj1, obj2] 
   // We can return the objects in an array, but it becomes unnecessary because objects are treated as reference values. Therefore, the function will affect the original objects directly.
}

changeUser(user1, user2)

log('user1: ', user1);// user1: Object { name: "Snoopy", age: undefined }
log('user2: ', user2);// user2: Object { name: "Kasperle", age: 12 }

function swapValues(a: number, b: number) {
    return { a: b, b: a }; // Return an object with swapped values
}

let x: number = 85;
let y: number = 17;

console.log("Before swap: ", x, y); // Before swap: 85 17

// Declare `d` and `e` before using them in destructuring
let d: number, e: number;
// Call the function and destructure the returned object into new variables
({ a: d, b: e } = swapValues(x, y));

console.log("After swap: ", x, y); // After swap: 85 17 (original values preserved)
console.log("New variables with values swapped: ", d, e); // New variables with values swapped: 17 85

// Now, swap the values in place by updating the original variables
console.log("Before swap: ", x, y); // Before swap: 85 17
({ a: x, b: y } = swapValues(x, y));

console.log("After swap: ", x, y); // After swap: 17 85 (original values updated)

/*
 * Note: Destructuring allows us to achieve both effects:
 * - Preserving original values by assigning swapped values to new variables.
 * - Swapping values in place by updating the original variables.
 *
 * Note 2: Destructuring creates a shallow copy. If objects are nested, the nested objects are not copied.
 */