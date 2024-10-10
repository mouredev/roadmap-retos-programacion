function greet(name: string): string {
    return `Hello, ${name}!`;
}

function logDecorator<T extends (...args: any[]) => any>(fn: T): (...args: Parameters<T>) => ReturnType<T> {
    return function(...args: Parameters<T>): ReturnType<T> {
        console.log(`Calling function: ${fn.name}`);
        const result = fn(...args);
        console.log(`Function ${fn.name} executed with result: ${result}`);
        return result;
    };
}

const decoratedGreet = logDecorator(greet);
console.log(decoratedGreet("Isaac"));

// ** Extra Exercise ** //
function callCountDecorator<T extends (...args: any[]) => any>(fn: T): (...args: Parameters<T>) => ReturnType<T> {
    let count = 0;

    return function(...args: Parameters<T>): ReturnType<T> {
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
