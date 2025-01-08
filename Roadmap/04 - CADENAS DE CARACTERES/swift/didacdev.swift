import Foundation

// Concatenación

var hello = "hello"
var world = " world"

print(hello + world)

// Iterar
var animals = "🐶🐵🐻"

for animal in animals {
    print(animal)
}

// Construcción a partir de caracteres
let characters:[Character] = ["h", "e", "l", "l", "o"]
let string = String(characters)
print(string)

// Interpolación
let name = "Diego"
let message = "Su nombre es \(name)"
print(message)

// Unicode
let character = "\u{1F425}"
print(character)

// Combinar caracteres
let combine = "\u{65}\u{301}" // é
print(combine)

// Tamaño de la cadena
let word = "esternocleidomastoideo"
print(word.count)

// Obtener un caracter
let saludo = "hello world"

print(saludo[saludo.startIndex]) // primero
print(saludo[saludo.index(before: saludo.endIndex)]) // último
print(saludo[saludo.index(after: saludo.startIndex)]) // segundo
print(saludo[saludo.index(saludo.startIndex, offsetBy: 6)]) // cualquier posición

for index in saludo.indices {
    print("\(saludo[index])")
}

// Insertar
hello.insert(contentsOf: "\(world)!", at: hello.endIndex)
print(hello)

// Eliminar
hello.remove(at: hello.index(before: hello.endIndex))
print(hello)

// Subcadenas
let index = hello.firstIndex(of: " ") ?? hello.endIndex
let beggining = hello[..<index]

hello = String(beggining)

print(hello)

// Comparación
let sameHello = "hello"

if hello == sameHello {
    print("\(hello) y \(sameHello) Son iguales")
}

// Repetición
let doubleHello = String(repeating: hello, count: 2)
print(doubleHello)

// Conversión mayúsculas
let mayusHello = hello.uppercased()

print(mayusHello)

// Conversión a minúsculas
let minusHello = mayusHello.lowercased()
print(minusHello)

// Reemplazar caracter
let newHello = String(hello).replacingOccurrences(of: "h", with: "H")
print(newHello)

// División
let sentence = "hello world"
let words = sentence.split(separator: " ")
print(words)

// Verificación
if newHello.contains("H") {
    print("Contiene H")
}

// -------------------- Ejercicio ------------------------

func checkWords(word1: String, word2: String) {
    if isPalindromo(word1: word1, word2: word2) {
        print("\(word1) y \(word2) son palíndromos")
    } else {
        print("\(word1) y \(word2) no son palíndromos")
    }
    
    if isAnagrama(word1: word1, word2: word2) {
        print("\(word1) y \(word2) son anagramas")
    } else {
        print("\(word1) y \(word2) no son anagramas")
    }

    if isIsograma(word: word1) {
        print("\(word1) es un isograma")
    } else {
        print("\(word1) no es un isograma")
    }

    if isIsograma(word: word2) {
        print("\(word2) es un isograma")
    } else {
        print("\(word2) no es un isograma")
    }
}

func isPalindromo(word1: String, word2: String) -> Bool{

    let reversedWord2 = String(word2.reversed())
    if word1.count == word2.count {

        for i in 0..<word1.count {
            let character1 = word1[word1.index(word1.startIndex, offsetBy: i)]
            let character2 = reversedWord2[reversedWord2.index(reversedWord2.startIndex, offsetBy: i)]

            if character1 != character2 {
                return false
            }
        }

        return true
    } 

    return false
}

func isAnagrama(word1: String, word2: String) -> Bool {
    var checkingWord = word2 

    for character in word1 {
        if checkingWord.contains(character) {
            
            if let index = checkingWord.firstIndex(of: character) {
                checkingWord.remove(at: index)
            }
        } else {
            return false
        }
    }

    return true
}

func isIsograma(word: String) -> Bool{
    var characters: [String: Int] = [:]

    for character in word {
        characters[String(character)] = characters[String(character)] != nil ? characters[String(character)]! + 1 : 1
    }

    var i = 0
    for (key, value) in characters {
        
        if i == 0 {
            i = value
        } else {
            if i != value {
                return false
            }
        }
    }

    return true
}

checkWords(word1: "lacteo", word2: "coleta")