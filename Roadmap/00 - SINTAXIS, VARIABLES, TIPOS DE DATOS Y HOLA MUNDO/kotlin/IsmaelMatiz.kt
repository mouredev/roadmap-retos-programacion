//pagina oficial https://kotlinlang.org/
/*
* comentario de varias lineas
* */

/**
 * Kdoc lo mismo que Javadoc pero en kotlin
 */
fun main(args: Array<String>) {
      //variable
      var name: String

      //constante
      val str1: String

      /*
       * Variable primitivas, en teoria son las mismas de Java pero aqui es como si siempre
       * usaramos los wrappers y pues no es tan necesario especificarlos excepto
       * quizas en los casos de short y byte
       */
      val c: Char = 'c' //acepta cualquier caracter Unicode

      val i: Int = 50 //acepta enteros con signo desde -2.147.483.648 hasta 2.147.483.649

      val s: Short = -32768 // acepta enteros con signo desde -32.768 hasta 32.767

      val l: Long = -9223372036854775807L // acepta enteros con signo desde -9.223.372.036.854.775.807 hasta 9.223.372.038.854.775.807

      val f: Float = 7.233433f // acepta hasta 6 decimales

      val d: Double = 3.14159 // acepta hasta 14 decimales

      val b: Boolean = true //True or false

      val byte1: Byte = -128 // acepta enteros con signo desde -128 hasta 127


      println("¡Hola, Kotlin!")

}
