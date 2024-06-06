import Foundation


// FUNCION DE SUMA
print("\nFUNCION DE SUMA")

func addTwoInts(addEnd1 n1: Int, addEnd2 n2: Int) -> Int {
    n1 + n2
}

func testAddTwoIntsFunction() {

    let result1 = addTwoInts(addEnd1: 2, addEnd2: 2) == 4
    
    assert(result1, "El resultado deveria ser: 4")
    
    print("Test de la funcion de suma pasado.")
}
testAddTwoIntsFunction()




// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA.")

var dictionary: [String : Any] = [
    "name" : "alberto",
    "age" : 39,
    "birthDate" : "04/07/1984",
    "programmingLenguages" : ["Swift", "Python", "Bash"]
]

func testDictionaryKeys() {

    let nameChecker = dictionary.keys.contains("name")
    let ageChecker = dictionary.keys.contains("age")
    let birthDateChecker = dictionary.keys.contains("birthDate")
    let programmingLenguagesChecker = dictionary.keys.contains("programmingLenguages")

    assert(nameChecker, "El campo name no existe.")
    assert(ageChecker, "El campo age no existe.")
    assert(birthDateChecker, "El campo birthDate no existe.")
    assert(programmingLenguagesChecker, "El campo programmingLenguages no existe.")

    print("Test de campos del diccionario pasado.")

}
testDictionaryKeys()

func testDictionaryValues() {

    let nameValueChercker = dictionary["name"] as? String == "alberto"
    let ageValueChecker = dictionary["age"] as? Int == 39
    let birthDateValueChecker = dictionary["birthDate"] as? String == "04/07/1984"
    let programmingLenguagesValueChecker = dictionary["programmingLenguages"] as? [String] == ["Swift", "Python", "Bash"]

    assert(nameValueChercker, "El valor de name no es alberto")
    assert(ageValueChecker, "El valor de age no es 39")
    assert(birthDateValueChecker, "El valor de birthDate no es 04/07/1984")
    assert(programmingLenguagesValueChecker, "Los valores de programmingLenguages no es [Swift, Python, Bash]")

    print("Test del los valores del diccionario pasado.")
}
testDictionaryValues()