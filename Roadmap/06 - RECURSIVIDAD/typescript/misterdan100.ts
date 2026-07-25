// print number 1 - 100 recursive function

const print1to100 = (initNumber: number): void => {
    if(initNumber <= 100) {
        console.log(initNumber)
        print1to100(initNumber + 1)
    }
}

print1to100(20)


//* Factorial number
const factorial = (number: number): number => {
    if( number === 0 || number === 1) {
        return 1
    }
    return number * factorial(number -1)
}

console.log(factorial(5))


//* Fibonachi number recursion
// recursion for fibonacci is slow with big number like 77

const fibonacci = (number: number): number => {
    if(number === 1 ) return 1
    if(number === 0 ) return 0

    return fibonacci(number -1 ) + fibonacci(number -2 )
}

console.log(fibonacci(3))

//* Fibonacci function to big numbers like 77
const fibonacciLarge = (n: number): number => {
    let a = 1
    let b = 1
    let c = 1
    for( let i = 3; i <= n; i++) {
        c = a + b
        a = b
        b = c
    }

    return b
}

console.log(fibonacciLarge(2))