import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*
import java.time.Duration


//1.-Definir entidades

data class Friend constructor(
    val name:String,
    val skill:String,
    val damage:Int=(10..120).random()
)

data class Warrior constructor(
    val name:String="Deadpool",
    var life:Int=0,
  )


enum class Fighter{
    DEADPOOL,
    WOLVERINE
}

//2.-Definir datos auxiliares

val deadpoolFriens= listOf(
    Friend("Cable","Telequinesis Shooter"),
    Friend("Yukio","Energy Attack"),
    Friend("Domino","Lucky Evasion",0),
    Friend("Colosus","Steal Punch")
)
val wolverineFriends= listOf(
    Friend("Cyclops","Slash"),
    Friend("Jean Gray","Fenix force",120),
    Friend("Rougue","Drain Attack"),
    Friend("Storm","Hurancane")
)

val deadpoolSkills= listOf(
    "Shooter Attack",
    "Katana Slash",
    "Granate Attack",
   )

val wolverineSkills= listOf(
    "Drill Claw",
    "Tornado Claw",
    "Berserker Slash",
  )

//3.-Definir comportamiento de la aplicación

interface Fighting {
   suspend fun asssigmentLife()
   suspend fun simulateFight()
   suspend fun ShowResult()
}

interface StateFighting{
    suspend fun criticalAttack(fighter: Fighter,damageFigther:Int): Boolean
    suspend fun infoTurn(warrior1:Warrior,warrior2:Warrior,turn:Int)
    suspend fun friendAttack(fighter: Fighter): Int
    fun getSkill(fighter: Fighter): String
    fun genererateRandomDamage(limit:Int):Int
    fun getEvasion(probability: Double): Boolean
}

//4.- Implementar comportamiento


class FigthingState:StateFighting{

    override suspend fun criticalAttack(fighter: Fighter, damageFigther: Int): Boolean=when(fighter) {
        Fighter.DEADPOOL -> if (damageFigther == 100) true else false
        else -> if (damageFigther == 120) true else false
    }

    override suspend fun infoTurn(warrior1: Warrior, warrior2: Warrior, turn: Int) {
        val info="""
        :::::::::::Turn: $turn:::::::::::::
        ${warrior1.name} Life: ${if(warrior1.life<0) 0 else warrior1.life}
        ${warrior2.name} Life: ${if(warrior2.life<0) 0 else warrior2.life}
    """.trimIndent()

      println(info)

    }

    override fun getSkill(fighter: Fighter): String = when (fighter) {
        Fighter.DEADPOOL -> (0..<deadpoolSkills.size).random().let { deadpoolSkills[it] }
        Fighter.WOLVERINE -> (0..<wolverineSkills.size).random().let { wolverineSkills[it] }
    }

    override fun getEvasion(probability: Double): Boolean = (0..5).random() <= probability


    override  suspend fun friendAttack(fighter: Fighter): Int= coroutineScope {
      val damage= async {
          if (fighter == Fighter.DEADPOOL) {
              val friend = (0..<deadpoolFriens.size).random().let { deadpoolFriens[it] }
              if (friend.skill == "Lucky Evasion") println("Deadpool use Lucky Evasion thanks to ${friend.name} an evade damage")
              else println("Deadpool call friend ${friend.name} and use ${friend.skill}  cause damage ${friend.damage}")
              friend.damage
          }
          if (fighter == Fighter.WOLVERINE) {
               (0..<wolverineFriends.size).random().let { wolverineFriends[it] }.let {
                  println("Wolverine call friend ${it.name} and use ${it.skill}  cause damage ${it.damage}")
                  it.damage
              }
          }
          0//encaso de no entrar a ninguna condicion
      }.await()
        return@coroutineScope damage
    }

    override fun genererateRandomDamage(limit:Int):Int=(10..limit).random()

}



context(StateFighting)
class FightMarvel:Fighting{
    private val deadPool=Warrior()
    private val wolverine=Warrior("Wolverine")

    override suspend fun asssigmentLife():Unit= coroutineScope {
      launch {
          println("Enter deadpool life: ")
          val lifeD = readLine()!!.toInt()
          println("Enter wolverine life: ")
          val lifeW = readLine()!!.toInt()
          deadPool.life = lifeD
          wolverine.life = lifeW
      }
    }

    override suspend fun simulateFight(): Unit = coroutineScope {
        var turn = 1
        while (deadPool.life >= 0 && wolverine.life >= 0) {
            val skillDeadpool = getSkill(Fighter.DEADPOOL)
            val skillWolverine = getSkill(Fighter.WOLVERINE)
            var damageD = 0
            var damageW = 0

            var criticalD = criticalAttack(Fighter.DEADPOOL, damageD)
            var criticalW = criticalAttack(Fighter.WOLVERINE, damageW)

            if (getEvasion(0.25)) {
                println("Deadpool evades attack")
                continue
            }
            if (getEvasion(0.20)) {
                println("Wolverine evades attack")
                continue
            }

            attackCritical(criticals = Pair(criticalD, criticalW), skills = Pair(skillDeadpool, skillWolverine))


            val friendAttack = (0..5).random()
            if (friendAttack == 0) damageD = friendAttack(Fighter.DEADPOOL)
            if (friendAttack == 1) damageW = friendAttack(Fighter.WOLVERINE)

            if (damageD > 0) {
                damageW = genererateRandomDamage(120)
                deadPool.life -= damageW
                wolverine.life -= damageD
                println("Wolverine use $skillWolverine and cause damage $damageW")
                continue
            }

            if (damageW > 0) {
                damageD = genererateRandomDamage(100)
                deadPool.life -= damageW
                wolverine.life -= damageD
                println("Deadpool use $skillDeadpool and cause damage $damageD")
                continue
            }

            if (criticalW.not() && criticalD.not()) {
                damageD = genererateRandomDamage(100)
                damageW = genererateRandomDamage(120)
                deadPool.life -= damageW
                wolverine.life -= damageD
                println("Deadpool use $skillDeadpool and cause damage $damageD")
                println("Wolverine use $skillWolverine and cause damage $damageW")
            }

            infoTurn(deadPool, wolverine, turn)
            delay(Duration.ofSeconds(1).toMillis())
            turn++

        }
    }

    override suspend fun ShowResult() {
        if (deadPool.life <= 0) println("Wolverine win")
        if (wolverine.life <= 0) println("Deadpool win")
    }

    private fun attackCritical(criticals:Pair<Boolean,Boolean>,skills:Pair<String,String>){
        if (criticals.first){
            println("Wolverine receives critical attack need regenerate in this turn")
            val damageD =genererateRandomDamage(100)
            wolverine.life -= damageD
            println("Deadpool use ${skills.first} and cause damage $damageD")
        }

        if (criticals.second){
            println("Deadpool receives critical attack need regenerate in this turn")
            val damageW =genererateRandomDamage(120)
            deadPool.life -= damageW
            println("Wolverine use ${skills.second} and cause damage $damageW")
        }
    }
 }



fun main()= runBlocking {
  with(FigthingState()) {
      val fight = FightMarvel()
      fight.asssigmentLife()
      fight.simulateFight()
      fight.ShowResult()
  }
}
