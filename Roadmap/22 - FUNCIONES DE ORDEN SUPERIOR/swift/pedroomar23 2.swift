import Foundation 

/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */

// Ejemplos simples de funciones de orden superior

// 1. Map: Transforma cada elemento de una colección
let numbers = [1, 2, 3, 4, 5]
let squaredNumbers = numbers.map { $0 * $0 }
print("Números al cuadrado: \(squaredNumbers)")

// 2. Filter: Filtra elementos de una colección basado en una condición
let evenNumbers = numbers.filter { $0 % 2 == 0 }
print("Números pares: \(evenNumbers)")

// 3. Reduce: Combina todos los elementos de una colección en un único valor
let sum = numbers.reduce(0, +)
print("Suma de números: \(sum)")

// 4. Función que recibe otra función como parámetro
func applyOperation(_ a: Int, _ b: Int, operation: (Int, Int) -> Int) -> Int {
    return operation(a, b)
}

let result = applyOperation(5, 3, operation: *)
print("Resultado de la operación: \(result)")

// Dificultad Extra
struct Student {
    let name: String
    let birthDate: Date
    let grades: [Double]
}

let dateFormatter = DateFormatter()
dateFormatter.dateFormat = "yyyy-MM-dd"

let students = [
    Student(name: "Ana", birthDate: dateFormatter.date(from: "2000-05-15")!, grades: [8.5, 9.0, 7.5, 10.0]),
    Student(name: "Carlos", birthDate: dateFormatter.date(from: "1999-11-22")!, grades: [7.0, 8.5, 9.5, 8.0]),
    Student(name: "Elena", birthDate: dateFormatter.date(from: "2001-03-10")!, grades: [9.5, 9.0, 9.5, 10.0]),
    Student(name: "David", birthDate: dateFormatter.date(from: "2000-09-05")!, grades: [6.5, 7.0, 8.0, 7.5])
]

// 1. Promedio de calificaciones
let averageGrades = students.map { student in
    (name: student.name, average: student.grades.reduce(0, +) / Double(student.grades.count))
}
print("Promedio de calificaciones:")
averageGrades.forEach { print("\($0.name): \(String(format: "%.2f", $0.average))") }

// 2. Mejores estudiantes
let bestStudents = students.filter { student in
    student.grades.reduce(0, +) / Double(student.grades.count) >= 9.0
}.map { $0.name }
print("\nMejores estudiantes: \(bestStudents)")

// 3. Ordenar por nacimiento (más joven primero)
let sortedByAge = students.sorted { $0.birthDate > $1.birthDate }
print("\nEstudiantes ordenados por edad (más joven primero):")
sortedByAge.forEach { print("\($0.name): \(dateFormatter.string(from: $0.birthDate))") }

// 4. Mayor calificación
let highestGrade = students.flatMap { $0.grades }.max() ?? 0.0
print("\nCalificación más alta: \(highestGrade)")