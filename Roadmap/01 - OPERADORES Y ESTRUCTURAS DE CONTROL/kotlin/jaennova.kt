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


 fun operadoresAritmeticos(){
    val a1: Int = 4
    val a2: Int = 42
    println("Operadores Aritmeticos")
    println("a1 = $a1, a2 = $a2\n")
    println("$a1 - $a2 = ${a1 - a2}")
    println("$a1 * $a2 = ${a1 * a2}")
    println("$a1 / $a2 = ${a1 / a2}")
    println("$a1 % $a2 = ${a1 % a2}")
}


fun operadoresLogicos(){
    val o1: Int = 23
    val o2: Int = 41
    println("\nOperadores Logicos")
    println("o1 = $o1, o2 = $o2\n")
    println("$o1 == $o2 = ${o1 == o2}")
    println("$o1 != $o2 = ${o1 != o2}")
}

fun operadoresRelacionCompuesta(){
    val a = 5
    val b = 3
    val c = 1
    println("/nOperadores de relacion compuesta")
    println("a = $a, b = $b, c = $c")
    println("a > b && b > c = ${a > b && b > c}")  // imprime true, ya que a > b y b > c son ambas verdaderas
    println("a < b || b > c = ${a < b || b > c}")  // imprime true, ya que al menos una de las expresiones es verdadera (b > c)
}

fun operadoresRelacionales(){
    val a = 5
    val b = 3
    val c = 5
    println(a == b)  // imprime false
    println(a != b)  // imprime true
    println(a > b)   // imprime true
    println(a < b)   // imprime false
    println(a >= b)  // imprime true
    println(a <= b)  // imprime false
    println(a == c)  // imprime true
}

fun condicionales(){
    val a = 5
    val b = 3
    val c = 5
    if(a != b) println("a es diferente de b") else println("a no es diferente de b")
    if(b && c > a){
        println("$a y $c son mayores que $a")
    } else{
        println("$a y $c no son mayores que $a")
    }
}
//  * DIFICULTAD EXTRA (opcional):
//  * Crea un programa que imprima por consola todos los números comprendidos
//  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
fun ejercicio(){
    for(i in 10..5){
        if(i % 2 == 0 && i != 16 && i % 3 != 0){
            println(i)
            }
        }
}
fun main(){
    operadoresAritmeticos()
    operadoresLogicos()
    operadoresRelacionCompuesta()
    condicionales()
    ejercicio()
}