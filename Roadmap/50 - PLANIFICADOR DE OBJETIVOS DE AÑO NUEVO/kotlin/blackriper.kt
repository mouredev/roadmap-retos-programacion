import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.emptyFlow
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.runBlocking
import java.io.File
import java.io.FileWriter
import java.io.PrintWriter

//models

data class Task(
    val goal: String,
    val cant: Int,
    val unit: String,
    val term: Int
)



interface ManagerTask{
    suspend fun saveTask()
    suspend fun calculatePlanning()
    suspend fun savePlanning()
}

// implementation

class TaskManager(private val src: String):ManagerTask{

    private val tasks= mutableListOf<Task>()
    private lateinit var terms: Flow<String>
    private val months=mapOf(
        1 to "Enero",
        2 to "Febrero",
        3 to "Marzo",
        4 to "Abril",
        5 to "Mayo",
        6 to "Junio",
        7 to "Julio",
        8 to "Agosoto",
        9 to "Septiembre",
        10 to "Octubre",
        11 to "Noviembre",
        12 to "Diciembre"
    )

    override suspend fun saveTask() {
        while (true){
            println("¿Cual es la meta a cumplir?")
            val goal= readLine()!!
            println("cantidad de pasos para lograr la meta ")
            val cant= readLine()!!.toInt()
            println("unidad para lograr la meta ")
            val unit=readLine()!!
            println("Define un plazo para cumplir tu meta ")
            val term=readLine()!!.toInt()
            if (term>12){
                println("El plazo maximo es de 12 meses ")
                continue
            }
            if (tasks.size>=10) println("solo se permiten un maximo de 10 metas ")
            else tasks.add(Task(goal,cant,unit,term))

            println("¿Deseas agregar otra meta S/N ?")
            val option = readLine()!!.uppercase()
            if (option=="N") break

        }
    }

    override suspend fun calculatePlanning() {
        terms = flow {
            repeat(12) {
              emit(months[it+1]!!)
              tasks.forEach { task->
                   if (it<task.term){
                      val unitMon=task.cant/task.term
                      emit("[] ${task.goal} ($unitMon ${task.unit}/mes) Total: ${task.cant}")
                  }
              }
            }
        }
    }

    override suspend fun savePlanning() {
       terms.collect { item ->
           println(item)
           PrintWriter(FileWriter(src,true)).use {
                  it.write("$item \n")
          }
       }
    }

}

fun main() = runBlocking{
    val manager=TaskManager("src/main/resources/terms.txt")
    manager.saveTask()
    manager.calculatePlanning()
    manager.savePlanning()
}