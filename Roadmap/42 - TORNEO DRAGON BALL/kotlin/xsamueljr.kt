import kotlin.math.roundToInt
import kotlin.random.Random

class Fighter(
    val name: String,
    val speed: Int,
    val attack: Int,
    val defense: Int
) {

    init {
        if (speed < 0 || speed > 100) {
            throw IllegalArgumentException("La velocidad debe estar entre 0 y 100")
        }

        if (attack < 0 || attack > 100) {
            throw IllegalArgumentException("El ataque debe estar entre 0 y 100")
        }

        if (defense < 0 || defense > 100) {
            throw IllegalArgumentException("La defensa debe estar entre 0 y 100")
        }
    }
    var health = 100

    fun attack(target: Fighter) {
        var damage = attack - target.defense
        val hasDodged = Math.random() < 0.2

        if (hasDodged) return

        if (damage <= 0) damage = (attack * 0.1).roundToInt()

        target.health -= damage
    }

    fun isDefeated() = health <= 0

    fun heal() {
        health = 100
    }

    companion object {
        fun new(name: String): Fighter = Fighter(
            name,
            randomAttribute(),
            randomAttribute(),
            randomAttribute()
        )

        private fun randomAttribute(): Int = Random.nextInt(0, 101)
    }
}

class Battle(val fighter1: Fighter, val fighter2: Fighter) {
    fun perform(): Fighter {
        println("Comienza la batalla entre ${fighter1.name} y ${fighter2.name}!")

        val fastest = if (fighter1.speed > fighter2.speed) {
            fighter1
        } else {
            fighter2
        }
        val slowest = if (fighter1 == fastest) {
            fighter2
        } else {
            fighter1
        }

        while (true) {
            fastest.attack(slowest)
            if (slowest.isDefeated()) return fastest

            slowest.attack(fastest)
            if (fastest.isDefeated()) return slowest
        }
    }
}

class Tournament(val fighters: List<Fighter>) {
    init {
        if (fighters.isEmpty()) throw IllegalArgumentException("No se puede hacer un torneo sin luchadores")

        val isPowerOf2 = fighters.count() > 0 && (fighters.count() and (fighters.count() - 1)) == 0

        if (!isPowerOf2) throw IllegalArgumentException("La cantidad de luchadores debe ser potencia de 2")
    }

    fun perform(): Fighter {
        var fightersLeft = fighters
        while (fightersLeft.count() != 1) {
            fightersLeft = performRound(fightersLeft)
        }
        return fightersLeft[0]
    }

    private fun performRound(fighters: List<Fighter>): List<Fighter> {
        val fighters = fighters.toMutableList()

        val battles = buildList {
            while (fighters.isNotEmpty()) {
                add(Battle(fighters.removeFirst(), fighters.removeFirst()))
            }
        }

        val winners = battles.map {
            val winner = it.perform()
            winner.heal()
            winner
        }

        return winners
    }
}

fun main() {
    val fighterNames = listOf(
        "Goku",
        "Vegeta",
        "Krillin",
        "Gohan",
        "Androide 17",
        "Androide 18",
        "Trunks",
        "Yamcha",
        "Freezer",
        "Cell",
        "Buu",
        "Piccolo",
        "Tenshinhan",
        "Goten",
        "Raditz",
        "Bardock"
    )
    val fighters = fighterNames.map { Fighter.new(it) }
    val tournament = Tournament(fighters)

    val winner = tournament.perform()
    println("¡Ha ganado ${winner.name}!")
}