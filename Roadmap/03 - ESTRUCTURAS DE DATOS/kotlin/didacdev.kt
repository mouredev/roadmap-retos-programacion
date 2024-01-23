fun main() {

// ---------- Array ------------
/*
    - Número fijo de datos del mismo tipo
*/
    val array = arrayOf(0, 1, 2, 3, 4)

    // Obtener
    println(array[2])

// ----------- List -----------
/*
    - Almacena elementos en un orden especificado
*/
    val immutableList = listOf(0, 1, 2, 3, 4)
    val mutableList = mutableListOf(0, 3, 6, 2, 4)

    // Obtener
    println(immutableList.get(2))
    println(immutableList[2])

    // Añadir
    mutableList.add(1)

    // Eliminar
    mutableList.removeAt(2)

    // Actualizar
    mutableList[0] = 5

    println(mutableList)

    // Ordenar
    mutableList.sort()
    println(mutableList)

// -------- Set -------------
/*
    - Almacena elementos no repetidos
    - No tienen un orden definido
*/

    val immutableSet = setOf(1, 2, 3, 4)
    val mutableSet = mutableSetOf(2, 1, 5, 4)

    // Añadir
    mutableSet.add(3)

    // Eliminar
    mutableSet.remove(1)

    println(mutableSet)

    // Ordenar
    val ordenado = mutableSet.sorted()
    println(ordenado)

// ----------------- Map -------------
/*
    - Almacena pares clave-valor del mismo tipo
    - Claves únicas
*/
    val immutableMap = mapOf(1 to "pepe", 2 to "juan")
    val mutableMap = mutableMapOf(2 to "pepe", 1 to "juan")

    // Añadir
    mutableMap.put(3, "pedro")
    mutableMap[0] = "ana"

    // Actualizar
    mutableMap[1] = "paco"

    // Eliminar
    mutableMap.remove(0)

    println(mutableMap)

    // Ordenar
    val mapOrdenado = mutableMap.toSortedMap()

    println(mapOrdenado)

// -------------- ArrayDeque ----------------
/*
    - Implementación de cola y pila
    - permite añadir y eliminar el primer o último elemento
*/
    val deque = ArrayDeque(listOf(1, 2, 3, 4))

    // Añadir
    deque.addFirst(0)
    deque.addLast(5)

    println(deque)

    // Obtener
    println(deque.first())
    println(deque.last())

    // Eliminar
    deque.removeFirst()
    deque.removeLast()

    println(deque) 

    agenda()

}

fun agenda() {
    println("--------------")
    println("    Agenda    ")
    println("--------------")
    val agenda = mutableMapOf<String, Int>()
    var quit = false

    while(!quit) {
        println("")
        println("1 - Buscar")
        println("2 - Insertar")
        println("3 - Actualizar")
        println("4 - Eliminar")

        val entrada = readLine()

        if (entrada != null) {
            when (entrada) {
                "1" -> search(agenda)
                "2" -> insert(agenda)
                "3" -> update(agenda)
                "4" -> delete(agenda)
                else -> println("Opción incorrecta")
            }
        } else {
            println("No has introducido nada.")
        }
    }
}

fun search(agenda: MutableMap<String, Int>) {
    println("")
    println("Nombre del contacto:")

    val contactName = readLine()

    if (contactName != null) {
        val contact = agenda[contactName]
        
        if (contact != null) {

            println(" $contactName: $contact")
        } else {
            println("No existe el contacto")
        }
    } 
}

fun  insert(agenda: MutableMap<String, Int>) {
    var name: String = ""
    var number: Int

    println("")
    println("Nombre del contacto:")

    val contactName = readLine()

    if (contactName != null) {
        name = contactName
    } else {
        println("No existe el contacto")
    }

    println("Número del contacto: ")
    val contactNumber = readLine()
    val numberInt = contactNumber?.toInt()

    number = if (numberInt != null) numberInt else 0

    agenda[name] = number

    print("$name: $number")

}

fun update(agenda: MutableMap<String, Int>) {
    println("")
    println("Nombre del contacto:")

    val contactName = readLine()

    if (contactName != null) {
        if (agenda[contactName] != null){
            println("Nuevo número:")
            val newNumber = readLine()

            val numberInt = newNumber?.toInt()

            if (numberInt != null) {
                agenda[contactName] = numberInt
            }
        } else {
            println("No existe el contacto")
        }
    } else {
        println("No se ha introducido nada")
    }
}

fun delete(agenda: MutableMap<String, Int>) {
    println("")
    println("Nombre del contacto")

    val contactName = readLine()

    if (contactName != null) {
        if (agenda[contactName] != null) {
            agenda.remove(contactName)
        } else {
            println("No existe el contacto")
        }
    }
}
