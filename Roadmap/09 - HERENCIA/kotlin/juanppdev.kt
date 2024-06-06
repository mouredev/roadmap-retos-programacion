    /*Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.*/


// Definición de la superclase Animal
open class Animal(val nombre: String) {
    open fun hacerSonido() {}
}

// Definición de la subclase Perro
class Perro(nombre: String) : Animal(nombre) {
    override fun hacerSonido() {
        println("$nombre dice: ¡Guau!")
    }
}

// Definición de la subclase Gato
class Gato(nombre: String) : Animal(nombre) {
    override fun hacerSonido() {
        println("$nombre dice: ¡Miau!")
    }
}

// Función para imprimir el sonido de un Animal
fun imprimirSonido(animal: Animal) {
    animal.hacerSonido()
}

// Ejemplo de uso
fun main() {
    val miPerro = Perro("Buddy")
    val miGato = Gato("Whiskers")

    imprimirSonido(miPerro) // Salida: Buddy dice: ¡Guau!
    imprimirSonido(miGato)  // Salida: Whiskers dice: ¡Miau!
}


 /*Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.*/

// Clase base Empleado
open class Empleado(val identificador: Int, val nombre: String) {
    open fun trabajar() {}
}

// Clase Gerente, subclase de Empleado
class Gerente(identificador: Int, nombre: String, val departamento: String) : Empleado(identificador, nombre) {
    val empleadosACargo = mutableListOf<Empleado>()

    fun asignarEmpleado(empleado: Empleado) {
        empleadosACargo.add(empleado)
    }

    override fun trabajar() {
        println("$nombre está supervisando el departamento $departamento")
    }
}

// Clase GerenteProyecto, subclase de Gerente
class GerenteProyecto(identificador: Int, nombre: String, departamento: String, val proyecto: String) : Gerente(identificador, nombre, departamento) {
    override fun trabajar() {
        println("$nombre está supervisando el proyecto $proyecto")
    }
}

// Clase Programador, subclase de Empleado
class Programador(identificador: Int, nombre: String, val lenguaje: String) : Empleado(identificador, nombre) {
    override fun trabajar() {
        println("$nombre está programando en $lenguaje")
    }
}

// Ejemplo de uso
fun main() {
    val gerente = Gerente(1, "Juan", "Desarrollo")
    val gerenteProyecto = GerenteProyecto(2, "Maria", "Desarrollo", "Sistema de Gestión")
    val programador1 = Programador(3, "Pedro", "Python")
    val programador2 = Programador(4, "Ana", "JavaScript")

    gerente.asignarEmpleado(programador1)
    gerente.asignarEmpleado(programador2)

    gerente.trabajar()
    for (empleado in gerente.empleadosACargo) {
        empleado.trabajar()
    }

    gerenteProyecto.trabajar()
}
