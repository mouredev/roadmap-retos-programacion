private def countWithCount(string: String, char: Char): Int = string.count(_ == char)

@main def hello(): Unit =
  println("Interpolación de cadenas.  Uso de variables dentro de las cadenas")
  // Dadas estas dos variables inmutables
  val nombre : String = "Edwin"
  val apellido : String = "Martinez"
  // Se pueden combinar en una cadena 
  println(s"Nombre Completo: $nombre $apellido")
  /* Se precede la cadena con la letra s y se antepone el símbolo $ antes de cada nombre de variable
     Dentro de la cadena. 
     Scala provee tres métodos de interpolación de cadenas s, f y raw
     Estos métodos están explicados en https://docs.scala-lang.org/scala3/book/string-interpolation.html   
  */
  // Uso del interpolador f
  val altura: Float = 1.7
  println(f"$nombre%s es de $altura%2.2f metros de altura")
  // Uso del interpolador raw
  println(raw"a\nb")
  // Para embeber expresiones dentro de una cadena, se encierran entre llaves {}
  println(s"La suma de (2 + 2) es ${2 + 2}")
  println("")

  println("Cadenas Multilínea.  Son creadas incluyendo dentro de la cadena tres comillas dobles o comillas inglesas")
  val mensaje : String = """Este es un mensaje de múltiples
  líneas como ejemplo en Scala"""
  println(mensaje)
  // Cadenas multilinea con interpolación
  val edad: Int = 40
  println(s"""Nombre: "$nombre",
             |Edad: $edad""".stripMargin)

  /* En Scala las cadenas no son secuencias directas pero se pueden convertir en ellas, y también 
     admiten todas las operaciones de secuencias */
  println("")
  println("Operaciones con cadena")
  val original = "anita lava la tinA"
  println(s"Cadena Original: $original")
  println(s"Cadena Invertida: ${original.reverse}")
  println(s"Longitud de la cadena: ${original.length()}")
  println(s"Cadena en mayúscula: ${original.toUpperCase()}")
  println(s"Cadena en minúscula: ${original.toLowerCase()}")
  println(s"Cadena Capitalizada: ${original.capitalize}")
  val otraCadena = "Todos los días"
  println("Concatenando cadenas")
  println(original + " " + otraCadena.toLowerCase())
  println(original ++ " " ++ otraCadena.toLowerCase())
  println("Repetición de Cadenas")
  println("Hola"*(5))

  /* Las cadenas tienen una longitud y sus elementos tienen índices 
     de posición fija que comienzan en 0*/
  println("")
  println(s"Cadena Original: $original")
  println(s"Caracter en la posición 3: ${original.apply(3)}")
  println(s"La cadena contiene el caracter 'x': ${if original.contains('x') then "Verdadero" else "Falso"}")
  println(s"La cadena contiene el caracter 't': ${if original.contains('t') then "Verdadero" else "Falso"}")
  println(s"La cadena tiene ${countWithCount(original.toLowerCase(),'a')} 'a' o 'A'")
  println(s"Caracteres distintos usados en la cadena: ${original.distinct}")
  println(s"Primer Caracter: ${original.head}")
  println(s"Último Caracter: ${original.last}")
  println(s"Rellenar la cadena con *: ${original.padTo(25, '*')}")
  println(s"Obtener una parte de la cadena: ${original.slice(6, 10)}")
