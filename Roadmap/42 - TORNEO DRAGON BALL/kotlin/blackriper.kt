import kotlinx.coroutines.CoroutineDispatcher
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.asCoroutineDispatcher
import kotlinx.coroutines.async
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import org.jetbrains.annotations.BlockingExecutor
import java.util.concurrent.Executors
import kotlin.math.atan

// me gusta experimentar con conceptos en este caso concurrencia si eres muy nuevo puedes ignorar
//las funciones suspend y solo ver la logica


interface ActionWarrior{
    fun attackEnemy(): Int
    fun dodgeAttack(): Boolean
    fun getStatus(): String
}

interface Tournament {
    suspend fun tournament(warriors: List<WarriorZ>)
}



data class Technique constructor(
    var name:String="",
    var attack: Int=0
)

data class WarriorZ constructor(
    var name:String="",
    var speed: Int=0,
    var defense: Int=0,
    var health:Int=100,
    var techniques: List<Technique> = emptyList()
):ActionWarrior{
    override fun attackEnemy(): Int {
        val tech= techniques[(0..<techniques.size).random()]
        println("El participante $name ha usado ${tech.name} para atacar")
        return tech.attack
    }

    override fun dodgeAttack(): Boolean= (0..100).random() < 20

    override fun getStatus(): String = " Warrior $name  health: ${if(health<0)0 else health}"

}

// contruir objetos con dsl basico
fun technique(block:Technique.()-> Unit):Technique= Technique().apply(block)
fun warriorZ(block: WarriorZ.() -> Unit):WarriorZ=WarriorZ().apply(block)


class TekiachiBudokai:Tournament{
    private suspend fun figthing(warrior1: WarriorZ, warrior2: WarriorZ): WarriorZ {
        var attacker=if (warrior1.speed>warrior2.speed) warrior1 else warrior2
        var defenser= if (attacker==warrior1) warrior2 else warrior1

        while (warrior1.health>0 && warrior2.health>0){
            attacker.attackEnemy().run {
                val damage = if (!defenser.dodgeAttack()) maxOf(defenser.defense-this, 0) else 0
                val finalDamage=if (defenser.defense > this) (this * 0.1).toInt() else damage
                defenser.health -= finalDamage
                println("El partipante ${defenser.name} ha recibido ${finalDamage} de daño")
            }
            println(attacker.getStatus())
            println(defenser.getStatus())

            attacker=defenser.also {
                defenser=attacker
            }
        }
        return if (warrior1.health>0) warrior1 else warrior2
    }

    override suspend fun tournament(warriors: List<WarriorZ>): Unit= coroutineScope {
        if (warriors.size%2!=0){
            println("Solo se permite que el numero de participantes sea un numero potencia 2")
            return@coroutineScope
        }
       var rounds=warriors.shuffled()
       var counterRound=1
       while (rounds.size>1) {
           val winners = mutableListOf<WarriorZ>()
           for (i in rounds.indices step 2) {
               val winner = async(Dispatchers.LOOM) { figthing(rounds[i], rounds[i + 1]) }.await()
               winners.add(winner)
           }
           println("loa ganadores de la ronda $counterRound son")
           winners.forEach { println(it.name) }
           rounds = winners
           counterRound++
       }
        println("¡El ganador del torneo es ${rounds.first().name}!")
    }

}

val warriorsMock= listOf(
    warriorZ {
        name="Goku"
        speed=90
        defense=85
        techniques=listOf(
            technique {
                name="Kame Hame Ha !"
                attack=45
            },
            technique {
                name="Kaio Ken !"
                attack=40
            }
        )
    },
    warriorZ {
        name="Vegeta"
        speed=85
        defense=90
        techniques= listOf(
            technique {
                name="Harlic Ho!!"
                attack=40
            },
            technique {
                name="Final flash"
                attack=67
            }
        )
    } ,
    warriorZ {
       name="Piccolo"
       speed=85
       defense=80
       techniques=listOf(
           technique {
               name="Mankankosappoo "
               attack=63
           },
           technique {
               name="Giganta Max"
               attack=32
           }
       )
      },

    warriorZ {
        name="Krillin"
        speed=90
        defense=50
        techniques=listOf(
            technique {
                name="Kienzan "
                attack=70
            },
            technique {
                name="taioken"
                attack=5
            }
        )

    }
)


fun main()= runBlocking {
  val toournament= TekiachiBudokai()
  val job= launch{
       toournament.tournament(warriorsMock)
  }
  job.join()
}




// experimentar con loom proyect en kotlin ignorar
val Dispatchers.LOOM: @BlockingExecutor CoroutineDispatcher
    get() = Executors.newVirtualThreadPerTaskExecutor().asCoroutineDispatcher()



