import Foundation



// Cadena de caracteres
print("\nCADENA DE CARACTERES\n")

var string: String = "Hello, World"
print(string)


// Acceso a caracteres especificos
print("\nACCESO A CARACTERES ESPECIFICOS")

print("\nAcceso al Primer Caracter Del String")

// Accedar al primer caracter del string
let firstCharacter = string[string.startIndex]
print(firstCharacter)

// Acceder al primer caracter del string
if let firstCharacter: Character = string.first {
    print(firstCharacter)
} else {
    print("El string esta vacio")
}

print("\nAcceso al Ultimo Caracter Del Sting")

// Acceder al ultimo caracter del string
let lastCharacter: Character = string[string.index(before: string.endIndex)]
print(lastCharacter)

// Acceder al ultimo caracter del string
if let lastCharacter: Character = string.last {
    print(lastCharacter)
} else {
    print("El string esta vacio")
}

print("\nAcceso al Caracter en la Posicioón 3 Del String")

// Acceder al caracter en la posición 3 del string
let thirdCharacter: Character = string[string.index(string.startIndex, offsetBy: 2)]
print(thirdCharacter)

print("\nAcceso al Caracter en la Posición 2 Del String")

// Acceder al caracter en la posición 2 del string
let seconCharacter: Character = string[string.index(after: string.startIndex)]
print(seconCharacter)

print("\nAcceso al Caracter en la Posición 5 Del String")

// Acceder al caracter en la posición 5 del string
let fifthIndex: String.Index = string.index(string.startIndex, offsetBy: 4)
let fifthCharacte: Character = string[fifthIndex]
print(fifthCharacte)



// Recorrer
print("\nRECORRER")

print("\nRecorrer Todos Los Caracteres Del String")

// Recorrer todol los caracteres del string
for character in string {
    print(character)
}



// SubCadenas
print("\nSUBCADENAS")

print("\nSubstring Con Los 3 Primeros Caraxteres Del String")

// Substring con los tres primeros caracteres del string
let firstThreeCharacters = string.prefix(3)
print(firstThreeCharacters)

print("\nSubstring Con Los 5 Ultimos Caracteres Del String")

// Substring con los 5 ultimos caracteres del string
let lastFiveCharacters = string.suffix(4)
print(lastFiveCharacters)

print("\nSubstring Desde el Primer Caracter al 4")

// Substring desde el primer caracter al 4
let prefixTo = string.prefix(upTo: string.index(string.startIndex, offsetBy: 4))
print(prefixTo)

print("\nSubstring Desde el Caracter 4 Hasta el Final")

// Substring desde el caracter 4 hasta el final
let suffixFrom = string.suffix(from: string.index(string.startIndex, offsetBy: 4))
print(suffixFrom)

print("\nSubstring Desde el Primer Caracter Hasta Que Aparecca la Letra \"r")

// Substring Desde el primer caracter hasta que aparacca la letra "r"
let prefixWhile = string.prefix(while: { $0 != "r" })
print(prefixWhile)

print("\nSubstring Con Los Caracteres Del String Excluyendo Los 2 Primeros")

// Substring con los caracteres del string excluyendo los 2 primeros
let dropTwoFirstCharacters = string.dropFirst(2)
print(dropTwoFirstCharacters)

print("\nSubstring Con Los Caracteres Del String Excluyendo Los 4 Ultimos")

// Substring con los caracteres del string expluyendo los 4 ultimos
let dropFourLastCharacter = string.dropLast(4)
print(dropFourLastCharacter)

print("\nRango Para Obtener Substring Con Los 5 Primeros Caracteres")

// Rango para obtener substring con los 5 primeros caracteres
let startIndex = string.index(string.startIndex, offsetBy: 0)
let endIndex: String.Index = string.index(string.startIndex, offsetBy: 5)
let hello = string[startIndex..<endIndex]
print(hello)

print("\nRango Para Obtener Substring Con Los Caracteres Del 7 al 12")

// Rango para obtener substring con los caracteres del 7 al 12
let indexRange = string.index(string.startIndex, offsetBy: 7)..<string.index(string.startIndex, offsetBy: 12)
let world = string[indexRange]
print(world)

print("\nRango de Las Letras \"rld\" Del String")

// Rango de las letras "rld" del estring
if let range = string.range(of: "rld") {
    print(string[range])
}



// División
print("\nDIVISIÓN")

print("\nDivision en un Array Separados Por el Delimitador \",\"")

// Division en un arrray separados por el delimitador ","
let splitByComa = string.split(separator: ",")
print(splitByComa)

