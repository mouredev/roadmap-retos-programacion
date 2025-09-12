import com.jakewharton.picnic.table
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*
import java.util.UUID
import java.time.Duration

/*
librerias extra
corutinas : https://github.com/Kotlin/kotlinx.coroutines
tablas en consola : https://github.com/Jakewharton/picnic
*/


/* datos auxiliares y globales */

val country= buildMap<Int,String> {
   put(1,"United States")
   put(2,"France")
   put(3,"Japan")
   put(4,"China")
   put(5,"Russia")
   put(6,"Brazil")
   put(7,"México")
   put(8,"Uruguay")
   put(9,"Argentina")
   put(10,"Colombia")
   put(11,"Spain")
   put(12,"Germany")
   put(13,"United Kingdom")
}

val medalsList=country.values.toList().map { CountryMedals(it)}
var events: List<SportingEvent> =emptyList()

/* defininicion de entidades y interfaces */

data class CountryMedals constructor(
    val countryName:String,
    var gold:Int=0,
    var silver:Int=0,
    var bronze:Int=0
)


data class SportingEvent constructor(
    val id:UUID=UUID.randomUUID(),
    val title:String,
    var players:MutableList<Player> = mutableListOf()
    )

data class Player constructor(
    val name:String,
    val idEvent:UUID,
    val country : String,
    var score:Int=0
)

interface ForEvents{
  suspend fun registerEvent()
  suspend fun simulateEvents()
}

interface ForPlayers{
    suspend fun registerPlayer()
}


/* implementacion de repositorios */

class RepositoryEvents:ForEvents {

    override suspend fun registerEvent(): Unit = coroutineScope {
        val eventsRegitered=async {
            val eventsRegis = mutableListOf<SportingEvent>()
            var option: String = ""
            while (option != "N") {
                println("Enter a event name")
                val title = readLine() ?: ""
                SportingEvent(title = title)
                eventsRegis.add(SportingEvent(title = title))
                println("Do you want to continue? (Y/N)")
                option = readLine()?.let { it.uppercase() } ?: "N"
            }
            eventsRegis
        }
        events=eventsRegitered.await()
    }


    override suspend fun simulateEvents(): Unit = coroutineScope {
           println("Starting events")
           events.filter { it.players.size >= 3 }.forEach {
              launch {
                  it.players.forEach {
                      delay(1000L)
                      it.score = (1..100).random()
                  }
                  val winners = it.players.sortedByDescending { it.score }.take(3)
                  var i = 0
                  var listmedals = listOf("Gold", "Silver", "Bronze")

                  println("""Winners of ${it.title} are:""")
                  val results = table {
                      cellStyle {
                          border = true
                          paddingLeft = 1
                          paddingRight = 1
                      }
                      row("Medal", "Name", "Country", "Score")
                      winners.forEach {
                          updateMedalsList(listmedals[i], it.country)
                          row(listmedals[i++], it.name, it.country, it.score)
                      }
                  }
                  println(results)
              }

             }
        }

       private fun updateMedalsList(medal: String, country: String) {
        medalsList.run {
            when (medal) {
                "Gold" -> this.first { it.countryName == country }.gold++
                "Silver" -> this.first { it.countryName == country }.silver++
                "Bronze" -> this.first { it.countryName == country }.bronze++
                else -> {
                    println("Invalid medal type")
                }
            }
        }
    }
}

    class RepositoryPlayers : ForPlayers {
     
        override suspend fun registerPlayer(): Unit = coroutineScope {
            if (events.isEmpty()){
                println("no available events for registering players")
                return@coroutineScope
            }
            launch { getPlayers() }
        }

        private suspend fun getPlayers(){
            var option: String = ""
            while (option != "N") {
                println("Enter a player name")
                val name = readLine() ?: ""
                val country = getCountry()
                val idEvent = getEventID()
                events.first { it.id == idEvent }.players.add(Player(name, idEvent, country))
                println("Do you want to continue? (Y/N)")
                option = readLine()?.let { it.uppercase() } ?: "N"
             }
        }


        private fun getCountry(): String {
            country.forEach { indx, cou ->
                println("$indx - $cou")
            }
            println("Choose a country: ")
            val ind = readLine()!!.toInt()
            return country[ind]?:"United States"
        }

        private fun getEventID(): UUID {
            events.forEachIndexed { indx, event ->
                println("${indx+1} - ${event.title} - ${event.players.size} players")
            }
            println("Choose an event: ")
            val idx = readLine()!!.toInt()
            return events[idx-1].id
        }

    }


class JJOOController {
    private val repositoryPlayers = RepositoryPlayers()
    private val repositoryEvents = RepositoryEvents()

    suspend fun showMenu() {
        var option: Int = 0
        while (option != 5) {
            println("Welcome to JJOO 2024")
            println("1. Register event")
            println("2. Register player")
            println("3. Start events")
            println("4. Get list of countries with medals")
            println("5. Exit")
            println("Chosse a option")
            option = readLine()!!.toInt()
            when (option) {
                1 -> repositoryEvents.registerEvent()
                2 -> repositoryPlayers.registerPlayer()
                3 -> repositoryEvents.simulateEvents()
                4 -> getMedalsList()
                5 -> println("Good bye")
                else -> println("Invalid option")
            }
        }

    }

   private fun getMedalsList() {
       val results= table {
            cellStyle {
                border = true
                paddingLeft = 1
                paddingRight = 1
            }
            row("Country", "Gold", "Silver", "Bronze")
            medalsList.forEach {
                row(it.countryName, it.gold, it.silver, it.bronze)
            }
        }
       println(results)
    }
  }




 fun main()= runBlocking<Unit> {
  val jjoApp=JJOOController()
  jjoApp.showMenu()

}