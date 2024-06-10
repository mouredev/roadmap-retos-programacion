fun main() {
    val exampleSingleton = SingletonExample.instance
    val exampleSingleton2 = SingletonExample.instance
    exampleSingleton.str = "Soy otro ejemplo, mírame"
    println(exampleSingleton2.str)

    println("\n${"-".repeat(7)} EJERCICIO EXTRA ${"-".repeat(7)}")
    UserSession.setUser("rickjj97", "Rick", "mondongo@gmail.com")
    UserSession.showUser()
    UserSession.deleteUser()
    println(UserSession.user)
}

//le ponemos el constructor privado para que no pueda crear instancias. Se crean desde dentro
class SingletonExample private constructor() {
    var str = "Soy un ejemplo"

    //Un companion object es una forma de que otras clases puedan acceder a ésta sin tener un
    //objeto creado
    companion object {
        //by lazy hace que hasta que no se llame a la variable, ésta no se ejecutará, y
        //cuando la llamen, devolverá lo de dentro o hará lo que se especifique dentro
        val instance: SingletonExample by lazy { SingletonExample() }
    }
}

//un object es ya un objeto, una instancia que tiene el Singleton por detrás. Te hace el Singleton
object UserSession {
    private var username = ""
    private var name = ""
    private var email = ""
    val user = mutableListOf(chooseId(), username, name, email)

    private fun chooseId(): String {
        val numID = username.length * name.length * 123
        val id = "${numID}R"
        return id
    }

    fun setUser(user: String, name1: String, mail: String)  {
        username = user
        name = name1
        email = mail
    }

    fun showUser() {
        println("user ID: ${chooseId()}")
        println("username: $username")
        println("name: $name")
        println("email: $email")
    }

    fun deleteUser() {
        user.clear()
        println("Se han borrado los datos del usuario")
    }
}
