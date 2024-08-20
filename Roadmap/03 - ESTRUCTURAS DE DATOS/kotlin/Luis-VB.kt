import com.sun.jdi.IntegerType

//*
//* EJERCICIO:
//* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
//* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
//*
//* DIFICULTAD EXTRA (opcional):
//* Crea una agenda de contactos por terminal.
//* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//* - Cada contacto debe tener un nombre y un número de teléfono.
//* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//*   los datos necesarios para llevarla a cabo.
//* - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
//*   (o el número de dígitos que quieras)
//* - También se debe proponer una operación de finalización del programa.
//*/

// List
fun myDataStructures () {
    //# List
    var myList = listOf<String>("Ahoj","Ja jsem","dobre","aitjak")
    println(myList)
    println("Number of elements: ${myList.size}")   // Number of elements
    println("Third word is ${myList.get(2)}")       // Access element at index 2
    println("Index of element \"Ja jsem\" ${myList.indexOf("Ja jsem")}")    // Index of element "Ja jsem"

    //# List editable
    var myEditList = mutableListOf<Int>(1,2,3,4)
    println(myEditList)
    println(myEditList.add(5))                  // Insert 5 at the end
    println(myEditList.removeAt(2))             // Remove element at index 2
    println(myEditList[0])                      // Access element at index 0
    println(myEditList.shuffle())               // Shuffle the list

    //# Set
    var mySet = setOf<Int> (1,2,3,4,5)           // Set
    println(mySet)
    println(mySet.sorted())                     // Sort the set

    //# Set editable
    var myEditSet = mutableSetOf<Any> (1,"Hola", 3, "mystringhere")         // Editable set
    println(myEditSet.add(1))                   // Insert 1
    println(myEditSet.add("OH lala"))           // Insert "OH la la"
    println(myEditSet.remove(1))                // Remove 1
    println(myEditSet.contains(3))              // Check if 3 is in the set
    println(myEditSet.isEmpty())                // Check if the set is empty

    //# Map
    var myMap = mapOf<K,V>("name" to "Luis", "Surname" to "Barrera", "Alias" to "Tunnetopper", "Age" to "41")
}

fun main () {

    myDataStructures()
}