import Foundation 



// Función Recursiva Que Imprime Los Numeros Del 100 al 0
func recursiveFunction(number num: Int = 100) {
    if num == 0 {  // Si num es igual a 0, imprime num.
        print(num)
    } else {
        print(num)  // Imprime num.
        recursiveFunction(number: num - 1)  // Llama recursivamente a la función con num decrementado en 1.
    }
}
recursiveFunction()  // Llama a la función con el valor por defecto (100).


// Función Recursiva Que Calcula el Factorial de un Numero
func calculateTheFactorial(number num: Int) -> Int {
    if num == 0 {  // Si num es igual a 0, devuelve 1.
        return 1
    } else {
        return num * calculateTheFactorial(number: num - 1)  // Devuelve num multiplicado por el factorial de num - 1.
    }
}
let factorialNumber = calculateTheFactorial(number: 5)  // Calcula el factorial de 5.
print(factorialNumber)  // Imprime el resultado.


// Función Recursiva que Calcula la Posición de un Numero en la Secuencia Fibonacci
var secuence = [0, 1]  // Inicializa una secuencia Fibonacci con los dos primeros números.
var stepper1 = 0  // Inicializa el primer índice de la secuencia.
var stepper2 = 1  // Inicializa el segundo índice de la secuencia.
func calculateFibonacci(number num: Int) -> Int {
    if num == 0 {  // Si num es igual a 0, no hace nada.
        
    } else {
        // Añade el siguiente número en la secuencia Fibonacci a la lista.
        secuence.append(secuence[(num - num) + stepper1] + secuence[(num - num) + stepper2])
        stepper1 += 1  // Incrementa el primer índice.
        stepper2 += 1  // Incrementa el segundo índice.
        _ = calculateFibonacci(number: num - 1)  // Llama recursivamente a la función con num decrementado en 1.
    }
    return secuence[stepper1 - 1]  // Devuelve el número en la posición num de la secuencia Fibonacci.
}
let fibonacciPosition = calculateFibonacci(number: 10)  // Calcula el número en la posición 10 de la secuencia Fibonacci.
print(fibonacciPosition)  // Imprime el resultado.
