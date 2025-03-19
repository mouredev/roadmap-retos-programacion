fun main(){

    //Punto #1 -> Explorar funciones

    //Funciones sin retorno y sin parametros locales
    fun interna(){
        println("Esta es la salida de una funcion sin parametros locales ni retornos")
    }

    //Funciones con parametros locales y sin retorno
    fun locales(loc: String){
        println("Esta es la salida de una funcion con parametros locales, dichos parametros se dan al momento de llamar la funcion, en este caso son: $loc")
    }

    //Funciones con parametros locales y retornos
    fun sum(num1: Int, num2:Int): Int{ //Despeus de los parentesis se debe poner el tipo de dato que retornara la funcion
        var res = num1 + num2
        println("Esta es una funcion que recibe 2 parametros y tiene un retorno, en este caso el retorno sera la suma de 2 numeros enteros osea: $res")
        return res
    }

    //Funciones anidadas
    fun div(num1:Int, num2:Int){
        var res = num1/num2
        println("Esta es la prueba de una funcion dentro de otr funcion, la primera funcion contiene esta salida de texto y hace una division entre 2 numeros recibidos, el resultado es: $res")
        fun residuo(val1: Double, val2: Double){
            var residuoDiv =  val1%val2
            println("Esta cadena de texto se imprime desde la funcion residuo la cual se encuentra dentro de la funcion div, esta funcion devuelve el residuo de la division de 2 numeros solicitados, en este caso el residuo es: $residuoDiv")
        }
        residuo(1.22, 0.2)
    }

    //Funciones ya creadas
    val texto: String = "Kotlin lang"
    val textoUpper: String = texto.toUpperCase() //Esta funcion cambia toda la cadena de texto a mayusculas
    val textoLength: Int = texto.length //Esta funcion nos da el largo de la cadena de texto
    println("Demostracion de uso de funciones existentes, Texto original: $texto, Texto en mayusculas: $textoUpper, Largo del Texto: $textoLength")

    //Variables locales y globales

    //Globales
    var global = "Esto es una variable global ya que no esta definida dentro de ninguna funcion ni hace parte de una funcion como prametro, se puede usar en toda la clase sin problema"
    println(global)

    //Locales
    fun variables(locales1: String){
        var locales2 = "Esto es una variable local, solo funcionara dentro de esta funcion, al igual que locales1 el cual es parametro de esta funcion solo funciona dentro de ella a diferencia que se debe definir siempre que se llame esta funcion"
        println("$locales1 y $locales2")
    }

    //Ejecucion de las funciones anteriores

    interna() //Ejecucion de funcion sin parametros ni retornos
    locales("esto es una funcion con parametros") //Ejecucion de funcion con parametros, de deben dar los parametros solicitados entre los parentesis
    var retornos = sum(5, 5) //Ejecucion de funcion con parametros y con retornos, se debe hacer en una variable para poder almacenar el retorno
    div(2, 3) //Ejecucion de funciones anidadas, se ejecuta la funcion principal que contine las demas funciones, las funciones anidadas solo se pueden ejecutar en dicha funcion, no fuera
    variables("Hola Local")

    //Ejercicio extra
    fun multiplos(multiplos3: String, multiplos5: String): Int{
        var contador: Int = 0
        for(i in 1..100){
            when{
                i%3 == 0 && i%5 == 0 -> println("$multiplos3, $multiplos5")
                i%3 == 0 -> println("$multiplos3")
                i%5 == 0 -> println("$multiplos5")
                else -> {
                    println("$i")
                    contador++
                }
            }
        }
        return contador
    }

    val resultado = multiplos("Multiplo de 3", "Multiplo de 5")
    println("Se imprimio $resultado veces el numero")
}