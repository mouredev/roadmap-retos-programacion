// En Kotlin, necesitamos agregar la palabra 'open' a la clase padre (para que puede heredar)
// y a la función que queremos sobreescribir (cambiar) en la clase hija.
open class Animal(val nombre: String) {
    open fun sonido() {
        println("$nombre hace un sonido.")
    }
}
 
// La clase Perro hereda de la clase Animal
class Perro(nombre: String) : Animal(nombre) {
    // Sobreescribimos la función sonido
    override fun sonido() {
        println("$nombre hace guau.")
    }
}

class Gato(nombre: String) : Animal(nombre) {
    override fun sonido() {
        println("$nombre hace miau.")
    }
}

fun main() {
    val perro = Perro("Firulais")
    val gato = Gato("Garfield")

    perro.sonido()
    gato.sonido()

    //Extra
    val empleado1 = Empleado(1, "Juan")
    val empleado2 = Empleado(2, "Pedro")
    val empleado3 = Empleado(3, "Maria")

    val gerente = Gerente(4, "Luis", listOf(empleado1, empleado2, empleado3))
    val programador = Programador(5, "Carlos", "Kotlin")
    val gerenteProyecto = GerenteProyecto(6, "Ana", "Martes")

    gerente.trabajar()
    gerente.evaluar()
    programador.trabajar()
    programador.programar()
    gerenteProyecto.trabajar()
    gerenteProyecto.coordinar()

}

//Extra:
open class Empleado(val id: Int, val nombre: String) {
    fun trabajar() {
        println("El empleado $id de nombre $nombre está trabajando...")
    }
}

class Gerente(id: Int, nombre: String, val subordinados: List<Empleado>) : Empleado(id, nombre) {
    fun evaluar() {
        val empleadosSubordinados = subordinados.map { it.nombre }
        println("$nombre está evaluando a sus empleados: $empleadosSubordinados")
    }
}

class Programador(id: Int, nombre: String, val lenguajeFavorito: String) : Empleado(id, nombre) {
    fun programar() {
        println("$nombre está programando en $lenguajeFavorito.")
    }
}

class GerenteProyecto(id: Int, nombre: String, val diaFavorito: String) : Empleado(id, nombre) {
    fun coordinar() {
        println("Al gerente de proyecto $nombre le gusta hacer juntas los $diaFavorito")
    }
}