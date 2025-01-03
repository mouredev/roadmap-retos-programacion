import kotlinx.coroutines.*
import java.time.LocalTime
import java.time.format.DateTimeFormatter

suspend fun asyncFunction(name: String, duration: Int) {
    val formatter = DateTimeFormatter.ofPattern("HH:mm:ss")
    
    println("$name: Iniciando en ${LocalTime.now().format(formatter)}")
    println("$name: Duración de $duration segundos")
    
    delay(duration * 1000L)
    
    println("$name: Finalizando en ${LocalTime.now().format(formatter)}")
}

suspend fun main() = coroutineScope {
    // Parte básica del ejercicio
    launch { asyncFunction("Función de ejemplo", 5) }
    
    // Parte extra del ejercicio
    val jobC = launch { asyncFunction("Función C", 3) }
    val jobB = launch { asyncFunction("Función B", 2) }
    val jobA = launch { asyncFunction("Función A", 1) }
    
    // Esperamos a que las funciones A, B y C terminen
    jobC.join()
    jobB.join()
    jobA.join()
    
    // Ejecutamos la función D después de que A, B y C hayan terminado
    asyncFunction("Función D", 1)
}