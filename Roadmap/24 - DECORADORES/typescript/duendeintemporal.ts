//#24 { retosparaprogramadores } - PATRONES DE DISEÑO: DECORADORES
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
*/

/* Explanation Note for Decorators(from DeepSeek): 
What Are Decorators?

Decorators are special functions that can be attached to classes, methods, properties, or parameters. 
They are prefixed with the @ symbol and are executed at runtime when the class or method is defined.

TypeScript supports the following types of decorators:

    Class Decorators: Applied to a class.

    Method Decorators: Applied to a method.

    Property Decorators: Applied to a property.

    Parameter Decorators: Applied to a parameter of a method.
    
    Why Use Decorators?

    Separation of Concerns: Decorators allow you to add functionality (e.g., logging, validation)
     without modifying the core logic of your classes or methods.

    Reusability: You can reuse decorators across multiple classes or methods.

    Readability: Decorators make it clear what additional behavior is being applied to a class or method.

    Metadata: Decorators can be used to attach metadata to classes or methods, which can be used later 
    (e.g., for dependency injection frameworks).

    When to Use Decorators?

    Logging: Automatically log method calls or property changes.

    Validation: Validate inputs or properties.

    Dependency Injection: Mark classes or properties for automatic injection.

    Metadata: Attach metadata for frameworks or libraries.

    Performance Monitoring: Measure execution time of methods.
    */

let log = console.log;

// Conditional check for browser environment
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #24.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #24. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #24');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #24');
}

/* 
The decorator pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. In TypeScript, decorators can be implemented using higher-order functions.
*/

// Generic decorator function
function decorator(fn: (...args: any[]) => void) {
    return function(...args: any[]): void {
        log("Before calling the function");
        const result = fn(...args);
        log("After calling the function");
        return result;
    };
}

// Decorator to log execution time
function logExecutionTime(fn: (...args: any[]) => Promise<any>) {
    return async function(...args: any[]): Promise<any> {
        const start = performance.now(); // Start time
        const result = await fn(...args); 
        const end = performance.now(); // End time
        log(`Execution time for ${fn.name}: ${end - start} milliseconds`);
        return result; 
    };
}

// Example function that simulates a time-consuming task
function fetchData(): Promise<string> {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Data fetched!");
        }, 3000);
    });
}

// Decorated function
const loggedFetchData = logExecutionTime(fetchData);

// Using the decorated function
loggedFetchData().then(result => log(result)); 
// Data fetched!Execution time for fetchData: 3164.9740999999995 milliseconds
// Data fetched!

// EXTRA DIFICULTY EXERCISE

// Decorator to count function calls
function countCalls(fn: (...args: any[]) => any) {
    let callCount = 0; // Private variable to keep track of calls through closure

    return function(...args: any[]): any {
        callCount++; 
        log(`Function has been called ${callCount} times.`);
        return fn(...args); 
    };
}

// Original function
function hiGirl(): string {
    log('Hi Girl! 🌹');
    return '🌼';
}

// Decorated function
const countedHiGirl = countCalls(hiGirl);

// Using the decorated function
log(countedHiGirl()); // Function has been called 1 times. Hi Girl! 🌹
// 🌼
log(countedHiGirl()); // Function has been called 2 times. Hi Girl! 🌹
// 🌼
log(countedHiGirl()); // Function has been called 3 times. Hi Girl! 🌹
// 🌼

/* 
NOTE: When you define a function inside another function, the inner function creates a private scope. This means that the inner function has access to the variables and parameters of the outer function, but those variables are not accessible from outside the outer function. This is a key feature of closures in JavaScript.

Explanation of Private Scope with Closures
In the context of the decorator pattern, this private scope allows us to maintain state (like the callCount in the counting decorator) without exposing it to the outside world. Here’s a breakdown of how this works:

Closure: When the inner function is returned from the outer function, it retains access to the outer function's variables. This is known as a closure. The inner function can use and modify these variables even after the outer function has finished executing.
Private Variables: Variables defined in the outer function (like callCount) are not accessible from outside the function. This means that you cannot directly modify or read callCount from outside the countCalls function, which effectively makes it private.
*/
