/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

 let a = 10 
 let b = 5

 let suma = a + b
 let resta = a - b
 let multiplicacion = a * b
 let division = a / b
 let modulo = a % b
print("Suma: \(suma), Resta: \(resta), Multiplicación: \(multiplicacion), División: \(division), Módulo: \(modulo)")

let esIgual = a == b
let esDiferente = a != b
let esMayor = a > b
let esMenor = a < b 
let esMayorIgual = a >= b
let esMenorIgual = a <= b
print("Es igual: \(esIgual), Es diferente: \(esDiferente), Es mayor: \(esMayor), Es menor: \(esMenor), Es mayor o igual: \(esMayorIgual), Es menor o igual: \(esMenorIgual)")

let esCorrecto = (a > 0) && (b > 0)
let esIncorrecto = (a < 0) || (b < 0)
let esNegado = !(a > 0)
print("Es correcto: \(esCorrecto), Es incorrecto: \(esIncorrecto), Es negado: \(esNegado)")


var newA = a 
newA += 5
var newB = b
newB -= 3
var newC = a
newC *= 2
var newD = b
newD /= 2
var newE = a
newE %= 3
print("Asignación: newA = \(newA), newB = \(newB), newC = \(newC), newD = \(newD), newE = \(newE)")

// identidad
class Gato {
    let nombre: String
    init(nombre: String) {
        self.nombre = nombre
    }
}

let gato1 = Gato(nombre: "Michi")
let gato2 = gato1
let gato3 = Gato(nombre: "Pelusa")

print(gato1 === gato2)
print(gato1 === gato3)
print(gato1 !== gato3)

// Swift no tiene un operador de pertenencia como "in" de Python, se usa contains() con rangos o colecciones
let animales = ["perro", "gato", "conejo", "hamster"]
print("¿El perro está en la lista de animales? \(animales.contains("perro"))")

//Bits
let x = 12
let y = 10 

print("AND (&): \(x & y)")
print("OR  (|): \(x | y)")
print("XOR (^): \(x ^ y)")
print("NOT (~): \(~x)")
print("Left  (<<): \(x << 1)")
print("Right (>>): \(x >> 1)")




/*
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
*/

// Condicionales 
// If-else
let edad = 65
if edad > 65 {
    print("Puedes jubilarte")   
} else {
    print("Aún no puedes jubilarte")
}

// Switch
let dulzor = 7
switch dulzor {
case 8...10:
    print("Muy dulce")
case 5..<8:
    print("Dulce")
default:
    print("Poco dulce")
}

// Guard
func saludar(_ nombre: String?) {
    guard let nombreReal = nombre else {
        print("No hay un nombre válido")
        return
    }
    print("Hola, \(nombre)!")
}
saludar("Juan")
saludar(nil)    

// If-let
let texto = "24"
if let numero = Int(texto) {
    print("El número es \(numero)")
} else {
    print("No se pudo convertir a número")
}

// Iterativas
// For loop
for i in 1...3 {
    print("Iteración \(i)")
}

// While loop
var cantidad = 5
while cantidad > 0 {
    print("Cantidad: \(cantidad)")
    cantidad -= 1
}

// Repeat-while loop
var n = 0 
repeat {
    print("Número: \(n)")
    n += 1
} while n < 3   


// Excepciones
enum ErrorNota: Error {
    case negativa 
    case mayorQueDiez
}

func validarNota(_ nota: Int) throws -> String {
    if nota < 0 {
        throw ErrorNota.negativa
    }
    if nota > 10 {
        throw ErrorNota.mayorQueDiez
    }
    return "Nota válida: \(nota)"
}

for nota in [80, 5, -3] {
    do {
        let resultado = try validarNota(nota)
        print(resultado)
    } catch ErrorNota.negativa {
        print("Error: La nota no puede ser negativa")
    } catch ErrorNota.mayorQueDiez {
        print("Error: La nota no puede ser mayor que 10")
    } catch {
        print("Error desconocido: \(error)")
    }
}
 

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

 for numerito in 10...55 {
    if numerito % 2 == 0 && numerito != 16 && numerito % 3 != 0 {
        print("El número \(numerito) es par, no es 16 ni es múltiplo de 3")
    }
 }