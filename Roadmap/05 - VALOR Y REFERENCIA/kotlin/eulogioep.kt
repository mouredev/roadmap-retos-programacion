fun main() {
    println("1. Asignación de variables por valor y por referencia:")
    // Por valor (tipos primitivos)
    var numero1 = 5
    var numero2 = numero1
    numero2 = 10
    println("  Por valor:")
    println("  numero1: $numero1") // 5
    println("  numero2: $numero2") // 10

    // Por referencia (objetos)
    data class Persona(var nombre: String)
    val persona1 = Persona("Alice")
    val persona2 = persona1
    persona2.nombre = "Bob"
    println("  Por referencia:")
    println("  persona1.nombre: ${persona1.nombre}") // Bob
    println("  persona2.nombre: ${persona2.nombre}") // Bob

    println("\n2. Funciones con parámetros por valor y por referencia:")
    // Función con parámetro por valor
    fun incrementar(x: Int): Int {
        return x + 1
    }

    var a = 5
    println("  Por valor:")
    println("  Antes de incrementar: $a")
    a = incrementar(a)
    println("  Después de incrementar: $a")

    // Función con parámetro por referencia
    fun cambiarNombre(persona: Persona, nuevoNombre: String) {
        persona.nombre = nuevoNombre
    }

    val persona = Persona("Charlie")
    println("  Por referencia:")
    println("  Antes de cambiar nombre: ${persona.nombre}")
    cambiarNombre(persona, "David")
    println("  Después de cambiar nombre: ${persona.nombre}")

    println("\n3. Programa que intercambia valores por valor:")
    fun intercambiarPorValor(a: Int, b: Int): Pair<Int, Int> {
        return Pair(b, a)
    }

    var original1 = 10
    var original2 = 20
    println("  Originales antes: $original1, $original2")

    val (nuevo1, nuevo2) = intercambiarPorValor(original1, original2)
    println("  Originales después: $original1, $original2")
    println("  Nuevas variables: $nuevo1, $nuevo2")

    println("\n4. Programa que intercambia valores por referencia:")
    data class Contenedor(var valor: Int)

    fun intercambiarPorReferencia(a: Contenedor, b: Contenedor): Pair<Contenedor, Contenedor> {
        val temp = a.valor
        a.valor = b.valor
        b.valor = temp
        return Pair(Contenedor(a.valor), Contenedor(b.valor))
    }

    val originalRef1 = Contenedor(10)
    val originalRef2 = Contenedor(20)
    println("  Originales antes: ${originalRef1.valor}, ${originalRef2.valor}")

    val (nuevoRef1, nuevoRef2) = intercambiarPorReferencia(originalRef1, originalRef2)
    println("  Originales después: ${originalRef1.valor}, ${originalRef2.valor}")
    println("  Nuevas variables: ${nuevoRef1.valor}, ${nuevoRef2.valor}")
}