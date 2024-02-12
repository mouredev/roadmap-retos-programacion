import Foundation

let cadena = "Esta va a ser nuestra cadena de ejemplo"

print(cadena)

// acceder al priemr caracter

print("El primer caracter es: \(cadena[cadena.startIndex])")

// acceder al ultimo caracter

print("El ultimo caracter es: \(cadena[cadena.index(before: cadena.endIndex)])")

// acceder a un caracter en una posicion concreta

print("Caracter en la posición 5 es: \(cadena[adena.index(cadena.startIndex, offsetBy: 5)])")

// subcadena

print("Subcadena: \(cadena[cadena.index(cadena.startIndex, offsetBy: 5)..<cadena.index(cadena.startIndex, offsetBy: 10)])")

// longitud

print("Longitud: \(cadena.count)")

// concatenación

let otraCadena = " y esta es otra cadena"

print("Concatenación: \(cadena + otraCadena)")

// repetición

print("Repetición: \(String(repeating: cadena, count: 2))")

// recorrido

for caracter in cadena {
    print(caracter)
}

// conversión a mayúsculas y minúsculas

print("Mayúsculas: \(cadena.uppercased())")

print("Minúsculas: \(cadena.lowercased())")

// reemplazo

print("Reemplazo: \(cadena.replacingOccurrences(of: "a", with: "o"))")

// busqueda de substring    
if let index = cadena.firstIndex(of: "a"){
    print("Substring: \(cadena[index...])")
}

// división

print("División: \(cadena.components(separatedBy: " "))")

// unión

print("Unión: \(cadena.components(separatedBy: " ").joined(separator: "-"))")

// interpolación

let name = "Migue"

print("Interpolación: Me llamo \(name)")

// verificación

print("Contiene la letra 'a': \(cadena.contains("a"))")

// Extra

func esPalindromo(_ palabra: String) -> Bool {
    let palabraInvertida = String(palabra.reversed())
    return palabra.lowercased() == palabraInvertida.lowercased()
}

func sonAnagramas(_ palabra1: String, _ palabra2: String) -> Bool {
    return palabra1.sorted() == palabra2.sorted()
}

func esIsograma(_ palabra: String) -> Bool {
    let caracteresSinRepetir = Set(palabra)
    return palabra.count == caracteresSinRepetir.count
}

print ("Ana es palíndromo: \(esPalindromo("Ana"))")
print ("roma y amor son anagramas: \(sonAnagramas("roma", "amor"))")
print ("Murcielago es isograma: \(esIsograma("Murcielago"))")
print ("Pavor es palíndromo: \(esPalindromo("Pavor"))")
print ("hola y ola Son anagramas: \(sonAnagramas("hola", "ola"))")
print ("colegiala es isograma: \(esIsograma("colegiala"))")


