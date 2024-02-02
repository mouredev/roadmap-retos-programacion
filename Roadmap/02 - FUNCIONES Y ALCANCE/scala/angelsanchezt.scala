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

 // Funciones definidas por el usuario
 object Main {
  // Variable GLOBAL
  val variableGlobal: String = "Soy global"

  def main(args: Array[String]): Unit = {
    // Llamada a una función ya creada en el lenguaje
    println(s"Longitud de 'Hola, Scala!': ${longitud("Hola, Scala!")}")

    // Funciones básicas
    funcionSinParametrosNiRetorno()
    funcionConParametro(42)
    val resultado = funcionConRetorno(5)
    println(s"Resultado de la función con retorno: $resultado")

    // Variable LOCAL
    val variableLocal: Int = 100

    // Función dentro de función
    def funcionAnidada(): Unit = {
      println("Función anidada")
    }

    funcionAnidada()

    // Dificultad EXTRA
    val texto1 = "Fizz"
    val texto2 = "Buzz"
    val vecesImpreso = imprimirNumerosConTexto(texto1, texto2)
    println(s"La función se ejecutó $vecesImpreso veces")
  }

  // Función sin parámetros ni retorno
  def funcionSinParametrosNiRetorno(): Unit = {
    println("Función sin parámetros ni retorno")
  }

  // Función con parámetro
  def funcionConParametro(numero: Int): Unit = {
    println(s"Función con parámetro: $numero")
  }

  // Función con retorno
  def funcionConRetorno(numero: Int): Int = {
    println(s"Función con retorno: $numero")
    numero * 2
  }

  // Función ya creada en el lenguaje
  def longitud(texto: String): Int = {
    texto.length
  }

  // Función con dificultad EXTRA
  def imprimirNumerosConTexto(texto1: String, texto2: String): Int = {
    var contador = 0
    for (i <- 1 to 100) {
      if (i % 3 == 0 && i % 5 == 0) {
        println(texto1 + texto2)
      } else if (i % 3 == 0) {
        println(texto1)
      } else if (i % 5 == 0) {
        println(texto2)
      } else {
        println(i)
        contador += 1
      }
      
    }
    contador
  }
}
