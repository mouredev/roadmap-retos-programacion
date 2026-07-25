import java.time.LocalDateTime
import java.time.Duration

// Concepto de LOGS (Logging):
// Los logs son registros de eventos que ocurren durante la ejecución de un programa.
// Son cruciales para el diagnóstico de problemas, monitoreo del rendimiento y
// seguimiento de la actividad del sistema. En este ejemplo, implementaremos
// un sistema de logging simple para evitar problemas de permisos.

// Enum para los niveles de log
enum class LogLevel {
    INFO, WARNING, ERROR, DEBUG, TRACE
}

// Clase simple para manejar logging
class SimpleLogger(private val name: String) {
    fun log(level: LogLevel, message: String) {
        println("${LocalDateTime.now()} [$level] $name: $message")
    }

    fun info(message: String) = log(LogLevel.INFO, message)
    fun warning(message: String) = log(LogLevel.WARNING, message)
    fun error(message: String) = log(LogLevel.ERROR, message)
    fun debug(message: String) = log(LogLevel.DEBUG, message)
    fun trace(message: String) = log(LogLevel.TRACE, message)
}

class TaskManager {
    private val logger = SimpleLogger(TaskManager::class.java.simpleName)
    private val tasks = mutableListOf<Task>()

    fun addTask(name: String, description: String) {
        val startTime = LocalDateTime.now()
        logger.info("Iniciando añadir tarea: $name")
        
        tasks.add(Task(name, description))
        
        val endTime = LocalDateTime.now()
        val duration = Duration.between(startTime, endTime)
        logger.info("Tarea añadida: $name. Tiempo de ejecución: ${duration.toMillis()} ms")
    }

    fun removeTask(name: String) {
        val startTime = LocalDateTime.now()
        logger.warning("Iniciando eliminación de tarea: $name")
        
        val removed = tasks.removeIf { it.name == name }
        if (removed) {
            logger.info("Tarea eliminada: $name")
        } else {
            logger.error("No se encontró la tarea: $name")
        }
        
        val endTime = LocalDateTime.now()
        val duration = Duration.between(startTime, endTime)
        logger.debug("Tiempo de ejecución para eliminar tarea: ${duration.toMillis()} ms")
    }

    fun listTasks() {
        val startTime = LocalDateTime.now()
        logger.info("Listando todas las tareas")
        
        tasks.forEach { task ->
            logger.debug("Tarea: ${task.name}, Descripción: ${task.description}")
        }
        
        val endTime = LocalDateTime.now()
        val duration = Duration.between(startTime, endTime)
        logger.trace("Tiempo de ejecución para listar tareas: ${duration.toMillis()} ms")
    }
}

data class Task(val name: String, val description: String)

fun main() {
    val taskManager = TaskManager()

    // Ejemplos de uso con diferentes niveles de severidad
    taskManager.addTask("Comprar víveres", "Ir al supermercado y comprar alimentos")
    taskManager.addTask("Hacer ejercicio", "30 minutos de cardio")
    taskManager.listTasks()
    taskManager.removeTask("Hacer ejercicio")
    taskManager.removeTask("Tarea inexistente")
    taskManager.listTasks()
}