/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

class Animal {
    func sonidoAnimalGeneral() {
        print("Sonido General")
    }
}

class Perro: Animal {
    func sonidoPerro() {
        print("Guau guau")
    }
}

class Gato: Animal {
    func sonidoGato() {
        print("Miau miau")
    }
}

var perrito = Perro()
perrito.sonidoAnimalGeneral()
perrito.sonidoPerro()

var gatito = Gato()
gatito.sonidoAnimalGeneral()
gatito.sonidoGato()


/* DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Empleado {
    var id: Int
    var nombre: String
    
    init(id: Int, nombre: String) {
        self.id = id
        self.nombre = nombre
    }
    
    func diversasActividades() {
        print("Soy un empleado y puedo realizar actividades diversas")
    }
    
}

class Gerente: Empleado {
    
    func mandar() {
        print("Soy un gerente y doy instrucciones a empleados")
    }
}

class GerenteProyecto: Empleado {
    
    func darInstrucciones() {
        print("Soy un gerente, especializado en proyectos")
    }
}

class Programador: Empleado {
    var lenguaje: String
    
        init(id: Int, nombre: String, lenguaje: String) {
        self.lenguaje = lenguaje
        super.init(id: id, nombre: nombre)
    }

    func programar() {
        print("Soy una programadora y haré magia escribiendo código en \(lenguaje).")
    }
}

var kary = Programador(id: 1, nombre: "Karys", lenguaje: "Swift")
kary.programar()

