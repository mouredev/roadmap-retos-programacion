/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos. [x]
 * - Cada contacto debe tener un nombre y un número de teléfono. [x]
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo. [x]
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos. [x]
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa. [x]
 */

/*
*+---------------------+----------------------------------------+
*| Tipo de colección   | Descripción                            |
*+---------------------+----------------------------------------+
*| Lists               | Colecciones ordenadas de artículos.    |
*+---------------------+----------------------------------------+
*| Sets                | Colecciones únicas de artículos        |
*|                     | desordenados.                          |
*+---------------------+----------------------------------------+
*| Maps                | Conjuntos de pares clave-valor donde   |
*|                     | las claves son únicas y se asignan a un|
*|                     | solo valor.                            |
*+---------------------+----------------------------------------+
*| Mutables            | Se pueden modificar                    |
*+---------------------+----------------------------------------+
*| Inmutables          | No se pueden modificar (solo lectura)  |
*+---------------------+----------------------------------------+
* */

fun contactBook() {
    val contacts = mutableMapOf<String, Long>()

    fun checkOption(input: String): Int? {
        return try {
            input.toInt()
        } catch (e: NumberFormatException) {
            println("Debes ingresar una opción numérica.\n")
            null
        }
    }

    fun contactInfo(option: Int) {

        fun searchContact(name: String): String {
            return if (contacts.isNotEmpty()) {
                if (name in contacts) {
                    "Nombre: $name\nNumero: ${contacts[name]}\n"
                } else {
                    "No existe un contacto con ese nombre\n"
                }
            } else {
                "La lista de contactos esta vacía.\n"
            }
        }

        fun viewContacts() {
            if (contacts.isNotEmpty()) {
                contacts.forEach { (name, number) -> println("Nombre: $name - Número: $number") }
            } else {
                println("La lista de contactos esta vacía.\n")
            }
        }

        fun checkInput(number: String): Long? {
            return try {
                number.toLong()
            } catch (e: NumberFormatException) {
                println("Debes ingresar un número válido y con 11 dígitos\n")
                null
            }
        }

        fun checkNumber(number: Long): Boolean {
            return number.toString().length == 11
        }

        when (option) {
            1 -> {
                println("Ingresa el nombre:")
                val name = readln()

                println("Ingresa el número:")
                val input = readln()

                val number: Long? = checkInput(input)

                if (number != null && !checkNumber(number)) {
                    if (name !in contacts) {
                        contacts[name] = number
                    } else {
                        println("Ya existe un contacto con ese nombre.\n")
                    }
                }
            }

            2 -> {
                println("Ingresa el nombre:")
                val name = readln()
                println("Ingresa el número:")
                val input = readln()

                val number: Long? = checkInput(input)

                if (number != null && !checkNumber(number)) {
                    if (contacts.isNotEmpty() && name in contacts) {
                        contacts[name] = number
                    } else {
                        println("No existe un contacto con ese nombre\n")
                    }
                }
            }

            3 -> {
                println("Ingresa el nombre:")
                val name = readln()

                if (name in contacts) {
                    println("El contacto \"$name\" fue borrado correctamente.\n")
                    contacts.remove(name)
                } else {
                    println("No existe un contacto con ese nombre\n")
                }
            }

            4 -> {
                println("Ingresa el nombre:")
                val name = readln()
                println(searchContact(name))
            }

            5 -> {
                viewContacts()
            }

            0 -> {
                println("Cerrando lista de contactos..")
            }

            else -> println("Ingresa una opción correcta.\n")
        }
    }

    do {
        println("Que operación deseas realizar?:\n1) Agregar contacto\n2) Actualizar contacto\n3) Borrar contacto\n4) Buscar contacto\n5) Ver lista de contactos\n0) Finalizar")
        val input = readln()
        val option: Int? = checkOption(input)

        if (option != null) {
            contactInfo(option)
        }

    } while (option != 0)
}

fun main() {

    //    Listas
    //#Inmutables
    val inmutableList = listOf("Hola", "Mundo")
    println(inmutableList)
    //#Mutable
    val numberList = mutableListOf(12, 1874, 54, 698, 45)
    //#Inserción
    numberList.add(2, 134)
    //#Borrado
    numberList.removeAt(2)
    //#Actualización
    numberList[0] = 74
    //#Orden
    numberList.sort()
    println(numberList)

    //    Set
    //#Inmutable
    val inmutableSet = setOf("Manzana", "Banana")
    println(inmutableSet)
    //#Mutable
    val shopping = mutableSetOf("Leche", "Gaseosa", "Carne")
    //#Inserción
    shopping.add("Huevos")
    //#Borrado
    shopping.remove("Carne")

    //    Map
    //#Inmutable
    val inmutableMap = mapOf("Uno" to 1, "Dos" to 2, "Tres" to 3, "Cuatro" to 4, "Cinco" to 5)
    println(inmutableMap.forEach { (t, u) -> println("Clave:$t -> Valor:$u") })
    //#Mutable
    val salePrice = mutableMapOf("Tornillo" to 12, "Tuercas" to 8, "Clavos" to 5, "Arandelas" to 0)
    //#Inserción
    salePrice["Pilas"] = 50
    //#Actualización
    salePrice["Tornillo"] = 10
    //#Borrado
    salePrice.remove("Arandelas")
    println("Lista de precios")
    salePrice.forEach { (key, value) -> println("$key:$$value") }

    //    Extra*/
    contactBook()
}