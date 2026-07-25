
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.onCompletion
import kotlinx.coroutines.runBlocking
import java.time.Duration
import java.time.LocalDateTime
import java.time.temporal.ChronoUnit

//https://kotlinlang.org/docs/flow.html

data class CountDown(var days: Long, var seconds:Long)

fun CountDown.showCountDown(): String{
    val hours = Duration.ofSeconds(seconds).let {
        String.format("%02d:%02d:%02d", it.toHoursPart(), it.toMinutesPart(), it.toSecondsPart())
    }

    return "$days days -$hours"
}



fun getFinalDate(): LocalDateTime {
    var valid=false
    var data=""

   while (valid!=true) {
       println(
           "Enter Enter a date using the following format:\n" +
                   "year,month,day,hour,minute"
       )
       data = readLine().toString()
       if (data.contains("^\\d+(,\\d+){4}\$".toRegex())) valid=true
       else println("Incorrect format to date")
   }

    return data.split(",").map { it.toInt() }.let {
         LocalDateTime.of(it[0],it[1],it[2],it[3],it[4])
    }
}

fun calculateDateRest(finalDate: LocalDateTime,today: LocalDateTime)=CountDown(
        days = ChronoUnit.DAYS.between(today,finalDate),
        seconds = ChronoUnit.SECONDS.between(today,finalDate)
    )



 fun counterDown()= flow<String>{
    val finalDate=  getFinalDate()
    do {
         val today= LocalDateTime.now()
         val counter = calculateDateRest(finalDate, today)
         delay(1000)
         emit(counter.showCountDown())
     } while (counter.days.toInt() !=0 || counter.seconds.toInt()!=0)

}.onCompletion { println("The countdown is over, the day has arrived 😎😎😎 ") }




fun main(): Unit = runBlocking {
    counterDown().collect {
        println(it)
    }
}