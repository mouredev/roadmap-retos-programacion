
/*
 * 18miguelgalarza.swift Release #04 - swift
 * EJERCICIO: #04 CADENAS DE CARACTERES
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

import Foundation

//Concatenacion

let firstName = "John"
let lastName = "Doe"
let fullName = firstName + " " + lastName
print(fullName) // Salida: "John Doe"


//Intepolación

let age = 36
let message = "Tengo \(age) años de edad."
print(message) // Salida: "Tengo 30 años de edad."



//Longitud

let cadena = "Hello, playground!"
let length = cadena.count
print(length) // Salida: 13


//Acceso a caracteres individuales

let cadena1 = "world"
let firstChar = cadena1.first // Accede al primer carácter (opcional)
let lastChar = cadena1.last // Accede al último carácter (opcional)
print(firstChar as Any) // Salida: Optional("H")
print(lastChar as Any) // Salida: Optional("o")


//Comparacion

let c1 = "apple"
let c2 = "Apple"
if c1 == c2 {
    print("Las cadenas son iguales.")
} else {
    print("Las cadenas son diferentes.")
}


//Conversion a minúscula y mayúscula

let conversion = "Hello, World!"
let uppercaseStr = conversion.uppercased()
let lowercaseStr = conversion.lowercased()
print(uppercaseStr) // Salida: "HELLO, WORLD!"
print(lowercaseStr) // Salida: "hello, world!"

//Subcadenas

let sc = "Hello, World!"
let substring = sc.prefix(5) // Obtiene los primeros 5 caracteres
print(substring) // Salida: "Hello"


//Bûsqueda de subcadenas

let bs = "Hello, World!"
if bs.contains("World") {
    print("La subcadena 'World' está presente.")
} else {
    print("La subcadena 'World' no está presente.")
}





/*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
*/



func validaDosPalabrasPalindromo(_ word01:String, _ word02:String) -> Bool{
    return word01.lowercased().caseInsensitiveCompare(String(word02.lowercased().reversed())) == .orderedSame
}

func esPalindromo(_ word:String) -> Bool{
    return word.lowercased().caseInsensitiveCompare(String(word.lowercased().reversed())) == .orderedSame
}

func sonAnagramas(_ palabra1: String, _ palabra2: String) -> Bool {
    // Convertir las palabras a arrays de caracteres y ordenarlos alfabéticamente
    let array1 = palabra1.lowercased().sorted()
    let array2 = palabra2.lowercased().sorted()
    
    // Comparar los arrays resultantes
    return array1 == array2
}


func esIsograma(_ palabra: String) -> Bool {
    var letrasVistas = Set<Character>()
    
    for letra in palabra {
        if letrasVistas.contains(letra) {
            return false
        }
        letrasVistas.insert(letra)
    }
    
    return true
}


/*
print(validaDosPalabrasPalindromo("amor","roma") ? "Las palabras son palíndromos" : "No son Palíndromos")
print(esPalindromo("ama") ? "La palabra es palíndromo" : "No no es Palíndromo")
print(sonAnagramas("ama","ama") ? "Las palabras son Anagramas" : "No son Anagramas")
print(esIsograma("Marzo") ? "La palabra es Isograma" : "No no es Isograma")
*/

//programa

func analizadorDePalabras(_ p1:String, _ p2:String){
    print("\n\n")

    print(validaDosPalabrasPalindromo(p1,p2) ? "Las palabras son palíndromos" : "No son Palíndromos")
    print(esPalindromo(p1) ? "La palabra \(p1) es palíndromo" : "\(p1) no es Palíndromo")
    print(esPalindromo(p2) ? "La palabra \(p2) es palíndromo" : "\(p2) no es Palíndromo")
    print(sonAnagramas(p1,p2) ? "Las palabras son Anagramas" : "No son Anagramas")
    print(esIsograma(p1) ? "La palabra \(p1)  es Isograma" : "\(p1)  no es Isograma")
    print(esIsograma(p2) ? "La palabra \(p2)  es Isograma" : "\(p2)  no es Isograma")
}

analizadorDePalabras("ana", "marzo")

