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

protocol Animal {
    var name: String 
    func sound()
}

extension Animal {
    func sound() {
        print("Los animales de nombre \(name) tienen su propio sonido")
    }
}

class Perro: Animal {
    var name: String 

    init(name: String) {
        self.name = name 
    }

    func sound() {
        print("Los perros de nombre \(name) hacen jau jau")
    }
}

var sing = Perro(name: "Chams")
sing.sound()

class Gato: Animal {
    var name: String 

    init(name: String) {
        self.name = name 
    }

    func sound() {
        print("Los gatos de nombre \(name) hacen miau miau")
    }
}

var song = Gato(name: "Champions")
song.sound()

// Extra 
protocol Empresa {
    var name: String 
    var id: Int 

    func send()
}

extension Empresa {
    func send() {
        print("La empresa tiene programadores, gerentes y gerentes de proyectos")
    }
}

// Genrentes
class Gerentes: Empresa {
    var name: String 
    var id: Int 

    init(name: String, id: Int) {
        self.name = name 
        self.id = id 
    }

    func send() {
        print("Los gerentes de nombre \(name) trabajan en la empresa")
        print("Los gerentes de id \(id) trabajan en la empresa")
    }
}

var sang = Gerentes(name: "Carlos", id: 1234567)
sang.send()

// Gerentes de Proyectos
class GerentesP: Empresa {
    var name: String 
    var id: Int 

    init(name: String,, id: Int) {
        self.name = name 
        self.id = id 
    }

    func send() {
        print("Los gerentes de proyectos de noombre \(name) trabajan en la empresa")
        print("Los gerentes de proyectos de id \(id) trabajan en la empresa")
    }
}

var sing = GerentesP(name: "Carlos", id: 567890)
sing.send()

// Programadores
class Programadores: Empresa {
    var name: String 
    var id: Int 

    init(name: String, id: Int) {
        self.name = name 
        self.id = id 
    }

    func send() {
        print("Los programadores de nombre \(name) trabajan en la empresa")
        print("Los programadores de id \(id) trabajan en la empresa")
    }
}

var seng = Programadores(name: "Charles", id: 3245678)
seng.send()



