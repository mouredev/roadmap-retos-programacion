fun main() {
    // List
    val list = mutableListOf("Java", "C", "Python")
    list.add("Kotlin")
    list.remove("Java")
    list[1] = "C#"
    val sortedList = list.sorted()
    println(sortedList)

    // Set
    val set = mutableSetOf("Java", "C", "Python")
    set.add("Kotlin")
    set.remove("Java")
    val sortedSet = set.sorted()
    println(sortedSet)

    // Map
    val map = mutableMapOf("A" to "Java", "B" to "C", "C" to "Python")
    map["D"] = "Kotlin"
    map.remove("A")
    map["B"] = "C#"
    val sortedMap = map.toSortedMap()
    println(sortedMap)

    agendaTelefonica()
}

// ------------ Agenda Telefonica ------------

val contacts = mutableMapOf<String, Int>()

fun agendaTelefonica() {
    while (true) {
        println("¿Qué operación quieres realizar?")
        println("1. Añadir contacto")
        println("2. Actualizar contacto")
        println("3. Eliminar contacto")
        println("4. Buscar contacto")
        println("5. Salir")
        contacts.forEach { (key, value) -> println("$key: $value") }
        val opcion = readln().toInt()
        when (opcion) {
            1 -> addContact()
            2 -> editContact()
            3 -> deleteContact()
            4 -> searchContact()
            5 -> return
            else -> println("Opción no válida")
        }
    }
}

fun addContact() {
    val name = getInput("Introduce el nombre del contacto")
    val phone = getInput("Introduce el número de teléfono")
    if (isValidPhoneNumber(phone)) {
        contacts[name] = phone.toInt()
    } else {
        println("Numero invalido, debe ser numerico y no mayor a 11 digitos")
    }
}

fun editContact() {
    val name = getInput("Introduce el nombre del contacto")
    if (contacts.containsKey(name)) {
        val phone = getInput("Introduce el nuevo número de teléfono")
        if (isValidPhoneNumber(phone)) {
            contacts[name] = phone.toInt()
        } else {
            println("Numero invalido, debe ser numerico y no mayor a 11 digitos")
        }
    } else {
        println("El contacto no existe")
    }
}

fun deleteContact() {
    val name = getInput("Introduce el nombre del contacto")
    if (contacts.containsKey(name)) {
        contacts.remove(name)
    } else {
        println("El contacto no existe")
    }
}

fun searchContact() {
    val name = getInput("Introduce el nombre del contacto")
    if (contacts.containsKey(name)) {
        println("El número de teléfono de $name es ${contacts[name]}")
    } else {
        println("El contacto no existe")
    }
}

fun isValidPhoneNumber(phone: String) = phone.length <= 11 && phone.all { it.isDigit() }

fun getInput(prompt: String): String {
    println(prompt)
    return readln()
}
