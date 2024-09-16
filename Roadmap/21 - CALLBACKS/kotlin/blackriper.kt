import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.time.delay
import java.time.Duration
import kotlin.random.Random

/*
 una funcion callback  es una funcion   que se pasa como parametro de otra funcion y
 que se ejecuta cuando la primera funcion termina de ejecutarse.

 los callback  pueden ser de dos tipos:
 -asincronos
 -sincronos

 Antes de la llegada del async  las callbacks eran muy utilizadas

 en kotlin  las callbacks se pueden simplificar usando las funciones lambda


*/

fun exampleWithCallback(callback:(Int)->Int){
    val numbers= listOf(1,2,3,4,5,6,7,8,9,10);
    numbers.forEach{
       println(callback(it))
    }
}

// ejercicio extra en este caso de forma  concurrente

suspend fun confirmOrder(dishName:String,duration:Long){
    println("start to order $dishName")
    delay(Duration.ofSeconds(duration))
}

suspend fun orderList(dishName:String,duration:Long){
    delay(Duration.ofSeconds(duration))
    println("order $dishName is ready ")
}

suspend fun deliverOrder(dishName:String,duration:Long){
    delay(Duration.ofSeconds(duration))
    println("order $dishName  is recived ")
}

// para no escribir un tipo muy largo podemos crear un tipo personalizado
typealias Callback =suspend (String,Long)->Unit

fun restaurantOrder(confirm: Callback, order:Callback, deliver:Callback){
   runBlocking {
       val random= Random.nextInt(1,10)
       confirm("pizza hawaina",random.toLong())
       order("pizza hawaina",random.toLong())
       deliver("pizza hawaina",random.toLong())
   }

}



fun main() {
    // pasando callback mediante lambda function
    exampleWithCallback { it*2 }
    // pasando callback forma tradicional omitiendo paramatros de la funcion por eso se usan de los ::
    restaurantOrder(::confirmOrder,::orderList,::deliverOrder)
}