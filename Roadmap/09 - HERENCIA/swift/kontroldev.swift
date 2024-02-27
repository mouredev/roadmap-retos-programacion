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
protocol Empleado {
    var id: Int { get }
    var nombre: String { get }
    
    func trabajar()
}

// Implementación del protocolo para el empleado base
extension Empleado {
    func trabajar() {
        print("\(nombre) está trabajando.")
    }
}

// Definición de la estructura para los gerentes
struct GerenteStruct: Empleado {
    var id: Int
    var nombre: String
    var empleadosACargo: [Empleado]
    
    init(id: Int, nombre: String, empleadosACargo: [Empleado] = []) {
        self.id = id
        self.nombre = nombre
        self.empleadosACargo = empleadosACargo
    }
    
    mutating func asignarEmpleado(_ empleado: Empleado) {
        empleadosACargo.append(empleado)
        print("\(nombre) ha asignado a \(empleado.nombre) a su equipo.")
    }
    
    func trabajar() {
        print("\(nombre) está gestionando el equipo.")
    }
}

// Definición de la clase GerenteProyecto
class GerenteProyecto: Empleado {
    var id: Int
    var nombre: String
    var proyectos: [String]
    
    init(id: Int, nombre: String, proyectos: [String]) {
        self.id = id
        self.nombre = nombre
        self.proyectos = proyectos
    }
    
    func trabajar() {
        print("\(nombre) está supervisando proyectos.")
    }
}

// Definición de la clase Programador
class Programador: Empleado {
    var id: Int
    var nombre: String
    var lenguajeDominante: String
    
    init(id: Int, nombre: String, lenguajeDominante: String) {
        self.id = id
        self.nombre = nombre
        self.lenguajeDominante = lenguajeDominante
    }
    
    func trabajar() {
        print("\(nombre) está programando en \(lenguajeDominante).")
    }
}

// Ejemplo de uso
var gerente = GerenteStruct(id: 1, nombre: "Roswell")  // 👈 este es mi jefe Roswell 😋 🫣 👀
let gerenteProyecto = GerenteProyecto(id: 2, nombre: "MoureDev", proyectos: ["Proyecto A", "Proyecto B"])
let programador = Programador(id: 3, nombre: "kontroldev", lenguajeDominante: "Swift")

gerente.asignarEmpleado(gerenteProyecto)
gerente.asignarEmpleado(programador)

// Llamada a los métodos trabajar específicos de cada empleado
gerente.trabajar()
gerenteProyecto.trabajar()
programador.trabajar()
