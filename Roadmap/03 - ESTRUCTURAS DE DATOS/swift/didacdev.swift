import Foundation

//---------------- Array --------------------
/*
- Valores del mismo tipo ordenados.
- Puede incluir valores respetidos.
*/
let immutableArray: Array<String> // Immutable
var mutableArray: Array<String> = []
var arrayDos = Array(repeating: 0, count: 3)
var arrayTres = [0, 1, 2, 3]
var arrayCuatro = arrayTres + arrayDos

// Añadir
mutableArray.append("Hola")
print(mutableArray)
arrayTres += [4, 5, 6]
print(arrayTres)

// Obtener
print(arrayTres[0])

// Cambiar
mutableArray[0] = "adios"
print(mutableArray)
arrayTres[2...4] = [0, 0]
print(arrayTres)

// Insertar 
arrayTres.insert(4, at: 4)
print(arrayTres)

// Eliminar
arrayTres.remove(at: 2)
print(arrayTres)
arrayTres.removeLast()
print(arrayTres)
arrayTres.removeFirst()
print(arrayTres)
arrayTres.removeAll()
print(arrayTres)


//------------------- Set ------------
/*
- Distintos valores de un mismo tipo sin ordenar
*/
var emptySet = Set<String>()
var setDos: Set<Int> = [2, 1, 5, 4, 3]

// Añadir
emptySet.insert("Pepe")
print(emptySet)

// Eliminar
if let nombre = emptySet.remove("Pepe") {
    print(nombre)
} else {
    print("No existe")
}

// Ordenar
let ordenado = setDos.sorted()
print(ordenado)

//---------------- Dictionary -------------
/*
- Asociaciones clave-valor del mismo tipo
- Claves únicas
- No ordenados
*/

var emptyDict: [Int: String] = [:]
var dictDos = [2: "Pepe", 1: "Juan"]

// Actualizar
dictDos[1] = "Pedro"
print(dictDos)
dictDos.updateValue("Pablo", forKey: 2)
print(dictDos)

// Añadir
dictDos[0] = "Ana"
print(dictDos)

// Eliminar
dictDos.removeValue(forKey: 0)
print(dictDos)

print()

func agenda() {
    print("------------")
    print("    Agenda  ")
    print("------------")
    var agenda: [String: Int] = [:]
    let quit = false

    while(!quit) {
        print()
        print("1 - Buscar")
        print("2 - Insertar")
        print("3 - Actualizar")
        print("4 - Eliminar")

        if let entrada = readLine() {

            switch entrada {
                case "1":
                    search(agenda: &agenda)
                case "2":
                    insert(agenda: &agenda)
                case "3":
                    update(agenda: &agenda)
                case "4":
                    delete(agenda: &agenda)
                default:
                    print("Opción incorrecta.")
            }

        } else {
            print("No has introducido nada.")
        }
    }
}

func search(agenda: inout [String: Int]) {
    print()
    print("Nombre del contacto: ")

    if let contactName = readLine() {
        if let contact = agenda[contactName] {
            print("\(contactName): \(contact)")
        } else {
            print("No existe el contacto")
        }
    }
}

func insert(agenda: inout [String: Int]) {
    var name: String = ""
    var number: Int = 0

    print()
    print("Nombre del contacto: ")

    if let contactName = readLine() {
        name = contactName
    }
    
    print("Número del contacto: ")

    if let contactNumber = readLine() {
        if let numberInt = Int(contactNumber) {
            number = numberInt
        } else {
            print("Entrada incorrecta")
        }
    }

    agenda[name] = number

    print("\(name): \(number)")
}

func update(agenda: inout [String: Int]) {
    print()
    print("Nombre del contacto: ")

    if let contactName = readLine() {
        if let contactExist = agenda[contactName] {
            print("Nuevo número:")

            if let newNumber = readLine() {
                if let numberInt = Int(newNumber) {
                    agenda[contactName] = numberInt
                }
            } 
        } else {
            print("No existe el contacto")
        }
    }
}

func delete(agenda: inout [String: Int]) {
    print()
    print("Nombre del contacto")

    if let contactName = readLine() {
        if let contactExist = agenda[contactName] {
            agenda.removeValue(forKey: contactName)
        } else {
            print("El contacto no existe")
        }
    }
}

agenda()
