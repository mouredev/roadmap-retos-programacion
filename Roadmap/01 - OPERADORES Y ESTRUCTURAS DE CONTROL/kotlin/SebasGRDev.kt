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


// OPERADORES DE SIGNO
fun opSigno() {
    val a = -5

    println("a = ${-a}")
}

//OPERADORES ARITMETICOS
fun opAritmeticos(){
    val a = 15
    val b = 30

    println("$a + $b = ${a + b}")
    println("$a - $b = ${a - b}")
    println("$a * $b = ${a * b}")
    println("$a / $b = ${a / b}")
    println("$a % $b = ${a % b}")
}

//OPERADORES DE ASIGNACION COMPESTA
fun opAsignCompuesta() {
    var a = 500
    val b = 5

    a += b 
    println("+= $a")

    a -= b
    println("-= $a")

    a *= b 
    println("*= $a")

    a /= b 
    println("/= $a")

    a %= b 
    println("%= $a")
}

//OPERADORES DE INCREMENTO Y DECREMENTO
fun opIncrDecr() {
    var a = 1

    println("De $a a ${++a}")
    println("De $a a ${--a}")
    println("Valor final > $a")
}

//OPERADORES RELACIONALES
fun opRelacionales() {
    val a = 15
    val b = 20

    println("$a es igual a $b: ${a == b}")
    println("$a es diferente a $b: ${a != b}")
    println("$a es menor que $b: ${a < b}")
    println("$a es mayor a $b: ${a > b}")
    println("$a es menor o igual $b: ${a <= b}")
    println("$a es mayor o igual $b: ${a >= b}")
}

//OPERADORES LOGICOS
fun opLogicos() {
    val a = 15
    var res: Boolean

    val mayorQueCero = a > 0
    val isEven = a % 2 == 0

    res = mayorQueCero & isEven
    println("Es mayor que cero y par: $res")

    res = mayorQueCero || isEven
    println("Es mayor que cero o par: $res")

    res = mayorQueCero && !isEven
    println("Es mayor que cero e impar: $res")
}

//OPERADORES A NIVEL DE BITS
val a = 8
val b = 3

println("a and b: ${a and b}")
println("a or b: ${a or b}")
println("a xor b: ${a xor b}")
println("a inv b: ${a .inv() b}")
println("a shl b: ${a shl b}")
println("a shr b: ${a shr b}")
println("a ushr b: ${a ushr b}")

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

 fun numeracion (){
    for(i in 9..56) {
        if (i % 2 == 0 && i % 3 != 0 && i != 16) {
            println("numero = $i")
        }
    }
 }