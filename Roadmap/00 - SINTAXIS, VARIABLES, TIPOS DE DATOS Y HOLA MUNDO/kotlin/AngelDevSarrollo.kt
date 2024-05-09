fun main() {
    // caracteres
    val caracter: Char = '\u0040'
    val decimal: Char = 64.toChar()
    println("caracter = $caracter")
    println("decimal = $decimal")
    println("decimal = caracter: ${decimal == caracter}")

    val simbolo: Char = '@'
    println("simbolo = $simbolo")
    println("simbolo = caracter: ${simbolo == caracter}")

    val espacio: Char = '\u0020'
    val retroceso: Char = '\b'
    val tabulador: Char = '\t'
    val nuevaLinea: Char = '\n'
    val retornoCarro: Char = '\r'

    println("char corresponde en byte:\n${Character.BYTES}")
    println("Char corresponde en bits = ${Character.SIZE}")
    println("Character.MIN_VALUE = ${Character.MIN_VALUE}")
    println("Character.MAX_VALUE = ${Character.MAX_VALUE}")

    // Enteros y flotantes
    val numeroByte: Byte = 127
    println("numeroByte = $numeroByte")
    println("tipo byte corresponde en byte a ${Byte.BYTES}")
    println("tipo byte corresponde en bits a ${Byte.SIZE}")
    println("valor máximo de un byte: ${Byte.MAX_VALUE}")
    println("valor mínimo de un byte: ${Byte.MIN_VALUE}")

    val numeroShort: Short = 32767
    println("numeroShort = $numeroShort")
    println("tipo short corresponde en byte a ${Short.BYTES}")
    println("tipo short corresponde en bits a ${Short.SIZE}")
    println("valor máximo de un short: ${Short.MAX_VALUE}")
    println("valor mínimo de un short: ${Short.MIN_VALUE}")

    val numeroInt: Int = 2147483647
    println("numeroInt = $numeroInt")

    println("tipo int corresponde en byte a ${Integer.BYTES}")
    println("tipo int corresponde en bits a ${Integer.SIZE}")
    println("valor máximo de un int: ${Integer.MAX_VALUE}")
    println("valor mínimo de un int: ${Integer.MIN_VALUE}")

    val numeroLong: Long = 9223372036854775807L
    println("numeroLong = $numeroLong")

    println("tipo long corresponde en byte a ${Long.BYTES}")
    println("tipo long corresponde en bits a ${Long.SIZE}")
    println("valor máximo de un long: ${Long.MAX_VALUE}")
    println("valor mínimo de un long: ${Long.MIN_VALUE}")

    val numeroVar = 9223372036854775808f

    // booleanos
    var datoLogico = true
    println("datoLogico = $datoLogico")

    val d = 98765.43e-3 // 98.76543
    println("d = $d")

    val f = 1.2345e2f // 123.45
    println("f = $f")

    datoLogico = d < f
    println("datoLogico = $datoLogico")

    val esIgual = 3 - 2 == 1
    println("esIgual = $esIgual")

    val nombre = "AngelDev"

}