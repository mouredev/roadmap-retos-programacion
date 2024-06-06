import Foundation

/*arrays*/

var arrayNum = [1, 2, 3, 4, 5, 6, 7] // Mutable


// Agregar valores
arrayNum.append(8) // Agrega el valor dentro del array
arrayNum.insert(0, at: 2) // Añade el valor 0 en la posición 2.
print("arrayNumAdd = \(arrayNum)")


// Eliminar valores
arrayNum.removeLast() // Elimina el último valor del array
arrayNum.remove(at:3) // Elimina el valor ubicado en la posición 3
arrayNum.removeFirst() // Elimina el primer valor del array
arrayNum.removeSubrange(4...5) // Elimina los valores del 3 al 5
print("arrayNumDelete = \(arrayNum)")


// actualizar valores
arrayNum = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
arrayNum[4] = 125 // Actualiza el valor de la 4ta ubicación (130->125)
print("arrayNumUpdate = \(arrayNum)")

// Actualización de un valor concreto
arrayNum.replace([100, 110], with: [25, 50])
print("arrayNumReplace = \(arrayNum)")

/* sets de datos*/
var mySet = Set<Int>(arrayNum)
print("mySet = \(mySet)")

// agregar elementos
mySet.insert(11)
print("mySetAdd = \(mySet)")

// borrar elementos
mySet.remove(11)
print("mySetDelete = \(mySet)")

// actualizar 
mySet = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
print("mySetUpdate = \(mySet)")

// ordenar
print("mySetSorted = \(mySet.sorted())")

/* diccionarios*/
var myDictionary = [Int:String]()
// agregar datos 
myDictionary = [001:"Turing", 002: "Schrödinger"]
myDictionary[003] = "Planck"
myDictionary[004] = "Bohr"
myDictionary[005] = "Oppenheimer"
myDictionary[006] = "Einstein"
print("myDictionary = \(myDictionary)")

// actualizar datos 
myDictionary.updateValue("Erwin Schrödinger", forKey: 002)
print("myDictionaryUpdate = \(myDictionary)")

// borrar datos
myDictionary.removeValue(forKey: 002)
print("myDictionaryDelete = \(myDictionary)")




// ejercicio extra 

// funcion para validar siel numero es  valido

func isValidNumber(_ number: String) -> Bool {
    var valid = false
    for char in number {
        if char.isNumber {
            valid=true
        }
    }
   return valid 
}


// funcion para agregar contacto
func addContact()->[String:String]{
   var contact:[String: String] = [:]
   var correct:Bool=false

  while correct==false{
        print("Input the contact name:")
        let name=readLine() ?? ""
        print("Input the phone number of the contact")
        let number=readLine() ?? ""
        
        if isValidNumber(number) && number.count == 10{
            contact.updateValue(number, forKey: name)
            print("New contact accepted")
            correct=true
        }else{
            print("Invalid phone number")
        }
    }
  return contact
}

func showAllContacts(_ contacts:[[String:String]]){
    print("Lists of contacts")
    for contact in contacts{
         for (key,value) in contact{
            print("Name: \(key) Number: \(value)")
     
        }       
    }

}



func bookOfContacts(){
    var option:String="0"
    var contacts :[[String:String]] = []
    
    while option != "4"{
        print("Select an option:")
        print("1.-Show all contacts")
        print("2.-Insert new contact")
        print("3.-Delete contact")
        print("4.-Exit")
        
        option = readLine() ?? ""
        
       switch option {
        case "1":
            showAllContacts(contacts)
           
        case "2":
           let contact=addContact()
           contacts.append(contact)

        case "3":
            print("Input the  name contact you want to delete:")
            let name=readLine() ?? ""
            contacts.removeAll(where: {$0.keys.contains(name)})
            print("The \(name)'s contact has been deleted")
        
        case "4":
            print("Exit contact list")
            

        default:
           print("Option invalid")
           
        }
    }
}

bookOfContacts()