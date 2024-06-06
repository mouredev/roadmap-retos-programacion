/*
 EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
*/

class Person {
    var name: String
    var country: String
    var hobby: String
    var isHappy: Bool
    
    init(name: String, country: String, hobby:String, isHappy: Bool) {
        self.name = name
        self.country = country
        self.hobby = hobby
        self.isHappy = isHappy
    }
    
    func printPersonalData() {
        
        if isHappy {
            print("My name is \(name), I live in \(country) and I enjoy \(hobby).")
        } else {
            print("This is a person that isn't currently happy.")
        }
    }
}

var me = Person(name: "Karys", country: "Mexico", hobby: "Learn", isHappy: true)
var sadPerson = Person(name: "James", country: "Argentina", hobby: "Soccer", isHappy: false)
me.printPersonalData()
sadPerson.printPersonalData()