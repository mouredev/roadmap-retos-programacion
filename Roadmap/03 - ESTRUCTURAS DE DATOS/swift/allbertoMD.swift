import Foundation

// Array
print("\nArray")
var myArray: [Int] = [20, -2, 39, 88, 1024, -210, 72]
print(myArray)


// Metodos de inserción
print("\nMetodos de Inserción")

// Inserta un 50 al final del array
myArray.append(50)
print(myArray)

// Concatena un el array [800, 129. 0] al final del array
myArray.append(contentsOf: [800, -129, 0])
print(myArray)

// Inserta 420 en la posición 0 del array
myArray.insert(420, at: 0)
print(myArray)

// Concatena el array [12, -874, 48] en la posición 3 del array
myArray.insert(contentsOf: [12, -874, 48], at: 3)
print(myArray)

// Concatena el array [222, 57] al final del array
myArray += [222, 57]
print(myArray)


// Metodos de borrado
print("\nMetodos de Borrado")

// Borra el elemento 1 del array
myArray.remove(at: 1)
print(myArray)

// Borra el ultimo elemento del array
myArray.removeLast()
print(myArray)

// Borra el primer elemento del array
myArray.removeFirst()
print(myArray)

// Borra los elementos del 2 al 4 del array
myArray.removeSubrange(2...4)
print(myArray)

// Borra todos los elementos que complan con la condicion. La condicion es los multiplos de 3
myArray.removeAll { $0 % 3 == 0}
print(myArray)

// Borra todos los elementos del array
myArray.removeAll()
print(myArray)


// Metodos de actualización
print("\nMetodos de Actualización")

// Actualiza el array con los nuevos valores
myArray = [420, 20, -2, 12, -874, 48, 39, 88, 1024, -210, 72, 50, 800, -129, 0, 222, 57]
print(myArray)

// Actualiza el la posición 1 del array con 770
myArray[1] = 770
print(myArray)

// Actualiza el -2 y el 12 por el 903, 11, 4 
myArray.replace([-2, 12], with: [903, 111, 4])
print(myArray)

// Actualiza del elemento 4 al 7 del arrau por 96, 414, 33, 1739
myArray.replaceSubrange(4...7, with: [96, 414, 33, 1739])
print(myArray)


// Metodos de ordenación
print("\nMetodos de Ordenación")

// Ordena los elementos de menor a mayor y lo asigna a una variable
var sortedArray = myArray.sorted()
print(sortedArray)

// Ordena los elementos de mayor a menor, da la vuelta al array anteriormente ordenado
sortedArray.reverse()
print(sortedArray)

// Ordena los elementos de menor a mayor y lo asigna a la variable
sortedArray = myArray.sorted { $0 < $1 }
print(sortedArray)

// Ordena los elementos de menor a mayor y lo asigna a la variable
sortedArray = myArray.sorted { $0 > $1 }
print(sortedArray)

// Ordena los elementos de menor a mayor
myArray.sort { $0 < $1 }
print(myArray)

// Ordena los elementos de mayor a menor
myArray.sort { $0 > $1 }
print(myArray)




// Diccionario
print("\nDiccionario")
var myDictionary: [Int:String] = [
    9 : "nueve",
    2 : "dos",
    34 : "treinta y cuatro",
    0 : "cero"
]
print(myDictionary)


// Metodos de inserción
print("\nMetodos de inserción")

// Inserta la clave 7 con el valor "siete" al diccionario
myDictionary[7] = "siete"
print(myDictionary)

// Inserta el valor "ciento uno" con la clave 101
myDictionary.updateValue("ciento uno", forKey: 101)
print(myDictionary)

// Inserta los valores del nuevo dicionario a myDictionary
var newDictionary = [38 : "treinta y ocho"]
myDictionary.merge(newDictionary) { (_, newValue) in newValue }
print(myDictionary)


// Metodos de borrado
print("\nMetodos de Borrado")

// Borra el elemento con la clave 34
myDictionary.removeValue(forKey: 34)
print(myDictionary)

// elimina el elemento con la clave 101
if let index = myDictionary.index(forKey: 101) {
    myDictionary.remove(at: index)
}
print(myDictionary)

// Borra todos los elementos de Diccionario
myDictionary.removeAll()
print(myDictionary)


// Metodos de actualización
print("\nMetodos de Actualización")

// Actualiza el diccionario con los nuevos valores
myDictionary = [
    34: "treinta y cuatro", 
    0: "cero",
    2: "dos",
    38: "treinta y ocho",
    7: "siete",
    101: "ciento uno",
    9: "nueve"
]
print(myDictionary)

// Actualiza el elemento con la clave 2 a "d o s"
myDictionary[2] = "d o s"
print(myDictionary)

// Actualiza el elemento con la clave 0 a "ce ro"
myDictionary.updateValue("ce ro", forKey: 0)
print(myDictionary)

// Actualiza el elementos con la clave 38 a "treintayocho"
newDictionary[38] = "treintayocho"
myDictionary.merge(newDictionary) { (_, newValue) in newValue }
print(myDictionary)


// Metoos de ordenación
print("\nMetodos de Ordenación")

// Ordenar los elementos por clave de menor a mayor
let dictionaryByGreaterKey = myDictionary.sorted { $0.key < $1.key }
print(dictionaryByGreaterKey)

// Ordenar los elementos por clave de mayor a menor 
let dictionaryByLessKey = myDictionary.sorted { $0.key > $1.key }
print(dictionaryByLessKey)

// Ordenar los elementos por valor de menor a mayor
let dictionaryByGreaterValue = myDictionary.sorted { $0.value < $1.value }
print(dictionaryByGreaterValue)

