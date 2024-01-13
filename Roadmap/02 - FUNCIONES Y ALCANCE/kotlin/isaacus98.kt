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

private var VariableGlobal: Int = 1000

fun main(){
    funcionSinRetorno()

    funcionSinRetornoConUnParametro("Hola")

    funcionSinRetornoConDosParametros("parámetro 1", "parámetro 2")

    // Función con parámetro opcional definido
    funcionSinRetornoConParametroOpcional("Hola");
    // Función con parámetro opcional en el qual no se ha definido el parámetro
    funcionSinRetornoConParametroOpcional();

    funcionSinRetornoVarArgs(1, 2, 3, 4, 5)
    funcionSinRetornoVarArgs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    println(suma(4, 6))

    imprimirArea(5, 5)

    // Función lambda
    val sum: (Int, Int) -> Int = { x: Int, y: Int -> x + y }
    println(sum(5,8))

    // Función del propio lenguaje
    val str: String = "hola"
    println(str.uppercase()) // Función uppercase: Convierte la minúsculas en mayúsculas

    // Función global
    // Las variables globales se pueden usar en todas las funciones de la classe.
    // Las variables locales solo se pueden usar dentro de la función donde se han definido.
    println(VariableGlobal);

    // Reto extra
    println("Se ha impreso un total de ${retoExtra("FIZZ", "BUZZ")} de numeros")
}

fun retoExtra(str1: String, str2: String): Int {
    var contador: Int = 0
    for (i in 1..100){
        when{
            i % 15 == 0 -> println("$str1  $str2")
            i % 3 == 0 -> println(str1)
            i % 5 == 0 -> println(str2)
            else -> {
                println(i)
                contador++
            }
        }
    }

    return  contador
}

// Función sin parámetros
fun funcionSinRetorno(){
    println("Función sin retorno")
}

// Función con 1 parámetro
fun funcionSinRetornoConUnParametro(str: String){
    println(str)
}

// Función con 2 parámetros
fun funcionSinRetornoConDosParametros(str1: String, str2: String){
    println("Primer parametro: $str1")
    println("Segundo parametro: $str2")
}

// Función con parámetro opcional
fun funcionSinRetornoConParametroOpcional(parametroOpcional: String = "parametro opcional"){
    println(parametroOpcional)
}

// Función con número de parámetros variable
fun funcionSinRetornoVarArgs(vararg listaNumeros: Int){
    println(listaNumeros.sum())
}

// Función que devuelve valor
fun suma(num1: Int, num2: Int) : Int {
    return num1 + num2
}

// Función dentro de función
fun imprimirArea(ancho: Int, altura: Int): Unit {
    fun calcularArea(ancho: Int, altura: Int): Int {
        return ancho * altura
    }
    val area = calcularArea(ancho, altura)
    println("El area es $area")
}
