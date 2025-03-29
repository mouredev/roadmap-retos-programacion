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

import Foundation

// Creación de cadena de caracteres
let Saludo: String = "Hola!"
print(Saludo)

// Concatenación de cadena de caracteres
let palabra1: String = "Bienvenido"
let palabra2: String = " al curso de Swift!"
let mensaje: String = palabra1 + palabra2
print(mensaje)

var mutableSaludo: String = "Mundo!"
mutableSaludo.append(" ¿Cómo estás?")
print(mutableSaludo)

//interopolación de cadena de caracteres
let nombre: String = "Arturo"
let edad: Int = 25
let saludoPersonalizado: String = "Hola, mi nombre es \(nombre) y tengo \(edad) años."
print(saludoPersonalizado)

// Longitud de cadena de caracteres
let texto: String = "Soy una cadena de caracteres"
print(texto.count)

// Acceso a caracteres
let palabra3: String = "Swift"
let indice = palabra3.index(palabra3.startIndex, offsetBy: 1)
print (palabra3[indice])

// Recorrer cadena de caracteres
let palabra4: String = "Pirineos"
for caracter in palabra4 {
    print(caracter)
}

// Convertir a mayusculas o minusculas
let palabra5 : String = "Mandarina"
print(palabra5.uppercased())
print(palabra5.lowercased())

// Buscar palabra en una cadena
let palabra6: String = "El almendro florece al principio de la primavera"
print(palabra6.contains("primavera"))

//Obtener el indice de una palabra
if let rango = palabra6.range(of: "primavera") {
    print("Encontrado en la posición \(palabra6.distance(from: palabra6.startIndex, to: rango.lowerBound))")
}

// Remplazar texto en cadena
let palabra7: String = "Swift es un lenguaje de programación"
let nuevaFrase: String = palabra7.replacingOccurrences(of: "Swift", with: "Kotlin")
print(nuevaFrase)

//Extraer subcadenas de carateres
let palabra8: String = "La Jirafa tiene un largo cuello"
let inicio = palabra8.index(palabra8.startIndex, offsetBy: 25)
let subcadena = palabra8[inicio...]
print(subcadena)

//Dividir una cadena de caracteres
let lista: String = "camarón, langosta, langostino"
let mariscos = lista.split(separator: ",")
print (mariscos)
print(mariscos[1])

//Convertir entre String y Int
let numeroYTexto: String = "123"
if let numero: Int = Int(numeroYTexto) {
    print(numero)
}

// Eliminar espacios en blanco
let textoConEspacios: String = " Texto con espacios "
print(textoConEspacios)
print(textoConEspacios.trimmingCharacters(in: .whitespaces))

//Compararar cadena de caracteres
let a: String = "Swift"
let b: String = "swift"
print (a == b)
print(a.lowercased() == b.lowercased())
 
func menu(){
    
    print(" ------------------------------------------ ")
    print("| Bienvenido al comparador de palabras!    |")
    print("|   Ingresa palabras para comprobar si     |")
    print("| son palíndromos,anagramas o isogramas:   |")
    print("|         Elige una opcion:                |")
    print("|          1 - Palindromos                 |")
    print("|          2 - Anagramas                   |")
    print("|          3 - Isogramas                   |")
    print("|          4 - Salir                       |")
    print(" ------------------------------------------ ")
    
    if let opcionUsuario = readLine(){
        switch opcionUsuario {
        case "1":
            palindromo()
        case "2":
            anagrama()
        case "3":
            isograma()
        case "4":
            print("Gracias por usar el programa!")
            break
        default:
            print("Opcion no valida")
            
        }
    }
}

func palindromo(){
    print("Ingresa una palabra:")
    if let primeraPalabra = readLine(){
        if primeraPalabra == String(primeraPalabra.reversed()) {
            print("Es un palindromo")
            sleep(3)
            menu()
        } else {
            print("No es un palindromo")
            sleep(3)
            menu()
        }
    }
}

func anagrama(){
    print("Ingresa la primera palabra")
    if let primeraPalabra = readLine(){
        print("Ingresa la segunda palabra")
        if let segundaPalabra = readLine(){
            let primeraConvert = primeraPalabra.lowercased()
            let segundaConvert = segundaPalabra.lowercased()
            if String(primeraConvert.reversed( )) == segundaConvert {
                print( "Son anagramas" )
                sleep(3)
                menu()
            }else {
                print( "No son anagramas" )
                sleep(3)
                menu()
            }
        }
    }
    
}

func isograma(){
    print("Ingresa una palabra")
    if let primeraPalabra = readLine(){
        let caracteres = primeraPalabra.lowercased()
        let SetCaracteres = Set(caracteres)
        if SetCaracteres.count == caracteres.count {
            print("Es un isograma")
            sleep(3)
            menu()
        } else {
            print("No es un isograma")
            sleep(3)
            menu()
        }
        
    }
}

menu()

