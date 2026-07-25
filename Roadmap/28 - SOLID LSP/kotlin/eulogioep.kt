/*
 * Principio de Sustitución de Liskov (LSP):
 * 
 * El LSP establece que los objetos de una superclase deben poder ser reemplazados
 * por objetos de sus subclases sin afectar la corrección del programa. En otras palabras,
 * las subclases deben ser completamente sustituibles por sus clases base.
 *
 * Este principio asegura que una subclase puede asumir el lugar de su superclase
 * sin causar errores o comportamientos inesperados en el programa.
 */

// Clase base Vehiculo
abstract class Vehiculo {
    abstract fun acelerar(incrementoVelocidad: Int)
    abstract fun frenar(decrementoVelocidad: Int)
    abstract fun obtenerVelocidadActual(): Int
}

// Subclase Coche
class Coche : Vehiculo() {
    private var velocidad = 0

    override fun acelerar(incrementoVelocidad: Int) {
        velocidad += incrementoVelocidad
        println("Coche acelerando. Velocidad actual: $velocidad km/h")
    }

    override fun frenar(decrementoVelocidad: Int) {
        velocidad = maxOf(0, velocidad - decrementoVelocidad)
        println("Coche frenando. Velocidad actual: $velocidad km/h")
    }

    override fun obtenerVelocidadActual(): Int = velocidad
}

// Subclase Motocicleta
class Motocicleta : Vehiculo() {
    private var velocidad = 0

    override fun acelerar(incrementoVelocidad: Int) {
        velocidad += incrementoVelocidad
        println("Motocicleta acelerando. Velocidad actual: $velocidad km/h")
    }

    override fun frenar(decrementoVelocidad: Int) {
        velocidad = maxOf(0, velocidad - decrementoVelocidad)
        println("Motocicleta frenando. Velocidad actual: $velocidad km/h")
    }

    override fun obtenerVelocidadActual(): Int = velocidad
}

// Subclase Bicicleta
class Bicicleta : Vehiculo() {
    private var velocidad = 0

    override fun acelerar(incrementoVelocidad: Int) {
        velocidad += incrementoVelocidad
        println("Bicicleta acelerando. Velocidad actual: $velocidad km/h")
    }

    override fun frenar(decrementoVelocidad: Int) {
        velocidad = maxOf(0, velocidad - decrementoVelocidad)
        println("Bicicleta frenando. Velocidad actual: $velocidad km/h")
    }

    override fun obtenerVelocidadActual(): Int = velocidad
}

// Función para probar el LSP
fun probarLSP(vehiculo: Vehiculo) {
    vehiculo.acelerar(20)
    vehiculo.frenar(10)
    println("Velocidad final: ${vehiculo.obtenerVelocidadActual()} km/h")
    println()
}

fun main() {
    val coche = Coche()
    val motocicleta = Motocicleta()
    val bicicleta = Bicicleta()

    println("Probando Coche:")
    probarLSP(coche)

    println("Probando Motocicleta:")
    probarLSP(motocicleta)

    println("Probando Bicicleta:")
    probarLSP(bicicleta)
}