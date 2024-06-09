import Foundation


let stringArray: [String] = ["Swift", "Kotlin", "Java", "Python", "Ruby", "JavaScript", "C#", "C++", "Go", "Rust", "256", "360"]
let intArray: [Int] = [10, 23, 35, 42, 57, 61, 74, 86, 95, 100]




print("\nFunciones de orden superior del lenguaje.")
// Funciones de orden superior del lenguaje.


print("\nFunción map.")
// Multiplica por 10 cada elemento del array lo.
let mapIntArray = intArray.map { item in
    item * 10
}
print(mapIntArray)


print("\nFunción compactMap.")
// Conviert todos los Strings del array a entero y si alguno es nil lo descarta.
let compactMapStringArray = stringArray.compactMap { item in
    Int(item)
}
print(compactMapStringArray)


print("\nFunción filter.")
// Filtra los elementos del array por la palabra Swift.
let filterStringArray = stringArray.filter { item in
    item == "Swift"
}
print(filterStringArray)


print("\nFunción reduce.")
// resta el resultado de cada elemento del array empezando en el con el 10 y devuelve el resultado. (10 - 10 = 0) - (0 - 23 = -23) etc
let reduceIntArray = intArray.reduce(10) { partialResult, item in
    item - partialResult
}
print(reduceIntArray)


print("\nFunción forEach.")
// Imprime cada elemento del array
stringArray.forEach { item in
    print(item)
}


print("\nFunción sorted.")
// Ordena los elementos del array de menor a mayor.
let sortedStringArray = stringArray.sorted { first, second in
    first < second
}
print(sortedStringArray)


print("\nFunción contains.")
// Devuelve verdadero o falso si la condicion se cumple.
let containsIntArray = intArray.contains { item in
    item == 10
}
print(containsIntArray)


print("\nFunción satisfy.")
// Devuelve verdadero a falso si todos los elementos del array cumplen con la condicion.
let satisfyStringArray = stringArray.allSatisfy { item in
    item.count == 4
}
print(satisfyStringArray)


print("\nFunción first.")
// Devuelve el elemento que compla con la condición.
let firstIntArray = intArray.first { item in
    item % 3 == 0
}
if let number = firstIntArray {
    print(number)
}


print("\nFunción drop.")
// Elimina el elemento primero del array si se cumple con la condición.
let dropStringArray = stringArray.drop { item in
    item.first == "S"
}
print(dropStringArray)


print("\nFunción prifix")
// Devuelve el primer elemento del array si cumple con la condición.
let prefixStringArray = stringArray.prefix { item in
    item.first == "S"
}
print(prefixStringArray)




print("\nFunciones de orden superior personalizadas.")
// Funciones de orden superior personalizadas.


print("\nFunción con función como parametro.")
// Función con función de parametro.
func applyFunctionToArray(array: [Int], function: (Int) -> Int) -> [Int] {
    var result: [Int] = []
    for value in array {
        result.append(function(value))
    }
    return result
}

// Definición de la variable que se pasara como parametro a la función applyFunctionToArray.
func square(number: Int) -> Int {
    return number * number
}

// Uso de la función de orden superior.
let squaredNumbers = applyFunctionToArray(array: intArray, function: square)
print(squaredNumbers)


print("\nFunción que devuelve una función.")
// Función que devuelve una función.
func makeMultiplier(factor: Int) -> (Int) -> Int {
    return { number in
        return number * factor
    }
}

// Uso de la función de orden superior.
let multiplyByThree = makeMultiplier(factor: 3)
print(multiplyByThree(5)) // 15




// DIFICULTAD EXTRA.
print("\n\nDIFICULTAD EXTRA.")


struct Student {
    let name: String
    let birthDate: Date
    let califications: [String : Float]
    
    static func createBirthDate(date: String) -> Date {
        let dateFormater = DateFormatter()
        dateFormater.dateFormat = "dd/MM/yyyy"
        let birthDate = dateFormater.date(from: date)
        guard let bd = birthDate else {
            fatalError()
        }
        return bd
    }
}

