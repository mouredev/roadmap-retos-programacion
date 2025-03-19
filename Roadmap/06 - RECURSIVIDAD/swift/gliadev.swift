import Foundation

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */

func imprimirNumerosRecursivos(numero: Int){
    if numero < 0 {
        return
    }
    print(numero)
    
    imprimirNumerosRecursivos(numero: numero - 1)
}


imprimirNumerosRecursivos(numero: 100)







/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */

// calculamos el factorial de un numero. Le pasamos el numero que queremos calcular
// y se lo pasamos en la funcion pero
func factorial(numero: Int) -> Int {
    if numero == 0 { // si el numero es 0 devuelve 1
        return 1
    } else {
        return numero * factorial(numero: numero - 1)
    }
}

let numero = 9
print("El factorial de \(numero) es  \(factorial(numero: numero))")


func fibonacci(_ n: Int) -> Int {
    if n <= 0 {
        return 0
    } else if n == 1 {
        return 1
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2)
    }
}

let posicion = 5
print("El elemento en la posición \(posicion) de la sucesión de Fibonacci es \(fibonacci(posicion))")

