import io.github.oshai.kotlinlogging.KotlinLogging


/*
Logs
Los logs son mensajes que sirven como historial de eventos sucedidos en la aplicacion
estos sirven para informar  a los desarrolladores sobre diferentes eventos que ocurren en la aplicacion

los logs se clasifican en
- Debug
- Trace
- Info
- Warning
- Error

como sus nombres los indican estos  son eventos que ocurren en la aplicacion al clasficarlos
tambien se les puede dar prioridad esto ayuda a configurar parametros para dar a conocer a los
desarrolladores eventos que ocurren en la aplicacion. por lo general los Error tienen mayor prioridad

depedencias
https://github.com/oshai/kotlin-logging logger
https://mvnrepository.com/artifact/org.slf4j/slf4j-api depedencia padre
https://mvnrepository.com/artifact/ch.qos.logback/logback-classic/1.5.6  formateo y prioridada de los logs
https://github.com/Tuxdude/logback-colorizer dar color a los logs opcional pero quedan bonitos con colores

archivo basico de formatos de logs src/main/resources/logback.xml
    <property scope="context" name="COLORIZER_COLORS" value="red@,yellow@,green@,blue@,cyan@" />
    <conversionRule conversionWord="colorize" converterClass="org.tuxdude.logback.extensions.LogColorizer" />
    <appender name="STDOUT" class="ConsoleAppender">
        <encoder class="PatternLayoutEncoder">
            <pattern>%colorize(%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} -- %msg%n) </pattern>
        </encoder>
    </appender>

    <root level="trace">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>

tutorial basico
https://saltnlight5.blogspot.com/2013/08/how-to-configure-slf4j-with-different.html

 */

val logger= KotlinLogging.logger {  }

fun exampleWithLogs() {
    // probando alguna funcion
    logger.debug { "debug message" }
    // seguimientos de eventos en la aplicacion conexion de base de datos etc
    logger.trace { "trace message" }
    // informamos sobre  cosas que ocurren en la aplicacion
    logger.info { "info message" }
    // informamos sobre eventos que podrian generar error en caso de no atederse
    logger.warn { "warn message" }
    // informamos sobre eventos  de error en la aplicacion
    logger.error { "error message" }
}

// ejercicio extra
data class Task(val name:String,val description:String,var done:Boolean=false)

interface TaskRepository{
    fun save(task:Task)
    fun delete(name:String)
    fun completedTask(name: String)
    fun getAll():List<Task>
    fun getTaskBy(predicate:(Task)->Boolean):List<Task>
}

class TaskManager:TaskRepository{
    private val tasks= mutableListOf<Task>()
    override fun save(task: Task) {
        logger.trace { "new task recived for add list" }
        val registred=tasks.add(task)
        if(registred) logger.info { "task ${task.name} was added to the list" }
     }

    override fun delete(name: String) {
       logger.trace { "task $name recived for deleted" }
       val deleted=tasks.removeIf { it.name==name }
       if(deleted) logger.info { "task $name was deleted" }
       else logger.error { "task $name not found" }
    }

    override fun completedTask(name: String) {
        logger.trace { "task $name recived for completed" }
        tasks.find { it.name==name }.let {
            if (it==null) logger.warn {"task name is null value"  }
            it?.done=true
            logger.info { "task $name was completed" }
        }
    }

    override fun getAll(): List<Task> {
        logger.trace { "get all tasks" }
        return tasks
    }

    override fun  getTaskBy(predicate: (Task) -> Boolean): List<Task>{
        logger.trace {"find task with predicate"}
        return tasks.filter { predicate(it) }
    }

}



fun main() {
    exampleWithLogs()
    val task1=Task("Clean my room","clean my room")
    val task3=Task("migration","migrate maven to kotlin dsl")
    val task4=Task("solution for programming roadmap","create a solution for programming roadmap")
    val manager=TaskManager()
    manager.save(task1)
    manager.save(task3)
    manager.save(task4)
    manager.delete("migration")
    manager.completedTask("Clean my room")
    manager.getAll().forEach { println(it) }
    manager.getTaskBy { it.done==true }.forEach { println(it) }

}