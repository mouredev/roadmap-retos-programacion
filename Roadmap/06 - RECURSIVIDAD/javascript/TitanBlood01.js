//Recursividad

/* 
La recursividad es una practica que permite a una funcion poder llamarse
a si misma, se lo usa cuando es necesario realizar mismos procedimientos
*/

function myRecursiveFunc(num) {
    console.log(num)
    if (num<=0) {
        console.log('Fin recursividad')
        return;
    }
    myRecursiveFunc(num-1)
}

myRecursiveFunc(100)


/* Extra
Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
*/

const factorial = function (num) {
    if (num <= 1) {
        return 1
    }
    return num * factorial(num -1)
}

let resultFact = factorial(5)
console.log(resultFact)

//let fibonacciSucession = [0,1,1,2,3,5,8,13,21,34]
let fibonacciSucession = []

const fibonacciElementValue = (pos) => {
    let result = 0;
    if (pos == 0) {
        return 0
    } else if (pos == 1 ) {
        return 1
    } else if (fibonacciSucession[pos]) {
        return fibonacciSucession[pos]
    } else {
        result = fibonacciElementValue(pos-1) + fibonacciElementValue(pos-2)
        fibonacciSucession[pos] = result
    }
    return result
}

const numberFib = 6
const resultFibonacci = fibonacciElementValue(numberFib)
console.log(`Fibonacci de ${numberFib}: ${resultFibonacci}`)