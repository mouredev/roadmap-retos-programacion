import kotlin.random.Random
import kotlinx.coroutines.*

// Clase para representar a un personaje
data class Character(
    val name: String,
    var health: Int,
    val minDamage: Int,
    val maxDamage: Int,
    val evasionChance: Double,
    var canAttack: Boolean = true
)

// Función principal
suspend fun main() = coroutineScope {
    // Solicitar la vida inicial de los personajes
    println("Ingrese la vida inicial de Deadpool:")
    val deadpoolHealth = readLine()?.toIntOrNull() ?: 1000
    println("Ingrese la vida inicial de Wolverine:")
    val wolverineHealth = readLine()?.toIntOrNull() ?: 1000

    // Crear los personajes
    val deadpool = Character("Deadpool", deadpoolHealth, 10, 100, 0.25)
    val wolverine = Character("Wolverine", wolverineHealth, 10, 120, 0.20)

    var turn = 1

    // Bucle principal de la batalla
    while (deadpool.health > 0 && wolverine.health > 0) {
        println("\nTurno $turn")
        
        // Simular el ataque de Deadpool
        if (deadpool.canAttack) {
            attack(deadpool, wolverine)
        } else {
            println("${deadpool.name} se está regenerando y no puede atacar este turno.")
            deadpool.canAttack = true
        }

        // Verificar si Wolverine ha sido derrotado
        if (wolverine.health <= 0) break

        // Simular el ataque de Wolverine
        if (wolverine.canAttack) {
            attack(wolverine, deadpool)
        } else {
            println("${wolverine.name} se está regenerando y no puede atacar este turno.")
            wolverine.canAttack = true
        }

        // Mostrar la vida restante de ambos personajes
        println("Vida de ${deadpool.name}: ${deadpool.health}")
        println("Vida de ${wolverine.name}: ${wolverine.health}")

        turn++
        delay(1000) // Pausa de 1 segundo entre turnos
    }

    // Mostrar el resultado final
    val winner = if (deadpool.health > 0) deadpool.name else wolverine.name
    println("\n¡$winner ha ganado la batalla!")
}

// Función para simular un ataque
fun attack(attacker: Character, defender: Character) {
    // Determinar si el defensor evade el ataque
    if (Random.nextDouble() < defender.evasionChance) {
        println("${defender.name} ha evadido el ataque de ${attacker.name}!")
        return
    }

    // Calcular el daño
    val damage = Random.nextInt(attacker.minDamage, attacker.maxDamage + 1)
    
    // Aplicar el daño
    defender.health -= damage
    println("${attacker.name} ha causado $damage de daño a ${defender.name}!")

    // Verificar si el daño es máximo
    if (damage == attacker.maxDamage) {
        println("¡Golpe crítico! ${defender.name} no podrá atacar en el próximo turno.")
        defender.canAttack = false
    }
}