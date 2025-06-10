// Recursividad

function oneHundred(n) {
    if (n < 0) {
        return
    }

    console.log(n)
    oneHundred(n - 1)
}

oneHundred(100);

// Factorial

function factorial(n) {
    if (n === 0) {
        return 1
    }

    return n * factorial(n - 1)
}

console.log(factorial(4))

// Fibonacci 

function fibonacci (n) {
    if (n === 0) {
        return 0
    }

    if (n === 1) {
        return 1
    }

    return fibonacci(n - 1) + fibonacci(n - 2)
}

console.log(fibonacci(10))