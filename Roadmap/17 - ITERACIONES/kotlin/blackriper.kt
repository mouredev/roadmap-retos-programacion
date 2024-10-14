/*
Interaciones
Es una forma  para poder recorrer una lista de elementos de una coleccion
*/

fun exampleWithIterators(){
  val list = listOf(1,2,3,4,5,6,7,8,9,10)

  // foreach
  println("using foreach")
  list.forEach { println(it) }

  // for convencional
  println("using for")
  for (i in list){
      println(i)
  }

  // while
  println("using while")
  var i = 0
  while (i < list.size){
      println(list[i])
      i++
  }

}

fun exampleWithOthersIterators(){
 val list = listOf(1,2,3,4,5,6,7,8,9,10)

    // utilizando el iterator
    println("using iterator")
    for (item in list.iterator()){
        println(item)
    }

    // utilizando el listIterator
    println("using listIterator")
    val listIterator= list.listIterator()
    while (listIterator.hasNext()){
        println(listIterator.next())
    }

    // usando do while
    println("using do while")
    var i = 0
    do {
        println(list[i])
        i++
    }while (i < list.size)

    // usando el map por lo general es para hacer algun cambio sobre la lista sin mutar el array original
    println("using map")
    list.map { println(it) }

    // for con rango
    println("using for with range")
    for (num in 1..10){
        println(num)
    }


}


fun main() {
    exampleWithIterators()
    exampleWithOthersIterators()
}
