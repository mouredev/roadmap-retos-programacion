function greet(name) {
    return `Hello, ${name}!`;
}

function logDecorator(fn) {
    return function(...args) {
        console.log(`Calling function: ${fn.name}`);
        const result = fn(...args);
        console.log(`Function ${fn.name} executed with result: ${result}`);
        return result;
    };
}

const decoratedGreet = logDecorator(greet);
console.log(decoratedGreet("Isaac"));

// Extra Exercise //
function callCountDecorator(fn) {
    let count = 0;
    
    return function(...args) {
        count++;
        console.log(`Function ${fn.name} has been called ${count} times`);
        return fn(...args);
    };
}

const decoratedGreet2 = callCountDecorator(greet);
console.log(decoratedGreet2("Hiel"));
console.log(decoratedGreet2("Kurama"));
console.log(decoratedGreet2("Yusuke"));
console.log(decoratedGreet2("Kuwabara"));