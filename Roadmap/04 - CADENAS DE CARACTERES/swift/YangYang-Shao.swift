/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


import Foundation

//Acceso a caracteres específicos
let saludo = "Bonjour, monde!"
let primerCaracter = saludo[saludo.startIndex]
let tercerCaracter = saludo[saludo.index(saludo.startIndex, offsetBy: 2)]
print("Primer caracter: \(primerCaracter), Tercer caracter: \(tercerCaracter)")

let saludo2 = "Hola, mundo!"
let accesoCaracteres = Array(saludo2)
print(accesoCaracteres[0]) 
print(accesoCaracteres[1])
print(accesoCaracteres[2])
print(accesoCaracteres[4])

//Logitud
let longitudSaludo = saludo.count
print("Longitud del saludo: \(longitudSaludo)")

//Concatenación
let nombre = "Ruru"
let saludo3 = "Hello"
let saludoCompleto = saludo3 + ", " + nombre + "!"
print(saludoCompleto)

//Uppercase y Lowercase
let saludoMayusculas = saludo.uppercased()
let saludoMinusculas = saludo.lowercased()
print("Saludo en mayúsculas: \(saludoMayusculas)")
print("Saludo en minúsculas: \(saludoMinusculas)")

//Recorrido
for c in saludo {
    print(c)
}   

//Interpolación
let edad = 25
let mensaje = "Tengo \(edad) años."
print(mensaje)

//Verificación
let esVacio = saludo.isEmpty
print("El saludo está vacío? \(esVacio)")

let checkPrefix = saludo.hasPrefix("Bonjour")
print("El saludo empieza con 'Bonjour'? \(checkPrefix)")

let checkSuffix = saludo.hasSuffix("monde!")
print("El saludo termina con 'monde!'? \(checkSuffix)")

let checkContains = saludo.contains("monde")
print("El saludo contiene 'monde'? \(checkContains)")

//Subcadenas
let subIndice = saludo.prefix(3)
let subFinal = saludo.suffix(6)
print("Subcadena desde el inicio: \(subIndice)")
print("Subcadena desde el final: \(subFinal)")

let wholeString = String(saludo.prefix(3))
print("Subcadena completa: \(wholeString)")

//Repetición
let repetido = String(repeating: "Hola! ", count: 3)
print("Cadena repetida: \(repetido)")

//Reemplazo
let saludoReemplazado = saludo.replacingOccurrences(of: "Bonjour", with: "Salut")
print("Saludo reemplazado: \(saludoReemplazado)")   

//División
let saludoParts = saludo2.split(separator: ",")
print(saludoParts)

//Unión
let words = ["Swift", "es", "genial"]
let joinedWords = words.joined(separator: " ")
print("Palabras unidas: \(joinedWords)")


//DIFICULTAD EXTRA
func esPalindromo(_ palabra: String) -> Bool {
    let alReves = String(palabra.reversed())
    return palabra.lowercased() == alReves.lowercased()
}
print(esPalindromo("Ana"))
print(esPalindromo("GATO"))

func sonAnagramas(_ palabra1: String, _ palabra2: String) -> Bool {
    let sorted1 = palabra1.lowercased().sorted()
    let sorted2 = palabra2.lowercased().sorted()
    return sorted1 == sorted2
}
print(sonAnagramas("Roma", "Amor"))
print(sonAnagramas("Hola", "Adiós"))

func esIsograma(_ palabra: String) -> Bool {
    let lowercasedWord = palabra.lowercased()
    let uniqueCharacters = Set(lowercasedWord)
    return uniqueCharacters.count == lowercasedWord.count
}
print(esIsograma("Roma"))
print(esIsograma("CASA"))