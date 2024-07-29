fun main() {
    //Uso incorrecto
    class Worker(val name: String) {
        fun toWork() = "Soy $name y estoy trabajando"
    }

    class Proyect(val nameProyect: String) {
        fun workinProyect(): String {
            val workerName = Worker("John")
            return "${workerName.name} está trabajando en $nameProyect"
        }
    }
    val proy = Proyect("Google")
    println(proy.workinProyect())
    /*
    Aquí incumplimos el DIP porque vemos que el proyecto depende del trabajador, y si cambiara el trabajador
    el proyecto se rompe, y eso no debe ocurrir
     */

    //Uso correcto
    abstract class Department {
        abstract fun work(): String
    }

    class Employee(val name: String): Department() {
        override fun work() = "Soy $name y estoy trabajando"
    }

    class Project(val project: String): Department() {
        override fun work() = "El departamento está trabajando en $project"
    }
    val emp = Employee("John")
    println(emp.work())
    val proj = Project("BushiGPT")
    println(proj.work())
    /*
    Aquí sí se cumple porque depende de una interfaz, algo abstracto, y si cambia tendrá que
    cambiar en todas sus implementaciones
     */

    println("\n ${"*".repeat(7)} EJERCICIO EXTRA ${"*".repeat(7)}")
    class Email: SendNotif {
        override fun sendNotification(user: String): String {
            print("Para: ")
            val dest = readln()
            print("Asunto: ")
            val subject = readln()
            print("Mensaje: ")
            val text = readln()

            return "from: $user \nto: $dest\nasunto: $subject\n $text"
        }
    }

    class Push: SendNotif {
        override fun sendNotification(user: String): String {
            print("Mensaje: ")
            val text = readln()

            return "@$user\n $text"
        }
    }

    class SMS: SendNotif {
        override fun sendNotification(user: String): String {
            print("Mensaje: ")
            val text = readln()

            return "to: $user\n $text"
        }
    }

    fun sendMessage() {
        println("¿Qué tipo de notificación quieres mandar?\n" +
                "1.- Correo\n" +
                "2.- Notificación Push\n" +
                "3.- SMS")
        val option = readln().toInt()

        when (option) {
            1 -> println(Email().sendNotification("ejemplo@prueba.com"))
            2 -> println(Push().sendNotification("TipodeIncognito"))
            3 -> println(SMS().sendNotification("123456789"))
        }
    }
    sendMessage()
}

interface SendNotif {
    fun sendNotification(user: String): String
}
