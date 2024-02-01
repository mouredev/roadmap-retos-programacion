fun main() {

    /*
    EJERCICIO:
    * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
    * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
    * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
    *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
    *
    */

    var miCadena: String = "Hola esto es una cadena"
    var miCadena2: String = "Esto es otra cadena"

    // Acceso a caracteres específicos
    println("ACCEDER a caracteries especificos")
    val Caracter = miCadena[2]
    println("El segundo caracter empezando por 0 de '$miCadena' es $Caracter")

    // Subcadenas
    println("CREAR SUBCADENAS:")
    val subcadena = miCadena2.slice(0..3)
    println(subcadena)

    val subcadena1 = miCadena2.substring(0, 7)
    println(subcadena1)

    // Longitud
    println("INDICAR LA LONGITUD TOTAL DE LAS CADENA:")
    println("La longitud de '$miCadena' es ${miCadena.length} caracteres")
    println("La longiutud de '$miCadena2' es ${miCadena2.length} caracteres")

    // Concatenar

    println("Aqui la CONCATENACIÓN " + miCadena2 + miCadena)
    println("$miCadena se une $miCadena2") // String templates

    // Repetición
    println("LA REPETICIÓN:")
    //val repeticion:String = miCadena*3
    //println (repeticion)

    val repeticion1 = miCadena.repeat(3)
    println(repeticion1)

    // Recorrido
    println("RECORRIDO")
    for (char in miCadena) {
            println(char)
    }
    // conversión a mayúsculas y minúsculas
    println("CONVERSION A MAYUSCULAS Y MINUSCULAS:")
    println(miCadena.uppercase())
    println(miCadena.lowercase())

    // reemplazo,
    println("REEMPLAZO")
    val nuevaCadena = miCadena.replace("cadena", "nueva cadena")
    println(nuevaCadena)

    // división,
    // . Dividir en palabras con el metodo split. Crea una lista.
    println("DIVISION")
    val palabras = nuevaCadena.split(" ")
    println(palabras)


    // unión,
    val cadenaUnida = palabras.joinToString("-")
    println(cadenaUnida)

    // empieza con, termina con

    val email = "usuario@example.com"

    // Verificar si la cadena comienza con "usuario"

    val comienzaConUsuario = email.startsWith("usuario")
    println("Comienza con 'usuario': $comienzaConUsuario")

    // Verificar si la cadena termina con ".com"
    val terminaConCom = email.endsWith(".com")
    println("Termina con '.com': $terminaConCom")

    // verificación

    println(cadenaUnida.contains("-"))

    //dar la vuela a una cadena
    println("DAR LA VUELTA A UNA PALABRA:")
    var cadena3: String = "cadena"
    var delreves: String = cadena3.reversed()
    println("La palabra '$cadena3' puesta al reves es '$delreves'")

    //ordenar los caracteres
    println("ORDENAR LAS LETRAS")
    var palabra: String = "roma"
    var nuevapalabra = palabra.toSortedSet()
    println(nuevapalabra)
// Extra:


    /* Crea un programa que analice dos palabras diferentes y realice comprobaciones
             * para descubrir si son:
             * - Palíndromos
             * - Anagramas
             * - Isogramas

            Palíndromos: Secuencias de caracteres que se leen igual de izquierda a derecha que de derecha a izquierda, como "oso" o "reconocer".

            Anagramas: Palabras o frases formadas reorganizando las letras de otra palabra o frase, manteniendo todas las letras originales. Ejemplo: "amor" y "Roma".

            Isogramas: Palabras en las que no se repite ninguna letra. Cada letra aparece solo una vez. Ejemplo: "murciélago".
             */

    println("INTRODUCE DOS PALABRAS")
    print("Primera palabra:")
    var palabra1: String= readln()
    print("Segunda palabra:")
    var palabra2: String= readln()
    println("La palabra 1 es '$palabra1' y la segunda es '$palabra2'")
    println(" ")
    println("Análisis de las palabras:")
    if (esPalindromo(palabra1)) {println ("La palabra $palabra1 es un palindromo")}
    if (esPalindromo(palabra2)) {println ("La palabra $palabra2 es un palindromo")}
    if(esAnagrama(palabra1,palabra2)) {println("La palabra $palabra1 y la palabra $palabra2 forman un anagrama")}
    if (esIsograma(palabra1)) {println ("La palabra $palabra1 es un isograma")}
    if (esIsograma(palabra2)) {println ("La palabra $palabra2 es un isograma")}

}

fun esPalindromo(palabra: String):Boolean{
    var reversa:String=palabra.reversed()
    return (palabra==reversa)
}

fun esAnagrama (palabra1:String, palabra2:String):Boolean{
    var ordenada1=palabra1.toCharArray().sorted()
    var ordenada2=palabra2.toCharArray().sorted()
    return (ordenada1==ordenada2)
}

fun esIsograma(palabra: String): Boolean {
    for (i in 0 until palabra.length - 1) {
            val subDivide = palabra.slice(i + 1 until palabra.length)
            if (subDivide.contains(palabra[i])) {
                    return false
            }
    }
    return true
}
