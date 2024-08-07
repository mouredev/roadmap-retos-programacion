import Foundation

/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

// Superclase Animal
class Animal {
    var nombre: String

    init(nombre: String) {
        self.nombre = nombre
    }

    func emitirSonido() -> String {
        return "Este animal hace un sonido"
    }
}

// Subclase Perro
class Perro: Animal {
    override func emitirSonido() -> String {
        return "Guau"
    }
}

// Subclase Gato
class Gato: Animal {
    override func emitirSonido() -> String {
        return "Miau"
    }
}

// Función para imprimir el sonido de un animal
func imprimirSonidoDe(animal: Animal) {
    print("\(animal.nombre) dice: \(animal.emitirSonido())")
}

// Uso de las clases
let miPerro = Perro(nombre: "Rex")
let miGato = Gato(nombre: "Whiskers")

imprimirSonidoDe(animal: miPerro)
imprimirSonidoDe(animal: miGato)


/* DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */


// Clase base Empleado
class Empleado {
    var id: Int
    var nombre: String

    init(id: Int, nombre: String) {
        self.id = id
        self.nombre = nombre
    }

    func describir() -> String {
        return "\(nombre) (ID: \(id))"
    }
}

// Subclase Gerente
class Gerente: Empleado {
    var empleadosACargo: [Empleado] = []

    func agregarEmpleado(empleado: Empleado) {
        empleadosACargo.append(empleado)
    }

    override func describir() -> String {
        return super.describir() + ". Gerente con \(empleadosACargo.count) empleados a cargo."
    }
}

// Subclase Gerente de Proyectos
class GerenteDeProyectos: Gerente {
    var proyectos: [String] = []

    func agregarProyecto(proyecto: String) {
        proyectos.append(proyecto)
    }

    override func describir() -> String {
        return super.describir() + " Encargado de los proyectos: \(proyectos.joined(separator: ", "))."
    }
}

// Subclase Programador
class Programador: Empleado {
    var lenguajes: [String]

    init(id: Int, nombre: String, lenguajes: [String]) {
        self.lenguajes = lenguajes
        super.init(id: id, nombre: nombre)
    }

    override func describir() -> String {
        return super.describir() + ". Programador especializado en: \(lenguajes.joined(separator: ", "))."
    }
}

// Instancias específicas según el requerimiento
let mouredev = Gerente(id: 1, nombre: "Mouredev")
let gerenteProyectos = GerenteDeProyectos(id: 2, nombre: "Mouredev")
let gliaDEV = Programador(id: 4, nombre: "gliaDEV", lenguajes: ["Swift","SwiftUI", "Objective-C", "Kotlin"])

// Configuración de la jerarquía
mouredev.agregarEmpleado(empleado: gerenteProyectos)
mouredev.agregarEmpleado(empleado: gliaDEV)
gerenteProyectos.agregarProyecto(proyecto: "Revolución Móvil 2024")

// Imprimiendo descripciones
print(mouredev.describir())


