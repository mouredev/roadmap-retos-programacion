fun main() {
/*
1) TODOS LOS OPERADORES DEL LENGUAJE. CON EJEMPLOS. 
 */
// - Ejemplos de operadores aritmeticos
// Son los siguientes: +, -, *, /, % - mathematical operators
val numero1 = 10
val numero2 = 5

println("Los operadores matematicos: Ejemplo con el 10 y el 5")
println("$numero1 + $numero2 =${numero1+numero2}")
println("$numero1 - $numero2 =${numero1-numero2}")
println("$numero1 * $numero2 =${numero1*numero2}")
println("$numero1 / $numero2 =${numero1/numero2}")
println("$numero1 % $numero2 =${numero1%numero2}")

// Ejemplos de operadores lógicos
// &&, ||, ! - logical 'and', 'or', 'not' operators
println("-----------------------------------------------------")
println("Los operadores logicos:")
val myboolean1=true
val myboolean2=false
println("$myboolean1 and (&&) $myboolean2 =${myboolean1 && myboolean2}")
println("$myboolean1 or (||) $myboolean2 =${myboolean1 || myboolean2}")
println("not (!) $myboolean1 = ${!myboolean1}")

// Ejemplos de operadores de comparación
// <, >, <=, >= - comparison operators 
println("-----------------------------------------------------")
println("Los operadores de comparacion")
println("$numero1 > $numero2 = ${numero1>numero2}")
println("$numero1 < $numero2 = ${numero1<numero2}")
println("$numero1 <= $numero2 = ${numero1<=numero2}")
println("$numero1 >= $numero2 = ${numero1>=numero2}")
println("$numero1 == $numero2 = ${numero1==numero2}")
println("$numero1 != $numero2 = ${numero1!=numero2}")
// Ejemplos de operadores de asignación, identidad, pertenencia, bits
//Asignación
println("-----------------------------------------------------")
println("El operador de asignacion :  = ")
 // Declaración de una variable sin iniciarla:
 var numero: Int
// Asignación de un valor a la variable
 numero = 10
 // Imprimir el valor de la variable
 println("El valor de la variable 'numero' es: $numero y la he asignado con =")

 //identidad son === y !==
 println("-----------------------------------------------------")
 println("Los operadores de identidad son === y !==, se utilizan para verificar ")
 println("si dos referencias apuntan al mismo objeto en la memoria.")
 val a: String = "Hola"
 val b: String = "Hola"
 val resultado1: Boolean = (a === b)
 println("a y b apuntan al mismo objeto? $resultado1")  // Imprime: ¿a y b apuntan al mismo objeto? true

 //pertenencia
 /*En Kotlin, los operadores de pertenencia se utilizan 
 para verificar si un elemento está presente en una colección o en un rango. 
 Los operadores principales de pertenencia son in y !in
*/
 println("-----------------------------------------------------")
 println("Los operadores de pertenencia ")
 var numeros = listOf(1, 2, 3, 4, 5)
 var resultado2: Boolean = 3 in numeros
 println("El numero 3 esta en la lista? $resultado2")  // Imprime: ¿El número 3 está en la lista? true

//BITS
println("-----------------------------------------------------")
println("Los operadores de BITS ")
// Operador AND a nivel de bits
val resultadoAnd = 0b1010 and 0b1100
println("Resultado de AND a nivel de bits: $resultadoAnd")  // Imprime: Resultado de AND a nivel de bits: 8 (binario: 0b1000)

// Operador OR a nivel de bits
val resultadoOr = 0b1010 or 0b1100
println("Resultado de OR a nivel de bits: $resultadoOr")  // Imprime: Resultado de OR a nivel de bits: 14 (binario: 0b1110)

// Operador XOR a nivel de bits
val resultadoXor = 0b1010 xor 0b1100
println("Resultado de XOR a nivel de bits: $resultadoXor")  // Imprime: Resultado de XOR a nivel de bits: 6 (binario: 0b0110)

// Operador de desplazamiento a la izquierda
val resultadoShl = 0b1010 shl 2
println("Resultado de desplazamiento a la izquierda: $resultadoShl")  // Imprime: Resultado de desplazamiento a la izquierda: 40 (binario: 0b101000)

// Operador de desplazamiento a la derecha
val resultadoShr = 0b1010 shr 1
println("Resultado de desplazamiento a la derecha: $resultadoShr")  // Imprime: Resultado de desplazamiento a la derecha: 5 (binario: 0b0101)

// Operador de desplazamiento a la derecha con extensión de signo
val resultadoUshr = (-8).ushr(1)
println("Resultado de desplazamiento a la derecha sin extensión de signo: $resultadoUshr")  // Imprime: Resultado de desplazamiento a la derecha sin extensión de signo: 2147483644


/*
2) Ejemplos de todos los tipos de estructuras de control que existan en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
*/

println("-----------------------------------------------------")
println("LAS ESTRUCTURAS DE CONTROL")
estructurasControl()


/*3) EXTRA: Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  */

  println("-----------------------------------------------------")
  println("EL EXTRA")
  val rango = 10..55 
  for (i in rango ){
        if (i %2 == 0 && i!=16 && i%3!=0){
            println(i)
        }}

println("de otra forma")
for (i in 10..55 step 2) {
            if (i != 16 && i % 3 != 0) {
                println(i)
            }
        }

    }



fun estructurasControl() {
    // Estructura de control if
    val numero = 10
    if (numero > 0) {
        println("El numero es positivo")
    } else if (numero < 0) {
        println("El número es negativo")
    } else {
        println("El número es cero")
    }

    // Estructura de control when (similar a switch en otros lenguajes)

    val diaSemana = 3
    when (diaSemana) {
        1 -> println("Lunes")
        2 -> println("Martes")
        3 -> println("Miércoles")
        4 -> println("Jueves")
        5 -> println("Viernes")
        else -> println("Fin de semana")
    }

    // Estructura de control for
    val listaNumeros = listOf(1, 2, 3, 4, 5)
    println("Recorriendo lista con for:")
    for (a in listaNumeros) {
        println(a)
    }

    // Estructura de control while
    var contador = 0
    println("Contando hasta 5 con while:")
    while (contador <= 5) {
        println(contador)
        contador++
    }

    // Estructura de control do-while
    var contadorDoWhile = 0
    println("Contando hasta 5 con do-while:")
    do {
        println(contadorDoWhile)
        contadorDoWhile++
    } while (contadorDoWhile <= 5)
}