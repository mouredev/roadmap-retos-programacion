import Foundation

func sumaRecursiva(a: Int, b: Int) -> Int {
    if b == 0 {
        return a
    } else {
        return sumaRecursiva(a: a + 1, b: b - 1)
    }
}

print("La suma de 5 +3 usando recursividad es = " +  String(sumaRecursiva(a: 5, b: 3)))

func potenciaRecursiva(base: Int, exponente: Int) -> Int {
    if exponente == 0 {
        return 1
    } else {
        return base * potenciaRecursiva(base: base, exponente: exponente - 1)
    }
}

print("La potencia de 2^3 usando recursividad es = " +  String(potenciaRecursiva(base: 2, exponente: 3)))

func imprimirNumeros(_ numero: Int) {
    if numero >= 0 {
        print(numero, terminator: " ")
        imprimirNumeros(numero - 1)
    }
}

print("De 100 a 0 usando rercursividad: ")
imprimirNumeros(100)

// Extra

func factorialRecursivo(numero: Int) -> Int {
    if numero == 0 {
        return 1
    } else {
        return numero * factorialRecursivo(numero: numero - 1)
    }
}

print("El factorial de 5 usando recursividad es = " +  String(factorialRecursivo(numero: 5)))

func fibonacciRecursivo(posicion: Int) -> Int {
    if posicion == 0 {
        return 0
    } else if posicion == 1 {
        return 1
    } else {
        return fibonacciRecursivo(posicion: posicion - 1) + fibonacciRecursivo(posicion: posicion - 2)
    }
}

print("El fibonacci de la posicion 5 usando recursividad es = " +  String(fibonacciRecursivo(posicion: 5)))

// Vamos a continuación a probar las funcioens de factorial y fibonacci de forma iteractiva, pidiendo al usuario que introduzca el número para el factorial y la posición para el fibonacci

print("Introduce un número para calcular su factorial")
let numeroFactorial = Int(readLine()!)!
print("El factorial de \(numeroFactorial) es = " +  String(factorialRecursivo(numero: numeroFactorial)))

print("Introduce una posición para calcular el fibonacci")
let posicionFibonacci = Int(readLine()!)!
print("El fibonacci de la posición \(posicionFibonacci) es = " +  String(fibonacciRecursivo(posicion: posicionFibonacci)))









