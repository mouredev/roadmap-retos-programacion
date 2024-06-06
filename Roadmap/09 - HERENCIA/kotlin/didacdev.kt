import java.util.UUID

fun main() {
    var gerente = Gerente("Paco")
    var gerentesDeProyectos1 = GerentesDeProyectos("Pedro")
    var gerentesDeProyectos2 = GerentesDeProyectos("Ana")
    var programador1 = Programador("Sandra", mutableListOf("Swift", "Java"))
    var programador2 = Programador("Julian", mutableListOf("Kotlin"))
    var programador3 = Programador("Jose", mutableListOf("Python", "CSS"))
    var programador4 = Programador("Lisa", mutableListOf("HTML", "C"))

    gerentesDeProyectos1.addProgramador(programador1)
    gerentesDeProyectos1.addProgramador(programador2)
    gerentesDeProyectos1.addProgramador(programador3)
    gerentesDeProyectos2.addProgramador(programador4)

    gerente.addGerenteDeProyectos(gerentesDeProyectos1)
    gerente.addGerenteDeProyectos(gerentesDeProyectos2)

    println("${programador1.nombre} sabe programar ${programador1.lenguajes}")
    println("${programador2.nombre} sabe programar ${programador2.lenguajes}")
    println("${programador3.nombre} sabe programar ${programador3.lenguajes}")
    println("${programador4.nombre} sabe programar ${programador4.lenguajes}")

    println("${gerentesDeProyectos1.nombre} está a cargo de:")
    for (programador in gerentesDeProyectos1.programadores) {
        println("${programador.nombre}")
    }
    println("${gerentesDeProyectos2.nombre} está a cargo de:")
    for (programador in gerentesDeProyectos2.programadores) {
        println("${programador.nombre}")
    }
    println("${gerente.nombre} manda sobre:")
    for (gerenteDeProyecto in gerente.gerentesDeProyectos) {
        println("${gerenteDeProyecto.nombre}")
    }
}

open class Empleado(val identificador: String = UUID.randomUUID().toString(), val nombre: String = "") {
}

class Gerente(nombre: String) : Empleado(nombre = nombre) {
    val gerentesDeProyectos: MutableList<GerentesDeProyectos> = mutableListOf()

    fun addGerenteDeProyectos(gerente: GerentesDeProyectos) {
        gerentesDeProyectos.add(gerente)
    }
}

class GerentesDeProyectos(nombre: String): Empleado(nombre = nombre) {
    val programadores: MutableList<Programador> = mutableListOf()

    fun addProgramador(programador: Programador) {
        programadores.add(programador)
    }
}

class Programador(nombre: String, lenguajes: MutableList<String>): Empleado(nombre = nombre) {
    val lenguajes: MutableList<String> = lenguajes

    fun addLenguajes(lenguaje: String) {
        lenguajes.add(lenguaje)
    }
}
