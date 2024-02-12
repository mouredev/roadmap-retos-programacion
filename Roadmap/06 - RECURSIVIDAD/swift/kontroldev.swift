import Foundation

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


// Función recursiva que imprime números del 100 al 0
func imprimirNumeros(numero: Int) {
  // Caso base: si el número es 0, lo imprimimos y terminamos
  if numero == 0 {
    print(numero)
    return
  }
  // Caso recursivo: si el número es mayor que 0, lo imprimimos y llamamos a la función con el número menos 1
  else if numero > 0 {
    print(numero)
    imprimirNumeros(numero: numero - 1)
  }
}


// Función recursiva que calcula el factorial de un número
func factorial(numero: Int) -> Int {
  // Caso base: si el número es 1, devolvemos 1
  if numero == 1 {
    return 1
  }
  // Caso recursivo: si el número es mayor que 1, devolvemos el número multiplicado por el factorial del número menos 1
  else if numero > 1 {
    return numero * factorial(numero: numero - 1)
  }
  // Si el número es menor que 1, devolvemos un error
  else {
    return -1
  }
}


// Función recursiva que calcula el valor de un elemento en la sucesión de Fibonacci
func fibonacci(posicion: Int) -> Int {
  // Caso base: si la posición es 1 o 2, devolvemos 1
  if posicion == 1 || posicion == 2 {
    return 1
  }
  // Caso recursivo: si la posición es mayor que 2, devolvemos la suma de los valores de las posiciones anteriores
  else if posicion > 2 {
    return fibonacci(posicion: posicion - 1) + fibonacci(posicion: posicion - 2)
  }
  // Si la posición es menor que 1, devolvemos un error
  else {
    return -1
  }
}



