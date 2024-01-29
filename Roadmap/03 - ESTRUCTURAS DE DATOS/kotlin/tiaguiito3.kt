

// En Kotlin, existen las siguientes estructuras de datos:

/*
Listas: Interfaz que representa una coleccion ordenada de elementos.
Puedes usar listOf() para una lista inmutable, o
mutableListOf() para una lista inmutable.
 */

fun listas (): String{

    val listaInmutable = listOf("a", "b", "c", "a")
    val listaMutable = mutableListOf("b", "c", "a", "b")
    val listaMutableCleared = mutableListOf(1, 2, 3)
    val listaMutableAscending = mutableListOf(1,2,3,4,5,6,7,8,9)
    val listaMutableDisordered = mutableListOf(1,3,7,5,3,3)
    println("Operaciones de insercion en listas")
    println(listaMutable)
    listaMutable.add("d")
    listaMutable.add(1, "e")
    println(listaMutable)
    println("-")
    println("Operaciones de borrado en listas")
    println("Eliminar 'b': ${listaMutable.also { it.remove("c") }}")
    println("Eliminar por indice: ${listaMutable.also {it.removeAt(2)}}")
    println("Una lista comun: $listaMutableCleared")
    println("Lista anterior limpiada: ${listaMutableCleared.also {it.clear()}}")
    println("-")
    println("Operacion de actualizacion en lista")
    println("Lista mutable: $listaMutable")
    println("Actualizando el valor 'b' de la lista: ${listaMutable.also{it[0] = "a"}} ")
    println("-")
    println("Operaciones de ordenacion en listas")
    println("Lista desordenada: $listaMutableDisordered")
    println("Ordenando la anterior lista: ${listaMutableDisordered.also {it.sort()}}")
    println("Lista ordenada ascendiente: $listaMutableAscending")
    println("Haciendo que la lista vaya para abajo: ${listaMutableAscending.also{it.sortDescending()}}")
    println("-")
    println("Operacion de busqueda en listas")
    var valorBuscado = "c"
    println("El valor que busco es: $valorBuscado")
    var indice = listaInmutable.indexOf(valorBuscado)
    println("El valor que busco se encuentro en el indice: $indice")

    return ""
        }

/*
Sets: Set es una colección que no permite duplicados.
Puedes usar setOf() para un conjunto inmutable o mutableSetOf()
para uno mutable.
 */

fun sets(): String {

    val setInmutable = setOf("a", "b", "c")
    val setMutable = mutableSetOf("a", "b", "c")
    val setMutableCleared = mutableSetOf(1, 2, 3)
    println("Operacion de insercion en sets")
    println(setMutable)
    setMutable.add("d")
    println(setMutable)

    println("Operaciones de borrado en sets")
    println("Borrando un valor: ${setMutable.also {it.remove("d")}}")
    println("Set comun: $setMutableCleared")
    println("Borrando todos los valores del anterior set: ${setMutableCleared.also {it.clear()}}")

    //En conjuntos, no se actualizan directamente elementos, normalmente
    //para cambiar un elemento hay que eliminar el antiguo y agregar el nuevo

    println("Operacion de buscado en sets")
    val valorBuscado = "a"
    println("Valor buscado: $valorBuscado")
    if (valorBuscado in setInmutable) println("Se encontro el valor buscado")

    return ""
    }

/*
Mapas: Map es una colección de pares key-value.
Puedes usar mapOf() para un mapa inmutable o mutableMapOf()
para uno mutable.
 */

