import kotlinx.coroutines.async
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlin.system.measureTimeMillis
import kotlin.time.measureTime

/*
La asincronia es una forma de  ejecutar una o mas tareas en segundo plano algunas formas de la
misma siguen dependiendo del hilo principal en el que se ejecute.Los principales conceptos  al ejecutar
tareas en paralelo son.

Asincronia: Tarea no bloqueante que puede seguir ejecutando el hilo principal aunque la tarea
que este en segundo plano no se ha completado.

Concurrencia: Tarea no bloqueante que acomparacion dela anterior no tiene un orden de ejecucion
de las tareas. sigue dependendo del hilo principal en el que se ejecute.

Paralelismo: Tarea que se puede ejecutar en paralelo de forma simultanea y no depende del hilo principal

En kotlin hay diferentes tecnicas para la ejecucion de tareas en segundo plano.

-Thereading (hilo de ejecucion) un hilo
-Callback (llamada de retorno) una llamada de retorno
-Futures , promises
-Reactive extensions
-Coroutines

para este erjercicio usaremos la libreria coroutines para la ejecucion de tareas en segundo plano
ya que es la mas utilizada.

para mas informacion ver la documentacion de coroutines en
https://github.com/Kotlin/kotlinx.coroutines
https://kotlinlang.org/docs/coroutines-basics.html

measureTime: sirve para medir el tiempo de ejecucion de una tarea

dentro de corutines existen las que se corren de mode concurrente con la palabra launch y async
lo cual lo hace de forma asincrona  esta forma es parecida a como lo hacen lenguajes como rust o
typescript

*/


suspend  fun runTask(nameTask:String,duration:Long){
    val time= measureTimeMillis {
        println("starting $nameTask")
        delay(duration)
        println("finishing $nameTask")
    }
    println("task $nameTask took $time.ms")
}



fun main() = runBlocking {
    runTask("Example", 1000L)

    // reto extra
    val taskA = async { runTask("Task A", 1000L) }
    val taskB = async { runTask("Task B", 2000L) }
    val taskC = async { runTask("Task C", 3000L) }
    val taskD = async { runTask("Task D", 1000L) }

    taskA.await()
    taskB.await()
    taskC.await()
    if (taskA.isCompleted && taskB.isCompleted && taskC.isCompleted) taskD.await()
}