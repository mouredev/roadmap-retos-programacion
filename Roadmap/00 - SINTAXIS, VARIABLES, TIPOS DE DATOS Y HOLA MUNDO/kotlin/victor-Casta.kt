fun main() {
  //Sitio oficial: https://kotlinlang.org/
  
  //Tipos de comentarios
  //Comentarios de una linea
  /*
    Comentarios en varias lineas 
  */
  
  //variables y constantes
  var a: String = "hello";
  val LANGUAGE: String = "Kotlin";
  
  //Datos primitivos
      // Números
      val byte: Byte = 127;
      val short: Short = 32767;
      val int: Int = 2147483647;
      val long: Long = 9223372036854775807;
      val float: Float = 2.7182818284f;
      val double: Double = 1.8e+308;
      // Caracteres
      val char: Char = 'a';
      // Cadenas
      val string: String = "Hola, mundo";
      // Booleanos
      val boolean: Boolean = true;

  
  println("¡${a}, ${LANGUAGE}!")
  
}