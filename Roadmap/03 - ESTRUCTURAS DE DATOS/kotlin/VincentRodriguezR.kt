class principal {

    fun dataTypes(){

        //Punto #1 -> Explorar estructuras de datos en el lenguaje

        //Arrays
        var arreglo1: Array<Int> = arrayOf(1, 2, 3, 4)
        var arreglo2 = arrayOf(1, 2, 3, 4)
        var matriz = arrayOf(
            intArrayOf(1,2,3),
            intArrayOf(4,5,6),
            intArrayOf(7,8,9)
        )

        //Operaciones con Arrays

        //Iterar Array directamente
        for(i in arreglo1){
            println("Esta linea se ejecutara por cada elemento que tenga el array")
        }

        //Tamaño del Array
        val tamanio = arreglo1.size

        //Busqueda de elementos en el array
        val contiene = 9 in arreglo1
        println(contiene)

        //Copiar Array
        val arregloCopia = arreglo1.copyOf()

        //Ordenar Array
        val arregloOrdenado = arreglo1.sort()

        //FIltro de elementos que cumplen una condiciion
        val arregloFiltro = arreglo1.filter {it > 2}

        //Acceder por indice
        val primerElemento = arreglo1[0] //Los arrays en Kotlin inician desde la posicion 0

        //Modificar elementos por indice
        arreglo1[1] = 9

        //Colecciones de datos
        val coleccion1: Set<Int> = setOf(1, 2, 3)
        val coleccion2 = setOf(1, 2, 3)
        val coleccionMutable: MutableSet<Int> = mutableSetOf(1, 2, 3)
        val coleccionMutable2 = mutableSetOf(1,2,3)

        //Operaciones con Set

        //Adicion de elementos
        coleccionMutable.add(4)

        //Eliminar un elemnto
        coleccionMutable.remove(4) //El 4 simboliza el valor, no la posicion del elemento

        //Eliminar todos los elementos
        coleccionMutable.clear()

        //Listas
        val lista1: List<Int> = listOf(1, 2, 3)
        val lista2 = listOf(1, 2, 3)
        val listaMutable: MutableList<Int> = mutableListOf(1, 2, 3)
        val listaMutable2 = mutableListOf(1, 2, 3)

        //Operaciones con Listas

        //Agregar elementos
        listaMutable.add(1, 10) //Primero se coloca la posicion donde se agregara el nuevo valor, luego el valor a agregar

        //Eliminar posicion
        listaMutable.remove(3) //Elimina el item con el valor indicado, en este caso 3
        listaMutable.removeAt(0) //Elimina el item basado en la posicion en este caso la posicion fue 0 se eliminara el numero 1

        //Modificar elemento
        listaMutable[0] = 1

        //Mapas o Diccionarios de datos
        val mapa1: Map<Int, String> = mapOf( //El primer tipo de dato definido corresponde a la clave y el segundo al valor
            1 to "Primero",
            2 to "Segundo",
            3 to "tercero"
        )

        val mapa2: Map<Any, Any> = mapOf( //Al usar Any dejamos que el lenguaje infiera el tipo de dato
            1 to "Primero",
            2 to "Segundo",
            3 to "tercero"
        )

        val mapa3 = mapOf(
            1 to "Primero",
            2 to "Segundo",
            3 to "tercero"
        )

        val mapaMutable: MutableMap<Int, String> = mutableMapOf(
            1 to "Primero",
            2 to "Segundo",
            3 to "tercero"
        )

        val mapaMutable2 = mutableMapOf(
            1 to "Primero",
            2 to "Segundo",
            3 to "tercero"
        )

        //Operaciones con mapas

        //Agregar o actualizar
        mapaMutable[4] = "cuarto" //En este caso la clave no existe entonces se agrega la clave 4 y se le asigna el valor cuarto
        mapaMutable[1] = "Primerisimo" //En este caso como la clave ya existia se le asigna un nuevo valor osea a la clave 1 se le asigna primerisimo
        mapaMutable.put(5, "quinto") //Una alternativa para crear items en el mapa

        //Eliminar un registro (clave, valor)
        mapaMutable.remove(5) //para eliminar se referencia la clave y se eliminara tanto la clave como el valor

        //Obtener el valor de una clave
        val valor = mapaMutable[4]

        //iterar de forma rapida el elemento unicamente para funciones de lectura
        mapaMutable.forEach{ (clave, value) -> //El forEach tambien funciona para listas
            println(value)
        }
    }

    //Punto Extra, programa para la gestion de agenda

    val menu: Map<Int, String> = mapOf(
        1 to "Agregar contacto",
        2 to "Buscar contacto",
        3 to "Mostrar todos los contactos",
        4 to "Actualziar contacto",
        5 to "Eliminar contacto",
        6 to "Cerrar programa",
    )
    val menuAux: Map<Int, String> = mapOf(
        1 to "Volver a ejecutar accion",
        2 to "Volver al menu principal"
    )
    var selection: String? = "0"
    var selectionAux: String? = ""
    var agenda: MutableMap<Int, List<String?>> = mutableMapOf()
    var index: Int = 1

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val programa = principal()
            programa.main()
        }
    }

    fun main() {
        println("Bienvenido al gestor de agenda!!!")
        showMenu()
    }

    fun showMenu() {
        menu.forEach { (id, value) ->
            println("$id. $value")
        }
        println("Digite el numero de la accion que desea realizar")
        selection = readLine()
        switch()
    }

    fun addContact() {
        println("Escriba el nombre del contacto")
        var name = readLine()
        println("Escriba el numro del contacto")
        var number = readLine()
        while (number!!.toIntOrNull() == null || number.length > 11) {
            println("Ha ingresado un numero incorrecto o muy largo, intente de nuevo, el largo maximo son 11 digitos")
            number = readLine()
        }
        val contact: List<String?> = listOf(number, name)
        agenda?.put(index, contact)
        index++
        showMenuAux()
    }

    fun lookup() {
        println("Digite el nombre o el numero de la persona que desea buscar")
        val value = readLine()
        val filter = agenda.mapValues { (id, list) ->
            list.filter { it == value }
        }
        val toShow = filter.values.flatten()
        println("Se ha encontrado el siguiente contacto: $toShow")
        showMenuAux()
    }

    fun showAll() {
        println("A continuacion, se mostraran todos los contactos en su agenda")
        agenda.forEach { (id, value)->
            println("$id. $value")
        }
        if(selection!!.toInt() !== 4 && selection!!.toInt() !== 5){
            showMenuAux()
        }
    }

    fun updateContact() {
        showAll()
        println("Digite la opcion del contacto que desea editar")
        val edit = readLine()
        println("Digite el nuevo nombre")
        val name = readLine()
        println("Digite el nuevo numero")
        val number = readLine()
        val list = listOf(number, name)
        agenda[edit!!.toInt()] = list
        println("Se ha actualizado el contacto de forma exitosa!")
        showMenuAux()
    }

    fun deleteContact() {
        showAll()
        println("Digite la opcion del contacto que desea eliminar")
        val delete = readLine()
        agenda.remove(delete!!.toInt())
        println("Se ha eliminado el contacto de forma exitosa!")
        showMenuAux()
    }

    fun switch() {
        when (selection!!.toInt()) {
            1 -> addContact()
            2 -> lookup()
            3 -> showAll()
            4 -> updateContact()
            5 -> deleteContact()
            6 -> true
        }
    }

    fun showMenuAux() {
        menuAux.forEach { (id, value) ->
            println("$id. $value")
        }
        println("Digite el numero de la opcion que desea realziar")
        selectionAux = readLine()
        if (selectionAux!!.toInt() == 1) {
            switch()
        } else {
            showMenu()
        }
    }
}