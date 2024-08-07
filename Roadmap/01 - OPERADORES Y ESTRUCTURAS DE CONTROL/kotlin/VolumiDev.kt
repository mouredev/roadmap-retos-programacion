fun main(args: Array<String>) {
  var num1 = 10
  var num2 = 6

  // Operadores aritmeticos (+, -, *, /, %)
  // suma
  println("### Suma ###")
  println("$num1 + $num2 = ${ num1 + num2 }")
  
  // resta
  println("### Resta ###")
  println("$num1 - $num2 = ${ num1 - num2 }")


  // multiplicacion
  println("### Multiplicación ###")
  println("$num1 * $num2 = ${ num1 * num2 }")

  //division
  println("### División ###")
  println("$num1 / $num2 = ${ num1 / num2 }")

  // resto
  println("### Resto ###")
  println("$num1 % $num2 = ${ num1 % num2 }")

  //operadores de asignacion 
  println("### Operadores de asignación ###")
  num1 = 100
  num1 += 1 
  println("El nuevo valor de num1 = $num1")
  num1 -= 1
  println("El nuevo valor de num1 = $num1")
  num1 *= 2
  println("El nuevo valor de num1 = $num1")
  num1 /= 2
  println("El nuevo valor de num1 = $num1")
  num1 %= 24
  println ("El nuevo valor de num1 = $num1")

  //operadores unarios 
  println("### Operadores de unarios ###")
  println("Num1 mas 1 = ${ ++num1 }")
  println("Num1 menos 1 = ${ --num1 }")
  println("Num1 en negativo = ${ -num1 }")
  var bol = true

  //operadiores de comparacion
  println("### Operadores de comparación ###")
  println("$num1 > $num2 -> ${ num1 > num2 }")
  println("$num1 < $num2 -> ${ num1 < num2 }")
  println("$num1 igual $num2 -> ${ num1 == num2 }")
  println("$num1 distinto $num2 -> ${ num1 != num2 }")
  println("$num1 mayor o igual $num2 -> ${ num1 >= num2 }")
  println("$num1 menor o igual $num2 -> ${ num1 <= num2 }")

  
  //operadores logicos (&&, ||, !)
  println("### Operadores de lógicos ###")
  println("$bol && ${ !bol } => ${ bol && !bol }")
  println("$bol || ${ !bol } => ${ bol || !bol }")
  println("La negacion de $bol es ${ !bol }")

  // operadores de bits (and, or, xor, inv, shl, shr, ushr, ushl)
  println("### Operadores de bits ###")
  num1 = 0b1100
  num2 = 0b1010
  println("El resultado de AND $num1 y $num2 es -> ${ num1 and num2 }") 
  println("El resultado de OR $num1 y $num2 es -> ${ num1 or num2 }")
  println("El resultado de XOR $num1 y $num2 es -> ${ num1 xor num2 }")
  println("El resultado de complemento (inv) es -> ${ num1.inv() }")
  println("El resultado de desplazamiento a la izquerda es -> ${ num1 shl 1 }")
  println("El resultado de desplazamiento a la derecha es -> ${ num1 shr 1 }")
  println("El resultado de desplazamiento a la derecha sin signo es -> ${ num1 ushr 1 }")

  // Estructura de control
  var var1 = 10
  var var2 = 5

  println("### IF / ELSE ###")
  if ( var1 > var2 ) println("Aqui se cumple") else println("Aqui no se cumple")

  println("### WHEN ###")
  when (var2){
    1 -> println("es un uno")
    2 -> println("es un dos")
    3 -> println("es un tres")
    4 -> println("es un cuatro")
    5 -> println("es un cinco")
    else -> println("opcion no valida")
  }

  println("### FOR ###")
  var frutas = listOf("Platano", "Naranja", "Manzana", "Melon")

  for ( fruta in frutas){
    print("$fruta - ")
  }

  var indice = 0 
  println("### WHILE ###")
  while (indice < frutas.size){
    println("fruta en el indice $indice es ${ frutas[indice] }")
    indice++
  }

  println("### DO WHILE ###")

  indice = 0
  do{
    println("El indice ira aumentando, ahora es $indice")
    indice++
  }while (indice <= 5)

  /*
  DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  */

  for (x in 10..55){
    if (x % 2 == 0){
      if (x != 16 && x % 3 != 0) print("$x - ")
    }
  }
}