 /*
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
  
val PI = 3.14

fun main() {
    // Función sin parámetros ni valor de retorno:
    helloWorld()
    // Funcion con parametros sin valor de retorno
    saludar("Adrian")
    // Función con parámetros y valor de retorno:
    val resultado = sumar(10, 6)
    println(resultado)
    // Funcion con parametros por defecto
    restar()
    // Funcion propia del lenguaje
    val texto: String = "HOLA"
    println(texto.lowercase())

    println("El valor de pi es $PI")

    val veces = retoExtra("Fizz", "Buzz")
    println("Veces: $veces")
}

fun retoExtra(cadena1: String, cadena2: String): Int {
    var contador = 0

    for (i in 1..100) {
        if (i % 3 == 0 && i % 5 == 0) 
            println("$cadena1$cadena2")
        else if (i % 3 == 0) 
            println(cadena1)
        else if (i % 5 == 0) 
            println(cadena2)
        else{
            println(i)
            contador++
        } 
    }

    return contador
}

fun helloWorld(){
    println("Hola mundo!")
}

fun saludar(nombre: String){
    println("Bienvenido $nombre")
}

fun sumar(a: Int, b: Int): Int{
    println("La suma de $a + $b es igual a ${a + b}")
    return a + b
}

fun restar(a: Int = 5, b: Int = 1){
    println("La resta de $a - $b es igual a ${a - b}")
}