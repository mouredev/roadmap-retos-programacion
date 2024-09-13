// Función principal que demuestra las estructuras de datos básicas
fun demostrarEstructurasDeDatos() {
    // Lista mutable
    println("Lista mutable:")
    val listaNumeros = mutableListOf(1, 2, 3, 4, 5)
    println("Original: $listaNumeros")
    listaNumeros.add(6)
    println("Después de añadir 6: $listaNumeros")
    listaNumeros.removeAt(0)
    println("Después de eliminar el primer elemento: $listaNumeros")
    listaNumeros[0] = 10
    println("Después de actualizar el primer elemento a 10: $listaNumeros")
    listaNumeros.sort()
    println("Después de ordenar: $listaNumeros")

    // Conjunto mutable
    println("\nConjunto mutable:")
    val conjuntoFrutas = mutableSetOf("manzana", "plátano", "naranja")
    println("Original: $conjuntoFrutas")
    conjuntoFrutas.add("pera")
    println("Después de añadir 'pera': $conjuntoFrutas")
    conjuntoFrutas.remove("manzana")
    println("Después de eliminar 'manzana': $conjuntoFrutas")

    // Mapa mutable
    println("\nMapa mutable:")
    val mapaEdades = mutableMapOf("Alice" to 25, "Bob" to 30)
    println("Original: $mapaEdades")
    mapaEdades["Charlie"] = 35
    println("Después de añadir Charlie: $mapaEdades")
    mapaEdades.remove("Bob")
    println("Después de eliminar Bob: $mapaEdades")
    mapaEdades["Alice"] = 26
    println("Después de actualizar la edad de Alice: $mapaEdades")

    // Array
    println("\nArray:")
    val arrayLetras = arrayOf("A", "B", "C", "D")
    println("Original: ${arrayLetras.joinToString()}")
    arrayLetras[1] = "Z"
    println("Después de cambiar B por Z: ${arrayLetras.joinToString()}")
}

// Clase para representar un contacto
data class Contacto(val nombre: String, val telefono: String)

// Clase para la agenda de contactos
class AgendaContactos {
    private val contactos = mutableListOf<Contacto>()

    fun agregarContacto(nombre: String, telefono: String) {
        if (validarTelefono(telefono)) {
            contactos.add(Contacto(nombre, telefono))
            println("Contacto agregado exitosamente.")
        } else {
            println("Número de teléfono inválido.")
        }
    }

    fun buscarContacto(nombre: String) {
        val contactoEncontrado = contactos.find { it.nombre.equals(nombre, ignoreCase = true) }
        if (contactoEncontrado != null) {
            println("Contacto encontrado: ${contactoEncontrado.nombre} - ${contactoEncontrado.telefono}")
        } else {
            println("Contacto no encontrado.")
        }
    }

    fun actualizarContacto(nombre: String, nuevoTelefono: String) {
        val indice = contactos.indexOfFirst { it.nombre.equals(nombre, ignoreCase = true) }
        if (indice != -1 && validarTelefono(nuevoTelefono)) {
            contactos[indice] = Contacto(contactos[indice].nombre, nuevoTelefono)
            println("Contacto actualizado exitosamente.")
        } else {
            println("Contacto no encontrado o número de teléfono inválido.")
        }
    }

    fun eliminarContacto(nombre: String) {
        val eliminado = contactos.removeIf { it.nombre.equals(nombre, ignoreCase = true) }
        if (eliminado) {
            println("Contacto eliminado exitosamente.")
        } else {
            println("Contacto no encontrado.")
        }
    }

    fun mostrarContactos() {
        if (contactos.isEmpty()) {
            println("La agenda está vacía.")
        } else {
            println("Contactos en la agenda:")
            contactos.forEach { println("${it.nombre} - ${it.telefono}") }
        }
    }

    private fun validarTelefono(telefono: String): Boolean {
        return telefono.all { it.isDigit() } && telefono.length <= 11
    }
}

fun main() {
    println("Demostración de estructuras de datos básicas:")
    demostrarEstructurasDeDatos()

    println("\nAgenda de Contactos:")
    val agenda = AgendaContactos()

    while (true) {
        println("\nSeleccione una operación:")
        println("1. Agregar contacto")
        println("2. Buscar contacto")
        println("3. Actualizar contacto")
        println("4. Eliminar contacto")
        println("5. Mostrar todos los contactos")
        println("6. Salir")

        when (readLine()) {
            "1" -> {
                println("Ingrese el nombre del contacto:")
                val nombre = readLine() ?: ""
                println("Ingrese el número de teléfono:")
                val telefono = readLine() ?: ""
                agenda.agregarContacto(nombre, telefono)
            }
            "2" -> {
                println("Ingrese el nombre del contacto a buscar:")
                val nombre = readLine() ?: ""
                agenda.buscarContacto(nombre)
            }
            "3" -> {
                println("Ingrese el nombre del contacto a actualizar:")
                val nombre = readLine() ?: ""
                println("Ingrese el nuevo número de teléfono:")
                val nuevoTelefono = readLine() ?: ""
                agenda.actualizarContacto(nombre, nuevoTelefono)
            }
            "4" -> {
                println("Ingrese el nombre del contacto a eliminar:")
                val nombre = readLine() ?: ""
                agenda.eliminarContacto(nombre)
            }
            "5" -> agenda.mostrarContactos()
            "6" -> {
                println("Saliendo del programa.")
                return
            }
            else -> println("Opción no válida. Intente de nuevo.")
        }
    }
}