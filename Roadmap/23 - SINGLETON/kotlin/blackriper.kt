import java.util.UUID

/*
Los patrones de diseño son soluciones habituales a problemas que ocurren frecuentemente en el desarollo de software

estos de clasifican  en
 - patrones creacionales
 - patrones de comportamiento
 - patrones estructurales

Singleton
es un patron creacional que nos permite crear una  unica instancia de una clase. ala vez que nos proporciona acceso
a la instancia de la clase.

Como implementarlo

1.- Añadir un capmpo estatico ala clase para almacenar la instancia singlenton

2.- Crear un metodo estatico publico  que devuelva la instancia de la clase

3.- Implementa una inicialización diferida dentro del método estático.
 debe crear un nuevo objeto en su primera llamada y colocarlo dentro del campo estático.
 el método deberá devolver siempre esa instancia en todas las llamadas siguientes.

4.- Declara el constructor de clase como privado. El método estático de la clase
 seguirá siendo capaz de invocar al constructor, pero no a los otros objetos.

 para mas informacion sobre los patrones de diseño revisa https://refactoring.guru/design-patterns/singleton
*/


//implementando singleton

                    //paso 4
class Configuration private constructor(){
    private var theme = "dark"
    private var printer = "hp"
   //paso 2
    companion object {
        //paso 1
        private var instance: Configuration? = null

        //paso 3
        fun getInstance(): Configuration {
            if (instance == null) {
                instance = Configuration()
            }
            return instance!!
        }
    }
   fun getConfiguration() = "theme:$theme, printer:$printer"
}

// en kotlin hay una forma corta de crear una instancia singleton y esta es usando el keyword object

object Configuration2 {
    private var theme = "light"
    private var printer = "hp"
    fun getConfiguration() = "theme:$theme, printer:$printer"
}

// ejercicio extra

data class User(val id:UUID, val username:String, val name:String,val email:String)


class Session private constructor(){
   private  var userSession:User?=null
    companion object {
        private var instance: Session? = null
        fun getInstance(): Session {
            if (instance == null) {
                instance = Session()
            }
            return instance!!
        }
    }
    fun login(username:String ,name:String, email: String):User{
         userSession=User(UUID.randomUUID(),username,name,email)
        return userSession!!
    }

    fun logout() {
        userSession = null
        println("closing session")
    }
}



fun main() {
    // aunque se vuela a llamar el metodo getInstance  esta sera la misma instancia
    val config = Configuration.getInstance()
    println(config.getConfiguration())

    val config2 = Configuration.getInstance()
    println(config2.getConfiguration())

    println(config == config2)

    // forma abreviada del singlenton
    val config3 = Configuration2
    println(config3.getConfiguration())

    val config4 = Configuration2
    println(config4.getConfiguration())

    println(config3 == config4)

    // ejercicio extra
    val session= Session.getInstance()
    val user= session.login("blackriper","rodolfo","devgo@gmail.com")
    println(user)
    session.logout()


    val user2 = session.login("cisagroups","daniel","company@gmail.com")
    println(user2)
    session.logout()

}