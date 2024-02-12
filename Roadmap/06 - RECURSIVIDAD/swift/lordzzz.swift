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

import Foundation


// recursividad
func recursiva(numero: Int){
   
    print(numero )
   
    if numero > 0 {
        recursiva(numero: numero - 1)
        
    }
}
recursiva(numero: 100)

// Numero Factorial
func factorial(_ numeros: Int) -> Int{
    if numero < 1 {
        return 1
    }else  {
        return numero * factorial(numero - 1)
    }
    
}
let numero = 5
var result = factorial(numero)
print("Fatorial de \(numero) es \(result)")


// Fibonacci
func scesionFibonacci(_ posicion: Int) -> Int {
    if posicion <= 1{
        return posicion
    }else {
        return scesionFibonacci(posicion - 1) + scesionFibonacci(posicion - 2)
    }
}
let posicion = factorial(numero)
let valorFibonacci = scesionFibonacci(posicion)
print("el valor en la posición \(posicion) de la sucesión de Fibonacci es \(valorFibonacci)")

