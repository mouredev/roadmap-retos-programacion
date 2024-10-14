import java.lang.IllegalArgumentException

open class exceptions(var numero1: Int) {
    open fun excep() {
        //Manejo de errores, try, catch, finally

        //en try se definen las instrucciones que se controlaran
        try {
            var numero2 = 0
            var resultado = numero1 / numero2
            //En catch se dedefinen las instrucciones a ejecutar en caso de excepcion, se puede controlar una serie de instrucciones por tipo de excepcion, o si se desean manejar todas las excepciones se puede dejar "Exception"
        } catch (excep: ArithmeticException) {
            println("(Mensaje especifico por tipo de error)No es posible realizar la division, no se puede dividir un numero entre 0, error -> $excep")
            //Es posible almacenar el mensaje de error mediante el parametro definido en el catch, en este caso es llamado "excep"
        } catch (excep: Exception) {
            println("(Mensaje  general para todas las excepciones)No es posible realizar la division, no se puede dividir un numero entre 0, error -> $excep")
            //Es posible definir varios catch con diferentes tipos de excepciones por si se desea controlarlos de forma diferente dependiendo del tipo de excepcion, pero se ejecutara el primer catch que cumpla con el tipo de error
            //En este caso se ejecutara el anterior, este no se lograra ejecutar
        } finally {
            println("Las instrucciones definidas en finally se ejecutan independientemente de si hubo un error o no")
        }

        //Ceracion de excepciones propias
        //El primer paso es crear una calse que herede de la clase Exceptions o de la clase de la excepcion especifica que necesitemos
        class excepcionPropia(mensaje: String) : Exception(mensaje) {
            fun showCustom() {
                println("Este es un mensaje personalizado de la excepcion personalizada")
            }
        }

        //try - catch con la excepcion personalizada
        try {
            println("Prueba de manejo de excepcion personalziada")
            //Con throw se puede generar el error si o si independientemente si las sentecias ejecutadas no lo generan, despues del throw se debe colocar el tipo de excepcion y el mensaje que rebotara, en este caso uso la excepcion creada
            throw excepcionPropia("Mensaje controaldo desde excepcion personalizada")
        } catch (excep: excepcionPropia) {
            println("A continuacion se mostrara un mensaje de ejemplo que viene desde la excepcion personalizada, se genera el siguiente mensaje de error desde la excepcion personalizada -> $excep")
            excep.showCustom()
        }
    }
}

//Ejercicio Extra
class customException(message: String): IllegalArgumentException(message) {
    fun showCustomMessage() {
        println("Se ha producido un error, este error se personaliza tomando como base el tipo de excepcion -> NumberFormatException")
    }
}

fun div(num1: Int?, num2: Int?): Int {

    if(num1 == 0 || num2 == 0){
        throw ArithmeticException()
    }else if(num1 == null || num2 == null){
        throw NullPointerException()
    }else if(num1 <0 || num2  <0){
        throw customException(message = "IllegalArgumentException generado de forma personalizada")
    }else{
        return num1/num2
    }

}

fun main() {
    var excepciones = exceptions(100)
    excepciones.excep()

    //Extra excution
    var res = 0
    try{
        res = div(1, 1)
    }catch(excep: ArithmeticException){
        println("Se ha producido un error de tipo aritmetico, el error producido fue -> $excep")
    }catch(excep: NullPointerException){
        println("Se ha producido un error al enviar un nulo, el error producido fue -> $excep")
    }catch(excep: customException){
        println("Se ha producido un error al enviar un string, el error producido fue -> $excep")
    }finally {
        println("Ejecuciones con exito")
    }

    if (res != 0){
        println("No han habido errores")
    }
}