print("\nDivision en un Array de un Maximo de 3 Elementos Omitiendo los Substrings Vacios y separados pr el delimitador \"o\"")

// Division en un array de un maximo de 3 subcastring, omitiendo los subcadenas vacias y separados por el delimitador "0"
let splitWhere = string.split(maxSplits: 3, omittingEmptySubsequences: true, whereSeparator: { $0 == "o"})
print(splitWhere)

print("\nDivision en un Array Separados Por el Delimitador \", \"")

// Division en un array separados por el dilimitador ", "
let componentsByComaAndSpace = string.components(separatedBy: ", ")
print(componentsByComaAndSpace)



// Longitud
print("\nLONGITUD")

print("\nLongitud Del String")

// Longitud del string
let countString = string.count
print(countString)



// Concatenación
print("\nCONCATENACIÓN")

print("\nConcatenación de \"!\" al String")

// Concatena "!" sl string 
string += "!"
print(string)

print("\nConcatenación de \"!!!\" al String")

// Concate "!!!" al string
let concatenation1 = string + "!!"
print(concatenation1)

print("\nConcatenación de \"Hello, World\" al String")

// Concatena "Hello, World" al string
let concatenation2 = String("Hello" + "," + " " + "World!")
print(concatenation2)



// Interpolación
print("INTERPOLACIÓN")

print("\nInterpolación de \"I'm Swift\" al String")

// Interpola "I'm Seift" al string
let interpolation1 = "\(string) I'm Swift"
print(interpolation1)



// Union
print("\nUNIÓN")

print("\nConcatenación de \"Are You Ready to Code?\" al String")

// Concatena "Are you Ready to Code?" al string
let concatenation3 = string.appending(" Are You Readi to Code?")
print(concatenation3)



// Repetición
print("\nREPETICIÓN")

print("\nRepetición de 10 Veces el Caracter \"a\" en un string")

// Repite el caracter "a" 10 veces en un string
let repeatingCharacters = String(repeating: "a", count: 10)
print(repeatingCharacters)

print("\nRepetición de 10 Veces el String \"Swift\" en un String")

// Repite el string "Swift" 10 veces en un string
let repeatingString = String(repeating: "Swift", count: 10)
print(repeatingString)



// Mayusculas
print("\nMAYUSCULAS")

print("\nTransformar el String a Mayusculas")

// Transforma el string a mayusculas
let upperCasedSting = string.uppercased()
print(upperCasedSting)

print("\nTransformas el String a Mayusculas Teniendo en Cuenta la Localizacion y Reglas linguisticas Del Dispositivo")

// Transforma a mayusculas teniendo en cuenta la localización, y las reglas linguisticas del dispositivo
let upperCasedByLocation: String = string.uppercased(with: Locale.current)
print(upperCasedByLocation)

print("\nTranformar el String a Mayusculas Uno a Uno Con un Bucle")

// Transforma el string a mayusculas uno a uno con un bucle
var upperCasedLoop = ""
for character in string {
    upperCasedLoop += String(character).uppercased()
}
print(upperCasedLoop)

print("\nTransformar Cade Caracter Del String a Mayusculas y metiendolos en un arry")

// Transforma el string a mayusculas y metie cada caracter en un array
let upperCasedMap = string.map( { String($0.uppercased()) } )
print(upperCasedMap)



// Minusculas
print("\nMINUSCULAS")

print("\nTransformar el String a Minusculas")

// Transforma el string a minusculas
let lowerCasedString = string.lowercased()
print(lowerCasedString)

print("\nTransformas el String a Minusculas Teniendo en Cuenta la Localizacion y Reglas linguisticas Del Dispositivo")

// Transforma a minusculas teniendo en cuenta la localización, y las reglas linguisticas del dispositivo
let lowerCasedByLocation = string.lowercased(with: Locale.current)
print(lowerCasedByLocation)

print("\nTransformar el String Uno a Uno Usando un Bucle")

// Transforma el string a minusculas uno a uno usando un bucle
var lowerCasedLoop = ""
for character in string {
    lowerCasedLoop += String(character).lowercased()
}
print(lowerCasedLoop)

print("\nTransforma el String a Minusculas y Mete Cada Caracter en un Array")

// Transforma el string a minusculas y metie cada caracter en un array
let lowerCasedMap = string.map( { String($0.lowercased()) } )
print(lowerCasedMap)



// Reemplazo
print("\nREEMPLAZO")

print("\nReemplaza el caracter \"r\" por \"R\"")

// Reemplaza el caracter "r" por "R" 
let remplacingOcurrencesString = string.replacingOccurrences(of: "r", with: "R")
print(remplacingOcurrencesString)

