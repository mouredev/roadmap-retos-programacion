fun main() {
    // Creamos un conjunto mutable
    val conjunto = mutableListOf("A", "B", "C")
    println("Conjunto inicial: $conjunto")

    // Añade un elemento al final
    conjunto.add("D")
    println("Después de añadir al final: $conjunto")

    // Añade un elemento al principio
    conjunto.add(0, "Z")
    println("Después de añadir al principio: $conjunto")

    // Añade varios elementos en bloque al final
    conjunto.addAll(listOf("E", "F", "G"))
    println("Después de añadir en bloque al final: $conjunto")

    // Añade varios elementos en bloque en una posición concreta
    conjunto.addAll(2, listOf("X", "Y"))
    println("Después de añadir en bloque en posición 2: $conjunto")

    // Elimina un elemento en una posición concreta
    conjunto.removeAt(3)
    println("Después de eliminar el elemento en posición 3: $conjunto")

    // Actualiza el valor de un elemento en una posición concreta
    conjunto[1] = "W"
    println("Después de actualizar el elemento en posición 1: $conjunto")

    // Comprueba si un elemento está en un conjunto
    println("¿El conjunto contiene 'F'? ${conjunto.contains("F")}")

    // Elimina todo el contenido del conjunto
    conjunto.clear()
    println("Después de eliminar todo el contenido: $conjunto")

    // DIFICULTAD EXTRA
    val conjunto1 = setOf(1, 2, 3, 4, 5)
    val conjunto2 = setOf(4, 5, 6, 7, 8)

    // Unión
    val union = conjunto1.union(conjunto2)
    println("Unión: $union")

    // Intersección
    val interseccion = conjunto1.intersect(conjunto2)
    println("Intersección: $interseccion")

    // Diferencia
    val diferencia = conjunto1.subtract(conjunto2)
    println("Diferencia (conjunto1 - conjunto2): $diferencia")

    // Diferencia simétrica
    val diferenciaSimetrica = conjunto1.symmetricDifference(conjunto2)
    println("Diferencia simétrica: $diferenciaSimetrica")
}

// Función de extensión para calcular la diferencia simétrica
fun Set<Int>.symmetricDifference(other: Set<Int>): Set<Int> {
    return (this subtract other) union (other subtract this)
}