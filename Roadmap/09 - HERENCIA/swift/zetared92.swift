import Foundation
// RETO #09 HERENCIA


protocol Animal {
    var name: String { get }
    func makeNoise()
}


extension Animal {
    func makeNoise() {
        print("The \(name) make some noise.")
    }
}


class Dog: Animal {
    var name: String
    
    init(name: String) {
        self.name = name
    }
    
    func makeNoise() {
        print("The dog \(name) barks.")
    }
}


class Cat: Animal {
    var name: String
    
    init(name: String) {
        self.name = name
    }
    
    func makeNoise() {
        print("The cat \(name) meows.")
    }
}


let dogName = Dog(name: "LUKE")
let catName = Cat(name: "VADER")

dogName.makeNoise()
catName.makeNoise()

// 🧩 DIFICULTAD EXTRA 🧩 - JERARQUÍA DE EMPRESA
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
        print("\(self.name) is coordinating the projects")
    }
}

class ProjectManager: Employee {
    var project: String

    init (id: Int, name: String, project: String) {
        self.project = project
        super.init(id: id, name: name)
    }

    func superviseProjects() {
        print("\(self.name) is supervising the projects")
    }
}

class Developer: Employee {
    var program: String

    init(id: Int, name: String, program: String) {
        self program = program
        super.init(id: id, name: name)
    }

    func development() {
        print("\(self.name) is developing \(self.program)")
    }

    override func add(employee: Employee) {
        print("He's the last monkey")
    }
}

let theManager = Manager(id: 1, name: "T-Bug")
let theProjectManager = ProjectManager(id: 2, name: "Vik Vector", project: ["Cibernetic Update v1.0", "Biometrical Update v.4.0"])
let theDeveloper = Developer(id: 3, name: "Zeta", program: "health programm update")
let theSecondPDeveloper

theManager.add(employee: theProjectManager)

theProjectManager.add(employee: theDeveloper)

theDeveloper.add(employee: theSecondPDeveloper)

theManager.coordinateProjects()
theManager.printEmployees()
theProjectManager.superviseProjects()
theProjectManager.printEmployees()
theDeveloper.development()
theDeveloper.printEmployees()