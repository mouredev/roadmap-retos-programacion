import Foundation
// RETO #04 CADENA DE CARACTERES

// Acceso a caracteres específicos
let my_str = "Rubik"
// Accede al primer caracter, en este caso "R"
let firstCharacter = my_str[my_str.startIndex]
print(firstCharacter)

// Accede al último caracter
let lastCharacter = my_str[my_str.index(before: my_str.endIndex)]
print(lastCharacter)

// Acceder a un caracter en posición X (En este caso la U)
let xPositionChar: Character = my_str[my_str.index(my_str.startIndex, offsetBy: 1)]
print(xPositionChar)

// Eliminar
// Eliminar el primer caracter
my_str.removeFirst()
print(my_str)
//Eliminar el último caracter
my_str.removeLast()
print(my_str)
// Eliminar todo
my_str.removeAll()
print(my_str)

// Concatenación
let my_str2 = "'s Cube"
let concatenation = my_str + my_str2
print(concatenacion)

// División
let div = "Cubik's Rubik".components(separatedBy: "'s")
print(div)

// Interpolación
let year = 1974
let text = "The Rubik's Cube was invented in \(year)"
print(text)

// Longitud
let length = my_str.count
print(length)

// Recorrer los caracteres que contiene el String
for character in my_str {
    print(character)
}

// Reemplazo
let replancing = my_str.replacingOccurrences(of: "u", with: "o")
print(replancing)

// Repetición
let rep = String(repeating: my_str, count: 3)
print(rep)

// Subcadenas
let subStr = my_str[1..<4]

// Verificación
let verification = my_str.contains("k")
print(verification)


// 🧩 DIFICULTAD EXTRA 🧩

func palindromo(_ str1: String) -> Bool {
    let invertedStr = String(str1.reversed())
    return str1 == invertedStr

} 

func anagrama(_ str2: String, _ str3: String) -> Bool {
    return str2.sorted() == str3.sorted()
}

func isograma(_ str4: String) -> Bool {
    let nonRepeatedChar = Set(str4)
    return str4.count == nonRepeatedChar.count
}

let str1 = "radar"
let str2 = "electromagnético"
let str3 = "magnetoeléctrico"
let str4 = "bebe"

print("Radar es palíndromo: \(palindromo(str1))")
print("Electromagnético y Magnetoeléctrico son anagramas: \(anagrama(str2, str3))")
print("Bebé es un isograma: \(isograma(str4))")