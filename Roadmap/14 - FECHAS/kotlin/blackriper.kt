import java.text.SimpleDateFormat
import java.time.LocalDateTime
import java.time.ZoneId
import java.time.format.DateTimeFormatter
import java.time.temporal.ChronoUnit
import java.util.*
import java.util.concurrent.TimeUnit

/*
 En kotlin al igual que java se pueden utilizar  tres objetos principales para
 trabajar con fechas y tiempo:

 - Date
 - Calendar
 - LocalDateTime

*/




fun exampleWithDate(bornDay : Date) {
    val formatter = SimpleDateFormat("dd/MM/yyyy hh:mm:ss")
    println("working with date")
    val today = Date()
    println("Today is ${formatter.format(today)}")
    println("birthday  is ${formatter.format(bornDay)}")

    // obtener la diferencia de tiempo entre dos fechas
    val diff = today.time - bornDay.time
    val years = TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS) / 365
    println("I am $years years old")
}

fun exampleWithCalendar(bornDay: Date) {
    println("working with calendar")
    val today = Calendar.getInstance()
    val born = Calendar.getInstance().apply { this.time = bornDay }
    val years = today.get(Calendar.YEAR) - born.get(Calendar.YEAR)
    println("I am $years years old")
}

fun exampleWithLocalDateTime(bornDay: Date) {
    println("working with LocalDateTime")
    val today = LocalDateTime.now()
    val born = LocalDateTime.ofInstant(bornDay.toInstant(), ZoneId.systemDefault())
    val years = ChronoUnit.YEARS.between(born, today)
    println("I am $years years old")
}

fun formatWithDateAndCalendar(bornDay: Date) {
    val formatter = SimpleDateFormat("dd/MM/yyyy")
    println(formatter.format(bornDay))
    formatter.applyPattern("HH:mm:ss")
    println(formatter.format(bornDay))

    val born = Calendar.getInstance().apply { this.time = bornDay }
    println("day of year ${born.get(Calendar.DAY_OF_YEAR)}")
    println("day of week ${born.get(Calendar.DAY_OF_WEEK)}")
    println("name of month ${born.getDisplayName(Calendar.MONTH, Calendar.LONG, Locale.getDefault())}")

}
fun formatWithLocalDateTime(bornDay: Date) {
    val formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy ")
    val born = LocalDateTime.ofInstant(bornDay.toInstant(), ZoneId.systemDefault())
    println(formatter.format(born))
    val formatter2 = DateTimeFormatter.ofPattern("HH:mm:ss")
    println(formatter2.format(born))

    println("day of year ${born.dayOfYear}")
    println("day of week ${born.dayOfWeek}")
    println("name of month ${born.month}")
}


fun main() {
 // dar formato ala fecha en este caso  dia , mes , año y hora con minuto y segundo
 val formatter = SimpleDateFormat("dd/MM/yyyy HH:mm:ss")
 val birthday= "20/05/1994 15:30:00"
    // convertir fecha string a Date
 val bornDay = formatter.parse(birthday)
 exampleWithDate(bornDay)
 exampleWithCalendar(bornDay)
 exampleWithLocalDateTime(bornDay)
 formatWithDateAndCalendar(bornDay)
 formatWithLocalDateTime(bornDay)
}