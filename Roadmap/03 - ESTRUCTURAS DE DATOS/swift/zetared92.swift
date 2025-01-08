import Foundation

// RETO #03 ESTRUCTURAS DE DATOS

// ARRAYS
var arrayNum = [1, 2, 3, 4, 5, 6] // Mutable
let arrayNumLet = [6, 5, 4, 3, 2, 1] // Inmutable

// Agregar valores
arrayNum.append(4) // Agrega el valor dentro del array
arrayNum.insert(0, at: 2) // Añade el valor 0 en la posición 2.

// Eliminar valores
arrayNum.removeLast() // Elimina el último valor del array
arrayNum.remove(at:3) // Elimina el valor ubicado en la posición 3
arrayNum.removeFirst() // Elimina el primer valor del array
arrayNum.removeSubrange(3...5) // Elimina los valores del 3 al 5

// Eliminar todo el array
arrayNum.removeAll()

// Actualización de datos del array
arrayNum = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190] // Actualiza al nuevo array
arrayNum[4] = 125 // Actualiza el valor de la 4ta posición (130->125)

// Actualización de un valor concreto
arrayNum.replace([100, 110], with: [25, 50])

// Actualización de un subrange
arrayNum.replaceSubrange(3...6, with:[75, 100, 125, 150])


// Ordenaciones
var sortedArray = arrayNum.sorted() // Ordena de menor a mayor los valores
sortedArray.reverse() // De mayor a menor inviertiendo el array anterior
sortedArray = arrayNum.sorted {$0 < $1} // De menor a mayor asignándole una var
sortedArray = arrayNum.sorted {$0 > $1} // De mayor a menor asignándole una var
arrayNum.sort {$0 < $1} // Ordenación de elementos de menor a mayor
arrayNum.sort {$0 > $1} // Ordenación de elementos de mayor a menor


// DICCIONARIOS
let myClassicDictionary = Dictionary<Int, String>() // Forma clásica
var myDictionary = [Int:String]() // Forma moderna

// Añadir datos
myDictionary = [001:"Turing", 002: "Schrödinger"]

// Añadir un solo dato
myDictionary[003] = "Planck"
myDictionary[004] = "Bohr"
myDictionary[005] = "Oppenheimer"
myDictionary[006] = "Einstein"

// Acceso a un dato
myDictionary[002]

// La clave del diccionario es única
myDictionary[002] = "Schrödinger"
myDictionary.updateValue("Erwin Schrödinger", forKey: 002) // Opción clásica
myDictionary[002]

// Borrado de datos
myDictionary[002] = nil // La palabra nil significa nulo. Esta es la opción moderna.
myDictionary.removeValue(forKey:002) // Opción clásica.
myDictionary.removeAll()

// Ordenación
var myDicGreaterKey = myDictionary.sorted {$0.key < $1.key} // Menor a mayor
var myDicLessKey = myDictionary.sorted {$0.key > $1.key} // Mayor a menor
var myDicGreaterVal = myDictionary.sorted {$0.value < $1.value} // Menor a mayor
var myDicLessVak = myDictionary.sorted {$0.value > $1.value} // Mayor a menor


// SETS
var mySet: Set<Int> = [10, 20, 30, 40, 50, 60, 70, 80. 90]

mySet.insert(100) // Inserta el valor 100 dentro del set
mySet.update(with:00) // Inserta el 00 dentro del set independientemente de su posición

// Borrado
mySet.remove(50)
mySet.removeFirst()
mySet.removeLast()
mySet.removeAll()

// Ordenación
let sortedSet = mySet.sorted()


// TUPLAS
/* No es una colección pero actúa como tal. Agrupan múltiples valores en un solo valor
compuesto. Los valores pueden ser de cualquier tipo y no tienen que ser del mismo tipo
entre sí.*/
            // Name, Surname, Age, Height
var person = ("Zeta", "Red", 31, 1.70) // Tipos: String, String, Int, Double.
person.2 // De esta manera accedemos a un valor determinado en la tupla.
var (name, surname, age, height) = person // De esta manera estamos asignando los valores de nuestra tupla
Age
var personNameTuples = (name: "Zeta", surname: "Red", age: 31, height: 1.70)
personNameTuples.Age // Esta es una manera de acceder a valores concretos usando el nombre.

// 🧩 DIFICULTAD EXTRA 🧩
var contacts: [String: String] = [
    "Princess Diana" : "678905467",
    "Barry Allen" : "654321231",
    "Dick Grayson" : "690877809",
    "Jim Gordon" : "686754857",
    "Alfred Pennyworth" : "606321074",
    "Selina Kyle" : "620897645",
]

var next = true
print("Welcome to the contact book Mr. Wayne")

// Bucle
while next {
    print("Select an option:")
    print("1.-Search")
    print("2.-Insert new contact")
    print("3.-Update a contact")
    print("4.-Delete contact")
    print("5.-Exit")

    let option = readLine () ?? ""

    switch option {
    case "1":
        print("Input the contact name:")
        let name = readLine() ?? ""
        if let num = contacts[name] {
            print("The \(name)'s phone number is: \(num)")
        } else {
            print("This contact does not exist")
        }
    case "2":
        print("Input the name of the new contact")
        let name = readLine() ?? ""
        print("Input the number of the new contact")
        let num = readLine() ?? ""
        // The new contact must meet the entry requirements
        if let _ = Int(num), num.count < 9 {
            contacts[name] = num
            print("New contact accepted")
        } else {
            print("Invalid phone number")
        }
    case "3":
        print("Input the contact name you want to update")
        let name = readLine() ?? ""
        if contacts[name] != nil {
            print("Input the new phone number")
            let num = readLine() ?? ""
            if let _ = Int(num), num.count < 9 {
                contacts[name] = num
                print("The \(name)'s phone number is update now")
            } else {
                print("Invalid phone number")
            }
        } else {
            print("This contaxt does not exist")
        }
    case "4":
        print("Input the contact you want to delete:")
        let name = readLine() ?? ""
        if contacts[name] != nil {
            contacts[name] = nil
            print("The \(name)'s contact has been deleted")
        } else {
            print("This contact does not exist")
        }
    case "5":
        print("Every damn night and yet.. I'm still here")
        next = false
    default:
        print("Invalid option")
    }
}
