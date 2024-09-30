//Exercice #5 Valor y Referencia
// I use GPT for translation. generate comments an also as a reference.

let log = console.log.bind(console);

//Variables by Value

/*Primitive data types in JavaScript (such as number, string, boolean, null, undefined, and symbol) are assigned by value. This means that when you assign a primitive value to a variable, a copy of that value is made.*/

let a = 44; // a is a number (primitive type)
let b = a;  // b is assigned the value of a

log(a); //  44
log(b); //  44

b += 20; // Changing b does not affect a
log(a); //  44
log(b); //  64

//Variables by Reference

/*Reference data types in JavaScript (such as object, array, and function) are assigned by reference. This means that when you assign an object to a variable, you are actually assigning a reference to that object, not a copy of it.*/


let obj1 = { name: "Julia" }; // obj1 is an object (reference type)
let obj2 = obj1; // obj2 is assigned the reference of obj1

log(obj1.name); //  Julia
log(obj2.name); //  Julia

obj2.name = "Karla"; // Changing obj2 affects obj1 because they reference the same object
log(obj1.name); //  Karla
log(obj2.name); //  Karla

obj2.age = 32;
log(obj2.age)// 32
log(obj1.age)// 32

//Arrays (Reference Type) in JavaScript are also reference types.

let arr1 = [7, 4, 90]; // arr1 is an array (reference type)
let arr2 = arr1; // arr2 is assigned the reference of arr1

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
        
    function greet() {
        log("Hello everybody! is time for coding...");
    }
    
    let greetCopy = greet; // greetCopy is assigned the reference of greet
    
    greet();      // Hello everybody! is time for coding...
    greetCopy();  // Hello everybody! is time for coding...
    
    // Changing the function reference
    greetCopy = function() {
        log("This world is turning into a weird scenario with all those AIs, M2M (technology), and there are cyber attacks that can explode beepers, cell phones, and a big media that shows only a tiny fragment of reality. ");
    };
    
    greet();      // Hello everybody! is time for coding...
    greetCopy();  //This world is turning into a weird scenario with all those AIs, M2M (technology), and there are cyber attacks that can explode beepers, cell phones, and big media that shows only a tiny fragment of reality.
    
    // Passing Functions as Arguments
    
    //You can pass functions as arguments to other functions. This demonstrates that functions are treated as reference types.
    
       
    function callFunct(fn) {
        fn();
    }
    
    function sayByeLady() {
        log("See you later, lady!");
    }
    
    callFunct(sayByeLady); // See you later, lady
    
    //Returning Functions from Functions
    
    //You can also return functions from other functions, which shows that functions can be created dynamically and assigned by reference.
    
        
    function saySomethingTo(greeting) {
        return function(name) {
            log(`${greeting}, ${name}!`);
        };
    }
    
    let say = saySomethingTo("Wellcome to coding lab");
    let say2 = saySomethingTo("Is a long way home");
    
    say("Nicky"); // Wellcome to coding lab, Nicky
    say2("Jhon");      // Is a long way home, Jhon
    
    //  Modifying Functions
    
    //Since functions are reference types, if you modify a function that is referenced by multiple variables, it will affect all references.
    
    function hiMiss() {
        log("Hello, miss. Have a beautiful day");
    }
    
    let funcRef = hiMiss; // funcRef points to hiMiss
    
    funcRef(); //  Hello, miss, have a beautiful day
    
    // Modifying the original function
    hiMiss = function() {
        log("Sometimes I feel jealous of the wind that caresses your hair, sometimes the rain....");
    };
    
    funcRef(); //  Hello, miss, have a beautiful day (still points to the original function)

    //but if we fro example...
    funcRef = ()=>{
     return hiMiss;
    }

    funcRef()()// Sometimes I feel jealous of the wind that caresses your hair, sometimes the rain.... (now every change in hiMiss will be reflexted)
    

/*  In JavaScript, when you pass arguments to a function, the behavior depends on whether the argument is a primitive type (passed by value) or a reference type (passed by reference). Here’s an example that demonstrates both concepts:  */
      

// Function that takes a primitive type (passed by value)
function doSomething(value) {
    value = 20; // This change does not affect the original variable
    log("Value Inside doSomething:", value); // Value Inside doSomething: 20
}

// Function that takes an object (passed by reference)
function setUserName(obj, name) {
    obj.name = name; // This change affects the original object
    log("Value Inside setUserName:", obj.name); 
}

// Testing the functions
let num = 'something';
log("Value Before doSomething:", num); // Value Before doSomething: something
doSomething(num);
log("After doSomething:", num); // After doSomething: something (remains unchanged)

let user = { name: "Luna", age: 32 };
log("Before setUserName:", user.name); // Before setUserName: Luna
setUserName(user, 'Kia'); // Value Inside setUserName: Kia
log("After setUserName:", user.name); // After setUserName: Kia (changed)

//Note: the same apply to arrays that are reference values.

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #5.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #5. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #5'); // this will be logged at the end cause the nature of window event
});


/* EXTRA DIFFICULTY (optional):

    Create two programs that receive two parameters (each) defined as variables previously.
    One program receives, in one case, two parameters by value, and in another case, by reference.
    These parameters are swapped between each other internally, returned, and their return values are assigned to two variables different from the originals. Then, print the value of the original variables and the new ones, checking that their values have been inverted in the second set.
    Also verify that the original values have been preserved in the first set.
 */

let user1 = {
    name: 'Kasperle',
    age: 12
}

let user2 = {
    name: 'Snoopy',
    age: void(0)
}

log('user1: ', user1);// user1: Object { name: "Kasperle", age: 12 }
log('user2: ', user2);// user2: Object { name: "Snoopy", age: undefined }

function changeUser(obj1, obj2) {
   const provisional = {};
    Object.assign(provisional, obj1);// Object.assign allow a deep copy
    Object.assign(obj1, obj2);
    Object.assign(obj2, provisional);
   // return [obj1, obj2] 
   // We can return the objects in an array, but it becomes unnecessary because objects are treated as reference values. 
   // Therefore, the function will affect the original objects directly.
}

changeUser(user1, user2)

log('user1: ', user1);// user1: Object { name: "Snoopy", age: undefined }
log('user2: ', user2);// user2: Object { name: "Kasperle", age: 12 }

function swapValues(a, b) {
    return { a: b, b: a };    // using destructuring to return the swapped values as an object
}

//You can call the function and use destructuring to assign the returned values to new variables:

let x = 85;
let y = 17;

log("Before swap: ", x, y);// Before swap: 85 17

// Call the function and destructure the returned object
({ a: d, b: e } = swapValues(x, y));

log("After swap: ", x, y);// After swap:  85 17
log('new variables with values swapped: ', d, e)// new variables with values swapped: 17 85

//Note: destructuring allow us to achive the effect of reference values with primitive values. Say using destructuring we can achive both effects. Conserving the originals values or swapping the values.
log("Before swap: ", x, y);// Before swap:  85 17
({ a: x, b: y } = swapValues(x, y));

log("After swap: ", x, y);// After swap: 17 85


//Note: using destructuring we can achive both effects. Conserving the originals values or swapping the values

//Note2: have in mind that when you use destructuring you make a shallow copy, it means that if are object nested inside, the nested ones don't be copied