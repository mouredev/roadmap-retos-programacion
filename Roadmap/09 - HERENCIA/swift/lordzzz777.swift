/*
 * 09, EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

class Animal {
    
    var patas: Int
    var boca: Int
    var reproduccion: String
    var clase: String
    var genero: String
    var comer: String
    var pelaje: String
    var nombre: String
    
    init(patas: Int, boca: Int, reproduccion: String, clase: String, genero: String, comer: String, pelaje: String, nombre: String) {
        self.patas = patas
        self.boca = boca
        self.reproduccion = reproduccion
        self.clase = clase
        self.genero = genero
        self.comer = comer
        self.pelaje = pelaje
        self.nombre = nombre
    }
    
    func nacer(_ formaNacer: String) -> String {
        return "Los animales de la clase \(clase) nacen \(formaNacer)"
    }
    
    func comer(_ alimento: String) -> String {
        return "Los animales de la clase \(clase) comen \(alimento)"
    }
    
    func duermen(_ formaDe: String) -> String {
        return "Los animales de la clase \(clase) duermen \(formaDe)"
    }
    
    func reproducen(_ especie: String) -> String {
        return "Los animales de la clase \(clase) se reproducen mediante \(reproduccion)"
    }
}

class Perro: Animal {
    
    var sonido: String
    
    init(sonido: String, comer: String, pelaje: String, nombre: String) {
        self.sonido = sonido
        super.init(patas: 4, boca: 1, reproduccion: "viviparo", clase: "canido", genero: "mamifero", comer: comer, pelaje: pelaje, nombre: nombre)
    }
    
    func emiteSonido() -> String {
        return "Mi perro se llama \(nombre), al detectar ruido \(sonido)"
    }
}

class Gato: Animal {
    
    var sonido: String
    
    init(sonido: String, comer: String, pelaje: String, nombre: String) {
        self.sonido = sonido
        super.init(patas: 4, boca: 1, reproduccion: "viviparo", clase: "felino", genero: "mamifero", comer: comer, pelaje: pelaje, nombre: nombre)
    }
    
    func emiteSonido() -> String {
        return "Mi gato se llama \(nombre), y cuando tiene hambre \(sonido)"
    }
}

// Instanciación de un perro
let miPerro = Perro(sonido: "ladrido", comer: "croquetas", pelaje: "corto", nombre: "Fido")

// Acceso a propiedades y métodos del perro
print("Mi perro tiene \(miPerro.patas) patas y \(miPerro.boca) boca.")
print(miPerro.nacer("de una madre perro"))
print(miPerro.comer("huesos"))
print(miPerro.duermen("en su cama"))
print(miPerro.emiteSonido())

// Instanciación de un gato
let miGato = Gato(sonido: "maullido", comer: "pescado", pelaje: "largo", nombre: "Misi")

// Acceso a propiedades y métodos del gato
print("Mi gato tiene \(miGato.patas) patas y \(miGato.boca) boca.")
print(miGato.nacer("de una madre gato"))
print(miGato.comer("atún"))
print(miGato.duermen("en una caja"))
print(miGato.emiteSonido())

/*
 * DIFICULTAD EXTRA (opcional):
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
    
    func trabaja() -> String {
        return "\(nombre) está trabajando"
    }
}

class Gerente: Empleado {
    var equipo: [Empleado]
    init(id:Int,nombre: String, equipo: [Empleado]) {
        self.equipo = equipo
        super.init(id: Int, nombre: String)
    }
    
    func asignarTrabajo() -> String{
        return "El gerente \(nombre), está asignando trabajo a su equipo"
    }
}

class JefeProyecto: Gerente {
    var proyectos: [String]
    
    override init(id: Int, nombre: String, equipo: [Empleado], proyectos: [String]) {
        self.proyectos = proyectos
        super.init(id: Int, nombre: String, equipo: [Empleado])
    }
    
    func revisarProyectos() -> String {
        return "\(nombre), está revisando los progreso de los proyectos"
    }
}

class Programador: Empleado {
    var lenguaje: String
    
    override init(id: Int, nombre: String, lenguaje: String) {
        self.lenguaje = lenguaje
        super.init(id: Int, nombre: String)
    }
    
    func picarCodigo() -> String {
        return "\(nombre) esta creando un proyecto en el lenguaje \(lenguaje)"
    }
}

// Crear empleados
let gerente = Gerente(id: 1, nombre: "Juan", equipo: [])
let gerenteProyecto = JefeProyecto(id: 2, nombre: "Maria", equipo: [], proyectos: ["Proyecto A", "Proyecto B"])
let programador = Programador(id: 3, nombre: "Pedro", lenguaje: "Swift")

// Acceder a propiedades y métodos específicos de cada tipo de empleado
print(gerente.asignarTrabajo())
print(gerenteProyecto.revisarProyectos())
print(programador.picarCodigo())
