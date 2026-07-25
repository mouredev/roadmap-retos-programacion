//#24 - PATRONES DE DISEÑO: DECORADORES
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
*/

let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #24.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #24. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #24'); 
});


/* The decorator pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. In JavaScript, decorators can be implemented using higher-order functions. */

// Generic decorator function
function decorator(fn) {
    return function(...args) {
        log("Before calling the function");
        const result = fn(...args);
        log("After calling the function");
        return result;
    };
}

// Decorator to log execution time
function logExecutionTime(fn) {
    return async function(...args) {
        const start = performance.now(); // Start time
        const result = await fn(...args); 
        const end = performance.now(); // End time
        log(`Execution time for ${fn.name}: ${end - start} milliseconds`);
        return result; 
    };
}

// Example function that simulates a time-consuming task
function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Data fetched!");
        }, 3000);
    });
}

// Decorated function
const loggedFetchData = logExecutionTime(fetchData); // Execution time for fetchData: 10732 milliseconds

//Note: the fetchData() has delate of 3 seconds so the previus msj will be logged at the end after that time.

// Using the decorated function
loggedFetchData().then(result => log(result)); // Data fetched!


//EXTRA DIFICULTY EXERCISE

// Decorator to count function calls
function countCalls(fn) {
    let callCount = 0; // Private variable to keep track of calls through closure

    return function(...args) {
        callCount++; 
        log(`Function has been called ${callCount} times.`);
        return fn(...args); 
    };
}

// Original function
function hiGirl() {
    log('Hi Girl! \uD83C\uDF39');
    return '\uD83C\uDF3C';
}

// Decorated function
const countedhiGirl = countCalls(hiGirl);

// Using the decorated function
log(countedhiGirl()); // Function has been called 1 times. Hi Girl! 🌹 
log(countedhiGirl()); // Function has been called 2 times. Hi Girl! 🌹
log(countedhiGirl()); // Function has been called 3 times. Hi Girl! 🌹

// Trying to access countedhiGirl directly will result in an error
// log(countedhiGirl); // Uncaught ReferenceError: countedhiGirl is not defined



/* NOTE: When you define a function inside another function, the inner function creates a private scope. This means that the inner function has access to the variables and parameters of the outer function, but those variables are not accessible from outside the outer function. This is a key feature of closures in JavaScript.

Explanation of Private Scope with Closures
In the context of the decorator pattern, this private scope allows us to maintain state (like the callCount in the counting decorator) without exposing it to the outside world. Here’s a breakdown of how this works:

Closure: When the inner function is returned from the outer function, it retains access to the outer function's variables. This is known as a closure. The inner function can use and modify these variables even after the outer function has finished executing.
Private Variables: Variables defined in the outer function (like callCount) are not accessible from outside the function. This means that you cannot directly modify or read callCount from outside the countCalls function, which effectively makes it private.*/