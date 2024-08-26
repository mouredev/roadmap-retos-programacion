import java.util.*

//1.-Definir estructura de datos para guardar valores
val ringList= mutableMapOf(
    "elves" to 0,
    "dwarves" to 0,
    "humans" to 0,
    "sauron" to 1
)


//2.- Definir funcion auxilares

fun String.capitalizeWord():String {
    return replaceFirstChar { if (it.isLowerCase()) it.titlecase(Locale.getDefault()) else it.toString() }
}

fun isPrime(num: Int): Boolean {
    if (num<=1) return false
    for (i in 2..num / 2) {
        if (num % i == 0) {
            return false
        }
    }
    return true
}

fun numberRings():Int{
    println("Enter number of rings: ")
    return readLine()?.let { it.toInt()-1 } ?:0
}

fun repartitionRings(numRings:Int) {
    var elves=0
    var dwarves=0
    var humans=0

   for (i in 1.. numRings){
       if (i%2==0) elves++
       else if(isPrime(i)) dwarves++
       else humans++
   }
   ringList["elves"]=elves
   ringList["dwarves"]=dwarves
   ringList["humans"]=humans

}

fun printResults(){
    ringList.forEach { specie, numRings ->
        println("${specie.capitalizeWord()} has $numRings rings")
    }
}



fun main() {
    val numRings=numberRings()
    repartitionRings(numRings)
    printResults()
}