var studentsList = [Student(name: "Sara",
                            birthDate: Student.createBirthDate(date: "06/07/2001"),
                            califications: ["Algorithms" : 7.1,
                                            "Operating System" : 5.9,
                                            "Data Base" : 9.0,
                                            "AI" : 2.5]),
                    Student(name: "Helena",
                            birthDate: Student.createBirthDate(date: "27/10/2002"),
                            califications: ["Algorithms" : 3.9,
                                            "Operating System" : 9.0,
                                            "Data Base" : 7.3,
                                            "AI" : 8.1]),
                    Student(name: "Kendrick",
                            birthDate: Student.createBirthDate(date: "11/03/2001"),
                            califications: ["Algorithms" : 5.0,
                                            "Operating System" : 7.9,
                                            "Data Base" : 5.9,
                                            "AI" : 6.3]),
                    Student(name: "Tyler",
                            birthDate: Student.createBirthDate(date: "07/11/2002"),
                            califications: ["Algorithms" : 9.1,
                                            "Operating System" : 7.5,
                                            "Data Base" : 8.6,
                                            "AI" : 10.0])
]




print("\nPromedio de cada estudiante.")
// Función promedio de cada estudiante.
func namesAndAverages(to students: [Student], function: ([String]) -> [String]) -> [String] {
    var califications: [Float] = []
    var notes: [[Float]] = []
    for cal in students {
        for (_, value) in cal.califications {
            califications.append(value)
        }
        notes.append(califications)
    }
    var sumNotes: [Float] = []
    for n in notes {
        let sum: Float
        sum = n.reduce(0, { partialResult, float in
            partialResult + float
        })
        sumNotes.append(sum)
    }
    var averages: [Float] = []
    var division: Float = 0.0
    for n in sumNotes {
        division = round(n / Float(sumNotes.count))
        averages.append(Float(division))
    }
    var namesAndAverages: [String] = []
    for item in studentsList {
        namesAndAverages.append(item.name)
    }
    var sttepper = 0
    for item in averages {
        namesAndAverages[sttepper] += ": \(String(item))"
        sttepper += 1
    }
    let result = function(namesAndAverages)
    return result
}

func createNamesAndAverages(array: [String]) -> [String] {
    array
}

let namesAndAveragesArray = namesAndAverages(to: studentsList, function: createNamesAndAverages)
print(namesAndAveragesArray)



print("\nAlumnos con promedios mayor a 9.0")
// Función alumnos con promedios superior a 9.0
func averagePluss(to students: [Student], function: ([String]) -> [String]) -> [String] {
    var averagesPlus: [String] = []
    for student in students {
        for (_, value) in student.califications {
            if value >= 9.0 {
                averagesPlus.append(student.name)
                break
            }
        }
    }
    let result = function(averagesPlus)
    return result
}

func createAveragePlusArray(array: [String]) -> [String] {
    array
}

let averagePlussArray = averagePluss(to: studentsList, function: createAveragePlusArray)
print(averagePlussArray)




print("\nOrden de fechas de nacimiento.")
// Función de orden de fechas de nacimiento.
func datesOrder(to students: [Student], order: ([String]) -> [String]) -> [String] {
    let dates = students.sorted { first, second in
        first.birthDate > second.birthDate
    }
    let names = dates.map { name in
        name.name
    }
    let result = order(names)
    return result
}

func orderDates(names: [String]) -> [String] {
    names
}

let datesSorted = datesOrder(to: studentsList, order: orderDates)
print(datesSorted)



print("\nAlumno con el promedio mas alto.")
// Función con la nota mas alta.
func greaterAverage(to students: [Student], function: ([String]) -> [String]) -> [String] {
    var greaterAverage: [String] = []
    for student in students {
        for (_, value) in student.califications {
            if value == 10.0 {
                greaterAverage.append(student.name)
                break
            }
        }
    }
    let result = function(greaterAverage)
    return result
}

func createGreaterAverageArray(array: [String]) -> [String] {
    array
}

let greaterAverageArray = greaterAverage(to: studentsList, function: createGreaterAverageArray)
print(greaterAverageArray)

