fun main() {
    val miPerro = Perro("Yaki")
    val miGato = Gato("Yoga")

    hacerSonido(miPerro)
    hacerSonido(miGato)


    val programador = Programador(1, "Adri", "Kotlin")
    val gerente = Gerente(2, "Pepe", "Marketing")
    val gerenteProyecto = GerenteProyecto(2, "Juan", "herencia")

    programador.trabajar()
    gerente.trabajar()
    gerenteProyecto.trabajar()

    gerenteProyecto.agregarSubordinado(programador)
    gerenteProyecto.agregarSubordinado(gerente)
    gerenteProyecto.verSubordinados()
    gerenteProyecto.eliminarSubordinado(programador)
    gerenteProyecto.verSubordinados()
}

/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

open class Animal(val nombre: String) {
    open fun sonido() {}
}

class Perro(nombre: String) : Animal(nombre) {
    override fun sonido() {
        println("Guau Guau!")
    }
}

class Gato(nombre: String) : Animal(nombre) {
    override fun sonido() {
        println("Miau Miau!")
    }
}

fun hacerSonido(animal: Animal) {
    animal.sonido()
}

/* DIFICULTAD EXTRA (opcional):
* Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
* pueden ser Gerentes, Gerentes de Proyectos o Programadores.
* Cada empleado tiene un identificador y un nombre.
* Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
* actividad, y almacenan los empleados a su cargo.
*/

open class Empleado(val id: Int, val nombre: String) {
    open fun trabajar() {
        println("Empleado $nombre esta trabajando")
    }
}

class Gerente(id: Int, nombre: String, val departamento: String) : Empleado(id, nombre) {
    override fun trabajar() {
        println("$nombre es gerente y esta en el departamento $departamento")
    }
}

class GerenteProyecto(id: Int, nombre: String, val proyecto: String) : Empleado(id, nombre) {
    val subordinados = mutableListOf<Empleado>()

    fun agregarSubordinado(empleado: Empleado) {
        subordinados.add(empleado)
    }

    fun eliminarSubordinado(empleado: Empleado) {
        subordinados.remove(empleado)
    }

    fun verSubordinados() {
        for (subordinado in subordinados) {
            println(subordinado.nombre)
        }
    }

    override fun trabajar() {
        println("$nombre es gerente del proyecto $proyecto")
    }
}

class Programador(id: Int, nombre: String, val lenguaje: String) : Empleado(id, nombre) {
    override fun trabajar() {
        println("$nombre es programador y utiliza $lenguaje")
    }
}