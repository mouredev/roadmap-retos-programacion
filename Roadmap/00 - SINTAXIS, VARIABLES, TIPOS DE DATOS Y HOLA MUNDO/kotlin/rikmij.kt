//Con la doble barra creas un comentario de 1 sola línea
/*
Con estos símbolos se crea el comentario de varias líneas
En esta segunda línea agrego la web de Kotlin que es https://kotlinlang.org/
*/

//constantes y variables en Kotlin
val constante = "Soy una constante porque llevo val delante"

var variable = "Soy una variable declarada con var"


fun main() {
    /*Creando variables de distintos tipos
En Kotlin las variables se inician con camel case por convención
*/
    //Se puede cambiar por estar dentro de main, si no no se podría cambiar
    var tipoStr = "Esta variable va a ser cambiada"
    tipoStr = "Kotlin"

    var tipoNumEntero = 33

    var tipoDoub = 3.1415

    // Es un float porque lleva una f al final, si no sería Double
    var tipoFl = 3.1415f

    var tipoBool = true

    var tipoNulo = null

    var tipoArStr = arrayOf("Gracias", "por esto", "eres grande", "Moure")

    var tipoArNum = arrayOf(1, 2, 3, 4, 5)

    //Para imprimir hay que declarar la función main, si no no imprime
    println("Hola, $tipoStr")
}
