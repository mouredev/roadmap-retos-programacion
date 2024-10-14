/* EXCEPCIONES */
//bibliography reference
//Secrets of the JavaScript Ninja (John Resig, Bear Bibeault, Josip Maras) (z-lib.org)
//Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
//JavaScript Notes for Professionals (GoalKicker.com) (Z-Library)
//GPT

//Short for console.log()
let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #10.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #10. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #10'); 
});


/* Runtime errors in JavaScript are instances of the Error object. The Error object can also be used as-is, or as the base for user-defined exceptions. It's possible to throw any type of value - for example, strings - but you're strongly encouraged to use Error or one of its derivatives to ensure that debugging information -- such as stack traces -- is correctly preserved.
The first parameter to the Error constructor is the human-readable error message. You should try to always specify a useful error message of what went wrong, even if additional information can be found elsewhere.
} */

/* In JavaScript, exception handling is primarily done through the statements try, catch, finally, and throw. Here is a summary of each:

    try: It is used to wrap the code that may throw an exception. If an error occurs within the try block, control is transferred to the catch block.
    catch: It is used to handle the exception. It receives the error object as an argument.
    finally: This block executes after the try and catch blocks have completed, regardless of whether an exception was thrown or not.
    throw: It is used to manually throw an exception.
 */

let num = 0, result;

try {
    if(typeof num === 'number' && num != 0) {
        result = 10 / num;
    }else if(num == 0) {
        throw new Error("It seems you've tried to divide by zero, which is not permitted. Please enter a valid non-zero number.");
    }else{
        throw new Error("It seems you've tried to divide by a non number value, which is not permitted. Please enter a valid number.");
    }
} catch (error) {
    log('Something went wrong! ' + error.message);
}

log(result); // Something went wrong! It seems you've tried to divide by zero, which is not permitted. Please enter a valid non-zero number.

//Note: Javascript returns infinity for divide any number by 0, so we have to explicity throw and error if we want inform about it.

/* Exceptions are to synchronous code what rejections are to promise-based asynchronous code. If an exception is thrown in a promise handler, its error will be automatically caught and used to reject the promise instead. */

Promise.resolve(102)
    .then(result => {
        throw new Error("explicitly rejected promise");
})
    .then(result => {
        console.info("Promise resolved: " + result);
})
    .catch(error => {
        console.error("Promise rejected: " + error);
}); // Promise rejected: Error: explicitly rejected promise (it will be logged at the end cause the async nature of the promise constructor)

/* There are six specific core error constructors in JavaScript:
EvalError - creates an instance representing an error that occurs regarding the global function eval().
InternalError - creates an instance representing an error that occurs when an internal error in the
JavaScript engine is thrown. E.g. "too much recursion". (Supported only by Mozilla Firefox)
RangeError - creates an instance representing an error that occurs when a numeric variable or parameter is outside of its valid range.
ReferenceError - creates an instance representing an error that occurs when dereferencing an invalid
reference.
SyntaxError - creates an instance representing a syntax error that occurs while parsing code in eval().
TypeError - creates an instance representing an error that occurs when a variable or parameter is not of a valid type.
URIError - creates an instance representing an error that occurs when encodeURI() or decodeURI() are
passed invalid parameters.
If you are implementing error handling mechanism you can check which kind of error you are catching from code. */

function getUserName(user) {
    try {
        const name = user.name.toUpperCase();
        log(`User name: ${name}`);
    } catch (e) {
        if (e instanceof Error) {
            log('Instance of general Error constructor');
        }

        if (e instanceof TypeError) {
            log('TypeError: Cannot read property "name" of undefined or null');
        }
    }
}

getUserName({ name: 'Roxy' }); //  User name: Roxy

getUserName(undefined); // Instance of general Error constructor TypeError: Cannot read property "name" of undefined or null

//Extra excercises

const checkValues = (arr, index)=>{
    try{
        if(!Array.isArray(arr)){
            throw new TypeError('the first parameter most be of type array');
        }else{
            if(arr.length < 0 || arr.length == 0) throw new Error('You give a empty array as parameter!');

            if(!arr[index]) throw new ReferenceError(`${index} is not a valid index for the array given`);
        }

        log(`The position given corresponds to this value: ${arr[index]}`);
        log("There's no errors when executing the function.")

    }catch(e){
        log(e.name + ": Ooops! " + e.message);
    }finally{
        log('The process is finished')
    }
}

checkValues([8, 5, 6, 4], 8); // ReferenceError: Ooops! 8 is not a valid index for the array given
// The process is finished
checkValues([], 4); // Error: Ooops! You give a empty array as parameter!
// The process is finished
checkValues([0, 76, 32, 1, 4, 2], 'Kia'); // ReferenceError: Ooops! Kia is not a valid index for the array given
// The process is finished
checkValues('Dev', 5); // TypeError: Ooops! the first parameter most be of type array
// The process is finished
checkValues([4, 5, 3, 18, 22], 3); // The position given corresponds to this value: 18
// There's no errors when executing the function.
// The process is finished