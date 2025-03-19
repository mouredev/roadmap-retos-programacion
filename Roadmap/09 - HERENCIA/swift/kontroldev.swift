import Foundation

/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

// Definición de la clase Animal
// Definición de un protocolo Animal
protocol Animal {
    var nombre: String { get }
    func hacerSonido()
}

// Implementación por defecto del protocolo Animal
extension Animal {
    func hacerSonido() {
        print("El \(nombre) hace un sonido.")
    }
}

// Definición de la clase Perro que conforma al protocolo Animal
class Perra: Animal {
    var nombre: String
    
    init(nombre: String) {
        self.nombre = nombre
    }
    
    func hacerSonido() {
        print("La perra \(nombre) hace guau.")
    }
}

// Definición de la clase Gato que conforma al protocolo Animal
class Gato: Animal {
    var nombre: String
    
    init(nombre: String) {
        self.nombre = nombre
    }
    
    func hacerSonido() {
        print("El gato \(nombre) hace miau.")
    }
}

// Ejemplo de uso
let miPerro = Perra(nombre: "NALA")
let miGato = Gato(nombre: "ONYX")

miPerro.hacerSonido() // Salida: El perro NALA hace guau.
miGato.hacerSonido() // Salida: El gato ONYX hace miau.



// MARK: - DIFICULTAD EXTRA (opcional):
// Definición del protocolo Empleado
class Employee {
    var id: Int
    var name: String
    var employees: [Employee]
    
    init(id: Int, name: String) {
        self.id = id
        self.name = name
        self.employees = []
    }
    
    func add(employee: Employee) {
        self.employees.append(employee)
    }
    
    func printEmployees() {
        for employee in self.employees {
            print(employee.name)
        }
    }
}

class Manager: Employee {
    func coordinateProjects() {
        print("\(self.name) está coordinando todos los proyectos de la empresa.")
    }
}

class ProjectManager: Employee {
    var project: String
    
    init(id: Int, name: String, project: String) {
        self.project = project
        super.init(id: id, name: name)
    }
    
    func coordinateProject() {
        print("\(self.name) está coordinando su proyecto.")
    }
}

class Programmer: Employee {
    var language: String
    
    init(id: Int, name: String, language: String) {
        self.language = language
        super.init(id: id, name: name)
    }
    
    func code() {
        print("\(self.name) está programando en \(self.language).")
    }
    
    override func add(employee: Employee) {
        print("Un programador no tiene empleados a su cargo. \(employee.name) no se añadirá.")
    }
}

let myManager = Manager(id: 1, name: "MoureDev")
let myProjectManager = ProjectManager(id: 2, name: "Brais", project: "Proyecto 1")
let myProjectManager2 = ProjectManager(id: 3, name: "Moure", project: "Proyecto 2")
let myProgrammer = Programmer(id: 4, name: "Kontrol", language: "Swift")
let myProgrammer2 = Programmer(id: 5, name: "Roswell", language: "Cobol")
let myProgrammer3 = Programmer(id: 6, name: "Bushi", language: "klotin 😜")
let myProgrammer4 = Programmer(id: 7, name: "lordzzz", language: "Python")

myManager.add(employee: myProjectManager)
myManager.add(employee: myProjectManager2)

myProjectManager.add(employee: myProgrammer)
myProjectManager.add(employee: myProgrammer2)
myProjectManager2.add(employee: myProgrammer3)
myProjectManager2.add(employee: myProgrammer4)

myProgrammer.add(employee: myProgrammer2)

myProgrammer.code()
myProjectManager.coordinateProject()
myManager.coordinateProjects()
myManager.printEmployees()
myProjectManager.printEmployees()
myProgrammer.printEmployees()
