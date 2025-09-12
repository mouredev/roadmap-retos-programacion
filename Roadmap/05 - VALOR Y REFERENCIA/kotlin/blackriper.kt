/*
   En Kotlin no se pueden usar referencias o punteros a memoria , se utiliza la referencia de objeto para representar una ubicación de memoria.
   Las referencias de objeto son seguras por defecto, ya que no es posible que apunten a una
   ubicación de memoria que ya no contenga datos. Esto se debe a que Kotlin utiliza el sistema
   de recolección de basura para gestionar la memoria. Cuando un objeto ya no se utiliza, se
   elimina de la memoria y las referencias a ese objeto se vuelven nulas.
*/

// en kotlin tenemos dos referencias de objetos val y var
val a=1
var b=1

fun test() {
   // a=2 marca error porque a es val y no se puede reasignar
    b=2
}

// extra
fun changeParams( p1:Int) {
    //a=p1 marca error porque a es val y no se puede reasignar
    b=a
    b=p1
}


fun main() {
    val c=b
    test()
    println(b)
    changeParams(5)
    // a siempre sera inmutable mientras b cambia de acuerdo a su referencia de objeto perdiendo el valor original a menos que se conserve en otra variable
    println(b)
    println(a)
    println(c)
}
