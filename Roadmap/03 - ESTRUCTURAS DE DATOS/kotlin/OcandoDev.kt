val contactsMap: MutableMap<String, Int> = mutableMapOf()

fun addContact() {
    print("Name of contact: ")
    val name = readln() ?: ""

    if(contactsMap.containsKey(name)){
        println()
        println("Contact already exists. Please choose a different name.")
        return
    }

    println()

    print("Number of contact: ")
    val numberString = readln().trim() ?: ""

    if (!numberString.matches(Regex("^\\d+$")) && numberString.length !in 1..10) {
        println()
        println("Invalid number format! Please enter a numeric string 1 to 11 digits long.")
        return
    }

    val phoneNumber = numberString.toInt()

    contactsMap[name] = phoneNumber
    println("Contact added successfully!")
}

fun updateContact(){
    print("Enter the name of the contact you want to update: ")
    val oldName = readln()

    if(!contactsMap.containsKey(oldName)){
        println()
        println("Contact not found.")
        return
    }

    println()

    print("Insert the new name: ")
    val newName = readln() ?: ""

    if(contactsMap.containsKey(newName)){
        println()
        println("Contact of $newName already exists. Please choose a different name.")
        return
    }

    println()

    print("Insert the new phone number: ")
    val newNumber = readln().trim() ?: ""

    if (!newNumber.matches(Regex("^\\d+$")) && newNumber.length !in 1..10) {
        println()
        println("Invalid number format! Please enter a numeric string 1 to 11 digits long.")
        return
    }
    val newPhoneNumber = newNumber.toInt()

    println()

    contactsMap.remove(oldName)
    contactsMap[newName] = newPhoneNumber
    println("The contact has been updated.")
}

fun removeContact(){
    print("Which contact do you want to delete?: ")
    val deletionName = readln() ?: ""

    println()

    if(deletionName !in contactsMap){
        println()
        println("Contact not found.")
        return
    } else {
        contactsMap.remove(deletionName)
        println()
        println("The contact has been deleted.")
    }
}

fun searchContact(){
    print("Insert name of contact you are looking for: ")
    val search = readln() ?: ""
    if(search !in contactsMap){
        println()
        println("Contact not found.")
        return
    } else {
        println()
        println("Contact information: $search ${contactsMap[search]}")
    }
}


fun main(){
    //Listas
    val list = mutableListOf(1, 5, 3, 2, 4)

    //Insercion
    list.add(6) //Adicion
    list.add(1, 0) //Adicion en posicion especifica

    //Borrado
    list.remove(3)
    list.removeAt(2)

    //Actualizacion
    list[0] = 10

    //Ordenacion
    list.sort()
    list.sortWith(Comparator {a, b -> b - a})

    println(list)

    //Mapas
    val map = mutableMapOf("a" to 1, "b" to 2, "c" to 3)

    //Insercion
    map["d"] = 4

    //Borrado
    map.remove("b")

    //Actualizacion
    map["a"] = 10

    // Convertir a lista y ordenar
    val ordenedList = map.entries.sortedBy { it.key }.map { it.value }
    println(ordenedList)

    //Conjuntos
    val mSet = mutableSetOf(1, 2, 3, 4)

    //Insercion
    mSet.add(5)

    //Borrado
    mSet.remove(2)

    //Actualizacion
    mSet.remove(3)
    mSet.add(30)

    //Convertir a lista y ordenar
    val ordenedList2 = mSet.toList().sorted()

    println(ordenedList2)

    //Clases con datos
    data class Person(val name: String, var age: Int)

    var person1 = Person("Moure", 32)
    var person2 = Person("Fernando", 30)

    // Inserción
    var person3 = Person("Alejandro", 20)

    // Actualización
    person1.age = 33

    // Ordenación
    val personList = listOf(person1, person2, person3).sortedBy { it.age }

    println(personList)

    println()

    //Ejercicio

    println("Ejecicio")

    var closeApp = false

    do {
        println()

        println(
            "Welcome to your console contacts app! \n\n" +
                    "1. Add contact\n" +
                    "2. Update contact information\n" +
                    "3. Remove contact\n" +
                    "4. Search contact\n" +
                    "5. Close app"
        )

        println()

        val choice = readln()

        when (choice) {
            "1" -> addContact()
            "2" -> updateContact()
            "3" -> removeContact()
            "4" -> searchContact()
            "5" -> closeApp = true
            else -> println("Invalid choice. Please try again.")
        }
    } while (!closeApp)
}