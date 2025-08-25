/* { RETOS DE PROGRAMACIÓN }  #13 PRUEBAS UNITARIAS */
// I refer to "JavaScript Notes for Professionals" from the people of Stack Overflow. https://goalkicker.com/JavaScriptBook
// Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

// Short for console.log
let log = console.log;

// Welcome message
log('Welcome to the road of unit testing and error handling!');
// Welcome to the road of unit testing and error handling!

// Conditional check for browser environment
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #13.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #13. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #13');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    // This code is designed to run in a browser environment. Skipping window-related code.
    log('Retosparaprogramadores #13');  // Retosparaprogramadores #13
}

/* GoalKicker.com – JavaScript® Notes for Professionals 219
Section 30.9: Debugging with assertions - console.assert() Writes an error message to the console if the assertion is false. Otherwise, if the assertion is true, this does nothing. */

// Demonstrate console.assert with intentional type mismatch
console.assert('one' === String(1), 'Assertion failed: "one" is not equal to "1"');
// Assertion failed: Assertion failed: "one" is not equal to "1"

// Multiple arguments can be provided after the assertion–these can be strings or other objects–that will only be printed if the assertion is false:
console.assert(true, 'Testing assertion...', null, undefined, Object);
// Assertion failed: Testing assertion... null undefined [Function: Object]

console.assert(false, 'Testing assertion...', null, undefined, Object);
// Assertion failed: Testing assertion... NaN undefined function Object() { [native code] }

/* console.assert does not throw an AssertionError (except in Node.js), meaning that this method is incompatible with most testing frameworks and that code execution will not break on a failed assertion. */

// Custom assert function that logs an error instead of throwing
const assert = (condition: boolean, message: string, errors: string[]): void => {
    if (!condition) {
        console.error(message);
        errors.push(message);
    }
};

// Function to test
const sum = (a: number, b: number): number => {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    return a + b;
};

// Test cases for the sum function
const testSum = (errors: string[]): void => {
    try {
        assert(sum(2, 3) === 5, `Error: Expected 5 but got ${sum(2, 3)}`, errors);
        assert(sum(-1, 1) === 0, `Error: Expected 0 but got ${sum(-1, 1)}`, errors);
        assert(sum(0, 0) === 0, `Error: Expected 0 but got ${sum(0, 0)}`, errors);
        assert(sum(1.1, 2.2) === 3.3, `Error: Expected 3.3 but got ${sum(1.1, 2.2)}`, errors);
        assert(sum(Infinity, 1) === Infinity, `Error: Expected Infinity but got ${sum(Infinity, 1)}`, errors);
        assert(isNaN(sum(NaN, 1)), `Error: Expected NaN but got ${sum(NaN, 1)}`, errors);

        // Intentionally trigger an error (commented out to avoid crashing)
        // sum(2, '3'); // Uncommenting this will throw a TypeError: Both arguments must be numbers
    } catch (e: unknown) {
        if (e instanceof TypeError) {
            console.error('Caught an error:', e.message);
            assert(e instanceof TypeError, 'Error: Invalid argument type not handled', errors);
            assert(e.message === 'Both arguments must be numbers', 'Error: Argument type mismatch', errors);
        }
    }

    log('All sum tests have been executed.');
};

// Define a type for the personalInfo object
interface PersonalInfo {
    name: string;
    age: number;
    birth_date: string;
    programming_languages: string[];
}

// Object to test
const personalInfo: PersonalInfo = {
    name: "Niko Zen",
    age: 41,
    birth_date: "1983/08/08",
    programming_languages: ["JavaScript", "Python", "Rust", "Ruby", "Java"]
};

// Test cases for the personalInfo object
const testPersonalInfo = (obj: PersonalInfo, errors: string[]): void => {
    if (Object.keys(obj).length === 0) {
        log('The obj is empty, skipping personal info tests.');
        return;
    }

    try {
        // Check that all fields exist
        assert(obj.hasOwnProperty('name'), 'Missing field "name"', errors);
        assert(obj.hasOwnProperty('age'), 'Missing field "age"', errors);
        assert(obj.hasOwnProperty('birth_date'), 'Missing field "birth_date"', errors);
        assert(obj.hasOwnProperty('programming_languages'), 'Missing field "programming_languages"', errors);

        // Check data types
        assert(typeof obj.name === 'string', `"name" must be a string but got ${typeof obj.name}`, errors);
        assert(typeof obj.age === 'number', `"age" must be a number but got ${typeof obj.age}`, errors);

        // Check if birth_date is a valid date
        const birthDate = new Date(obj.birth_date);
        assert(!isNaN(birthDate.getTime()), `"birth_date" must be a valid Date but got ${obj.birth_date}`, errors);

        assert(Array.isArray(obj.programming_languages), `"programming_languages" is not an array but got ${typeof obj.programming_languages}`, errors);

        // Validate each programming language
        obj.programming_languages.forEach(lang => assert(typeof lang === 'string', `Each language must be a string but got ${typeof lang}`, errors));

        // Check fields are not empty
        assert(obj.name.length > 0, '"name" cannot be empty', errors);
        assert(obj.age > 0, `"age" must be greater than 0 but got ${obj.age}`, errors);
        assert(obj.birth_date.length > 0, '"birth_date" cannot be empty', errors);
        assert(obj.programming_languages.length > 0, '"programming_languages" should have at least one language', errors);
    } catch (e: unknown) {
        if (e instanceof Error) {
            console.error('Caught an error during personal info tests:', e.message); // Log the caught error
        }
    }

    log('All personal info tests have been executed.');
};

// Empty object for testing
const nikitaInfo: PersonalInfo = {
    name: "",
    age: 0,
    birth_date: "",
    programming_languages: []
};

// Run tests
const errors: string[] = [];
testSum(errors);
testPersonalInfo(personalInfo, errors); // Should pass
testPersonalInfo(nikitaInfo, errors); // Should fail

// Log all collected errors at the end
if (errors.length > 0) {
    log('Errors encountered during tests:');
    errors.forEach(error => log(error));
} else {
    log('No errors encountered during tests.');
}

/* Final General Output:
Welcome to the road of unit testing and error handling!
This code is designed to run in a browser environment. Skipping window-related code.
Assertion failed: "one" is not equal to "1"
Assertion failed: Testing assertion... null undefined function Object() { [native code] }
All sum tests have been executed.
All personal info tests have been executed.
The obj is empty, skipping personal info tests.
Errors encountered during tests:
Error: Expected 3.3 but got 3.3000000000000003
Error: "name" cannot be empty
Error: "age" must be greater than 0 but got 0
Error: "birth_date" cannot be empty
Error: "programming_languages" should have at least one language
*/