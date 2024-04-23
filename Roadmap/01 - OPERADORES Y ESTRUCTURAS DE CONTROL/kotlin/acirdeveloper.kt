fun main() {
   /** 
    * Todo: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    * ? Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
    *
    * ? DIFICULTAD EXTRA (opcional):
      - Crea un programa que imprima por consola todos los números comprendidos
      - entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    */
  val name = "Acir"
  val age = 25
  val isDeveloper = false
  var ageProgrammer = 1

  //* Comparacion
  println("Igual a: ${age == ageProgrammer}")
  println("Diferente a: ${age != ageProgrammer}")
  println("Mayor que: ${age > ageProgrammer}")
  println("Menor que: ${age < ageProgrammer}")
  println("Mayor o igual que: ${age >= ageProgrammer}")
  println("Menor o igual que: ${age <= ageProgrammer}")
  println("Comparacion de referencias: ${name === "Acir"}")
  
  val number = 10
  val number2 = 55

  //* Logicos
  if (number > 5 && number2 < 60) {
    println("Ambas condiciones son verdaderas")
  }

  if (number > 5 || number2 < 50) {
    println("Al menos una condicion es verdadera")
  }

  if (!isDeveloper) {
    println("No es desarrollador")
  }

  //* Arithmetic
 val i = 10
 println("Numeros comprendidos entre 10 y 55, pares y no son 16 ni multiplos de 3:")
  for (i in 10..55) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
      print("$i, ")
    }
  }

}