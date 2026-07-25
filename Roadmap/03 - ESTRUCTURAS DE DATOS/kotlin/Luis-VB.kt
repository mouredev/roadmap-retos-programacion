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
    println("Third word of my list is ${myList.get(2)}")       // Access element at index 2
    println("Index of element \"Ja jsem\" ${myList.indexOf("Ja jsem")}")    // Index of element "Ja jsem"
    println("Is \"Ja jsem\" in the list? ${myList.contains("Ahoj")}")    // Check if "Ahoj" is in the list
    println("Is the list empty? ${myList.isEmpty()}")    // Check if the list is empty
    println(myList.sortedBy { it })         // Sort the list alphabetically
    println()

    //# List editable
    var myEditList = mutableListOf<Int>(1,2,3,4)
    println(myEditList)
    myEditList.add(5)                // Insert 5
    println(myEditList)
    myEditList.removeAt(2)      // Remove element at index 2
    println(myEditList)
    println(myEditList[0])                   // Access element at index 0
    println(myEditList)
    myEditList[0] = 10              // Update element at index 0
    println(myEditList)
    myEditList.shuffle()            // Shuffle the list
    println(myEditList)
    println()

    //# Set
    var mySet = setOf<Int> (78,15,46,11,23,1)           // Set
    println(mySet)
    println(mySet.sorted())                     // Sort the set
    println()
    //# Set editable
    var myEditSet = mutableSetOf<Any> (1,"Hola", 3, "mystringhere")
    println(myEditSet)
    myEditSet.add(345)                  // Insert 345
    println(myEditSet)
    myEditSet.add("OH lala")           // Insert "OH la la"
    println(myEditSet)
    myEditSet.remove(1)         // Remove 1
    println(myEditSet)
    println(myEditSet.contains(3))     // Check if 3 is in the set
    println(myEditSet.isEmpty())       // Check if the set is empty


    //# Maps
    val users = listOf(
        mapOf("name" to "Luis", "Surname" to "Barrera", "Alias" to "Tunnetopper", "Age" to 41),
        mapOf("name" to "Paco", "Surname" to "Alcaraz", "Alias" to "Chopito", "Age" to 24),
        mapOf("name" to "Marta", "Surname" to "Garcia", "Alias" to "MvA", "Age" to 37),
        mapOf("name" to "Lucia", "Surname" to "Areso", "Alias" to "Lucha", "Age" to 21),
        mapOf("name" to "Javier", "Surname" to "Onesa", "Alias" to "Javi", "Age" to 31)
    )
    //    Lambda expression to print the name and age of each user
    users.forEach { user ->
        println("Name: ${user["name"]}, Age: ${user["Age"]}")
    }
    //    Lambda expression to print the name and age of each user over 30
    users.filter { (it["Age"] as Int) > 30 }
        .forEach { user ->
            println("Name: ${user["name"]}, Age: ${user["Age"]}")
        }

}

fun main () {

    myDataStructures()
}