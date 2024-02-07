import Foundation

// Arrays

var numeros = [1, 2, 3, 4, 5]

// Mostrar el array

print("Array original: \(numeros)")

// Añadir un elemento al final del array

numeros.append(10)

// Mostrar el array

print("Array con un elemento añadido: \(numeros)")

// Borrar el primer elemento del array

numeros.removeFirst()

// Mostrar el array

print("Array con el primer elemento borrado: \(numeros)")

// Actualizar el valor del tercer elemento del array

numeros[2] = 13

// Mostrar el array

print("Array con el tercer elemento actualizado: \(numeros)")

// Ordenar el array de forma ascendente

numeros.sort()

// Mostrar el array

print("Array ordenado de forma ascendente: \(numeros)")

// Sets

var frutas = Set(["Platano", "Manzana", "Pera"])

// Mostrar el set

print("Set original: \(frutas)")

// Añadir un elemento al set

frutas.insert("Sandia")

// Mostrar el set

print("Set con un elemento añadido: \(frutas)")

// Borrar un elemento del set

frutas.remove("Platano")

// Mostrar el set

print("Set con un elemento borrado: \(frutas)")

// Comprobar si el set contiene un elemento

print("El set contiene Manzana: \(frutas.contains("Manzana"))")

// Diccionarios

var ruedas = ["Coche": 4, "Triciclo": 3, "Bicicleta": 2]

// Mostrar el diccionario

print("Diccionario original: \(ruedas)")

// Añadir un par clave-valor al diccionario

ruedas["Monociclo"] = 1

// Mostrar el diccionario

print("Diccionario con un par clave-valor añadido: \(ruedas)")

// Borrar un par clave-valor del diccionario

ruedas["Monociclo"] = nil

// Mostrar el diccionario

print("Diccionario con un par clave-valor borrado: \(ruedas)")

// Actualizar el valor de una clave del diccionario

ruedas["Triciclo"] = 4

// Mostrar el diccionario

print("Diccionario con el valor de una clave actualizado: \(ruedas)")

// Ordenar el diccionario por clave

print("Diccionario ordenado por clave: \(ruedas.sorted(by: {$0.key < $1.key}))")

// Tuplas

var coordenada = (x: 0, y: 0)

// Mostrar la tupla

print("Tupla original: \(coordenada)")

// Acceder al primer elemento de la tupla

print("Primer elemento de la tupla: \(coordenada.x)")

// Actualizar el valor del segundo elemento de la tupla

coordenada.y = -20

// Mostrar la tupla

print("Tupla con el segundo elemento actualizado: \(coordenada)")

// Enums

enum Coordenada: String {
    case N = "Norte"
    case S = "Sur"
    case E = "Este"
    case W = "Oeste"
}

// Mostrar el enum

print("Enum original: \(Coordenada.N.rawValue)")

// Crear una variable de tipo enum

var miCoordenada = Coordenada.W

// Acceder al valor asociado al caso del enum

print("Valor asociado al caso del enum: \(miCoordenada.rawValue)")

// Structs

struct Coche {
    var motor: Int
    var ruedas: Int
    
    // Método para calcular el área
    func precio() -> Int {
        return motor * ruedas * 1000 / 3
    }
}

// Crear una instancia de struct

var miCoche = Coche(motor: 1500, ruedas: 4)

// Mostrar una propiedad del struct

print("Propiedad del struct: \(miCoche.motor)")

// Llamar a un método del struct

print("Método del struct: \(miCoche.precio())")

// Extra

var agenda: [String: String] = [:]

// Crear una variable para controlar el bucle
var continuar = true

// Mostrar un mensaje de bienvenida
print("Mi Agenda")

func menu() {
    print("1. Buscar un contacto")
    print("2. Insertar un contacto")
    print("3. Actualizar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")
    print("Selecciones opción:")
}
    
func findPerson() {

    print("Nombre del contacto:")
    let nombre = readLine() ?? ""
    if let numero = agenda[nombre] {
        print("El número de teléfono de \(nombre) es \(numero)")
    } else {
        print("Contacto no disponible")
    }
}

func addPerson(){
    print("Nombre del contacto:")
    let nombre = readLine() ?? ""
    print("Telefono:")
    let numero = readLine() ?? ""

    if let _ = Int(numero), numero.count < 11 {
        agenda[nombre] = numero
        print("Contacto añadido")
    } else {
        print("Telefono no valido")
    }
}

func erasePerson(){
    print("Contacto a borrar:")
    let nombre = readLine() ?? ""
    if agenda[nombre] != nil {
        agenda[nombre] = nil
        print("Eliminado\(nombre)")
    } else {
        print("Contacto no existente")
    }
}

func updatePerson(){
    print("Contacto a actualziar:")
    let nombre = readLine() ?? ""
    if agenda[nombre] != nil {
        print("Nuevo telefonoo:")
        let numero = readLine() ?? ""
        // Validar que el número sea numérico y tenga menos de 11 dígitos
        if let _ = Int(numero), numero.count < 11 {
            agenda[nombre] = numero
            print("Actualziado correctamente")
        } else {
            print("Telefono no valido")
        }
    } else {
        print("Contacto no existente")
    }
}


// Iniciar el bucle
while continuar {
    menu()
    let opcion = readLine() ?? ""
    
    switch opcion {
        case "1":
            // Buscar persona
           findPerson()
        case "2":
            // Insertar un contacto
            addPerson()
        case "3":
            // Actualizar un contacto
            updatePerson()
        case "4":
            // Eliminar un contacto
            erasePerson()
        case "5":
            // Salir
            print("Cerrando agenda")
            continuar = false
        default:
            // Opción inválida
            print("Error")
    }
}


