// In a recursive function, it is crucial to define a condition that stops the recursion 
// to avoid an infinite loop and a stack overflow error.

let counter = 0

function recurse(fromNumber) {
    console.log(fromNumber)
    while (counter < 100) {
        counter++
        recurse(fromNumber - 1)
    }
}
// recurse(100);


function factorial(number) {
    let value = 0
    let factor = 1

    if (number === 0 || number === 1) {
        return 1;
    }

    while (value < number) {
        factor *= number - value
        value++
    }
    return factor
}
// console.log(factorial(0))


function factorialRecurse(number) {
    if (number === 0 || number === 1) {
        return 1;
    }
    return number * factorialRecurse(number - 1);
}
// console.log(factorialRecurse(0))



//    - Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
function Fibonacci(number) {
    let a = 0
    let b = 1
    let c = a + b
    let counter = 0
    let sequence = []
    while (counter < number) {

        if (counter == 0) {
            sequence.push(a, b)
        } else {
            sequence.push(c)
            a = b
            b = c
            c = a + b
        }
        counter++
    }
    return sequence
}

// console.log(Fibonacci(10))

function FibonacciRecursive(positionNumber) {
    if (positionNumber == 0) {
        return 0
    }
    if (positionNumber == 1) {
        return 1
    }

    return FibonacciRecursive(positionNumber - 1) + FibonacciRecursive(positionNumber - 2)
}

console.log(FibonacciRecursive(5))

/* Logic
    F(2) = F(1) + F(0) = 1 + 0 = 1
    F(3) = F(2) + F(1) = 1 + 1 = 2
    F(4) = F(3) + F(2) = 2 + 1 = 3
    F(5) = F(4) + F(3) = 3 + 2 = 5
*/