
import java.time.DayOfWeek
import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.time.temporal.IsoFields
import kotlin.math.abs


/*
Reto 1
A partir de 2015, se estableció que el tercer sábado de septiembre sería la fecha oficial para celebrar el Batman Day en todo el mundo
**/
fun getWeekNameAndNum(date: String): Pair<DayOfWeek, Int>{
    val dt= LocalDate.parse(date,DateTimeFormatter.ofPattern("dd/MM/yyyy"))
    val numWeek=dt.get(IsoFields.WEEK_OF_WEEK_BASED_YEAR)
    return Pair(dt.dayOfWeek,numWeek)
}

fun calculateCenturyBatmanDay(){
    var anniversary=85
    var year= LocalDate.now().year

    while (anniversary<=100){
        for (i in 1..30){
            val day=if (i<10) "0$i" else "$i"
            val date=getWeekNameAndNum("$day/09/$year")
            if (date.first== DayOfWeek.SATURDAY && date.second==38){
                println("Batman's ${anniversary}th anniversary of the year $year is on $day/09/$year")
            }
        }
        anniversary++
        year++
    }

}


//reto 2

const val GOTHAM_MAP=20
const val MAX_UMBRAL=20



data class Sensor constructor(
    var nameSector: String="",
    var postionX: Int=0,
    var postionY: Int=0,
    var warningLevel: Int=0,
    var sumThreat: Int=0
)

fun sensor(block: Sensor.()-> Unit):Sensor =Sensor().apply(block)


fun calculateSumThreat(sensor:Sensor): Int {
    var sum=0
   for (i in sensor.postionX-1..sensor.postionX+1){
       for (j in sensor.postionY-1..sensor.postionY+1){
           if (i>=0 && i<GOTHAM_MAP && j>=0 && j<GOTHAM_MAP) sum+=sensor.warningLevel

       }
   }
    return sum
}

fun scanningSensors(sensors: List<Sensor>){
    sensors.forEach {
         it.sumThreat=calculateSumThreat(it)
      

    }
    val criticalZone=sensors.maxByOrNull { it.sumThreat }
    if (criticalZone!=null){
        val center= Triple(criticalZone.nameSector,criticalZone.postionX,criticalZone.postionY)
        val distance= abs(center.second)+abs(center.third)
        println("El sector mas peligroso es ${center.first} ubicado en [${center.second},${center.third}]")
        println("El sector ${center.first} se encuentra a una distancia de $distance de la baticueva")
        if (criticalZone.sumThreat>MAX_UMBRAL) println("Protocolo de seguridad Activado")
        else println("Protocolo de seguridad no Activado")

    }
}

fun readGotham(){
    val sensors=listOf(
        sensor {
            nameSector="Distrito Diamante"
            postionX=3
            postionY=3
            warningLevel=5
        },
        sensor {
            nameSector="Iceberg Lounge"
            postionX=12
            postionY=12
            warningLevel=7
        },
        sensor {
            nameSector="Gotica Bank"
            postionX=4
            postionY=4
            warningLevel=8
        }
    )

    scanningSensors(sensors)
}




fun main() {
  calculateCenturyBatmanDay()
  readGotham()
 }