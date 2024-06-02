fun main() {

    println("------------ APARTADO 1 ------------")

    println("--Class functionsNotReturn--")
    //Instance functionsNotReturn
    val instance1 = functionNotReturn()

    print("notParameterNotReturn -> ")
    instance1.notParametersNotReturn()

    print("parameterNotReturn -> ")
    instance1.parameterNotReturn("nameExample")

    print("parametersNotReturn -> ")
    instance1.parametersNotReturn(
        "nameExample",
        "lastnameExample",
        17
    )


    println("--Class functionsWithReturn--")
    //Instance functionWithReturn
    val instance2 = functionWhitReturn()

    println("notParameterReturn -> " + instance2.notParameterReturn())
    //Function only with a parameter and return
    println(
        "parameterReturn -> " +
                instance2.parameterReturn("nameExample")
    )
    //Function with very parameter and return
    println(
        "ParametersReturn -> " +
                instance2.parametersReturn(
                    "nameExample",
                    "lastnameExample",
                    17
                )
    )

    println("--Other--")
    print("parameterDefault -> ")
    parameterDefault()

    val resultALineExpression = aLineExpression()
    println("aLineExpression -> $resultALineExpression")

    val resultFunctionAnonymusLambda = functionAnonymusLambda(
        "nameExample"
    )
    println(
        "functionAnonymusLambda -> " +
                resultFunctionAnonymusLambda
    )

    val resultfunctionAnonymusLambdaParameters =
        functionAnonymusLambdaParameters(
            "nameExample",
            "lastnameExample",
            17
        )
    println(
        "functionAnonymusLambdaParameters -> " +
                resultfunctionAnonymusLambdaParameters
    )

    println("--higherOrderFunctions--")

    val name = "nameExample"
    val higherOrder = higherOrderFunctions()

    //Funcion de orden superior (recibe otra funcion como parametro)
    print("higherOrderWhithOtherFuncion -> ")
    higherOrder.higherOrderWhithOtherFuncion(
        name,
        higherOrder.greetingFuntion
    )

    //funcion de orden superior con retorno de funcion
    val returnString: (String) -> String = higherOrder.higherOrderReturn()
    val otherString = returnString("nameExample")
    println(otherString)

    print("Function Extension String -> ")
    val nameExtension = "exampleName"
    nameExtension.xd()

    print("Fuction extension Int -> ")
    val number1: Int = 3
    println(number1.addition(3))


    println("Funcion infix -> $resultado")

    print("Funcion con un numero variable de argumento -> ")
    printall("Hola", "Mundo")


    print("Llamado a la funcion inline (NO inflacion) -> ")
    inlineFunction {
        println("Hola")
    }

    print("Funcion local (definida dentro de otra funcion ->" )
    outerFunction()


    println ("----------DICULTAD EXTRA----------")
    println (prueba("multiplo3", "multiplo5"))


}



class functionNotReturn(){

    // funcion sin parametros sin retorno
    fun notParametersNotReturn(){
        println("nameExample")
    }

    // Funcion con un solo parametro sin retorno
    fun parameterNotReturn(name: String){
        println("Hola $name")
    }

    // Funcion con muchos parametros sin retorno
    fun parametersNotReturn(name: String, lastname: String, age: Int){
        println("Hola $name $lastname, tu edad es $age")
    }

}

class functionWhitReturn(){

    //Funcion sin parametro con retorno
    fun notParameterReturn(): String {
        return ("Hola Mundo")
    }

    //funcion con solo un parametro con retorno
    fun parameterReturn(name: String): String{
        return (name)
    }

    //Funcion con muchos parametro con retorno
    fun parametersReturn(
        name: String,
        lastname: String,
        age: Int): String{
        return ("Hola $name $lastname, tu edad es de $age")
    }


}

fun parameterDefault(
    name: String ="nameExample",
    age: Int = 17){
    println("Hola $name, tu edad es $age")
}

fun aLineExpression (name:String = "nameExample") = "Hola $name"

val functionAnonymusLambda = {name: String -> "Hello $name"}

val functionAnonymusLambdaParameters = {
        name: String,
        lastname: String,
        age: Int -> "Hola $name $lastname, tu edad es $age"}






class higherOrderFunctions(){

    val greetingFuntion: (String) -> String = {
            input -> "Hola, welcome"
    }

    fun higherOrderWhithOtherFuncion (
        name: String,
        greetingFuntion: (String) -> String
    ){
        println(greetingFuntion(name))
    }

    fun higherOrderReturn(): (String) -> String{
        return {name -> "Hello, $name"}
    }

}


fun String.xd(){
    println("Hello, $this")
}

// Define an extension function for Int class
fun Int.addition(number: Int): Int {
    return this * number
}


infix fun Int.times(str: String) = str.repeat(this)

val resultado = 3 times "hola"


fun printall (vararg texto: String){
    for (message in texto) println (message)
}


inline fun inlineFunction(block: () -> Unit) {
    block()
}


fun outerFunction() {
    fun innerFunction() {
        println("This is an inner function.")
    }
    innerFunction()
}


fun prueba(texto1:String, texto2: String): Int {

    var contadorNumberPrint = 0

    for (i in 1..100) {
        when {
            i % 3 == 0 && i % 5 == 0 -> println(texto1 + texto2)
            i % 3 == 0 -> println(texto1)
            i % 5 == 0 -> println(texto2)
            else -> {
                println(i)
                contadorNumberPrint++
            }

        }
    }
    return (contadorNumberPrint)

}


