fun main() {
    println("¡Hola Mundo!")

    val nombre: String = "Juan"
    var edad: Int = 30
    val altura: Double = 1.75
    var esEstudiante: Boolean = true

    println("Nombre: $nombre")
    println("Edad: $edad")
    println("Altura: $altura")
    println("¿Es estudiante? $esEstudiante")

    val nombre = "María"
    val edad = 25

    println("Hola, mi nombre es $nombre y tengo $edad años.")

    val numeroEntero: Int = 42
    val numeroLong: Long = numeroEntero.toLong()
    val numeroDouble: Double = 3.14
    val numeroFloat: Float = numeroDouble.toFloat()

    println("Número entero: $numeroEntero")
    println("Número long: $numeroLong")
    println("Número double: $numeroDouble")
    println("Número float: $numeroFloat")

    val PI = 3.14159
    val nombre: String? = null // Permitir valores nulos

    println("El valor de PI es $PI")
    println("Nombre: $nombre")
}