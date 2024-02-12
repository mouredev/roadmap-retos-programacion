object Main {
  def main(args: Array[String]): Unit = {
    // Operadores
    // Aritméticos
    val suma = 5 + 3
    println(s"Suma: 5 + 3 = $suma")

    val resta = 10 - 4
    println(s"Resta: 10 - 4 = $resta")

    val multiplicacion = 7 * 2
    println(s"Multiplicación: 7 * 2 = $multiplicacion")

    val division = 20 / 4
    println(s"División: 20 / 4 = $division")

    val modulo = 15 % 4
    println(s"Módulo: 15 % 4 = $modulo")

    // Lógicos
    val andLogico = true && false
    println(s"AND Lógico: true && false = $andLogico")

    val orLogico = true || false
    println(s"OR Lógico: true || false = $orLogico")

    val notLogico = !true
    println(s"NOT Lógico: !true = $notLogico")

    // De comparación
    val igual = 5 == 5
    println(s"Igual: 5 == 5 = $igual")

    val noIgual = 10 != 5
    println(s"No Igual: 10 != 5 = $noIgual")

    val mayorQue = 8 > 3
    println(s"Mayor Que: 8 > 3 = $mayorQue")

    val menorQue = 6 < 9
    println(s"Menor Que: 6 < 9 = $menorQue")

    val mayorIgual = 7 >= 7
    println(s"Mayor o Igual: 7 >= 7 = $mayorIgual")

    val menorIgual = 12 <= 15
    println(s"Menor o Igual: 12 <= 15 = $menorIgual")

    // De asignación
    var x = 10
    x += 5
    println(s"Asignación: x += 5 => x = $x")

    // De identidad
    val a = "Hola"
    val b = "Hola"
    val identico = a eq b
    println(s"Identidad: a eq b = $identico")

    // De pertenencia
    val lista = List(1, 2, 3)
    val contiene = lista.contains(2)
    println(s"Pertenencia: lista.contains(2) = $contiene")

    // Bits
    val bitAND = 5 & 3
    println(s"Bit AND: 5 & 3 = $bitAND")

    val bitOR = 5 | 3
    println(s"Bit OR: 5 | 3 = $bitOR")

    val bitXOR = 5 ^ 3
    println(s"Bit XOR: 5 ^ 3 = $bitXOR")

    val desplazamientoIzq = 8 << 2
    println(s"Desplazamiento Izquierdo: 8 << 2 = $desplazamientoIzq")

    val desplazamientoDer = 16 >> 2
    println(s"Desplazamiento Derecho: 16 >> 2 = $desplazamientoDer")


     // Estructuras de control
    // Condicionales
    if (x > 0) {
      println("x es positivo")
    } else if (x < 0) {
      println("x es negativo")
    } else {
      println("x es cero")
    }

    // Iterativas
    var i = 10
    while (i <= 55) {
      if (i % 2 == 0 && i != 16 && i % 3 != 0) {
        println(i)
      }
      i += 1
    }

    // Excepciones
    try {
      val resultado = 10 / 0
    } catch {
      case e: ArithmeticException => println("¡División por cero!")
    }

  }
}
