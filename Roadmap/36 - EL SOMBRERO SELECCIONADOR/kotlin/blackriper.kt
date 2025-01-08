import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.transform
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlin.jvm.optionals.toList

//1.- definir estructuras de datos y mock de datos

enum class School{
    FRONTEND, BACKEND, MOBILE, DATA
}

typealias Option= Pair<String,School>

data class Question constructor(var text:String="", var options:List<Option> = emptyList())

fun question(block: Question.()->Unit):Question= Question().apply(block)


data class Magician constructor(val name: String="", var frontend:Int=0, var backend:Int=0, var mobile:Int=0, var data:Int=0)


val quetions= listOf(
   question {
      text="¿Que parte del desarrollo de software llama mas tu atencion?"
      options= listOf(
         "Diseño de interfaces UX" to School.FRONTEND,
         "Diseño de Api para la consulta de datos " to School.BACKEND,
         "Diseño de la base de datos " to School.DATA,
         "Diseño de la interfaz de usuario mediante codigo o xml " to School.MOBILE
      )
   },
   question {
       text="¿Es de tu interes la gestión de servidores y la arquitectura de sistemas?"
       options= listOf(
           "Si totalmente " to School.BACKEND,
           "No prefiero el diseño UX para web " to School.FRONTEND,
           "No me interesa  esa parte prefiero trabajar con los datos de estos servidores" to School.DATA,
           "Prefiero diseñar apps para dispositivos moviles" to School.MOBILE
       )
   },
   question {
       text="Qué lenguaje de programación dominas mejor actualmente"
       options= listOf(
           "JavaScript/TypeScript" to School.FRONTEND,
           "Go/Java/Python" to School.BACKEND,
           "Kotlin/Swift" to School.MOBILE,
           "C/C++/Scala" to School.DATA
       )
   },
   question {
     text="¿Qué frameworks o herramientas dominas o te gustaria aprender mas ?"
     options= listOf(
         "React/express/Vue/Angular" to School.FRONTEND,
         "Gin/Spring boot/FastApi" to School.BACKEND,
         "Jetpack Compose/SwiftUI" to School.MOBILE,
         "Spark Mlib,NumPy" to School.DATA
     )
   },
   question {
       text="¿Es de tu interes el manejo de altos volumenes de datos?"
       options= listOf(
           "No me interesa" to School.FRONTEND,
           "Me interesa un poco pero uso librerias como Room para gestionar su manejo" to School.MOBILE,
           "Me interesa solo el acceso y proteccion de como los datos son guardados" to School.BACKEND,
           "Me interesa su manejo y la optimizacion de algoritmos" to School.DATA
       )
   },

   question {
       text="¿Qué plataforma es mas de tu preferencia ?"
       options= listOf(
           "Windows" to School.FRONTEND,
           "Linux" to School.BACKEND,
           "Android/IOS" to School.MOBILE,
           "Me da igual prefiero el trabajo con la data" to School.DATA
       )
   },

  question {
      text="¿Haz escuchado alguno de los siguientes conceptos?"
      options= listOf(
          "Css,Html,async/await" to School.FRONTEND,
          "Http/Jwt/Cors/concurrencia" to School.BACKEND,
          "Intents/xml/permissions" to School.MOBILE,
          "Pandas/bigdata" to School.DATA
      )
  },
  question {
      text="¿Manejas algun administrador de dependencias?"
      options= listOf(
          "Npm,bun,yarn" to School.FRONTEND,
          "Pip,maven,go" to School.BACKEND,
          "Swift package manager,gradle" to School.MOBILE,
          "Ninguna de las anteriores" to School.DATA
      )
  },

 question {
     text="¿Eres habil con el diseño?"
     options= listOf(
         "Si pero me acomodo hacerlo con Css o algun framework" to School.FRONTEND,
         "Si pero me gusta hacerlo con codigo o Xml " to School.MOBILE,
         "No es de mi interes prefiero las cosas que pasan por detras de la vision" to School.BACKEND,
         "No prefiero el modelo de datos" to School.DATA
     )
 },

 question {
     text="¿Cuanto dinero aspiras a ganar cuando te conviertas en un hechicero del ministerio?"
     options= listOf(
         "$ 60 K" to School.FRONTEND,
         "$ 80 K" to School.BACKEND,
         "$ 75 K" to School.MOBILE,
         "$ 100 K" to School.DATA
     )
 }
)

// 2.- definir funcioneamiento  del sombrero

interface  Sorting{
    fun registerMagician()
    fun evaluteAnswer(answer: String,options: List<Option>)
    fun printResult()
}

// 3.- Implementar clases

class Hat: Sorting{
    private lateinit var magician:Magician

    override fun registerMagician() {
       println("¿cual es tu nombre aspirante ?")
       val name = readLine()?.let { it.toString() } ?: ""
       magician = Magician(name)
    }

    override fun evaluteAnswer(answer: String, options: List<Option>) {
        val  school = options.first { it.first == answer }.second
        magician.apply {
            when (school) {
                School.FRONTEND -> frontend++
                School.BACKEND -> backend++
                School.MOBILE -> mobile++
                School.DATA -> data++
            }
        }
    }

    override fun printResult() {
      val scores= listOf(
          School.FRONTEND to magician.frontend,
          School.BACKEND to magician.backend,
          School.MOBILE to magician.mobile,
          School.DATA to magician.data
      )
      val numSchool= scores.count { it.second==scores.maxOf { it.second } }

      if (numSchool>1){
          val winners= scores.filter { it.second==scores.maxOf { it.second } }
          val winner=winners.random().first
          println("La decisión fue complicada pero tu casa aspirante ${magician.name} es ${winner.name.capitalizeWord()}")
      }

       if (numSchool==1){
           val winner= scores.first { it.second==scores.maxOf { it.second } }.first
           println("Tu casa aspirante ${magician.name} es ${winner.name.capitalizeWord()}")
       }

    }


}
context(Sorting)
suspend fun startSelection():Unit= coroutineScope{
    registerMagician()
    for (question in quetions) {
        println(question.text)
        var ind=1
        question.options.forEach {
            println("$ind.- ${it.first}")
            ind++
        }
        val option= readLine()?.let { it.toInt() } ?: 0
        evaluteAnswer(question.options[option-1].first,question.options)
    }
    printResult()
}

fun main()= runBlocking {
   val job= launch {
       with(Hat()){
           var option = ""
           while (option != "N") {
               startSelection()
               println("¿Deseas registrar una nuevo aspirante Y/N?")
               option = readLine()?.let { it.uppercase() } ?: "N"
           }
       }
   }
   job.join()
}

