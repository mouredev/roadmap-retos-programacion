// Ejemplos simples de funciones de orden superior

// 1. Función que recibe otra función como parámetro
fun operacion(a: Int, b: Int, funcion: (Int, Int) -> Int): Int {
    return funcion(a, b)
}

// 2. Función que devuelve otra función
fun multiplicadorPor(factor: Int): (Int) -> Int {
    return { numero -> numero * factor }
}

fun main() {
    // Uso de la función 'operacion'
    val suma = operacion(5, 3) { x, y -> x + y }
    println("Suma: $suma")

    val multiplicacion = operacion(5, 3) { x, y -> x * y }
    println("Multiplicación: $multiplicacion")

    // Uso de la función 'multiplicadorPor'
    val duplicar = multiplicadorPor(2)
    println("Duplicar 7: ${duplicar(7)}")

    // Ejercicio Extra
    data class Estudiante(
        val nombre: String,
        val fechaNacimiento: String,
        val calificaciones: List<Double>
    )

    val estudiantes = listOf(
        Estudiante("Ana", "2000-05-15", listOf(8.5, 9.0, 9.5, 10.0)),
        Estudiante("Carlos", "1999-11-30", listOf(7.0, 8.0, 8.5, 9.0)),
        Estudiante("Elena", "2001-03-22", listOf(9.0, 9.5, 10.0, 10.0)),
        Estudiante("David", "2000-09-10", listOf(6.5, 7.0, 7.5, 8.0))
    )

    // Promedio calificaciones
    val promedios = estudiantes.map { estudiante ->
        val promedio = estudiante.calificaciones.average()
        "${estudiante.nombre}: ${"%.2f".format(promedio)}"
    }
    println("Promedios: $promedios")

    // Mejores estudiantes
    val mejoresEstudiantes = estudiantes.filter { 
        it.calificaciones.average() >= 9.0 
    }.map { it.nombre }
    println("Mejores estudiantes: $mejoresEstudiantes")

    // Nacimiento (ordenado desde el más joven)
    val ordenPorEdad = estudiantes.sortedByDescending { it.fechaNacimiento }
        .map { it.nombre }
    println("Orden por edad (más joven primero): $ordenPorEdad")

    // Mayor calificación
    val mayorCalificacion = estudiantes.flatMap { it.calificaciones }.maxOrNull()
    println("Mayor calificación: $mayorCalificacion")
}