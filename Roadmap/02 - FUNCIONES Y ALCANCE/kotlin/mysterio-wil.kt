/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// --- Variable Global (propiedad top-level) ---
var globalVar = "Soy una variable global"

fun main() {
    println("===> Funciones básicas <===")

    // Sin parámetros ni retorno
    greet()

    // Con un parámetro
    greetPerson("Wilmer")

    // Con varios parámetros
    add(5, 3)

    // Con retorno
    val result = multiply(5, 3)
    println("El resultado de la multiplicación es $result")

    // Con parámetros por defecto y nombrados
    greetDefault("MoureDev")
    greetDefault("Wilmer", greeting = "Hello")

    // Con parámetros de longitud variable (vararg)
    println("Argumentos variables (vararg):")
    printArgs(1, "texto", true, 12.99)


    println("\n===> Funciones dentro de funciones (Local Functions) <===")
    outerFunction()


    println("\n===> Funciones de la Librería Estándar de Kotlin <===")
    val myList = listOf(1, 2, 3, 4, 5)
    println("Usando la propiedad 'size' de una Lista: La lista tiene ${myList.size} elementos.")
    println("Usando list.maxOrNull(): El valor máximo es ${myList.maxOrNull()}")


    println("\n===> Variable LOCAL y GLOBAL <===")
    myFunctionScope()

    // Modificar una variable global
    println("Antes de modificar: $globalVar")
    modifyGlobal()
    println("Después de modificar: $globalVar")


    /*
     * DIFICULTAD EXTRA (opcional):
     */
    println("\n====> DIFICULTAD EXTRA <====")
    val timesPrintedNumber = fizzBuzzExtra("Fizz", "Buzz")
    println("\nEl número se imprimió un total de $timesPrintedNumber veces.")
}

// --- Definiciones de funciones (top-level) ---

fun greet() {
    println("Hola, Kotlin!")
}

fun greetPerson(name: String) {
    println("Hola, $name!")
}

fun add(a: Int, b: Int) {
    println("La suma de $a y $b es ${a + b}")
}

fun multiply(a: Int, b: Int): Int {
    return a * b
}

fun greetDefault(name: String, greeting: String = "Hola") {
    println("$greeting, $name!")
}

fun printArgs(vararg args: Any) {
    for (arg in args) {
        println("- $arg")
    }
}

fun outerFunction() {
    println("Esta es la función externa.")
    fun innerFunction() {
        println("Esta es la función interna.")
    }
    innerFunction()
}

fun myFunctionScope() {
    val localVar = "Soy una variable local"
    println(globalVar) // Acceso a la variable global
    println(localVar)
}

fun modifyGlobal() {
    globalVar = "He modificado la variable global"
}

fun fizzBuzzExtra(text1: String, text2: String): Int {
    var count = 0
    for (i in 1..100) {
        val isMultipleOf3 = (i % 3 == 0)
        val isMultipleOf5 = (i % 5 == 0)

        when {
            isMultipleOf3 && isMultipleOf5 -> println("$text1$text2")
            isMultipleOf3 -> println(text1)
            isMultipleOf5 -> println(text2)
            else -> {
                println(i)
                count++
            }
        }
    }
    return count
}