fun maps(): String {

    val mapInmutable = mapOf("a" to 1, "b" to 2, "c" to 3)
    val mapMutable= mutableMapOf("a" to 1, "b" to 2, "c" to 3)
    val mapMutableCleared = mutableMapOf(1 to "a", 2 to "b")
    val mapMutableDisordered = mutableMapOf("b" to 2, "c" to 3, "a" to 1)
    var mapMutableOrdered = mapMutableDisordered

    println("Operacion de insercion en map")
    println(mapMutable)
    mapMutable["d"] = 4
    println(mapMutable)
    println("-")
    println("Operaciones de borrado en maps")
    println("Borrando un valor por su key: ${mapMutable.also {it.remove("c")}}")
    println("Un map comun: $mapMutableCleared")
    println("Borrando todo el map anterior: ${mapMutableCleared.also {it.clear()}}")
    println("-")
    println("Operacion de actualizacion en map, es igual a la de insercion")
    println("Actualizando el valor de la letra d en el map: ${mapMutable.also{it["d"] = 3}}")
    println("-")
    println("Operacion de ordenacion en map")
    println(mapMutableDisordered)
    println("Ordenando el anterior map: ${mapMutableOrdered.toSortedMap()}")

    return ""
    }

// Tambien hay arrays mutables e inmutables

fun arrays():String {

    val arrayInmutable = arrayOf(1, 2, 3)
    // (Arrays mutables, se usan las listas mutables)
    val arrayMutable = mutableListOf(1, 2, 3)
    println("Los arrays mutables, en verdad son listas mutables")

    return ""

    }

/*
Secuencias (Sequences): Las secuencias en Kotlin permiten la
manipulación eficiente de datos de manera "Lazy".
 */

fun sequences ():String {
    val secuencia = sequenceOf(1, 2, 3, 4, 5)
    print("I don't understand sequences")
    return "-"
    }


// RETO

fun agendaDeContactos() {
    val agenda = mutableMapOf<String, String>()
    var name: String
    var phone: String
    var isTrue = true


    do {
        println("")
        println("--- Agenda --- ")
        println("1- Buscar contacto")
        println("2- Insertar contacto")
        println("3- Actualizar contacto")
        println("4- Eliminar contacto")
        println("5- Salir")
        print("Elige una opcion: ")
        val input: String? = readLine() ?: ""

        when (input) {
            "1" -> {
                print("Escribe el nombre del contacto que quieres bucar: ")
                var busquedaContactoName = readLine() ?: ""
                if (busquedaContactoName in agenda) println("Su numero es: ${agenda[busquedaContactoName]}") else println("No se ha encontrado el contacto.")
                continue
            }
            "2" -> {
                print("Escribe el nombre del contacto: ")
                name = readLine() ?: ""
                print("Escribe el numero del contacto: ")
                phone = readLine() ?: ""
                agenda[name] = phone
                println("Contacto insertado!")
                continue
            }
            "3" -> {
                print("Ingresa el nombre del contacto que quieres actualizar: ")
                var actualizarContactoName = readLine() ?: ""

                if (actualizarContactoName in agenda) {
                    agenda.remove(actualizarContactoName)
                } else {
                    println("No se ha encontrado el conctacto")
                }
                print("Escribe el nuevo nombre para tu contacto: ")
                var nuevoName = readLine() ?: ""
                print("Escribe el nuevo telefono: ")
                var actualizarContactoPhone = readLine() ?: ""
                agenda[nuevoName] = actualizarContactoPhone
                println("Su contacto se ha actualizado!")
                continue
            }
            "4" -> {
                print("Escribe el nombre del contacto que deseas eliminar: ")
                var conctactoAEliminar:String? = readLine() ?: ""

                if (conctactoAEliminar in agenda) {
                    agenda.remove(conctactoAEliminar)
                    println("Su contacto se ha eliminado correctamente!")
                } else {
                    println("No se ha encontrado el contacto")
                }

                continue
            }
            "5" -> {
                println("Saliendo del programa!")
                isTrue = false
            }
            else -> {
                println("")
                println("Por favor, elige una opcion valida")
            }

        }


    } while(isTrue)
}

// NOTE: Le faltan muchas funciones, como validar si el input es Int, hay repeticion de codigo y en si la estructura no es la mejor
// pero siento que es valido mi progreso :)

fun main(args: Array<String>) {
    println(listas())
    println(sets())
    println(maps())
    println(arrays())
    println(sequences())
    agendaDeContactos()
}





