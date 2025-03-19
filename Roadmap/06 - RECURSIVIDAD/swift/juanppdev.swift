import Foundation

func printNumbers(_ n: Int) {
    if n < 0 {
        return
    }
    
    print(n)
    printNumbers(n - 1)
}

printNumbers(100)


// Función para calcular el factorial de un número
func factorial(_ n: Int) -> Int {
    if n == 0 {
        return 1
    } else {
        return n * factorial(n - 1)
    }
}

// Función para calcular el valor de un elemento en la sucesión de Fibonacci
func fibonacci(_ n: Int) -> Int {
    if n <= 1 {
        return n
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2)
    }
}

// Prueba de las funciones
let numFactorial = 5
let numFibonacci = 6

print("El factorial de \(numFactorial) es: \(factorial(numFactorial))")
print("El valor en la posición \(numFibonacci) de Fibonacci es: \(fibonacci(numFibonacci))")
