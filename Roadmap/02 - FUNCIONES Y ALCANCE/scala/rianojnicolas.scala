import scala.util.Random

object Main {
    def main(args: Array[String]): Unit = {
        // Variable Global
        var varGlobal = "Muchos Exitos, y que tenas un buen día"

        // Funciones:
        // Funcion sin parametros ni retorno
        def welcomePlayer(): Unit = {
            println("""
        Hola People !!, este es un juego improvisado de
        piedra, papel o tijera.
        
        las reglas son las siguientes:
        """)
        // Funcion dentro de otra funcion
            def reglas(): Unit = {
                print("""
            1. Debes ingresar el objeto con el que jugaras
            2. El pc elegira aleatoriamente un objeto
            3. Recuerda que: papel le gana a piedra,
                            piedra le gana a tijera,
                            tijera le gana a papel.
            
            Muchos Exitooooss !!!
            """)
            }
            reglas()
        }


        // Funcion sin parametros con retorno   
        // Funcion para pedir el objeto a jugar
        def functionInput(): String = {
            println("Ingresa tu objeto con el que vas a jugar: ")
            var option = scala.io.StdIn.readLine()
            while(option != "piedra" && option != "tijera" && option != "papel"){
                println("Ingresa tu objeto con el que vas a jugar: ")
                option = scala.io.StdIn.readLine()
            }
            return option
        }


        // (Funcion con un parametro y sin retorno)
        // Funcion competencia
        def playCompetition(optionPlayer:String): Unit = {
            // Concepto de Variable Local
            val optionList = List("piedra", "papel", "tijera")
            var optionPC = Random.shuffle(optionList).head
            println(s"la opcion del pc fue: $optionPC \n")
            if (optionPC == optionPlayer) {
                println("Emptados")
            }
            else if (optionPC == "papel") {
                if (optionPlayer == "piedra") {
                    println("perdiste")
                }
                else if(optionPlayer == "tijera") {
                    println("ganaste")
                }
            }
            else if (optionPC == "tijera") {
                if (optionPlayer == "papel") {
                    println("perdiste")
                }
                else if (optionPlayer == "piedra") {
                    println("ganaste")
                }
            }
            else if (optionPC == "piedra") {
                if (optionPlayer == "papel") {
                    println("ganaste")
                }
                else if (optionPlayer == "tijera") {
                    println("perdiste")
                }
            }
        }

        def run(): Unit = {
            welcomePlayer()
            println(varGlobal)
            var option_player = functionInput()
            playCompetition(option_player)
        }
        
        run()

        /*
        DIFICULTAD EXTRA
        */
        println("*---------------------------------*")
        println("*       DIFICULTAD EXTRA          *")
        println("*---------------------------------*")

        def extraDifficult(param1: String, param2: String): Float = {
            var contador = 0
            for (i <- 0 to 101) {
                if (i%3 == 0 && i%5 == 0) {
                    println(s"para el numero $i: $param1 $param2")
                }
                else if(i%3 == 0) {
                    println(s"para el numero $i: $param1")
                }
                else if(i%5 == 0) {
                    println(s"para el numero $i: $param2")
                }
                else {
                    contador += 1
                    println(s"para el numero $i no hay texto")
                }
            }
            return contador
        }

        println("\nAhora vamos con el ejercicio extra\n")
        println(extraDifficult("hola", "mundo"))
    }
}