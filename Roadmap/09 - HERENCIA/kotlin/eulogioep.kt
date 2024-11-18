// Ejercicio principal: Animales

open class Animal(val nombre: String) {
    open fun emitirSonido() {
        println("$nombre hace un sonido genérico")
    }
}

class Perro(nombre: String) : Animal(nombre) {
    override fun emitirSonido() {
        println("$nombre hace: Guau guau!")
    }
}

class Gato(nombre: String) : Animal(nombre) {
    override fun emitirSonido() {
        println("$nombre hace: Miau miau!")
    }
}

// Dificultad extra: Jerarquía de empresa

open class Empleado(val id: Int, val nombre: String) {
    open fun trabajar() {
        println("$nombre está trabajando")
    }
}

class Programador(id: Int, nombre: String, val lenguaje: String) : Empleado(id, nombre) {
    override fun trabajar() {
        println("$nombre está programando en $lenguaje")
    }
}

open class Gerente(id: Int, nombre: String) : Empleado(id, nombre) {
    val subordinados = mutableListOf<Empleado>()

    fun agregarSubordinado(empleado: Empleado) {
        subordinados.add(empleado)
    }

    override fun trabajar() {
        println("$nombre está gestionando el equipo")
    }

    open fun listarSubordinados() {
        println("Subordinados de $nombre:")
        subordinados.forEach { println("- ${it.nombre}") }
    }
}

class GerenteProyecto(id: Int, nombre: String, val proyecto: String) : Gerente(id, nombre) {
    override fun trabajar() {
        println("$nombre está gestionando el proyecto $proyecto")
    }

    override fun listarSubordinados() {
        println("Subordinados de $nombre en el proyecto $proyecto:")
        subordinados.forEach { println("- ${it.nombre}") }
    }
}

fun main() {
    // Demostración de Animales
    val perro = Perro("Buddy")
    val gato = Gato("Whiskers")

    perro.emitirSonido()
    gato.emitirSonido()

    // Demostración de Jerarquía de Empresa
    val programador1 = Programador(1, "Ana", "Kotlin")
    val programador2 = Programador(2, "Carlos", "Java")
    val gerenteProyecto = GerenteProyecto(3, "Diana", "App Móvil")
    val gerente = Gerente(4, "Eduardo")

    gerenteProyecto.agregarSubordinado(programador1)
    gerenteProyecto.agregarSubordinado(programador2)
    gerente.agregarSubordinado(gerenteProyecto)

    programador1.trabajar()
    gerenteProyecto.trabajar()
    gerente.trabajar()

    gerenteProyecto.listarSubordinados()
    gerente.listarSubordinados()
}