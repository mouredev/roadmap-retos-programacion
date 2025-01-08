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

// Operadores con cadena de caracteres 

// Caracteres especificos 
let nombre = "Pedro"
let fisrtCharacter = nombre[nombre.startIndex] // Verificar el primir caracter de la cadena P

print(fisrtCharacter) // Imprimir en la consola firstChracter 

// Interpolacion
let nombre = "Pedro"
let interpolacion = "El nombre es \(nombre)" // Interpolacion de la cadena de texto mediante \()

print(interpolacion)

// Concatenacion 
let nombre1 = "Pedro"
let nombre2 = "Juan"
let concatenacion = nombre1 + nombre2 // Se le suma una constante a la otra a traves de la concatenacion

print(concatenacion) // Imprimir en la consola concatenacion 

// Repeticion
let nombre = "Pedro"
let repeticion = String(repeating: "Pedro", count: 2) // La cadena de texto "Pedro" se repite 2 veces 

print(repeticion)

// Verificacion
let nombre = "Pedro"
let verificacion = nombre.contains("P") // Verificar si el caracter "P" se encuentra dentro de la cadena 

print(verificacion) // Imprimir en la consola verificacion 

// Longitud
let nombre = "Pedro"
let longitud = nombre.count // Verificar la longitud de la cadena de texto 

print(longitud) // Imprimir en la consola longitud

// Recorrido
let nombres = "Pedro"

for character in nombres { // Se recorre la cadena de texto "Pedro" 5 veces 
    print(nombres)
}

// Division 
let nombre = "Hola Mundo"
let division = "Hola, Mundo".components(separatedBy: ",") // Separa la cadena de texto "Hola Mundo" con la , 

print(division)

// Union
let division = "Hola, Mundo".joined(separated: " ") // La cadena de texto "Hola Mundo" se unen 

// Conversion a Mayuscula
let nombre = "pedro"
let conversion = nombre.uppercased() // La cadena de texto "pedro" cambia a mayuscula "PEDRO"

// Conversion a Minuscula 
let nombre = "PEDRO"
let conversion = nombre.lowercased() // La cadena de texto "PEDRO" cambia muniscula "pedro"

// Subcadenas 
let nombre = "Pedro"
let subcadena = nombre[1...<4] // Se crea una subcadena de la cadena de texto "Pedro" entre las posiciones 1, 2, 3




