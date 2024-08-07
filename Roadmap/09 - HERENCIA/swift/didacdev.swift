import Foundation

class Empleado {
    let identificador: UUID = UUID()
    var nombre: String

    init(nombre: String) {
        self.nombre = nombre
    }

    func getIdentificador() -> UUID {
        return identificador
    }

    func getNombre() -> String {
        return nombre
    }
}

class Gerente: Empleado {
    var gerentesDeProyectos: [GerentesDeProyectos]

    init(nombre: String, gerentesDeProyectos: [GerentesDeProyectos] = []) {
        self.gerentesDeProyectos = gerentesDeProyectos
        super.init(nombre: nombre)
    }

    func getGerentesDeProyectos() -> [GerentesDeProyectos] {
        return gerentesDeProyectos
    }

    func addGerenteDeProyecto(gerenteDeProyecto: GerentesDeProyectos) {
        gerentesDeProyectos.append(gerenteDeProyecto)
    }
}

class GerentesDeProyectos: Empleado {
    var programadores: [Programador] 

    init(nombre: String, programadores: [Programador] = []) {
        self.programadores = programadores
        super.init(nombre: nombre)
    }

    func getProgramadores() -> [Programador] {
        return programadores
    }

    func addProgramador(programador: Programador) {
        programadores.append(programador)
    }
}

class Programador: Empleado {
    var lenguajes: [String]

    init(nombre: String, lenguajes: [String]) {
        self.lenguajes = lenguajes
        super.init(nombre: nombre)
    }

    func getLenguajes() -> [String] {
        return lenguajes
    }

    func addLenguaje(lenguaje: String) {
        lenguajes.append(lenguaje)
    }
}


var gerente = Gerente(nombre: "Paco")
var gerenteDeProyectos1 = GerentesDeProyectos(nombre: "Pedro")
var gerenteDeProyectos2 = GerentesDeProyectos(nombre: "Ana")
var programador1: Programador = .init(nombre: "Sandra", lenguajes: ["Swift", "Java"])
var programador2: Programador = .init(nombre: "Julian", lenguajes: ["Kotlin"])
var programador3: Programador = .init(nombre: "Jose", lenguajes: ["Python", "CSS"])
var programador4: Programador = .init(nombre: "Lisa", lenguajes: ["HTML", "C"])

gerenteDeProyectos1.addProgramador(programador: programador1)
gerenteDeProyectos1.addProgramador(programador: programador2)
gerenteDeProyectos1.addProgramador(programador: programador3)
gerenteDeProyectos2.addProgramador(programador: programador4)

gerente.addGerenteDeProyecto(gerenteDeProyecto: gerenteDeProyectos1)
gerente.addGerenteDeProyecto(gerenteDeProyecto: gerenteDeProyectos2)

print("\(programador1.getNombre()) sabe programar \(programador1.getLenguajes())")
print("\(programador2.getNombre()) sabe programar \(programador2.getLenguajes())")
print("\(programador3.getNombre()) sabe programar \(programador3.getLenguajes())")
print("\(programador4.getNombre()) sabe programar \(programador4.getLenguajes())")   

print("\(gerenteDeProyectos1.getNombre()) está a cargo de:")
for programador in gerenteDeProyectos1.getProgramadores() {
    print(programador.getNombre())
}
print("\(gerenteDeProyectos2.getNombre()) está a cargo de:")
for programador in gerenteDeProyectos2.getProgramadores() {
    print(programador.getNombre())
}
print("\(gerente.getNombre()) manda sobre:")
for gerenteDeProyecto in gerente.getGerentesDeProyectos() {
    print(gerenteDeProyecto.getNombre())
}