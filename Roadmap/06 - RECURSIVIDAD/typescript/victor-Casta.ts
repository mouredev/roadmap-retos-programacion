(() => {
  /*
    * EJERCICIO:
    * Entiende el concepto de recursividad creando una función recursiva que imprima
    * números del 100 al 0.
  */

  const printNumbers = (a: number): void => {
    if (a < 0) return
    console.log(a)
    printNumbers(a - 1)
  }

  printNumbers(100)

  /*
    * DIFICULTAD EXTRA (opcional):
    * Utiliza el concepto de recursividad para:
    * - Calcular el factorial de un número concreto (la función recibe ese número).
    * - Calcular el valor de un elemento concreto (según su posición) en la
    *   sucesión de Fibonacci (la función recibe la posición).
  */

  const factorial = (n: number): number => {
    if (n < 1) return 1
    return n * factorial(n - 1)
  }

  console.log(factorial(8))

  const fibonacci = (position: number): number => {
    if (position === 0) {
      return 0
    }
    if (position === 1) {
      return 1
    }
    return fibonacci(position - 1) + fibonacci(position - 2)
  }
  console.log(fibonacci(7))
})()