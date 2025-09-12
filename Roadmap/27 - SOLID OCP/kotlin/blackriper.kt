@file:Suppress("UNCHECKED_CAST")

import java.util.UUID
import kotlin.math.pow

/*
Open Closed Principle

Este principio establece que una entidad de software (clase, módulo, función, etc)
debe quedar abierta para su extensión, pero cerrada para su modificación.

Con abierta para su extensión, nos quiere decir que una entidad de software debe tener la capacidad
de adaptarse a los cambios y nuevas necesidades de una aplicación, pero con la segunda parte de “cerrada
para su modificación” nos da a entender que la adaptabilidad de la entidad no debe darse
como resultado de la modificación del core de dicha entidad si no como resultado de un diseño
que facilite la extensión sin modificaciones.

*/

// ejemplo de lo que no debe hacerse

enum class AuthProviders{
    GOOGLE,
    FACEBOOK,
    GITHUB,
    APPLE
}

data class UserData(val userID:UUID,var name:String)


class AuthService{
     fun loginProvider(provider:AuthProviders):UserData{
         return when(provider){
             AuthProviders.GOOGLE-> signInWithGoogle()
             AuthProviders.FACEBOOK-> signInWithFacebook()
             AuthProviders.GITHUB-> signInWithGithub()
             AuthProviders.APPLE-> signInWithApple()
         }
     }

     private fun signInWithGoogle():UserData{
         return UserData(UUID.randomUUID(),"Google User")
     }

     private fun signInWithFacebook():UserData{
         return UserData(UUID.randomUUID(),"Facebook User")
     }

     private fun signInWithGithub():UserData{
         return UserData(UUID.randomUUID(),"Github User")
     }

     private fun signInWithApple():UserData{
         return UserData(UUID.randomUUID(),"Apple User")
     }
}

/* El Principio SOLID Open Closed se suele resolver utilizando polimorfismo,
 clases abstractas, herencia y interfaces en el ejemplo usando herencia*/

open class AuthProvider{
    open fun login():UserData{
        return UserData(UUID.randomUUID(),"User")
    }
}

// creamos los diferentes provedores
class GoogleProvider:AuthProvider(){
    override fun login():UserData{
        return UserData(UUID.randomUUID(),"Google User")
    }
}

class AppleProvider:AuthProvider(){
    override fun login():UserData{
        return UserData(UUID.randomUUID(),"Apple User")
    }
}

// refactorizamos la clase autService
class AuthProdService{
    fun loginProvider(provider:AuthProvider):UserData{
        return provider.login()
    }
}
// opcional crear singlenton
object ProvidersSinglenton{
    val apple=AppleProvider()
    val google=GoogleProvider()

}



fun exampleOpenClosed(){
    val authService = AuthService()
    val userData = authService.loginProvider(AuthProviders.GOOGLE)
    println(userData)
    // usando principio
    val authProd=AuthProdService()
    val userApple=authProd.loginProvider(ProvidersSinglenton.apple)
    val useGoogle=authProd.loginProvider(ProvidersSinglenton.google)
    println(userApple)
    println(useGoogle)
}

//ejercicio extra experimiento con genericos sustituir la T por el tipo que quieras
interface Operation{
    fun<T> execute(num1:T,num2:T):T
}
//crear clases de las operaciones borrar los ifs y solo dejar la suma
class Add:Operation{
    override fun <T> execute(num1: T, num2: T): T {
      if(num1 is Int && num2 is Int) return  (num1+num2) as T
      if (num1 is Double && num2 is Double) return (num1+num2) as T
      if (num1 is Float && num2 is Float) return (num1+num2) as T
      if (num1 is Long && num2 is Long) return (num1+num2) as T
      throw Exception("calculate type not supported")
    }

}

class Rest:Operation {
    override fun <T> execute(num1: T, num2: T): T {
        if (num1 is Int && num2 is Int) return (num1 - num2) as T
        if (num1 is Double && num2 is Double) return (num1 - num2) as T
        if (num1 is Float && num2 is Float) return (num1 - num2) as T
        if (num1 is Long && num2 is Long) return (num1 - num2) as T
        throw Exception("calculate type not supported")
    }
}

class Mul:Operation {
    override fun <T> execute(num1: T, num2: T): T {
        if (num1 is Int && num2 is Int) return (num1 * num2) as T
        if (num1 is Double && num2 is Double) return (num1 * num2) as T
        if (num1 is Float && num2 is Float) return (num1 * num2) as T
        if (num1 is Long && num2 is Long) return (num1 * num2) as T
        throw Exception("calculate type not supported")
    }
}

class Div:Operation {
    override fun <T> execute(num1: T, num2: T): T {
        if (num1 is Int && num2 is Int) return (num1 / num2) as T
        if (num1 is Double && num2 is Double) return (num1 / num2) as T
        if (num1 is Float && num2 is Float) return (num1 / num2) as T
        if (num1 is Long && num2 is Long) return (num1 / num2) as T
        throw Exception("calculate type not supported")
    }
}

class Calculate{
    fun <T>caculate(num1:T,num2:T,operation:Operation):T{
        if (num1 is Int && num2 is Int) return operation.execute(num1,num2)
        if (num1 is Double && num2 is Double) return operation.execute(num1,num2)
        if (num1 is Float && num2 is Float) return operation.execute(num1,num2)
        if (num1 is Long && num2 is Long) return operation.execute(num1,num2)
        throw Exception("calculate type not supported")
    }
}

// se cumple el principio open closed porque la clase operation puede ser extendida pero la
//clase calculate no puede ser extendida y no cambia su funcionamiento

class Pow:Operation{
    override fun <T> execute(num1: T, num2: T): T {
        if (num1 is Int && num2 is Int) return (num1.toDouble().pow(num2.toDouble())) as T
        if (num1 is Double && num2 is Double) return (num1.pow(num2)) as T
        if (num1 is Float && num2 is Float) return (num1.pow(num2)) as T
        if (num1 is Long && num2 is Long) return (num1.toFloat().pow(num2.toFloat())) as T
        throw Exception("calculate type not supported")
    }

}



// encapsular las operaciones en un singlenton para mayor comodidad opcional
object OperationSingleton{
    val add=Add()
    val rest=Rest()
    val mul=Mul()
    val div=Div()
    val pow=Pow()
}

fun calculatorExamples(){
    val calculator=Calculate()
    println("Add: "+calculator.caculate<Double>(2.5,2.5,OperationSingleton.add))
    println("Mul: "+calculator.caculate<Float>(2.5f,2.5f,OperationSingleton.mul))
    println("Div: "+calculator.caculate<Int>(2,2,OperationSingleton.div))
    println("Pow: "+calculator.caculate<Int>(2,2,OperationSingleton.pow))
}




fun main() {
    exampleOpenClosed()
    calculatorExamples()
}

