/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

 // Operadores Aritméticos
fun sum(numero1: Int, numero2: Int): Int {
    return a + b 
}

fun resta(a: Int, b: Int): Int {
    return a - b 
}

fun multiplicar(c: Int, d: Int): Int {
    return c * d 
}

fun dividir(e: Int, f: Int): Int {
    return e / f 
}

fun modulo(g: Int, h: Int): Int {
    return g % h
}

 // Operadores Logicos 
 val myTrue: Boolan = false || true // OR 
 val myFalse: Boolean = true && false // AND 
 val myTrueFalse: Boolean != false // Not 

 // Operadores de Comparacion 
 val mayor = 5 > 4 // Mayor Que 
 val menor = 4 < 5 // Menor que 
 val mayorIgual = 5 >= 4 // Mayor Igual 
 val menorIgual = 4 <= 5 // Menor Igual 

 
// Bucles 
 for (i in 1...3) {
    print(i)
 }

 // IF 
 if 5 > 4 {
    println("5 es mayor que 4 ")
 }

 // IF ElSE 
 if 5 < 4 {
    print("5 es menor que 4 ")
 } else {
    print("5 es menor que 4 ")
 }

 // WHEN 
 when (x) {
    0.1 -> print(x == 0, x == 1 )
    else -> print("otherwise")
 }

 // WHile 
 do {
    val y = 5 
 } while y < 5 