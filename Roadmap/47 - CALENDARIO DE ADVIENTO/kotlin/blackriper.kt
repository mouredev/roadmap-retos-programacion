
import java.util.Scanner


const val DAYS=24
val Dimensions= Pair(4,6)

val gifts = listOf(
    "Cupon 50% en mouredev pro", "Taza java", "Libro github", "Cupon 50% metalcode", "Consulta gratuita doc Mouredev", "Kotlin pet",
    "Descuento 50% en Be native", "Mac mini m4", "Curso swift", "Termo comunidad", "Playera", "Curso Reflex",
    "Curso python", "Descuento 30% udemy", "Taza Adviento", "Teclado", "Monitor de programador", "Stickers de mouredev",
    "Curso swift", "Curso javascript", "Curso go", "Mouredev pro cuenta gratis", "Poster", "Calendar gopher"
)

typealias Calendar=  Array<Array<String?>>

fun createAdviento(): Calendar{
    val calendar = Array(Dimensions.first) { arrayOfNulls<String>(Dimensions.second) }
    var day = 1

    // Fill the calendar with days
    for (i in 0 until Dimensions.first) {
        for (j in 0 until Dimensions.second) {
            if (day <= DAYS)
                calendar[i][j] = String.format("%02d", day)
                day++

        }
    }
    return calendar;
}



fun printCalendar(calendar: Calendar,selected: Int=0) {
    for (i in calendar.indices) {
        for (j in calendar[i].indices) {
            if (calendar[i][j] != null) {
                print("**** ")
            } else {
                print("     ")
            }
        }
        println()
        for (j in calendar[i].indices) {
            if (calendar[i][j] != null) {
                print(if (calendar[i][j]?.toInt()==selected) "**** " else "*${calendar[i][j]}* ")
            } else {
                print("     ")
            }
        }
        println()
        for (j in calendar[i].indices) {
            if (calendar[i][j] != null) {
                print("**** ")
            } else {
                print("     ")
            }
        }
        println()
    }
}

fun selectDay(calendar: Calendar) {
    var daySelected=0
    val daysSelected=mutableListOf<Int>()
    while (true) {
        printCalendar(calendar,daySelected)
        print("Selecciona un día (1-24) o 0 para salir: ")
         daySelected = readLine()!!.toInt()

        if (daySelected == 0)  break
        else if (daySelected < 1 || daySelected > 24)  println("Por favor, selecciona un día válido.")
        else if (daysSelected.contains(daySelected)) println("El dia ya ha sido descubierto")
        else  println("Regalo para el día $daySelected: ${gifts[daySelected - 1]}")
        daysSelected.add(daySelected)
   }
  }

fun main() {
    val calendar=createAdviento()
    selectDay(calendar)
}