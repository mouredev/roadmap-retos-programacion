import kotlin.random.Random

// estados de los caracteres
enum class CharacterStatus{
    CORRECT,PRESENT,INCORRECT
}

class LongitudException(override val message: String): Exception(message)


// generar password de la bodega
fun generatePassword(): String {
    var password = ""
    while (true) {
        val character = (if (Random.nextBoolean()) (1..3).random() else listOf("A", "B", "C").random()).toString()
        if (password.contains(character)) continue
        else password += character

        if (password.length==4) break
    }
 return password
}

//manejar las contraseñas introduccidas por el usuario
class DadNoelStorage(generator:()-> String){
    private var password=""
    private val regex = Regex("^[A-C1-3]+$")

    init {
        password=generator()
    }

   private  fun evaluateUserPassword(passCha: Char,position: Int):CharacterStatus{
        if (password.contains(passCha) && password[position] ==passCha) return CharacterStatus.CORRECT
        if (password.contains(passCha) && password[position] !=passCha) return  CharacterStatus.PRESENT
        return CharacterStatus.INCORRECT
    }

    private fun validatePassword(pass: String) = runCatching{
      if (regex.matches(pass).not())
          throw IllegalArgumentException("el password solo puede contener numeros del 1 al 3 y letras de la A la C")

      if (pass.length>4) throw LongitudException("el password solo puede tener una longitud de 4 caracteres")

      return@runCatching pass
    }

    private fun findAndShow(userPass: String){
        var ind=0
        for (ch in userPass){
            val result=evaluateUserPassword(ch,ind)
            when(result){
                CharacterStatus.CORRECT -> println("el caracter $ch es correcto")
                CharacterStatus.PRESENT -> println("el caracter  $ch es parte de la contraseña pero no esta en la posicion correcta")
                CharacterStatus.INCORRECT ->println("el caracter $ch no es parte de la contraseña ")
            }
            ind++
        }
     }




    fun questionPasswordStorage(){
        var intents=1
        while (true){
            println("introduce la contraseña del almacen ")
            val userPass= readLine()!!.uppercase()
            val valid=validatePassword(userPass)
            if (valid.isFailure){
                println("passowrd erroneo porque ${valid.exceptionOrNull()?.message}")
                continue
            }
            if (valid.isSuccess){
                 findAndShow(valid.getOrDefault("234"))
                 println("$intents/10 intentos")
                 intents++

                if (password==valid.getOrNull()){
                    println(" contraseña correcta bienvenido santa")
                    break
                }

                if (intents==10) {
                    println("has agotado tus 10 intentos has perdido")
                    break
                }
            }
        }

    }


}






fun main() {
    val storage=DadNoelStorage(::generatePassword)
    storage.questionPasswordStorage()
}