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

 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

//Without parameters or return
fun hello1() {}

// with one, two or more parameters

fun hello2(name: String) {
    println("Hello $name")
}

//With default params
fun hello3(name: String = "Luis") {
    println("Hello $name")
}

// with return
fun hello4(name: String): String {
    return "Hello $name"
}

//With functions inside functions
fun hello5(name: String) {
    fun hello6(name: String) {
        println("Hello $name")
    }
    hello6(name)
}

//With multiple arguments
fun multipleDefArgs(
    language: String = "Python",
    name: String = "Juan",
    alias: String = "Juanillo",
    age: String = "37"
) {
    println("Hello $name, your alias is $alias, you are $age years old and you like $language language")
}
//With variable args with key value

fun main() {
    hello1()
    println()
    hello2("Luis")
    println()
    hello3("Luis")
    println()
    hello3()
    println()
    hello4("Luis")
    println()
    hello5("Luis")
    println()
    multipleDefArgs("", "", "", "")
    println()
    mynums("The number \$i is multiple of 3 ", "The number \$i is multiple of 5")
    println()
}

fun mynums(text1: String, text2: String): Int {
    var count = 0
    for (i in 1..100) {
        when {
            i % 3 == 0 && i % 5 == 0 -> println(
                "${
                    text1.replace(
                        "\$i", i.toString()
                    )
                } ${text2.replace("\$i", i.toString())}"
            )

            i % 3 == 0 -> println(text1.replace("\$i", i.toString()))
            i % 5 == 0 -> println(text2.replace("\$i", i.toString()))
            else -> {
                println(i)
                count += 1
            }
        }
    }
    return count
}

//DIFICULTAD EXTRA (opcional):
//* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.




