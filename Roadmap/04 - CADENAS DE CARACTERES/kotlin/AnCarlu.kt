fun cadenas() {
//Operaciones con cadenas

    val name = "Adrian"
    //Concatenación
    println("Hola mi nombre es $name")

    //Acceso a caracteres especificos
    val firstCaracter = name[0]
    println("La primera letra de mi nombre es $firstCaracter")

    //Longitud de cadenas
    val lenghtName = name.length
    println("Ni nombre tiene $lenghtName caracteres")

    //Subcadenas
    val chain = "Las subcadenas muestran un conjunto de caracteres acotados"
    println(chain)
    println("Por ejemplo ${chain.substring(15, 35)}")

    //Comparacion de cadenas
    println("Comparación de cadenas:")
    println("Introduce un nombre")
    val newName = readln()
    if (name == newName) {
        println("Te llamas igual que yo :), ¡Hola tocayo!!")
    } else {
        println("Bonito nombre!!")
    }

    //Formateo de cadenas
    val newChain = "Ejemplo de Formateo de cadenas"
    println(newChain)
    println("Se puede modificar todo en mayusculas ${newChain.uppercase()}")
    println("Y tambien todo en minusculas ${newChain.lowercase()}")
    val trimChain = " Trim sirve para quitar los espacios en blanco tanto al principio como al final "
    println(trimChain.trim())

    //Remplazo de cadenas
    val replaceChain = "Hola a todos"
    println(replaceChain.replace("todos", "Kotlin"))

    //Division de cadenas
    val words = "Programar es pensar en soluciones"
    println(words.split(" "))

    //Verificacion
    println("¿Empieza con Hola?" + words.startsWith("Hola"))
    println("¿Termina en s?" + words.endsWith("s"))
    println("¿Contiene pensar? ${"pensar" in words}")
}

fun extraExercise() {
    println("Ahora comprobaremos si 2 palabras son palindromos, anagramas o isogramas")
    println("Añade la primera palabra")
    val word1 = readln()
    println("Añade la segunda palabra")
    val word2 = readln()
    palindromo(word1, word2)
    anagrama(word1,word2)
    isograma(word1)

}

fun palindromo(word1: String, word2: String) {
    //Comparo si la primera palabra es igual a la segunda al reves
    if (word1.lowercase() == word2.lowercase().reversed()) {
        println("Tus dos palabras son un palindromo")
    } else {
        println("Estas palabras no son un palindromo")
    }
}

fun anagrama(word1: String, word2: String): Boolean{
    //Primero compruebo si tiene la misma cantidad de letras
    if (word1.length!=word2.length){
        println("Tus palabras no pueden ser un anagrama porque no son de la misma longitud")
        return false
    }
    //Comparo si todas las letras de las dos palabras son iguales
    if ( word1.lowercase().toList().sorted()==word2.lowercase().toList().sorted()){
        println("Tus palabras añadidas podrian ser un anagrama")
        return true
    }else{
        println("No es posible que estas palabras sean un anagrama")
        return false
    }
}

fun isograma(word:String): Boolean{
    //Compruebo letra a letra la palabra
    val filterWord = word.lowercase().filter { it.isLetter() }
    //Si la longitud es la misma significa que no hay ninguna letra repetida, por lo tanto es un isograma
    if ( filterWord.toSet().size==filterWord.length){
        println("En la primera palabra no se repite ninguna letra" +
                "\nes un isograma")
        return true
    }else{
        println("Se repite alguna letra")
        return false
    }
}

fun main() {
    cadenas()
    extraExercise()
}