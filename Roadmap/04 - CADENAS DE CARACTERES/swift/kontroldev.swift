import Foundation

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


// Operaciones con cadenas de caracteres

// Acceso a caracteres específicos
let palabra = "Swift"
let primerCaracter = palabra[palabra.startIndex] // Accede al primer caracter ("S")

// Subcadenas
let subcadena = palabra[1..<3] // Crea una subcadena con los caracteres en las posiciones 1 y 2 ("wi")

// Longitud
let longitud = palabra.count // Obtiene la longitud de la cadena (5)

// Concatenación
let otraPalabra = " es genial"
let concatenacion = palabra + otraPalabra // Concatena dos cadenas ("Swift es genial")

// Repetición
let repetida = String(repeating: palabra, count: 2) // Repite la cadena dos veces ("SwiftSwift")

// Recorrido
for caracter in palabra {
    print(caracter) // Itera sobre cada caracter e imprime ("S", "w", "i", "f", "t")
}

// Conversión a mayúsculas y minúsculas
let mayusculas = palabra.uppercased() // Convierte a mayúsculas ("SWIFT")
let minusculas = palabra.lowercased() // Convierte a minúsculas ("swift")

// Reemplazo
let reemplazada = palabra.replacingOccurrences(of: "i", with: "o") // Reemplaza "i" con "o" ("Swott")

// División
let palabrasSeparadas = "Hola, mundo".components(separatedBy: ",") // Divide la cadena por coma (["Hola", " mundo"])

// Unión
let palabrasUnidas = palabrasSeparadas.joined(separator: " ") // Une las palabras con un espacio ("Hola mundo")

// Interpolación
let edad = 25
let mensaje = "Tengo \(edad) años" // Crea una cadena interpolada ("Tengo 25 años")

// Verificación
let contieneLetra = palabra.contains("w") // Verifica si la cadena contiene la letra "w" (true)


// Programa para comprobar palíndromos, anagramas e isogramas

func esPalindromo(_ palabra: String) -> Bool {
    let palabraInvertida = String(palabra.reversed())
    return palabra == palabraInvertida
}

func sonAnagramas(_ palabra1: String, _ palabra2: String) -> Bool {
    return palabra1.sorted() == palabra2.sorted()
}

func esIsograma(_ palabra: String) -> Bool {
    let caracteresSinRepetir = Set(palabra)
    return palabra.count == caracteresSinRepetir.count
}

// Ejemplos de uso

let palabra1 = "oso"
let palabra2 = "oso"
let palabra3 = "amor"

print("Es palíndromo: \(esPalindromo(palabra1))") // true
print("Son anagramas: \(sonAnagramas(palabra1, palabra2))") // true
print("Es isograma: \(esIsograma(palabra3))") // true

