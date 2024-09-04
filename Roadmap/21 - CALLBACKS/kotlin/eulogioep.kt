import kotlinx.coroutines.*
import kotlin.random.Random

// Ejemplo simple de callback
fun operacionAsincrona(callback: (String) -> Unit) {
    Thread {
        Thread.sleep(2000) // Simula una operación que tarda 2 segundos
        callback("Operación completada")
    }.start()
}

// Simulador de pedidos de restaurante
fun procesarPedido(
    nombrePlato: String,
    confirmarPedido: () -> Unit,
    platoProcesado: () -> Unit,
    platoEntregado: () -> Unit
) {
    println("Procesando pedido: $nombrePlato")
    confirmarPedido()
    
    runBlocking {
        delay(Random.nextLong(1000, 10001)) // Tiempo aleatorio entre 1 y 10 segundos
        platoProcesado()
        
        delay(Random.nextLong(1000, 10001))
        platoEntregado()
    }
}

fun main() {
    println("Ejemplo simple de callback:")
    operacionAsincrona { resultado ->
        println(resultado)
    }
    
    Thread.sleep(3000) // Espera para que se complete la operación asíncrona
    
    println("\nSimulador de pedidos de restaurante:")
    procesarPedido(
        "Pizza Margherita",
        { println("Pedido confirmado: Pizza Margherita") },
        { println("Pizza Margherita está lista") },
        { println("Pizza Margherita ha sido entregada") }
    )
}