fun ejercicioExtra(){
    print("Escoge la primera palabra para comprobar: ")
    val word1 = readln()
    print("Escoge la segunda palabra para comprobar: ")
    val word2 = readln()

    fun isPalindromo(word: String): String {
        //palíndromo: se lee igual al derecho que al revés
        return if (word == word.reversed()){
            ("Es un palíndromo")
        }else{
            ("No es un palíndromo")
        }
    }

    fun isAnagrama(word1: String, word2: String): String {
        //anagrama: cambian de orden las letras de una palabra para formar otra
        val list1 = mutableListOf<Char>()
        val list2 = mutableListOf<Char>()

        for (letter in word1.lowercase()){
            list1.add(letter)
            list1.sort()
        }
        for (letter2 in word2.lowercase()){
            list2.add(letter2)
            list2.sort()
        }
        return if (list1 == list2){
            "Estas 2 palabras son anagramas"
        }else{
            "Estas 2 palabras no son anagramas"
        }
    }

    fun isIsograma(word: String): String {
        //isograma: palabra o frase que cada letra aparece el mismo número de veces
        val letters = mutableMapOf<Char, Int>()

        for (letter in word){
            if (letter in letters){
                letters[letter] = letters[letter]!! + 1
            }else{
                letters[letter] = 1
            }
        }

        val setCounter = letters.values.toSet()

        if (setCounter.size == 1){
            return "Es un isograma"
        }else{
            val repeatedChars = mutableListOf<Char>()

            for ((key, value) in letters){
                if (value >= 2){
                    repeatedChars.add(key)
                }
            }
            return "No es un isograma. Se repiten las letras: $repeatedChars"
        }
    }

    println("Palabra 1: " + isPalindromo(word1))
    println("Palabra 2: " + isPalindromo(word2))
    println("Las palabras elegidas " + isAnagrama(word1, word2))
    println("Palabra 1: " + isIsograma(word1))
    println("Palabra 2: " + isIsograma(word2))
}


fun main() {
    val stringEjemplo = "Este es el string de ejemplo"
    println(stringEjemplo)

    println("\n\t-> Acceso a caracteres específicos:")
    println("En la posición ${stringEjemplo.indexOf("s el")} se encuentra el caracter ${stringEjemplo[6]}")

    println("\n\t-> Subcadenas")
    print("Acceso a una subcadena: ")
    println("\t" + stringEjemplo.substring(3,13))
    print("Está \"X\" en una cadena: ")
    println("\t ejemplo" in stringEjemplo)

    println("\n\t-> Longitud:")
    println("${stringEjemplo.length} caracteres")

    println("\n\t-> Concatenación")
    println(stringEjemplo + "y este es un añadido")
    val string2 = ", soy el string 2 añadido"
    println(stringEjemplo + string2)

    println("\n\t-> Repetición")
    println(stringEjemplo.repeat(2))

    println("\n\t-> Recorrido")
    for (elem in stringEjemplo){
        println(elem)
    }
    for (elem in stringEjemplo.split(" ")){
        println(elem)
    }

    println("\n\t-> Mayúsculas y minúsculas")
    println(stringEjemplo.uppercase())
    println(stringEjemplo.replaceFirstChar { it.uppercaseChar() })
            //también serviría .capitalize(), pero parece estar 'deprecated' y aparece tachado aunque funcione
    println(stringEjemplo.lowercase())

    println("\n\t-> Reemplazo")
    val wordsEjemplo = stringEjemplo.split(" ").toMutableList()
    wordsEjemplo[1] = "no es"
    val wordsUnit = wordsEjemplo.joinToString(" ")
    println(wordsUnit)

    println("\n\t-> División")
    println(stringEjemplo.split(" "))

    println("\n\t-> Interpolación")
    println("Recordemos que la cadena principal es: $stringEjemplo")

    println("\n\t-> Verificación")
    if (stringEjemplo is String){
        println("Es un string")
    }else{
        println("No es un string")
    }

    println("\n\t-> Pertenencia")
    println("ejemplo" in stringEjemplo)
    println("mondongo" in stringEjemplo)


    println("\n" + "~".repeat(9) + " EJERCICIO EXTRA " + "~".repeat(9))
    ejercicioExtra()
}
