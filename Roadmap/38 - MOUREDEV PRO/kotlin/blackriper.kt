import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.filter
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.toList
import kotlinx.coroutines.flow.transform
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import java.io.FileInputStream
import java.io.InputStream

//1.- definir una clase para parsear la info

enum class Status(val state: String){
    ACTIVE("active"),
    INACTIVE("inactive")

}

enum class Prize{
    Suscription,
    Discount,
    Book,
    NotWinner
}

data class Suscriptor(val id: Int,val email: String,val status: Status) {
  companion object {
      fun parseStatus(name: String): Status = when (name) {
          Status.ACTIVE.state -> Status.ACTIVE
          Status.ACTIVE.state -> Status.INACTIVE
          else -> Status.INACTIVE
      }
  }

  fun toWinner(prize:Prize):Winner{
      return Winner(
          id,
          email,
          prize
      )
  }
}

data class Winner(val id: Int, val email: String, val prize:Prize)

//2.- Definir comportamiento
interface CSVParse{
    suspend fun readCsv(): Flow<Suscriptor>
}

//3.- implementar interface
class CSVProcessor( private val input: InputStream):CSVParse{

   override suspend fun readCsv(): Flow<Suscriptor>{
       val reader= input.bufferedReader()
       val header= reader.readLine()

      val suscriptors= reader.lineSequence()
           .filter { it.isNotBlank() }
           .map { toSuscriptor(it) }
          .asFlow()

       return suscriptors
    }


   private fun toSuscriptor(value: String):Suscriptor{
      val(id,email,status)=value.split(',', ignoreCase = false, limit = 3)
      return Suscriptor(
           id.toInt(),
           email,
           Suscriptor.parseStatus(status)
      )
   }
}

//4.- funciones auxiliares
fun getInputStream(src: String): InputStream{
    val file= runCatching {
        FileInputStream(src)
    }
    if (file.isFailure) println("error to read file ${file.exceptionOrNull()}")
    return file.getOrDefault(FileInputStream("src/main/resources/datamoure.csv"))
}

fun getPrize(numWinner: Int):Prize=when(numWinner){
    1-> Prize.Suscription
    2->Prize.Discount
    3->Prize.Book
    else -> Prize.NotWinner
}


fun randomWinners(suscriptors: List<Suscriptor>): List<Winner>{
    return mutableListOf<Winner>().apply {
        var numWinner=0
        while (size != 3) {
            val ind = (0..suscriptors.size).random()
            val suscriptor = suscriptors.get(ind)
            if(count { it.email == suscriptor.email } == 0) {
                numWinner++
                val winner=Winner(
                    suscriptor.id,
                    suscriptor.email,
                    getPrize(numWinner)
                )
                add(winner)
            }
        }
    }

  }

suspend fun getWinners(suscriptors: Flow<Suscriptor>){
    val activeSuscriptor = suscriptors
        .filter { it.status == Status.ACTIVE }.toList()

    randomWinners(activeSuscriptor).run {
        println("Results")
        println("| Id   |   Email    |     Prize")
        this.forEach {
            println("  ${it.id}   ${it.email}   ${it.prize}")
        }
    }
}


fun main()= runBlocking {
    val file=getInputStream("src/main/resources/datamoure.csv")
    val csvParser=CSVProcessor(file)
    val suscriptors= async{csvParser.readCsv()}.await()
    val job=launch{getWinners(suscriptors)}
    job.join()
}