// Ordenar los elementos por valor de mayor a menor
let dictionaryBuLessValue = myDictionary.sorted { $0.value > $1.value }
print(dictionaryBuLessValue)




// Set
print("\nSet")
var mySet: Set<Int> = [11, 84, 8, -12, -2, 883, -100]
print(mySet)


// Metodos de inserción
print("\nMetodos de inserción")

// Inserta el 7 en cualquier posición del set
mySet.insert(7)
print(mySet)

// Inserta el 500 en cualquier posición del set
mySet.update(with: 500)
print(mySet)


// Metodos de borrado
print("\nMetodos de borrado")

// Borrar el elemento seleccionado del set
mySet.remove(500)
print(mySet)

// Borrar el primer elemento del set
mySet.removeFirst()
print(mySet)

// Borrar todos los elementos del set
mySet.removeAll()
print(mySet)


// Metodos de aztualización
print("\nMetodos de Actualización")

// Actualiza el set con los nuevos elementos
mySet = [11, 7, 84, 8, -100, -12, 883]
print(mySet)

// Actualiza los elementos del set con los elementos de los dos sets sin los elementos repetidos
let newSet: Set<Int> = [1, 2, 3, 11, -100]
mySet.formUnion(newSet)
print(mySet)

// Actualiza el set con los elementos repetidos en ambos sets
mySet.formIntersection(newSet)
print(mySet)

// Actualiza el set con todos los elementos menos los que esten repetidos en ambos sets
mySet = [11, 7, 84, 8, -100, -12, 883]
mySet.subtract(newSet)
print(mySet)


// Metodos de Ordenación
print("\nMetodos de Ordenación")

let sortedSet = mySet.sorted()
print(sortedSet)




// Tupla
print("\nTupla")
var myTuple = (12, 4, 74, 9)
print(myTuple)

// LAS TUPLAS SON INMUTABLES!!!




// Dificultad extro

var contacts: [String : String] = [
    "Sam" : "+1 696120338",
    "Jhonn" : "+1 555989001",
    "Jessica" : "+34 768341099",
    "Marta" : "+34 647290001"
]

showMenu()

var validInput: Bool = true

print("Introduce Una Opción")

while validInput {
    if let input = readLine() {
        switch input {
            case "1":
                addContact()
            case "2":
                removeContact()
            case "3":
                updateContact()
            case "4":
                searchContact()
            case "exit":
                validInput = false
                print("Salir")
            default:
                print("Opción no valida")
        }
    }
}

func showMenu() {
    print("[1]-Añadir Contacto")
    print("[2]-Borrar Contacto")
    print("[3]-Actualizar Contacto")
    print("[4]-Buscar Contacto")
    print("[exit]-Salir Del Menu")
}

func addContact() {
    var name = ""
    var phone = ""
    var validNumber: Bool = false

    print("Nuevo Contacto")
    print("Introduce un Nombre")

    if let input = readLine() {
        name = input
    }
    print("Nombre Introducido")
    print("Introduce un Numero de Telefono, Ejemplo: +12 292298799")

    while phone.count > 14 || phone.count < 12 || validNumber == false {
        if let input = readLine() {
            phone = input
            validNumber = evaluateString(phone)
        }
        if phone.count > 14 || phone.count < 12 || validNumber == false {
            print("Numero no valido")
            print("Introduce un Numero de Telefono, Ejemplo: +12 292298799")
        } else {
            print("Numero Introducido")
        }
    }
    contacts.updateValue(phone, forKey: name)

    sleep(2)

    showMenu()
}

func removeContact() {
    print("Borrar Contacto")
    print("Introduce un Numbre")

    while true {
        if let input = readLine() {
            if let index = contacts.index(forKey: input) {
                contacts.remove(at: index)
                
                print("Contacto Eliminado")
                
                break

            } else {
                print("Nombre no Encontrado")
                print("Introdule un Nombre")
            }
        }
    }
    sleep(2)

    showMenu()
}

func updateContact() {
    var name = ""
    var phone = ""
    var validNumber: Bool = false

    print("Actualizar Contacto")
    print("Introduce un Nombre")

    while true {
        if let input = readLine() {
            name = input
        }
        if let _: Dictionary<String, String>.Index = contacts.index(forKey: name) {
            print("Introduce unn numero de telefono, Ejemplo: +12 292298799 ")

            while phone.count > 14 || phone.count < 12 || validNumber == false {
                if let input: String = readLine() {
                    phone = input
                    validNumber = evaluateString(phone)
                }
                if phone.count > 14 || phone.count < 12 || validNumber == false {
                    print("Numero no Valido")
                    print("Introduce un Numero de Telefono, Ejemplo: +12 292298799")
                }
            }
            print("Contacto Actualizado")

            break

        } else {
            print("Nombre no Encontrado")
            print("Introduce el Nombre")
        }
    }
    contacts[name] = phone

    sleep(2)

    showMenu()
}

func searchContact() {
    print("Buscar Contacto")
    print("Introduce un Nombre")

    while true {
        if let input = readLine() {
            if let value = contacts[input] {
                print("El Contacto \(input) Tiene el Numero de Telefono: \(value)")
                
                break

            } else {
                print("Nombre no Encontrado")
                print("Introduce un Nombre")
            }
        }
    }
    sleep(2)

    showMenu()
}
print(contacts)

func evaluateString(_ string: String) -> Bool {
    let validCharacters: String = " +1234567890"
    
    for character in string {
        if !validCharacters.contains(character) {
            return false        }
    }
    return true
}


