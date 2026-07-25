object Source {
    def main(args: Array[String]): Unit = {
        // OPERACIONES CON CADENAS DE CARACTERES

        // 1. Asignacion
        val saludo = "Hola, "
        val nombre = "Mr X"

        // 2. Concatenacion
        val final_saludo_1 = saludo + nombre
        println(s"${final_saludo_1}\n")
        val final_saludo_2 = saludo.concat(nombre)
        println(s"${final_saludo_2}\n")

        // 3. Operaciones "Aritmeticas"
        val saludoTotal = saludo*3
        println(s"${saludoTotal}\n")

        // 4. Subcadenas
        val secuencia = "123456789"
        val primerSub = secuencia.substring(0, 5)
        val secondSub = secuencia.substring(3)
        val thirdSub =  secuencia.substring(2,6)
        println(s"Primera subcadena $primerSub") // Se toma 12345
        println(s"Segunda subcadena $secondSub") // Se toma 456789
        println(s"Tercera subcadena $thirdSub \n") // Se toma 3456

        // 5. Indexacion
        val char1 = final_saludo_1(1)
        val char2 = final_saludo_1(2)
        val char3 = final_saludo_1(3)
        println(s"caracter de saludo 1 = $char1")
        println(s"caracter de saludo 2 = $char2")
        println(s"caracter de saludo 3 = $char3 \n")

        // 6. Longitud
        val lenghtStr = final_saludo_1.length()
        println(s"Longitud del saludo es $lenghtStr \n")

        // 7. Recorrido
        println("Recorrido de Str - Forma 1: Ciclo for")
        for (caracter <- final_saludo_1) {
            println(s"Recorriendo el String $final_saludo_1 -> $caracter")
        }
        println("\nRecorrido de Str - Forma 2: Metodo foreach")
        final_saludo_1.foreach {
            caracter => println(s"Caracter: $caracter")
        }

        // 8. Mayusculas y Minusculas
        val salMayus = final_saludo_1.toUpperCase()
        val salMinus = salMayus.toLowerCase()
        println(s"\nSaludo en Mayuscula -> $salMayus")
        println(s"Saludo en Minuscula -> $salMinus \n")

        // 9. Reemplazo
        val newName = final_saludo_1.replace("X", "Z")
        println(s"Nuevo saludo = $newName")
        val newName2 = final_saludo_1.replaceAll("Mr X", "Señor X")
        println(s"Nuevo saludo = $newName2 \n")

        // 10. Division o Separacion
        println(s"Frase Inicial -> $final_saludo_1")
        val divSal = final_saludo_1.split(",")
        println(s"Resultado de dividir -> ${divSal.toList} \n")
        
        // 11. Union
        val myStringList = List("uno", "dos", "tres", "cuatro")
        println(s"Lista de Strings -> $myStringList.toString()")
        val myString = myStringList.mkString(", ")
        println(s"Strings unidos -> $myString \n")

        // 12. Verificacion/Contiene 
        val word = "scala"
        val subChar = "al"
        println(s"String Base -> ${word}")
        if (word.contains(subChar)) {
            println(s"la palabra '${word}' posee la cadena '${subChar}'\n")
        }
        else{
            println(s"la palabra '${word}' NO posee la cadena '${subChar}'\n")
        }

        // 13. Eliminar espacios en Blanco
        val saludoNoTrim = "     Hola, Mr X....         "
        println(s"Sin trimeo -> '${saludoNoTrim}'")
        val saludoTrim = saludoNoTrim.trim
        println(s"Con trimeo -> '${saludoTrim}'\n")

        // DIFICULTAD EXTRA
        def palindromo(palabra: String): Boolean = {
            var palabra_inver = palabra.trim.toLowerCase().reverse
            val numeros = Seq("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

            try {
                for (index <- numeros) {
                    if (palabra.contains(index)) {
                        throw new IllegalArgumentException("Por favor ingresa una palabra, por lo menos hay un número dentro de ella")
                    }
                }
                return palabra_inver == palabra
            }
            catch {
                case e: IllegalArgumentException => println(s"Error: ${e.getMessage}")
                return false
            }
        }

        def anagrama(palabra1: String, palabra2: String): Boolean = {
            val palabra1_clean = palabra1.trim.toLowerCase()
            val palabra2_clean = palabra2.trim.toLowerCase()
            // organizo en orden alfabetico los caracteres del String en otro String
            val palabra1_sorted = palabra1_clean.toCharArray.sorted.mkString("")
            val palabra2_sorted = palabra2_clean.toCharArray.sorted.mkString("")
            return palabra1_sorted == palabra2_sorted
        }

        def isograma(palabra: String): Boolean = {
            val palabra_clean = palabra.trim.toLowerCase()
            // Crear un set vacio
            var set_letters = Set[Char]()
            for (letter <- palabra_clean) {
                if (set_letters.contains(letter)) {
                    println(s"Se repite la letra ${letter}")
                    return false
                }
                else {
                    set_letters + letter
                }
            }
            return true
        }

        def run(): Unit = {
            println("Ingresa la primer palabra: ")
            val palabra1 = scala.io.StdIn.readLine()
            
            println("Ingresa la segunda palabra: ")
            val palabra2 = scala.io.StdIn.readLine()

            // Seccion Palindromo
            val es_palindromo1 = palindromo(palabra1)
            val es_palindromo2 = palindromo(palabra2)

            if (es_palindromo1) {
                println(s"${palabra1}, es palindroma")
            }
            else {
                println(s"${palabra1}, NO es palindroma")
            }
    
            if (es_palindromo2) {
                println(s"${palabra2}, es palindroma")
            }
            else {
                println(s"${palabra2}, NO es palindroma")
            }

            // Seccion Anagrama
            val es_anagrama = anagrama(palabra1, palabra2)
            if (es_anagrama) {
                println(s"${palabra1} y ${palabra2} son anagramas")
            }
            else {
                println(s"${palabra1} y ${palabra2} NO son anagramas")
            }

            // Seccion Isograma
            val es_isograma1 = isograma(palabra1)
            val es_isograma2 = isograma(palabra2)

            if (es_isograma1) {
                println(s"${palabra1}, si es isograma")
            }
            else {
                println(s"${palabra1}, NO es isograma")
            }
            
            if (es_isograma2) {
                println(s"${palabra2}, si es isograma")
            }
            else{
                println(s"${palabra2}, NO es isograma")
            }
        }
        
        run()
    }
}