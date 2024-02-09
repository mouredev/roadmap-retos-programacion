/*
ESTRUCTURAS DE DATOS
* EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.

DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar,
y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más
de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.
*/

fun lists() {
    val listExample = mutableListOf("Qui Gon Jinn", "Obi Wan", "Mace Windu")
    println(listExample)

    println("\n-> Agregar elementos a una lista:")
    listExample.add("Anakin")
    println(listExample)

    val addList = listOf("Ahsoka Tano", "Luke", "Rey")
    listExample.addAll(addList)
    println(listExample)

    println("\n-> Borrar elementos a una lista:")
    listExample.remove("Rey")
    println(listExample)

    listExample.removeAt(2)
    println(listExample)

    println("\n-> Ordenar elementos a una lista:")
    listExample.sort()
    println(listExample)

    println("\n-> Invertir elementos a una lista:")
    listExample.reverse()
    println(listExample)

    println("\n-> Vaciar una lista:")
    listExample.clear()
    println(listExample)
}


fun sets() {
    val setExample = mutableSetOf("Aragorn", "Légolas", "Gimli", "Gandalf")
    println(setExample)

    println("\n-> Añadir elementos a un set:")
    setExample.add("Gollum")
    println(setExample)

    val hobbits = setOf("Frodo", "Sam")
    val comunidadAnillo = setExample.union(hobbits)
    println(comunidadAnillo)

    println("\n-> Borrar elementos de un set:")
    setExample.remove("Gollum")
    println(comunidadAnillo)

    println("\n-> Ordenar set:")
    val comunidadAnilloOrden = comunidadAnillo.sorted()
    println(comunidadAnilloOrden)

    println("\n-> Borrar un set:")
    setExample.removeAll(comunidadAnillo)
    println(setExample)
}


fun tuples() {
    val tupleExample = Triple("Mario", "Luigi", "Peach")
    println(tupleExample)
}


fun dicts() {
    val dictExample = mutableMapOf("Charmander" to "Fuego",
        "Squirtle" to "Agua",
        "Bulbasaur" to "Planta")
    println(dictExample)

    println("\n-> Añadir elementos a un diccionario:")
    dictExample.put("Pikachu", "Eléctrico")
    println(dictExample)

    val dict2 = mapOf("Nidoran" to "Veneno", "Pidgey" to "Volador", "Abra" to "Psíquico", "Metapod" to "Bicho")
    val dictSum = dictExample + dict2
    println(dictSum)

    println("\n-> Borrar elementos de un diccionario:")
    dictExample.remove("Pikachu")
    println(dictExample)

    val dict3 = mapOf("Pidgey" to "Volador", "Metapod" to "Bicho")
    val dictRest = dictSum - dict3.keys
    /*hay que especificar keys aquí porque aunque esté en una variable nueva, se está restando el valor
    de dictSum, y especificamos que borramos las claves
    Para sumar no hace falta, porque los almacena en un nuevo diccionario, y + detecta automáticamente
    las claves
     */
    println(dictRest)

    println("\n-> Ordenar elementos de un diccionario:")
    val dictOrden = dictRest.toSortedMap()
    println(dictOrden)

    println("\n-> Invertir un diccionario:")
    val dictReverse = dictOrden.reversed()
    println(dictReverse)

    println("\n-> Borrar un diccionario:")
    dictOrden.clear()
    println(dictOrden)
}


fun ejExtra() {
    val contactList = mutableMapOf("Mouredev" to 3, "Aris" to 54)


    fun lookForContact(){
    if (contactList.isEmpty()){
        println("No hay contactos")
    }else{
        println("¿Quieres buscar por contacto (c) o por número (n)?: ")
        val lookFor = readln()

        if (lookFor == "c"){
            println("¿Qué contacto quieres buscar?: ")
            val contact = readln()

            if (contact in contactList){
                println("$contact : ${contactList[contact]}")
            }
        } else if (lookFor == "n"){
            println("Qué número quieres buscar?: ")
            val contactNum: Int = readln().toInt()

            if (contactNum in contactList.values){
                for ((name, number) in contactList){
                    if (number == contactNum){
                        println("El número $number pertenece a: $name")
                    }
                }
            }else{
                println("Este número no está en los contactos")
            }
        }else{
            println("Esta opción no está disponible")
        }
    }
        readln()
    }


    fun addContact() {
        println("Añada el nombre del contacto")
        val contactName = readln()

        println("Añada el número de teléfono del contacto")
        val contactNumber = readln()

        if (contactNumber.matches(Regex("\\d{9}"))){
            contactList[contactName] = contactNumber.toInt()
        }else{
            println("Formato de número no válido. Debe tener 9 cifras")
            addContact()
        }
        readln()
    }

    fun updateContact() {
        println("¿Quieres actualizar algún contasto?: Sí(y) / No(n)")
        val act = readln()

        if (act == "y"){
            println("¿Qué contacto quieres actualizar?: ")
            val contactName = readln()

            if (contactName in contactList){
                println("¿Cuál es el nuevo número?: ")
                val newNumber = readln()

                if (newNumber.matches(Regex("\\d{9}"))){
                    contactList[contactName] = newNumber.toInt()
                }else{
                    println("Formato de número no válido. Debe tener 9 cifras")
                    updateContact()
                }
            }else{
                println("Este contacto no está registrado")
                updateContact()
            }
        }else if (act == "n"){
            readln()
        }else{
            println("Opción no válida")
            readln()
            updateContact()
        }
    }


    fun deleteContact() {
        println("¿Quieres borrar algún contacto?: ")
        val deleteContact = readln()

        if (deleteContact in contactList){
            contactList.remove(deleteContact)
        } else{
            println("No existe ese contacto")
            deleteContact()
        }
        readln()
    }

    fun showContacts() {
        for (contact in contactList){
            println(contact)
        }
        readln()
    }


    fun inicio(){
        println("\n\t~~ AGENDA TELEFÓNICA ~~")
        print("¿Qué quieres hacer?:\n" +
                "1.- Buscar contacto\n" +
                "2.- Añadir contacto\n" +
                "3.- Actualizar listado\n" +
                "4.- Borrar contacto\n" +
                "5.- Mostrar contactos\n" +
                "6.- Salir\n-> ")

        try{
            val option = readln().toInt()

            when (option) {
                1 -> { lookForContact()
                    inicio() }

                2 -> { addContact()
                    inicio() }

                3 -> { updateContact()
                    inicio() }

                4 -> { deleteContact()
                    inicio() }

                5 -> { showContacts()
                    inicio() }

                !in 1..6 -> {
                    println("Opción no válida. ELige una de las disponibles")
                    inicio() }
            }
        }catch (e: NumberFormatException){
            println("Opción no válida, que sea un número del 1 al 6")
            inicio()
        }
    }

    inicio()
}


fun main() {
    println("*".repeat(7)+"ESTRUCTURAS DE DATOS EN KOTLIN"+"*".repeat(7))

    println("\n\t --> LISTAS")
    lists()

    println("\n\t --> SETS")
    sets()

    println("\n\t --> TUPLES (No son tuplas como tal, pero parecido)")
    tuples()

    println("\n\t --> DICCIONARIOS/MAPS")
    dicts()

    println('\n' + "-".repeat(9) + " EJERCICIO EXTRA " + "-".repeat(9))
    ejExtra()

}
