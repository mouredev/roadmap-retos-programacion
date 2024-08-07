
/*
 los Exception son una opcion de manejo de error que se puede producir en un programa
 esto nos ayuda a capturar el error para saber posibles causas y poder solucionarlo asi
 como saber que acciones reaizar cuando se produce el mismo.

 En kotlin  todas las excepciones son una subclase de la clase Throwable, cada excepcion
 contine  un mensaje que describe la excepcion  un stackTrace  y un opcional cause.

 ejemplo de manejo de excepciones
        try {
            // some code
        } catch (e: SomeException) {
            // handler
        } finally {
            // optional finally block
        }
para crear una excepcion se crear una clase  de la clase Exception
class MyException(message: String) : Exception(message)

 */

fun exception() {
    try {
        val c = 10 / 0
    } catch (e: Exception) {
        println("Error: ${e.message}")
    }
}

fun exceptionWithSpecificCause() {
    try {
        val c = 10 / 0
    } catch (e: ArithmeticException) {
        println("Error: ${e.message}")
    }
}

fun exceptionWithCustomError(){
    try {
        val c = 10 / 0
    } catch (e: ArithmeticException) {
       println( Error("Division by zero is invalid").message)
    }
}
// ejercicio extra

fun parseInt(s:String?){
   try {
       val n=notNull(s)
       println("No errors detected")
       println("The number is ${n.toInt()}")
   }catch (e:NumberNullException){
       println(e.message)
   }catch (e: NumberFormatException){
       println(e.message)
   }catch (e:ClassCastException){
       println(e.message)

   }finally {
       println("Execution finished")
   }

}

fun notNull(s:String?):String{
    if (s== null){
        throw NumberNullException("s is null")
    }
    return s
}

class NumberNullException(message: String) : Exception(message)


fun main() {
    // ejemplo de manejo de excepciones
    exception()
    exceptionWithSpecificCause()
    exceptionWithCustomError()
    //ejercicio extra
    println("Prueba 1")
    parseInt("10")
    println("Prueba 2")
    parseInt(null)

}