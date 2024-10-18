/* { RETOS DE PROGRAMACIÓN }  #13 PRUEBAS UNITARIAS */
// I refer to "JavaScript Notes for Professionals" from the people of Stack Overflow. https://goalkicker.com/JavaScriptBook
// Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

//short for console.log
let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #13.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #13. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #13'); 
});

/* GoalKicker.com – JavaScript® Notes for Professionals 219
Section 30.9: Debugging with assertions - console.assert() Writes an error message to the console if the assertion is false. Otherwise, if the assertion is true, this does nothing. */

console.assert('one' === 1); // Assertion failed:
//Note there's no message cause we didn't specify no one

//Multiple arguments can be provided after the assertion–these can be strings or other objects–that will only be printed if the assertion is false:

console.assert(true , 'Testing assertion...', null, undefined, Object); 

console.assert(false , 'Testing assertion...', null, undefined, Object); 
// Assertion failed: Testing assertion... NaN undefined funstion Object() { [native code] }


/*console.assert does not throw an AssertionError (except in Node.js), meaning that this method is incompatible with most testing frameworks and that code execution will not break on a failed assertion.  */

// Custom assert function that logs an error instead of throwing
const assert = (condition, message, errors) => {
    if (!condition) {
        console.error(message);
        errors.push(message); // Collect the error message
    }
};

const sum = (a, b) => {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    return a + b;
};

const testSum = (errors) => {
    assert(sum(2, 3) === 5, 'Error: 2 + 3 should be 5', errors);
    assert(sum(-1, 1) === 0, 'Error: -1 + 1 should be 0', errors);
    assert(sum(0, 0) === 0, 'Error: 0 + 0 should be 0', errors);
    
    try {
        sum(2, '3'); // This should throw an error
    } catch (e) {
        console.log('Caught an error:', e); // Log the caught error
        assert(e instanceof TypeError, 'Error: Invalid argument type not handled', errors);
        assert(e.message === 'Both arguments must be numbers', 'Error: Argument type mismatch', errors);
    }

    console.log('All sum tests have been executed.');
};

const personalInfo = {
    name: "Niko Zen",
    age: 41,
    birth_date: "1983/08/08",
    programming_languages: ["JavaScript", "Python", "Rust", "Ruby", "Java"] 
};

const testPersonalInfo = (obj, errors) => {
    if (Object.keys(obj).length === 0) {
        log('The obj is empty, skipping personal info tests.');
        return; 
    }

    // Check that all fields exist
    assert(obj.hasOwnProperty('name'), 'Missing field "name"', errors);
    assert(obj.hasOwnProperty('age'), 'Missing field "age"', errors);
    assert(obj.hasOwnProperty('birth_date'), 'Missing field "birth_date"', errors);
    assert(obj.hasOwnProperty('programming_languages'), 'Missing field "programming_languages"', errors);

    // Check data types
    assert(typeof obj.name === 'string', '"name" must be a string', errors);
    assert(typeof obj.age === 'number', '"age" must be a number', errors);
    
    // Check if birth_date is a valid date
    const birthDate = new Date(obj.birth_date);
    assert(!isNaN(birthDate.getTime()), '"birth_date" must be a valid Date', errors);
    
    assert(Array.isArray(obj.programming_languages), '"programming_languages" is not an array', errors);

    // Validate each programming language
    obj.programming_languages.forEach(lang => assert(typeof lang === 'string', 'Each language must be a string', errors));

    // Check fields are not empty
    assert(obj.name.length > 0, '"name" cannot be empty', errors);
    assert(obj.age > 0, '"age" must be greater than 0', errors);
    assert(obj.birth_date.length > 0, '"birth_date" cannot be empty', errors);
    assert(obj.programming_languages.length > 0, '"programming_languages" should have at least one language', errors);

    log('All personal info tests have been executed.');
};

/*Note: 
    The getTime() method returns the number of milliseconds since January 1, 1970, 00:00:00 UTC for the Date object.
    If the date is invalid (e.g., if the input string is not a valid date format), getTime() will return NaN.
    The isNaN() function checks if the value is NaN. Therefore, !isNaN(birthDate.getTime()) will be true if the date is valid and false if it is not.
 */ 


const nikitaInfo = {};

const errors = [];
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

/* Assertion failed: 
Assertion failed: Testing assertion... null undefined 
function Object()

Caught an error: TypeError: Both arguments must be numbers
All sum tests have been executed. 
All personal info tests have been executed. 
The obj is empty, skipping personal info tests. 
No errors encountered during tests. 
Retosparaprogramadores #13   
 */

