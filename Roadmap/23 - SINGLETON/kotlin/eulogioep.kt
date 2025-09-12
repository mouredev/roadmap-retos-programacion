// Ejemplo genérico de Singleton
object Singleton {
    init {
        println("Singleton inicializado")
    }
    
    fun doSomething() {
        println("Singleton está haciendo algo")
    }
}

// Ejemplo de la dificultad extra: Sesión de usuario
object UserSession {
    private var userId: Int? = null
    private var username: String? = null
    private var name: String? = null
    private var email: String? = null

    fun setUser(id: Int, username: String, name: String, email: String) {
        this.userId = id
        this.username = username
        this.name = name
        this.email = email
        println("Usuario asignado a la sesión")
    }

    fun getUserData(): Map<String, Any?> {
        return mapOf(
            "id" to userId,
            "username" to username,
            "name" to name,
            "email" to email
        )
    }

    fun clearSession() {
        userId = null
        username = null
        name = null
        email = null
        println("Sesión borrada")
    }
}

fun main() {
    // Uso del Singleton genérico
    println("Usando el Singleton genérico:")
    Singleton.doSomething()
    Singleton.doSomething()

    println("\nUsando el UserSession:")
    // Uso del UserSession
    UserSession.setUser(1, "eulogioep", "Eulogio EP", "eulogioep@ex.com")
    println("Datos del usuario: ${UserSession.getUserData()}")
    UserSession.clearSession()
    println("Datos después de borrar: ${UserSession.getUserData()}")
}