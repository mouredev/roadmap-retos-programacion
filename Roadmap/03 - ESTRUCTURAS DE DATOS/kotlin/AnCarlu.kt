import java.lang.System.exit

/**
 * Estructuras soportadas en kotlin
 */

fun estructuras() {
//Listas
    val mutableList = mutableListOf(1, 2, 3, 4, 5)
    println("Las listas son colecciones que permiten duplicar elementos $mutableList")
    //Inserción
    mutableList.add(7)
    println("Despues de añadir la lista muestra los siguientes numeros $mutableList")
    //Borrado
    mutableList.remove(5)
    println("Despues de borrar la lista muestra los siguientes numeros $mutableList")
    //Actualización
    mutableList[2] = 8
    println("Actualización del tercer dato de la lista $mutableList")
    //Ordenacion
    mutableList.sort()
    println("Ordenacion de la lista $mutableList")
//Set
    val mutableSet = mutableSetOf(1, 4, 3)
    println("\nSet son colecciones que no permiten elementos duplicados $mutableSet")
    //Insercion
    mutableSet.add(5)
    println("Despues de añadir a SET $mutableSet")
    //Borrado
    mutableSet.remove(2)
    println("Despues de borrar en SET $mutableSet")
    //No se pueden actualizar directamente, pero se puede convertir en una lista ordenada
    val sorterList = mutableSet.toList().sorted()
    println("SET no se puede ordenar directamente, \npero se puede convertir en una lista ordenada $sorterList ")
//Map
    val mutableMap = mutableMapOf(1 to "uno", 2 to "dos", 3 to "tres")
    println("\nLos mapas son colecciones de pares clave-valor $mutableMap")
    //Insercion
    mutableMap[4] = "cuatro"
    println("Despues de insertar $mutableMap")
    //Borrado
    mutableMap.remove(2)
    println("Despues de borrar $mutableMap ")
    //Actualizacion
    mutableMap[3] = "tres Actualizado"
    println("Actualización del map en la 3ª posicion")
    val sorterMap = mutableMap.toList().sortedBy { it.first }
    println(
        "MAP tampoco se puede actualizar directamente," +
                "\npero al igual que SET se pueden convertir en una lista ordenada $sorterMap"
    )
//Array
    val array = arrayOf(1, 2, 3)
    println("Un array en Kotlin es una estructura de tamaño fijo ${array.joinToString()}")
    println("No es posible ni añadir ni borrar, pero se puede actualizar")
    //Actualizacion
    array[0] = 4
    print(array.joinToString())
    //Ordenacion
    val sortedArray = array.sortedArray()
    println("\nAl igual que las anteriores, debemos convertirlo en una lista ordenada")
    println(sortedArray.joinToString())
}

//Data class para representar los contactos
data class Contacto(var nombre: String, var telefono: String)

//Clase para realizar las acciones
class Agenda {
    private val contacto = mutableListOf<Contacto>()

    fun removeContact(name: String) {
        contacto.removeIf {
            it.nombre == name
        }
    }

    fun updateContact(name:String, newName: String, newPhone:String) {
        val contac = searchContact(name)
        if (contac != null) {
            if(newPhone.matches(Regex("[0-9]{1,11}"))) {
                contac.nombre=newName
                contac.telefono = newPhone
            }else{
                println("El numero de telefono no es valido")
            }
        }
    }

    fun searchContact(name: String): Contacto? {
        return contacto.find {
            it.nombre == name
        }
    }

    fun addContact(name: String, number: String) {
        if(number.matches(Regex("[0-9]{1,11}"))){
            contacto.add(Contacto(name, number))
        }else{
            println("El numero de telefono no es valido")
        }

    }

    fun list() {
        contacto.forEach {
            println(it)
        }
    }

}

fun main() {
    estructuras()

    val agenda = Agenda()
    while (true) {
        println("-------AGENDA-----")
        println("Selecciona una opcion")
        println("1. Añadir contacto")
        println("2. Buscar contactos")
        println("3. Actualizar contactos")
        println("4. Eliminar contactos")
        println("5. Lista de contactos")
        println("0. Salir")

        when (readLine()) {
            "1" -> {
                println("Nuevo nombre de contacto:")
                val name = readln()
                println("Numero de telefono")
                val phone = readln()
                agenda.addContact(name, phone)
            }

            "2" -> {
                println("Nombre del contacto a buscar")
                val name = readln()
                val contact = agenda.searchContact(name)
                if (contact == null) {
                    println("No se ha encontrado ningun contacto con ese nombre")
                } else {
                    println("Contacto encontrado : \n$contact")
                }
            }

            "3" -> {
                println("Inserte el nombre del contacto que desea actualizar")
                val name= readln()
                val contact=agenda.searchContact(name)
                if (contact == null) {
                    println("No se ha encontrado ningun contacto con ese nombre")
                } else {
                    println("Nuevo nombre de contacto")
                    val newName= readln()
                    println("Nuevo numero de telefono")
                    val newPhone= readln()
                    agenda.updateContact(name,newName,newPhone)
                    println("El contacto se ha actualizado correctamente \n$contact")
                }
            }
            "4" -> {
                println("Introduzca el nombre del contacto a borrar:")
                val name = readln()
                agenda.removeContact(name)
                println("El contacto se ha borrado correctamente")
            }

            "5" -> {
                println("----LISTA DE CONTACTOS----")
                agenda.list()
            }

            "0" -> {
                println("Hasta la proxima!!!")
                exit(0)
            }
            else -> println("No es una opcion valida\n")
        }
    }
}