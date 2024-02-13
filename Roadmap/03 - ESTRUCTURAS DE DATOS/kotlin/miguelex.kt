data class Contacto(val nombre: String, val telefono: String)

class Agenda {
    private val contactos = mutableListOf<Contacto>()

    fun buscar(nombre: String): Contacto? {
        return contactos.find { it.nombre == nombre }
    }

    fun agregar(nombre: String, telefono: String) {
        if (telefono.matches(Regex("[0-9]{1,11}"))) {
            contactos.add(Contacto(nombre, telefono))
        } else {
            println("Número de teléfono no válido.")
        }
    }

    fun actualizar(nombre: String, nuevoNombre: String, nuevoTelefono: String) {
        var contacto = buscar(nombre) ?: return
        if (nuevoTelefono.matches(Regex("[0-9]{1,11}"))) {
            contacto.nombre = nuevoNombre
            contacto.telefono = nuevoTelefono
        } else {
            println("Número de teléfono no válido.")
        }
    }

    fun eliminar(nombre: String) {
        contactos.removeIf { it.nombre == nombre }
    }

    fun listar() {
        contactos.forEach { println(it) }
    }
}

fun main() {

    //Array
    val array = arrayOf(1, 2, 3, 4, 5)
    
    // Imprimir el array

    for (i in array) {
        println(i)
    }

    // Añadir un elemento al array

    array.set(5, 6)

    // Imprimir el array

    for (i in array) {
        println(i)
    }

    // Eliminar un elemento del array

    array.set(5, 0)

    // Imprimir el array

    for (i in array) {
        println(i)
    }

    // ordenar el array

    array.sort()

    // Imprimir el array

    for (i in array) {
        println(i)
    }

    // Listas

    val lista = mutableListOf(1, 2, 3, 4, 5)    

    // Imprimir la lista

    for (i in lista) {
        println(i)
    }

    // Añadir un elemento a la lista

    lista.add(6)

    // Imprimir la lista

    for (i in lista) {
        println(i)
    }

    // Eliminar un elemento de la lista

    lista.removeAt(5)

    // Imprimir la lista

    for (i in lista) {
        println(i)
    }

    // ordenar la lista

    lista.sort()

    // Imprimir la lista

    for (i in lista) {
        println(i)
    }

    // Mapas

    val mapa = mutableMapOf("uno" to 1, "dos" to 2, "tres" to 3, "cuatro" to 4, "cinco" to 5)

    // Imprimir el mapa

    for (i in mapa) {
        println(i)
    }

    // Añadir un elemento al mapa

    mapa.put("seis", 6)

    // Imprimir el mapa

    for (i in mapa) {
        println(i)
    }

    // Eliminar un elemento del mapa

    mapa.remove("seis")

    // Imprimir el mapa

    for (i in mapa) {
        println(i)
    }

    // ordenar el mapa

    val mapaOrdenado = mapa.toSortedMap()

    // Imprimir el mapa

    for (i in mapaOrdenado) {
        println(i)
    }

    // Conjuntos

    val conjunto = mutableSetOf(1, 2, 3, 4, 5)

    // Imprimir el conjunto

    for (i in conjunto) {
        println(i)
    }

    // Añadir un elemento al conjunto

    conjunto.add(6)

    // Imprimir el conjunto

    for (i in conjunto) {
        println(i)
    }

    // Eliminar un elemento del conjunto

    conjunto.remove(6)

    // Imprimir el conjunto

    for (i in conjunto) {
        println(i)
    }

    // ordenar el conjunto

    val conjuntoOrdenado = conjunto.toSortedSet()

    // Imprimir el conjunto

    for (i in conjuntoOrdenado) {
        println(i)
    }

    // Extra

    val agenda = Agenda()
    var continuar = true
    while (continuar) {
        println("¿Qué operación desea realizar?")
        println("1. Buscar contacto")
        println("2. Agregar contacto")
        println("3. Actualizar contacto")
        println("4. Eliminar contacto")
        println("5. Listar contactos")
        println("6. Salir")

        val opcion = readln().toInt()

        when (opcion) {
            1 -> {
                println("Introduzca el nombre del contacto a buscar:")
                val nombre = readln()
                val contacto = agenda.buscar(nombre)
                if (contacto != null) {
                    println("Contacto encontrado: $contacto")
                } else {
                    println("Contacto no encontrado.")
                }
            }
            2 -> {
                println("Introduzca el nombre del nuevo contacto:")
                val nombre = readln()
                println("Introduzca el número de teléfono del nuevo contacto:")
                val telefono = readln()
                agenda.agregar(nombre, telefono)
            }
            3 -> {
                println("Introduzca el nombre del contacto a actualizar:")
                val nombre = readln()
                println("Introduzca el nuevo nombre del contacto:")
                val nuevoNombre = readln()
                println("Introduzca el nuevo número de teléfono del contacto:")
                val nuevoTelefono = readln()
                agenda.actualizar(nombre, nuevoNombre, nuevoTelefono)
            }
            4 -> {
                println("Introduzca el nombre del contacto a eliminar:")
                val nombre = readln()
                agenda.eliminar(nombre)
            }
            5 -> {
                agenda.listar()
            }
            6 -> {
                continuar = false
            }
            else -> {
                println("Opción no válida.")
            }
        }
    }
    println("¡Gracias por usar la agenda de contactos!")

}