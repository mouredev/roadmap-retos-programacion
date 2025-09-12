/*
 conjunto: coleccion de elementos considerados como un objeto los mismos pueden ser de diferentes tipos
 no siempre son una coleccion ordenada.

 operaciones de conjuntos
  -Unión: operacion que combina dos conjuntos o mas para formar un nuevo conjunto cuyos elementos son todos los elementos de los conjuntos originales
  -Intersección: operacion que contienen elementos comunes entre dos conjuntos dando como resultado un nuevo conjunto
  -Diferencia: operacion que cuyo conjunto resultante son los elementos comunes entre dos conjuntos originales
  -Diferencia simetrica: operacion que cuyo conjunto resultante son los elementos que no son  comunes en ambos conjuntos


*/

fun basicOperations() {
    val listNumbers = mutableListOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    // add element
    listNumbers.add(11)
    println(listNumbers)
    // add element at start position
    listNumbers.add(0, 0)
    println(listNumbers)
    // adding multiple elements
    listNumbers.addAll(listOf(12, 13, 14))
    println(listNumbers)
    // add element at specific position
    listNumbers.addAll(3, listOf(15, 16, 17))
    println(listNumbers)
    // delete element
    listNumbers.removeAt(3)
    println(listNumbers)
    // update element
    listNumbers[4] = 4
    println(listNumbers)
    // find element
    println(listNumbers.contains(17))
    // delete all elements
    listNumbers.clear()
    println(listNumbers)
}

fun operationsWithConjuntos() {
    val characters = mutableListOf("cell","majin boo","yanemba","freezer","broly","cooler","slug")
    val characters2 = mutableListOf("cell","majin boo","gohan","freezer","broly","cooler","goten")

    // union
    val union = characters.union(characters2)
    println(union)

    // intersection
    val intersection = characters.intersect(characters2)
    println(intersection)

    // difference
    val difference = characters.subtract(characters2)
    println(difference)

    // symmetric difference
    val symmetricDifference = characters.filter {  !characters2.contains(it)  }.union(characters2.filter { !characters.contains(it) })
    println(symmetricDifference)


}


fun main() {
  basicOperations()
  operationsWithConjuntos()
}
