package com.cursoandroid.roadmap_retos_programacion

/*
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

fun main() {

    // Arrays
    val array: Array<Int> = arrayOf(1, 2, 3, 4, 5)
    val arrayString: Array<String> = arrayOf("uno", "dos", "tres")
    // Listas
    val lista: List<Int> = listOf(1, 2, 3, 4, 5)
    val listaMutable: MutableList<String> = mutableListOf("a", "b", "c")
    // Conjuntos
    val conjunto: Set<String> = setOf("manzana", "banana", "naranja")
    val conjuntoMutable: MutableSet<Int> = mutableSetOf(1, 2, 3)
    // Mapas
    val mapa: Map<String, Int> = mapOf("uno" to 1, "dos" to 2, "tres" to 3)
    val mapaMutable: MutableMap<String, String> = mutableMapOf("a" to "apple", "b" to "banana")

    agendaContactos()

}

fun agendaContactos() {
    val contactos = mutableMapOf("Adrian" to "111222333", "Raquel" to "444555666")
    var opcion: Int? = 0

    while (opcion != 6) {

        println("/*------- Agenda -------*/")
        println("1. Buscar contacto")
        println("2. Agregar contacto")
        println("3. Actualizar contacto")
        println("4. Eliminar contacto")
        println("5. Ver contactos")
        println("6. Salir\n->")

        val input = readLine()
        opcion = input?.toInt()

        when (opcion) {
            1 -> buscarContacto(contactos)
            2 -> agregarContacto(contactos)
            3 -> actualizarContacto(contactos)
            4 -> eliminarContacto(contactos)
            5 -> mostrarContactos(contactos)
            6 -> break
            else -> "La opcion indicada no es valida"
        }
    }
}

fun mostrarContactos(contactos: MutableMap<String, String>) {

    if (contactos.isNotEmpty()) {
        println("/*** Contactos ***\\")
        for ((clave, valor) in contactos) {
            println("$clave - $valor")
        }
    }
}

fun buscarContacto(contactos: MutableMap<String, String>) {
    println("Introduza el nombre del contacto que desea buscar:")
    val contacto = readLine().toString()

    if (contacto in contactos) {
        println("Contacto encontrado: ")
        println("$contacto - ${contactos[contacto]}")
    } else {
        println("El contacto no ha sido encontrado")
    }
}

fun agregarContacto(contactos: MutableMap<String, String>) {
    println("Introduza el nombre del contacto:")
    val contacto = readLine().toString()

    println("Introduzca el numero de telefono: ")
    val contactPhone = readLine().toString()

    if (contactPhone.matches(Regex("\\d{9}"))) {
        contactos[contacto] = contactPhone
    }

    contactos[contacto] = contactPhone
    println("El contacto $contacto ha sido agregado a la lista de contactos")
}

fun actualizarContacto(contactos: MutableMap<String, String>) {
    println("Introduzca el nombre del contacto que desea modificar: ")
    val contacto = readLine().toString()

    if (contacto in contactos) {
        println("Desea modificar los datos del contacto $contacto? s/n:")
        val check = readLine().toString()

        if (check == "s") {
            println("Introduzca el nuevo numero de telefono: ")
            val newPhone = readLine().toString()

            if (newPhone.matches(Regex("\\d{9}"))) {
                contactos[contacto] = newPhone
                println("Telefono actualizado correctamentes")
            } else {
                println("El numero de telefono debe tener 9 cifras")
            }
        } else {
            println("No se ha realizado ningun cambio")
        }
    } else {
        println("El contacto $contacto no se encuentra en la lista de contactos")
    }
}

fun eliminarContacto(contactos: MutableMap<String, String>) {
    println("Introduzca el nombre del contacto que desea eliminar:")
    val contacto = readLine().toString()

    if (contacto in contactos) {
        println("Va a eliminar el contacto $contacto de su agenda, esta de acuerdo? s/n")
        val check = readLine().toString()

        if (check == "s") {
            contactos.remove(contacto)
            println("El contacto $contacto ha sido eliminado")
        } else {
            println("El contacto no ha sido eliminado")
        }
    } else {
        println("El contacto $contacto no se encuentra en la lista de contactos")
    }
}