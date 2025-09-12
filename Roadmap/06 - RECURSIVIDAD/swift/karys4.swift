/*
EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
*/

func myRecursiveFunction(number: Int) {
  print(number)

  if number == 0 {
  print("End of the exercise")
  } else {
    myRecursiveFunction(number: number - 1)
  }
}

myRecursiveFunction(number:100)