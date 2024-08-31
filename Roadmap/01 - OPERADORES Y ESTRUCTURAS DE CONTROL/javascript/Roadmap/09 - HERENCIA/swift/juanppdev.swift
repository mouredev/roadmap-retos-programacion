/*
    Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

// Definición de la clase Animal
class Animal {
    var nombre: String
    
    init(nombre: String) {
        self.nombre = nombre
    }
    
    func hacerSonido() {
        // Método por defecto que no hace nada en la clase base
    }
}

// Definición de la subclase Perro
class Perro: Animal {
    override func hacerSonido() {
        print("\(nombre) dice: ¡Guau!")
    }
}

// Definición de la subclase Gato
class Gato: Animal {
    override func hacerSonido() {
        print("\(nombre) dice: ¡Miau!")
    }
}

// Función para imprimir el sonido de un Animal
func imprimirSonido(animal: Animal) {
    animal.hacerSonido()
}

// Ejemplo de uso
let miPerro = Perro(nombre: "Buddy")
let miGato = Gato(nombre: "Whiskers")

imprimirSonido(animal: miPerro) // Salida: Buddy dice: ¡Guau!
imprimirSonido(animal: miGato)  // Salida: Whiskers dice: ¡Miau!



/*
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
*/

// Clase base Empleado
class Empleado {
    var identificador: Int
    var nombre: String
    
    init(identificador: Int, nombre: String) {
        self.identificador = identificador
        self.nombre = nombre
    }
    
    func trabajar() {
        // Método por defecto que no hace nada en la clase base
    }
}

// Clase Gerente, subclase de Empleado
class Gerente: Empleado {
    var departamento: String
    var empleadosACargo: [Empleado]
    
    init(identificador: Int, nombre: String, departamento: String) {
        self.departamento = departamento
        self.empleadosACargo = []
        super.init(identificador: identificador, nombre: nombre)
    }
    
    func asignarEmpleado(empleado: Empleado) {
        empleadosACargo.append(empleado)
    }
    
    override func trabajar() {
        print("\(nombre) está supervisando el departamento \(departamento)")
    }
}

// Clase GerenteProyecto, subclase de Gerente
class GerenteProyecto: Gerente {
    var proyecto: String
    
    init(identificador: Int, nombre: String, departamento: String, proyecto: String) {
        self.proyecto = proyecto
        super.init(identificador: identificador, nombre: nombre, departamento: departamento)
    }
    
    override func trabajar() {
        print("\(nombre) está supervisando el proyecto \(proyecto)")
    }
}

// Clase Programador, subclase de Empleado
class Programador: Empleado {
    var lenguaje: String
    
    init(identificador: Int, nombre: String, lenguaje: String) {
        self.lenguaje = lenguaje
        super.init(identificador: identificador, nombre: nombre)
    }
    
    override func trabajar() {
        print("\(nombre) está programando en \(lenguaje)")
    }
}

// Ejemplo de uso
let gerente = Gerente(identificador: 1, nombre: "Juan", departamento: "Desarrollo")
let gerenteProyecto = GerenteProyecto(identificador: 2, nombre: "Maria", departamento: "Desarrollo", proyecto: "Sistema de Gestión")
let programador1 = Programador(identificador: 3, nombre: "Pedro", lenguaje: "Python")
let programador2 = Programador(identificador: 4, nombre: "Ana", lenguaje: "JavaScript")

gerente.asignarEmpleado(empleado: programador1)
gerente.asignarEmpleado(empleado: programador2)

gerente.trabajar()
for empleado in gerente.empleadosACargo {
    empleado.trabajar()
}

gerenteProyecto.trabajar()
