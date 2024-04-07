class strings {
    fun cadenas(){

        //Ejemplos de operaciones con cadenas de texto
        val cadena: String = "Este es un string y exploraremos diferentes operaciones con el, y sus posibilidades"

        //Operaciones con cadenas

        //Acceso a un caracter en especifico
        val caracter =  cadena[2]
        println("En este caso tare la letra $caracter ya que es la segunda letra de toda la cadena")

        //Subcadenas
        val subCadena = cadena.substring(0,3)
        println("En este caso tare unicamente la cadena $subCadena ya que le indicamos que traiga desde la primera letra que es 0 hasta la cuarta que es 3")

        //Longitud de la cadena
        val longitud = cadena.length
        println("La longitud de la cadena es $longitud")

        //Concatenacion
        val concatenacion = cadena + "En este caso se concateno un texto adicional"
        println(concatenacion)

        //Repeticion
        val repeticion = cadena.repeat(3)
        println("En este caso la cadena se repite el numero de veces que le indiquemos, como en este caso fueron 3 veces -> $repeticion")

        //recorrido de caracteres
        cadena.forEach{println("En este casi se imprimira caracter por caracter de la cadena -> $it")}

        //Conversion de mayusculas y minusculas
        val minus = cadena.toLowerCase()
        val mayus = cadena.toUpperCase()
        println("En este caso se convirtieron a mayusculas y minusculas -> Minus: $minus Mayus: $mayus")

        //Reemplazo
        val reemplazo = cadena.replace("string", "cadena de texto")
        println("Pra reemplazar primero se debe poner la palabra a reemplazar y luego la nueva -> $reemplazo")

        //Division en partes
        val division = cadena.split(",")
        division.forEach{println("En este caso la cedena se divide basado en un delimitador, ene ste caso una coma -> $it")}

        //Union de cadenas
        val union = division.joinToString(separator = ",")
        println("Aca unimos nuevamente la cadena que separamos anteriormenet y la unimos con la coma que antes era el delimitador")

        //Interpolacion
        println("Durante todo el ejercicio hemos aplicado la inetrpolacion, para hacerlo mas explicito aca interpolaremos la cadena inicial colocando el signo $ y el nombre de la variable -> $cadena")

        //verificacion de contenido
        val contiene = cadena.contains("string")
        val empiezaCon = cadena.startsWith("Este")
        val terminaCon = cadena.endsWith("posibilidades")
        println("En este caso se usan las funciones, contains, startsWith y endsWith, las cuales devuelven un valor booleano")

        //Eliminar espacios
        val noEspacios = cadena.trim()
        println("En este caso se eliminan los espacios de la cadena -> $noEspacios")

        //Punto Extra -> comprobador de cadenas

        //Begin
        println("Digita la primera palabra que vas a evaluar")
        val word1: String? = readLine()
        println("Digita la segunda palabra que vas a evaluar")
        val word2 = readLine()

        //Palindrome validation
        fun palindrome(word: String?){
            var counter: Int = 0
            var reverseWord: Int = 1
            for(i in word!!){
                for(j in word.length -reverseWord downTo 0){
                    val value = word[j]
                    if(i == value){
                        counter++
                        reverseWord++
                    }
                    break
                }
            }
            if(counter == word.length){
                println("La palabra $word es un palindromo")
            }else{
                println("La palabra $word no es un palindromo")
            }
        }

        //Anagram validation
        fun anagram(word1: String?, word2: String?){
            var counter: Int = 0
            if(word1!!.length == word2!!.length){
                val word1List = word1!!.toList()
                val word2List = word2!!.toList()
                for(i in word1.indices){
                    if(word1List.sorted()[i] == word2List.sorted()[i])
                        counter++
                }
                if(counter == word1.length){
                    println("Las palabras $word1 y $word2 forman un anagrama")
                }else{
                    println("Las palabras $word1 y $word2 no forman un anagrama")
                }
            }else{
                println("Las palabras no conforman un anagrama")
            }

        }

        //Isogram validation
        fun isogram(word: String?){
            var sum = 0
            var index = 0
            var unique = word!!.toList().distinct().joinToString("")
            var counter: MutableMap<Char, Int> = mutableMapOf()
            var iterator: Int = 0
            for(i in unique!!){
                counter.put(i, 0)
            }
            for(i in counter.keys){
                for(j in word){
                    if(i == j){
                        index++
                    }
                    counter[i] = index
                }
                index = 0
            }
            val values: List<Int> = counter.values.toList().distinct()
            if(values.size > 1){
                println("la palabra $word no es un isograma")
            }else{
                println("la palabra $word es un isograma")
            }
        }

        //Executions
        palindrome(word1)
        palindrome(word2)
        anagram(word1,  word2)
        isogram(word1)
        isogram(word2)

    }
    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val obj = strings()
            obj.cadenas()
        }
    }
}