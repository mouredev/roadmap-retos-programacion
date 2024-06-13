import java.text.SimpleDateFormat

/*
Las funciones de orden  superior  son cuyas funciones  que pueden recibir una funcion como argumento
o  devolver una funcion como resultado.

usos comunes de la funcion de orden superior son el manejo de  listas,  map,  filter, etc.

las funciones de orden superior no mutan las listas originales  dan como resultado una nueva lista
por lo cual la mutabilidad se mantiene al minimo.

*/

fun exampleWithOrderSuperiorFunc(){

 val list = listOf(1,2,3,4,5,6,7,8,9,10)
 println("list of kotlin $list")

 // usando map para generar un nuevo resultado este puede recibir una lambda funcion como argumento
 val newList = list.map { it * 2 }
 println("list of map kotlin $newList")

 // forma imperativa
 fun multiplyBy2(x:Int):Int = x * 2

 fun multipyNumber(listNum:List<Int>, func : (Int) -> Int): List<Int>{
     val listResult = mutableListOf<Int>()
     for (num in listNum){
         listResult.add(func(num))
     }
    return  listResult
 }

val newList2 = multipyNumber(list,::multiplyBy2)
println("list of my own function $newList2")

// lambda function
val newList3 = multipyNumber(list){it * 3}
println("list of lambda function $newList3")

}

// ejercicio extra

data class Student(val name:String,val birthDate:String,val scores:List<Int>)

val listOfStudents = listOf(
    Student("rodolfo","20/05/1994", listOf(8,9,9,10,9,10)),
    Student("martin","27/05/1993", listOf(5,6,7,8,9,9)),
    Student("roswell","12/03/1992", listOf(9,7,7,8,0,8)),
    Student("salvador","22/04/1995", listOf(9,9,9,10,10,10)),
    Student("luis","01/01/1990", listOf(8,9,5,4,9,10))
)


fun calculateAverageScore(student:Student):Int{
    val total = student.scores.sum()
    return total / student.scores.size
}



fun main() {
    exampleWithOrderSuperiorFunc()

    // ejercicio extra
    val averageScore = listOfStudents.map { it.name to  calculateAverageScore(it) }
    println("average score $averageScore")

    val bestStudents= averageScore.filter { it.second >=9 }
    println("best students $bestStudents")

    val youngStudents = listOfStudents.sortedByDescending { SimpleDateFormat("dd/MM/yyyy").parse(it.birthDate) }
    println("young students $youngStudents")

   val majorScores= listOfStudents.map { it.name to it.scores.max() }
    println("major scores $majorScores")
}