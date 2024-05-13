import scala.util.matching.Regex
import collection.immutable.SortedMap 
import scala.collection.immutable.SortedSet

object Main {
    def main(args: Array[String]): Unit = {

        // 1. Estrucutras de datos

        // 1.1 Listas:
        val myList = List(1, 2, 3, 4, 5)
        println(s"Lista = $myList\n")

        // 1.2 Secuencias:
        val mySeq = Seq(1, 2, 3, 4, 5)
        println(s"Secuencia = $mySeq\n")

        // 1.2 Maps:
        val myMap = Map(1 -> "one", 2 -> "two")
        println(s"Map = $myMap\n")

        // 1.3 Tuplas:
        val myTupla = (1, "one", 7.0, "seven")
        println(s"Tupla = $myTupla\n")

        // 1.4 Array:
        val myArray = Array(1, 2, 3, 4, 5)
        println(s"Array = ${myArray.toString}\n")

        // 1.5 Vector:
        val myVector = Vector(1, 2, 3, 4, 5)
        println(s"Vector = $myVector\n")

        // 1.6 Sets:
        val mySet = Set(1, 2, 3, 4, 5)
        println(s"Set = $mySet\n")

        // 2. Operando con las estructuras

        // Listas:
        println(s"Lista Inicial = ${myList}")
        var secondList = myList :+ 6 // Insercion
        println(s"Lista despues de agregar un elemento = ${secondList}")
        var secondList_filter = secondList.filter(_!=3) // Borrado
        println(s"Lista despues de borrar elementos = ${secondList_filter}")
        var secondList_updated = secondList_filter.updated(1, 10) // Actualizacion
        println(s"Lista actualizada = ${secondList_updated}")
        var secondList_sorted = secondList_updated.sorted // Ordenacion
        println(s"Lista ordenada = ${secondList_sorted}\n")

        // Secuencias:
        println(s"Secuencia Inicial = ${mySeq}")
        var secondSeq = mySeq :+ 6 // Insercion
        println(s"Secuencia despues de agregar un elemento = ${secondSeq}")
        var secondSeq_filter = secondSeq.filter(_!=3) // Borrado
        println(s"Secuencia despues de borrar elementos = ${secondSeq_filter}")
        var secondSeq_updated = secondSeq_filter.updated(1, 10) // Actualizacion
        println(s"Secuencia actualizada = ${secondSeq_updated}")
        var secondSeq_sorted = secondSeq_updated.sorted // Ordenacion
        println(s"Secuencia ordenada = ${secondSeq_sorted}\n")

        // Maps:
        println(s"Map Inicial = ${myMap}")
        var sencondMap = myMap + (100 -> "One hundred") + (3 -> "Three")  // Insercion
        println(s"Map despues de agregar un elemento = ${sencondMap}")
        var secondMap_filter = sencondMap - 1 // Borrado
        println(s"Map despues de borrar el elemento con clave 1 = ${secondMap_filter}")
        var secondMap_updated = secondMap_filter + (3 -> "Tres") // Actualizacion
        println(s"Map actualizado = ${secondMap_updated}")
        var secondMap_sorted = SortedMap.empty[Int, String] ++ secondMap_updated // Ordenacion
        println(s"Map ordenado = ${secondMap_sorted}\n")

        // Tuplas
        println(s"Tupla Inicial = ${myTupla}")
        var sencondTupla =  myTupla ++ (300, 10) // Insercion
        println(s"Tupla despues de agregar elementos = ${sencondTupla}")
        var secondTupla_delete = (sencondTupla._1, sencondTupla._3, sencondTupla._5, sencondTupla._6) 
        println(s"Tupla despues de borrar = ${secondTupla_delete}")
        var secondTupla_updated = (secondTupla_delete._1, 8, secondTupla_delete._3, secondTupla_delete._4)  // Actualizacion
        println(s"Tupla actualizada = ${secondTupla_updated}")
        var secondList_Tuple = (secondTupla_updated).toList // Ordenar
        var secondListTupla_order = secondList_Tuple.sorted
        var SecondTupla_ordered = secondListTupla_order match {
            case List(a, b) => (a,b)
            case List(a, b, c) => (a,b,c)
            case List(a, b, c, d) => (a,b,c,d)
        }
        println(s"Tupla ordenada = ${SecondTupla_ordered}\n")

        // Arrays No se puede visualizar muy bien
        // No encontre mucha documentación al respecto
        println(s"Array Inicial = ${myArray} \n")

        // Vectores
        println(s"Vector Inicial = ${myVector}")
        var sencondVector =  myVector ++ Vector(300, 10) // Insercion
        println(s"Vector despues de agregar un elemento = ${sencondVector}")
        val elementoEliminar = 10
        var secondVector_delete = sencondVector.filterNot(_ == elementoEliminar) // Borrar
        println(s"Vector despues de borrar = ${secondVector_delete}")
        val indice = 3
        val nuevoValor = 500
        var sencondVector_updated = secondVector_delete.updated(indice, nuevoValor) // Actualización
        println(s"Vector actualizado = ${sencondVector_updated}")
        var secondVector_sorted = sencondVector_updated.sorted // Ordenar
        println(s"Vector ordenado = ${secondVector_sorted}\n")

        // Sets
        println(s"Set Inicial = ${mySet}")
        var secondSet =  mySet + 300 + 10 // Insercion
        println(s"Set despues de agregar elementos = ${secondSet}")
        var secondSet_delete = secondSet - 5 // Borrado
        println(s"Set despues de borrar = ${secondSet_delete}")
        var secondSet_up1 = secondSet_delete - 3
        var secondSet_update = secondSet_up1 + 1050 // Actualizacion
        println(s"Set actualizado = ${secondSet_update}")
        var set_sorted = secondSet_update.to(SortedSet) // Ordenar
        println(s"Set ordenado = ${set_sorted}\n")

        // ----------------------------------------------------------- 
        // DIFICULTAD EXTRA                                          |
        // -----------------------------------------------------------
        var mapContacts = Map(
            "3015675434" -> "Lucho Diaz",
            "3106742354" -> "Rigoberto Uran",
            "3205438756" -> "Pedro Urango")

        def welcome_Menu(): String = {
            println("""
                Hola !!, soy tu agenda de contactos. Aca puedes agregar, 
                actualizar, borrar y buscar cualquiera de tus contactos.

                Recuerda que el contacto simplemente tiene el nombre y el
                telefono correspondiente.

                ¡¡¡ Comencemos!!!  
                """)
            println("Ingresa tu nombre: ")
            var name = scala.io.StdIn.readLine()
            println("Ingresa tu nombre: ")
            var option = mainMenu(name)
            return option
        }

        def mainMenu(userName:String): String = { 
            println(s"$userName, escoge alguna de las siguientes opciones: ")
            println("""
                1. Busqueda de contactos
                2. Agregar un contacto
                3. Actualizar un contacto
                4. Eliminar un contacto
                5. Salir 
                """)
            println("Ingresa la acción a realizar: ")
            var option = scala.io.StdIn.readLine()
            while (option != "1" && option != "2" && option != "3" && option != "4" && option != "5") {
                println("Ingresaste un valor erroneo, vuelvelo a intentar")
                println("Ingresa la acción a realizar: ")
                option = scala.io.StdIn.readLine() 
            }
            return option
        }

        def check_Input(numberContact: String): Boolean =  {
            val patron: Regex = """^\d{10}$""".r
            // Expresión regular para comprobar que tenga 10 dígitos y no contenga ningún carácter alfabético
            // Devolver True si el número cumple el patrón, o False en caso contrario
            return patron.findFirstIn(numberContact).isDefined
        }

        def printContacts(mapContacts: Map[String, String]): Unit = {
            println("Tu agenda queda de la siguiente manera:")
            for ((clave, valor) <- mapContacts) {
                println(s"${valor} su numero es ${clave}")
            }
        }

        def find_Contact(numberContact: String, nameContact: String, option: String): Unit = {
            if (option == "1") {
                var contact = mapContacts.getOrElse(numberContact, "No existe el numero de celular")
                println(s"El numero de celular ${numberContact} le corresponde a ${contact}")
            }
            else if (option == "2") {
                var keys: List[String] = List()
                for ((clave, valor) <- mapContacts) {
                    if (valor == nameContact) {
                        keys = keys ::: List(clave)
                    }
                }
                println(s"${nameContact} tiene el numero de celular ${keys.mkString(", ")}")
            }
        }

        def add_Contact(numberContact: String, nameContact: String): Unit = {
            mapContacts ++= Map(numberContact -> nameContact)
            println(s"Agregaste a tu agenda de contactos el nombre ${nameContact}")
            println(s"y le asignaste el numero de celular ${numberContact} \n")
            printContacts(mapContacts)
        }

        def del_Contact(numberContact: String, nameContact: String, option: String): Unit = {
            if (option == "1") {
                var contact = mapContacts.getOrElse(numberContact, "No existe el numero de celular")
                println(s"¿Estas seguro que deseas eliminar el contacto de ${contact} con el numero ${numberContact}?")
                println("Ingresa Yes/No: ")
                val delete = scala.io.StdIn.readLine()
                if (delete == "Yes"){
                    mapContacts = mapContacts - numberContact
                }
            }
            else if (option == "2") {
                var keys: List[String] = List()
                for ((clave, valor) <- mapContacts) {
                    if (valor == nameContact) {
                        keys = keys ::: List(clave)
                    }
                }   
                for (item <- keys) {
                    println(s"Encontramos que para el contacto de ${mapContacts.getOrElse(item, "No existe el numero de celular")} se tiene el numero ${item}")
                    println("Deseas Eliminarlo totalmente Yes/No: ")
                    var delete = scala.io.StdIn.readLine()
                    if (delete == "Yes") {
                        mapContacts = mapContacts - item
                    }
                    else if (delete == "No") {}
                    else {
                        println("Ingresaste una opción incorrecta")
                    }
                }
            }
        }

        def update_Contact(numberContact: String, nameContact: String, option: String): Unit = {
            if (option == "1") {
                var contact = mapContacts.getOrElse(numberContact, "No existe el numero de celular")
                println(s"Vas a actualizar el contacto de ${contact} con el numero ${numberContact}")
                println(s"¿Que numero deseas colocar ahora al contacto ${contact}?")
                println("Ingresalo aqui: ")
                var newNumberContact = scala.io.StdIn.readLine()

                while (!(check_Input(newNumberContact))){
                    println("Ingresaste un valor erroneo, vuelvelo a intentar")
                    println("Ingresalo nuevamente: ")
                    newNumberContact = scala.io.StdIn.readLine()
                }
                
                println(s"Vas a actualizar ${numberContact} por ${newNumberContact}")
                println("¿ Estas segur@ de realizar esta operacion ? (Yes/No): ")
                var update = scala.io.StdIn.readLine()
                if (update == "Yes"){
                    mapContacts = mapContacts - numberContact
                    mapContacts ++= Map(newNumberContact -> contact)
                }
            }
            else if (option == "2"){
                var keys: List[String] = List()
                for ((clave, valor) <- mapContacts) {
                    if (valor == nameContact) {
                        keys = keys ::: List(clave)
                    }
                }
                
                for (item <- keys) {
                    println(s"Encontramos que para el contacto de ${mapContacts.getOrElse(item, "No existe el numero de celular")} se tiene el numero ${item}")
                    println(s"Ingresa el nuevo nombre que le pondras al contacto: ")
                    var newNameContact = scala.io.StdIn.readLine()
                    println(s"Deseas actualizar el nombre ${nameContact} por ${newNameContact} Yes/No: ")
                    var update = scala.io.StdIn.readLine()
                    if (update == "Yes") {
                        mapContacts = mapContacts - item
                        mapContacts ++= Map(item -> newNameContact)
                    }    
                }
            
                printContacts(mapContacts)
            }
        }


        def execute_Option(option: String): Boolean = {
            var still = true
            if (option == "1") {
                println("""
                Para realizar la busqueda de algun contacto tienes dos opciones:
                    1. Buscar por el numero de telefono
                    2. Buscar por el nombre de contacto
                """)
                println("Ingresa la opcion que quieres: ")
                var optionSearch = scala.io.StdIn.readLine()
                
                while ((optionSearch != "1") && (optionSearch != "2")) {
                    println("Ingresaste un valor erroneo, vuelvelo a intentar")
                    println("Ingresa la opcion que quieres: ")
                    optionSearch = scala.io.StdIn.readLine()
                }

                if (optionSearch == "1") {
                    println("Ingresa el numero de telefono a buscar: ")
                    var numberContact = scala.io.StdIn.readLine()
                        
                    while (!(check_Input(numberContact))) {
                        println("Ingresaste un valor erroneo, vuelvelo a intentar")
                        println("Ingresa el numero de telefono a buscar: ")
                        numberContact = scala.io.StdIn.readLine()
                    }
                    find_Contact(numberContact, "0", optionSearch)
                }
                else if (optionSearch == "2") {
                    println("Ingresa el nombre del contacto a buscar: ")
                    var nameContact = scala.io.StdIn.readLine()
                    find_Contact("0", nameContact, optionSearch)
                }
                still = true
            }
            else if(option == "2") {
                println("Ingresa el nombre del contacto que vas a agregar: ")
                var nameContact = scala.io.StdIn.readLine()
                println("Ingresa el numero de telefono: ")
                var numberContact = scala.io.StdIn.readLine()

                while (!(check_Input(numberContact))) {
                    println("Ingresaste un valor erroneo, vuelvelo a intentar")
                    println("Ingresa el numero de telefono a buscar: ")
                    numberContact = scala.io.StdIn.readLine()
                }
                add_Contact(numberContact, nameContact)
                still = true
            }
            else if(option == "3") {
                println("""
                Para realizar la actualizacion de algun contacto tienes dos opciones:
                    1. Actualizar el numero de telefono
                    2. Actualizar el nombre de contacto
                """)
                println("Ingresa la opcion que quieres: ")
                var optionUpdate = scala.io.StdIn.readLine()
                
                while ((optionUpdate != "1") && (optionUpdate != "2")) {
                    println("Ingresaste un valor erroneo, vuelvelo a intentar")
                    println("Ingresa la opcion que quieres: ")
                    optionUpdate = scala.io.StdIn.readLine()
                }
                if (optionUpdate == "1") {
                    println("Ingresa el numero de telefono que vas a actualizar: ")
                    var numberContact = scala.io.StdIn.readLine()

                    while (!(check_Input(numberContact))) {
                        println("Ingresaste un valor erroneo, vuelvelo a intentar")
                        println("Ingresa el numero de telefono a buscar: ")
                        numberContact = scala.io.StdIn.readLine()
                    }  
                    update_Contact(numberContact, "0", optionUpdate)
                }
                else if (optionUpdate == "2") {
                    println("Ingresa el nombre del contacto a buscar: ")
                    var nameContact = scala.io.StdIn.readLine()
                    update_Contact("0", nameContact, optionUpdate) 
                }   
                still = true
            }
            else if(option == "4") {
                println("""
                Para eliminar un contacto tienes dos opciones:
                    1. Eliminar por el numero de telefono
                    2. Eliminar por el nombre de contacto
                """)
                println("Ingresa la opcion que quieres: ")
                var optionDel = scala.io.StdIn.readLine()

                while ((optionDel != "1") && (optionDel != "2")) {
                    println("Ingresaste un valor erroneo, vuelvelo a intentar")
                    println("Ingresa la opcion que quieres: ")
                    var optionDel = scala.io.StdIn.readLine()
                }
                
                if (optionDel == "1") {
                    println("Ingresa el numero de telefono a buscar: ")
                    var numberContact = scala.io.StdIn.readLine()

                    while (!(check_Input(numberContact))) {
                        print("Ingresaste un valor erroneo, vuelvelo a intentar")
                        println("Ingresa el numero de telefono a buscar: ")
                        numberContact = scala.io.StdIn.readLine()
                    }
                    del_Contact(numberContact, "0", optionDel)
                }
                else if (optionDel == "2") {
                    println("Ingresa el nombre del contacto a buscar: ")
                    var nameContact = scala.io.StdIn.readLine()
                    del_Contact("numberContact", nameContact, optionDel)
                }
                still = true
            }
            else if(option == "5") {
                still = false
            }                
            return still
        }


        def run(): Unit = {
            var x = true
            while(x) {
                var userOption = welcome_Menu()
                x = execute_Option(userOption)
            }
        }
        
        run()
    }
}