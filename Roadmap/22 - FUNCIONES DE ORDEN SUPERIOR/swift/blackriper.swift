import Foundation

/*
 una funcion de orden superior (higher-order function) es una funcion que recibe como argumento una funcion
 o rettorna una funcion.

se usan principalmente para  trabajar con colecciones de datos. estas no permiten que 
alguna coleccion sea modificada por una funcion de orden superior.

 */

let fruits = ["apple", "banana", "orange"]

//usando funcion filter 
if let fruit=fruits.first(where:{$0 == "apple"}){
    print(fruit)
}

// fomrma iperativa
func findFruit(_ fruits: [String], _ fruit: (String) -> Bool) -> String? {
    for f in fruits {
        if fruit(f) {
            return f
        }
    }
    return nil
}

if let fruit=findFruit(fruits, {$0 == "orange"}){
    print(fruit)
}

// ejercicio extra 

struct Student {
    let name: String
    let birthday: Date
    let scores : [Int]
}

let formatter = DateFormatter()
formatter.dateFormat = "dd/MM/yyyy"

let students: [Student] = [
    Student(name: "Marco", birthday: formatter.date(from:"10/10/1990")!, scores: [0,9,7,5,10,6]),
    Student(name: "Messi", birthday: formatter.date(from:"20/05/1994")!, scores: [1,8,8,8,9,10]),
    Student(name: "Cristiano", birthday: formatter.date(from:"20/05/1998")!, scores: [9,10,9,8,9,10]),
    Student(name: "Neymar", birthday: formatter.date(from:"20/05/2000")!, scores: [1,8,8,7,9,5]),
]


func average(_ scores: [Int]) -> Int {
    return scores.reduce(0, +) / scores.count
}



let averageStudents =  students.map{ [$0.name: average($0.scores)]}
print(averageStudents)

let majorStudents = averageStudents.filter{$0.values.allSatisfy{$0 >= 9}}
print("major students: \(majorStudents)")

let orderStudents = students.sorted(by: { $0.birthday > $1.birthday })
print(orderStudents)

let majorScores = students.map{[$0.name: $0.scores.max()!]}
print(majorScores)


