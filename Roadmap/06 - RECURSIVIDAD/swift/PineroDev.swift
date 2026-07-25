/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */


func impNumRecursivo(num: Int) {
    if num >= 0 {
        print(num)
        impNumRecursivo(num: num - 1)
    }
}

impNumRecursivo(num: 100)


func CalFactorial(num: Int) -> Int {
    guard num > 1 else {
        return 1
    }
    return num * CalFactorial(num: num - 1)
}

print(CalFactorial(num: 5))

func fibonacci(_ num: Int) -> Int {
    if num <= 0 {
        return 0
    }else if num == 1 {
        return 0
    }else if num == 2 {
        return 1
    }else{
        return fibonacci(num - 1) + fibonacci(num - 2)
    }
}

print(fibonacci(11))
