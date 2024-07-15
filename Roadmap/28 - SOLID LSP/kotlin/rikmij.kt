fun main() {
    //Forma incorrecta
    open class Pokes(val nAme: String) {
        open fun aTtack(aTtack: String): String {
            return "$nAme usó $aTtack"
        }
        open fun evoluciona(): String {
            return "Tu $nAme está evolucionando"
        }
    }

    class Seel(nAme: String): Pokes(nAme) {
        override fun evoluciona(): String {
            return "Tu $nAme está evolucionando en Dewgong"
        }
    }

    class Sableye(nAme: String): Pokes(nAme) {
        override fun evoluciona(): String {
            throw Exception("Tauros no evoluciona")
        }
    }

    val seel = Seel("Seel")
    println(seel.evoluciona())
    val sableye = Sableye("Sableye")
    println(sableye.aTtack("Rayo Confuso"))
    //println(taur.evolucionar())

    /*
    Como vemos, no todos los pokémon evolucionan, por lo que la función evoluciona() no debería estar
    en la clase general, sino en otra específica de los que sí evolucionen
     */

//Forma correcta
    open class Pokemon(val name: String) {
        open fun attack(attack: String): String {
            return "$name usó $attack"
        }
    }

    class Charmander(name: String): Pokemon(name) {
        fun evolve(): String {
            return "Tu $name está evolucionando en Charmeleon"
        }
    }

    class Tauros(name: String): Pokemon(name)

    val charmander = Charmander("Charmander")
    println(charmander.attack("Ascuas"))
    println(charmander.evolve())
    val tauros = Tauros("Tauros")
    println(tauros.attack("Derribo"))
    val krabby = Pokemon("Krabby")
    println(krabby.attack("Martillazo"))

    /*
    Aquí es correcto. Un pokémon que no evoluciona no tiene el método de evolucionar, y la superclase sólo
    tiene los métodos generales, lo que pueden hacer todos los pokémon
     */

    println("\n${"*".repeat(7)} EJERCICIO EXTRA ${"*".repeat(7)}")
    val coche = Car()
    println(coche.brake())
    println(coche.openTrunk())
    val moto = Moto()
    println(moto.speedUp())
    println(moto.makeNoise())
    val tractor = Tractor()
    println(tractor.sow())
    /*
    Las funciones openTrunk, makeNoise y sow son propias de cada tipo de vehículo, pero la de arrancar
    y frenar son comunes. Para brake() y speedUp() se podría usar cualquiera de las subclases o la propia
    clase Vehicle, pero para sus métodos específicos no
     */
}

open class Vehicle {
    open fun speedUp(): String {
        return "El vehículo está acelerando"
    }
    open fun brake(): String {
        return "El vehículo está frenando"
    }
}

class Car: Vehicle() {
    override fun speedUp(): String {
        return "El coche está acelerando"
    }
    override fun brake(): String {
        return "El coche está frenando"
    }
    fun openTrunk(): String {
        return "El maletero se ha abierto"
    }
}

class Moto: Vehicle() {
    override fun speedUp(): String {
        return "La moto está acelerando"
    }
    override fun brake(): String {
        return "La moto está frenando"
    }
    fun makeNoise(): String {
        return "BRRRRRUM BRRRRRUM"
    }
}

class Tractor: Vehicle() {
    override fun speedUp(): String {
        return "El tractor está acelerando"
    }
    override fun brake(): String {
        return "El tractor está frenando"
    }
    fun sow(): String {
        return "El tractor ha plantado semillas"
    }
}
