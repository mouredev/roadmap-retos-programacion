// link oficial de lenguaje SCALA
// https://www.scala-lang.org/

// link no oficial para hacer compilacion en linea para pruebas antes de instalar
// https://scastie.scala-lang.org/

//sintaxis de comentarios
//comentario en Scala de una sola linea
/* comentario en Scala
de
multiples lineas
 */

/** Este es comentario de tipo JavaDoc se puede tags como @param, @return,
  * \@throws, etc. entremezclado con el comentario.
  */

object variables {
// variable ejemplo
  val b: Int = 25 // tipo de dato : Int
  var c: Double = 34.67 // tipo de dato : Double (
  // se pueden asignar y cambiar su valor)

}

object constantes {
//constante
  val pi =
    scala.math.Pi // la constante Pi es un valor numerico que representa el valor representado en matematica por la letra griega π,

}

//imprimo en terminal saludo

object HolaScala {

  val scala = "scala"

  def main(): Unit = {
    println("Hola " + scala + "!")
  }
}

HolaScala.main()
