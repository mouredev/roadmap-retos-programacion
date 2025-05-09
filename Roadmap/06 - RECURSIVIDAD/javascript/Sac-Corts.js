// Exercise // 
function from100to0(n) {
    if (n <= 0) {
        return 0;
    }
    console.log(n);
    return from100to0(n - 1);
}

console.log(from100to0(100));

// Extra Exercise // 
function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
} 

console.log(factorial(5));

function fibonacci(n) {
    if (n == 1) {
        return 1;
    } else if (n == 0) {
        return 0;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

console.log(fibonacci(2));
