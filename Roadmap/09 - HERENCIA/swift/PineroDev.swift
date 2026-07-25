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

import Foundation

class Animal {
    var nombre: String
    
    init(nombre: String) {
        self.nombre = nombre
    }
    
    func sonido() -> String {
        return "ummmmm"
    }
}

class Perro: Animal {
    override func sonido() -> String {
        return "guauuuuu"
    }
}

class Gato: Animal {
    override func sonido() -> String {
        return "miauuuuuu"
    }
}

//func print_sound(animal: Animal) {
//    animal.sonido()
//}

let jacinto = Gato(nombre: "Jacinto")
print("\(jacinto.nombre) es un animal que hace el sonido \(jacinto.sonido())")
//print_sound(animal: jacinto)
let toby = Perro(nombre: "Toby")
print("\(toby.nombre) es un animal que hace el sonido \(toby.sonido())")
//print_sound(animal: toby)


//---------------
// Extra
//---------------

class Employee {
    var id: Int
    var nombre: String
    var employees: [Employee]
    
    init(id: Int, nombre: String) {
        self.id = id
        self.nombre = nombre
        self.employees = []
    }
    
    func add(employee:Employee){
        self.employees.append(employee)
    }
    
    func printEmployees(){
        print("Empleados de \(self.nombre):")
        for employee in self.employees {
            print(employee.nombre)
        }
    }
}

class Manager: Employee {
    
    func coordinateProjects(){
        print("El manager \(self.nombre) coordina todos los proyectos." )
    }
}
    
class ProjectManager: Employee {
        
    var project: String
        
    init(id: Int, nombre: String, project: String) {
            self.project = project
            super.init(id: id, nombre: nombre)
    }
    
    func coordinateProject(){
        print("El project manager \(self.nombre) coordina el proyecto \(self.project).")
    }
}

    
class Programmer: Employee {
    var language: String
        
    init(id: Int, nombre: String, language: String) {
            self.language = language
            super.init(id: id, nombre: nombre)
    }
        
        
    func code(){
            print("El programador \(self.nombre) esta programando en \(language).")
    }
    
    override func add(employee: Employee) {
        let name = employee.nombre
        print("El programador no puede tener nadie a cargo. \(name) no se añadio.")
    }
}

var my_manager = Manager(id: 1, nombre: "Pepe")
var my_project_manager = ProjectManager(id: 2, nombre: "Paco", project: "Proyecto 1")
var my_project_manager2 = ProjectManager(id: 3, nombre: "Juan", project: "Proyecto 2")
var my_programmer = Programmer(id: 4, nombre: "Luis", language: "Swift")
var my_programmer2 = Programmer(id: 5, nombre: "Marcos", language: "Java")
var my_programmer3 = Programmer(id: 6, nombre: "Andrés", language: "C++")
var my_programmer4 = Programmer(id: 7, nombre: "Ricardo", language: "Python")

my_manager.add(employee: my_project_manager)
my_manager.add(employee: my_project_manager2)

my_project_manager.add(employee: my_programmer)
my_project_manager2.add(employee: my_programmer2)
my_project_manager2.add(employee: my_programmer3)
my_project_manager.add(employee: my_programmer4)

my_programmer.add(employee: my_programmer2)

my_programmer.code()
my_project_manager.coordinateProject()
my_manager.coordinateProjects()

my_project_manager.printEmployees()
my_manager.printEmployees()