print("\nReemplaza los Caracteres \"l\" Por \"L\"")

// Reemplaza los caracteres ¨l" por "L"
let remplacingWhitMap = String(string.map({ $0 == "l" ? "L" : $0 }))
print(remplacingWhitMap)



// Verificación
print("\nVERIFICACIÓN")

print("\nVerificación si el String Contiene el Caracter \"W\"")

// Verifica si el string contiene el caracter "W"
let containsCharacter = string.contains("W")
print(containsCharacter)

print("\nVerificación si el String Contiene la Cadena \"Hello\"")

// Verifica si el string contiene la cadena "Hello"
let containsString = string.contains("Hello")
print(containsString)

print("\nVerificación si el String Contienen el Substring \"o,\"")

// Verifica si el string contiene el substring "o,"
let containsSubString = string.contains("o,")
print(containsSubString)

print("\nVerificación si el String Cumple con la Condición Del Parameter where")

// Verifica si el string cumple con la condición del parametro where
let containsWhere = string.contains(where: { $0 == "r" })
print(containsWhere)



// Eliminar
print("\nELIMINAR")

print("\nEliminar el Primer Caracter Del String")

// Elimina el primer caracter del string
string.removeFirst()
print(string)

print("\nEliminar Los Dos Primeros Caracterres Del String")

// Elimina los 2 primeros caracteres del string
string.removeFirst(2)
print(string)

print("\nEliminar el Ultimo Caracter Del String")

// Elimina el ultimo caracter del string
string.removeLast()
print(string)

print("\nElimina Los Dos Ultimos Caracteres Del String")

// Elimina los dos ultimos caracteres del string
string.removeLast(2)

print("\nElimina el Cuerto Elemento Del String")

// Elimina el cuarto elemento del string
string.remove(at: string.index(string.startIndex, offsetBy: 3))
print(string)

print("\nEliminar el Rango de Caracteres Del Tercer Elemento al Quinto Del String")

// Elimina el rango de caracteres del tercer al quinto del string
string.removeSubrange(string.index(string.startIndex, offsetBy: 2)...string.index(string.startIndex, offsetBy: 4))
print(string)

print("\nElimina Todos Los Caracteres Del String")

// Wlimina todos los caracteres del string
string.removeAll()
print(string)



// Dificultad Extra
print("\nDIFICULTAD EXTRA")

func isPalindromeAnagramOrIsogram(str1: String, str2: String) {
    // palindromo
    var wordOfStr1: String = ""
    var wordReversedOfStr1: String = ""
    var wordOfStr2 = ""
    var wordReversedOfStr2: String = ""

    wordOfStr1 = str1
    wordOfStr2 = str2
    
    for c in str1.reversed() {
        wordReversedOfStr1.append(c)
    }

    if wordOfStr1 == wordReversedOfStr1 {
        print("\(str1) es un palindromo")
    } else {
        print("\(str1) no es un palindromo")
    }

    for c in str2.reversed() {
        wordReversedOfStr2.append(c)
    }

    if wordOfStr2 == wordReversedOfStr2 {
        print("\(str2) es un palindromo")
    } else {
        print("\(str2) no es un palindromo")
    }


    // Anagrama
    let sortedArrayOfStr1 = str1.lowercased().sorted()
    let sortedArrayOfStr2 = str2.lowercased().sorted()

    if sortedArrayOfStr1 == sortedArrayOfStr2 {
        print("\(str1) y \(str2) son anagrama")
    } else {
        print("\(str1) y \(str2) no son anangramas")
    }


    // Isograma
    var repeatedCharacterOfStr1 = false
    var characterArrayOfStr1 = [Character]()
    var repeatedCharacterOfStr2 = false
    var characterArrayOfStr2 = [Character]()

    for character in wordOfStr1 {
        if characterArrayOfStr1.contains(character) {
            repeatedCharacterOfStr1 = true
            break
        } else {
            characterArrayOfStr1.append(character)
        }
    }

    if repeatedCharacterOfStr1 {
        print("\(str1) no es un isograma")
    } else {
        print("\(str1) es un isograma")
    }

    for character in wordOfStr2 {
        if characterArrayOfStr2.contains(character) {
            repeatedCharacterOfStr2 = true
            break
        } else {
            characterArrayOfStr2.append(character)
        }
    }

    if repeatedCharacterOfStr2 {
        print("\(str2) no es un isograma")
    } else {
        print("\(str2) es un isograma")
    }
    
}
isPalindromeAnagramOrIsogram(str1: "amor", str2: "roma")



