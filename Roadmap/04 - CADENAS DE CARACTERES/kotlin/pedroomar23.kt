/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

 // Cadena de Caracteres 
 val myString = "Hola Mundo"

 // Longitud 
 println(myString.length)

 // Concatenacion
 println("My Name" + myString)

 // Interpolacion 
 println("Kotlin usa $myString")

 // Mayuscula 
 println(myString.toUpperCase())

 // Minuscula 
 println(myString.toLowerCase())

 // SubCadenas 
 println(myString.substring(0, 2))

 // Reemplazar
 println(myString.remplace("H", "M"))

 // Recorrido 
 for (i in myString) {
    print(i)
 }

 


