//: [Previous](@previous)

/* 18miguelgalarza.swift Release #06 - swift
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


import Foundation

var greeting = "Hello, playground"

//: [Next](@next)


func imprimeNumero(_ n: Int) -> Int{
    print(n)
    if n == 0 {
        return 1 // Caso base
    } else {
        return imprimeNumero(n-1)
    }
}


imprimeNumero(100)


func factorial(_ n: Int) -> Int {
    if n == 0 {
        return 1 // Caso base
    } else {
        return n * factorial(n - 1) // Caso recursivo
    }
}

print(factorial(5)) // Output: 120 (5 * 4 * 3 * 2 * 1)


func fibonacci(_ n: Int) -> Int {
    if n <= 1 {
        return n // Caso base: si n es 0 o 1, devuelve n
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2) // Caso recursivo: devuelve la suma de los dos números Fibonacci anteriores
    }
}

print(fibonacci(7)) // Output: 13 (0, 1, 1, 2, 3, 5, 8, 13)


