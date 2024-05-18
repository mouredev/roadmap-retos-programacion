class numeroGrandes(message: String): Exception(message)


fun main(){

    /*APARTADO 1 */


    /*VARIABLES UTILS*/
    val numero1: Int = 12
    val numero2: Float = 12.32f
    val numero3: Double = 90.3
    var myBoolean: Boolean = false



    println ("----------- ALL OPERADORES ARIMETICOS -----------")

    //Operador aritmetico suma
    val suma = numero1 + numero2

    //Operador aritmetico resta
    val resta = numero1 - numero2

    //Operador aritmetico multiplicacion
    val multiplicacion = numero1 * numero2

    //Operador aritmetico division
    val division = numero1 / numero2

    //Operador aritmetico modulo
    val modulo = numero1 % numero2

    println ("Operador aritmetico de suma: $numero1 + $numero2 = $suma")
    println ("Operador aritmetico de resta: $numero1 - $numero2 = $resta")
    println ("Operador aritmetico de multiplicacion: $numero1 * $numero2 = $multiplicacion")
    println ("Operador aritmetico de division: $numero1 / $numero2 = $division")
    println ("Operador aritmetico de modulo: $numero1 % $numero2 = $modulo")

    println ()

    println ("----------- ALL OPERADORES LOGICOS -----------")


    /* Operador (or) || -  Operador (diferente que) !=*/
    if (numero1 == 12 || numero1.toFloat() != numero2) {
        println ("La variable $numero1 es igual a 12 y $numero2 es diferente de 12")
    }

    /*Operador (diferente que) != - Operador (Y) && */
    if (numero1.toDouble() != numero3 && numero2 < numero3){
        println ("La variable $numero1 es diferentes de la variable $numero3 y la variable $numero2 es menor que la variable $numero3")
    }

    println ("Actualmente el valor de la variable es: $myBoolean")
    if (!myBoolean){ // Si myBoolean es false, entonces !myBoolean es true
        println ("Si negamos la variable -> ${!myBoolean}")
    }else{ // Si myBoolean es true, entonces !myBoolean es false
        println ("Si no negamos la variable -> ${!myBoolean}")
    }


    println()


    println ("----------- ALL OPERADORES COMPARACION -----------")

    /* Operador igual que*/
    println ("Operador igual que: $numero1 == 12")

    /*Operador diferente de*/
    println ("Operador diferente de $numero1 != $numero2")

    /*Opoerador menor o igual que*/
    println ("Operador menor o igual que: $numero1 <= $numero2")

    /*Operador mayor o igual que*/
    println ("Operador mayor o igual que: $numero1 >= $numero2")


    println()


    println ("----------- ALL OPERADORES DE ASIGNACION -----------")

    /*declaracion de variables*/
    var x: Double = 15.2
    var y: Float = 1.1f

    //Asignacion simple
    x = y.toDouble()
    println("Asignacion simple: x = y.toDouble() -> $x")

    //Adiccion o sumna
    x += y.toDouble()
    println("Adiccion o suma: x += y.toDouble() -> $x")

    //Adiccion o resta
    x -= y.toDouble()
    println("Adiccion o resta: x -= y.toDouble() -> $x")

    //Adiccion o multiplicacion
    x *= y.toDouble()
    println("Adiccion o multiplicacion: x *= y.toDouble() -> $x")

    //Adicion o division
    x /= y.toDouble()
    println("Adiccion o division: x /= y.toDouble() -> $x")

    //Adiccion o modulo
    x %= y.toDouble()
    println("Adiccion o modulo: x %= y.toDouble() -> $x")


    println()

    println ("----------- ALL OPERADORES DE IDENTIDAD -----------")

    val a = listOf(1, 2, 3)
    val b = a
    val c = listOf(1, 2, 3)

    println(a == b)  // Devuelve true
    println(a === b)  // Devuelve true

    println(a == c)  // Devuelve true
    println(a === c)  // Devuelve false



    println ("----------- ALL OPERADORES DE PERTENENCIA -----------")

    val numbers = listOf(1,2,3,4,5,5,6,7,8,9)
    val number = 3

    println("Usando (in)")
    if (number in numbers){
        println ("La constante $number esta en la lista")
    }else{
        println("La constante $number no esta en la lista")
    }


    println("Usando (!in)")
    if  (number !in numbers) {
        println("La constante $number no esta en la lista")
    }else{
        println("La constante $number si esta en la lista")
    }



    println ("----------- ALL OPERADORES DE BITS -----------")

    println("Usando el Operador de bit (and)")
    val w = 0b10011 // 19
    val r = 0b11110 // 30

    println (w and r == 0b10010)


    println ("Usando el Operador de bit (or)")
    val o = 0b101001 // 41
    val t = 0b110011 // 51

    println(o or t == 0b111011)


    println ("Usando el Operador de bit (xor)")
    val m = 0b110101
    val n = 0b101010

    println (m xor n == 31)


    println("Usando el operador de bit (and & function .inv())")
    //010011 -> Original
    //111111 -> Original
    //010011 -> Bits invertidos

    println(0b101100.inv() and 0b111111 == 0b010011)


    println ("Usando la funcion (shl)")
    /*shl: Desplaza todos los bits del número a la izquierda un cierto número de posiciones,
    introduciendo 0s en las posiciones vacías.*/

    //110011 -> Original
    //110011 -> desplazamiento
    //11001100 -> shl

    println(0b110011 shl 2 == 0b11001100)


    println ("Usando la funcion (shr)")
    /*shr: Desplaza todos los bits del número a la derecha un cierto número de posiciones,
    introduciendo 0s en las posiciones vacías.*/

    //101011 -> original
    //  1010 -> desplazamiento derecha
    //001010-> shr

    println(0b101011 shr 2 == 0b001010)

    println ("Usando la funcion (ushr)")
    /*ushr: Desplaza todos los bits del número a la derecha un cierto
    número de posiciones, introduciendo 0s en las posiciones vacías y
    descartando los bits que se desplazan fuera del número.*/


    //101011 -> original
    //  1010 -> desplazamiento derecha
    //001010-> shr

    println(0b101011 ushr 2 == 0b001010)


    /*APARTADO 2*/

    println ("----------- ALL OPERADORES DE CONTROL -----------")

    println ("---Sentencias condicionales---")

    val oControl1: Any = 313.1
    val oControl2: Int = 90
    val oControl3: Any = 83
    val oControl4: Any = 83
    val oControl5: Any = 8

    println ("If como expresion")
    val sumaOControl = if (oControl1 is Double){
        oControl1 + oControl2
    }else{
        println ("La variable $oControl3 no es de tipo Double")
    }

    //Usando operadores aritmeticos
    println ("if-else")
    if(sumaOControl != 80){
        println ("La variable $sumaOControl es diferente de 80")
    }

    //Usando operadores logicos
    println ("if-else-if-else")
    if (oControl1 != oControl2){
        println ("La variable $oControl1 es diferente de la variable $oControl2")
    }else if(oControl1 is Double){
        println ("La variable $oControl1 es un numero Double")
    }else{
        println ("La variable $oControl1 ")
    }


    //Uso del when
    println ("Uso del when normal")
    when(oControl3){
        1 -> "Es igual a 1"
        83 -> println("La variable $oControl3 es igual a 83")
        else -> "Error"
    }

    println ("Uso del when como expresion")
    val Calificacion = when (oControl5){
        1 -> "Reprobado has obtenido 1"
        2 -> "Reprobado has obtenido 2"
        3 -> "Reprobado has obtenido 3"
        4 -> "Reprobado has obtenido 4"
        5 -> "Reprobado has obtenido 5"
        6 -> "Has pasado con 6 de calificacion"
        7 -> "Has pasado con 7 de calificacion"
        8 -> "Has pasado con 8 de calificacion"
        9 -> "Has pasado con 9 de calificacion"
        10 -> "Calificacion perfecta 10"
        else -> "NA"
    }

    println ("$Calificacion")

    println("---Bucles---")
    println("bucle for con lista:")

    val firstList = listOf(1,2,3,4,5,7)
    for (i in firstList){
        println (i)
    }

    println ("bulce for por Rangos:")
    for (i in 1..10){
        println (i)
    }

    println ("for con indices")
    val firstArray = arrayOf(1,2,3,4)
    for (i in firstArray.indices){
        println (firstArray[i])
    }

    /*for (i in firstArray.indices){
        println(i)
    }*/


    println ("While")
    while(oControl4 != oControl5){
        println("Todo es se va a ejecutar mientas la condicion sea verdadera")
        break
    }


    println("Do-while")
    do {
        println("Esto se va a ejecutar independiente de la condicion - se ejecuta al menos una vez")
        break
    }while (oControl4 != oControl5)


    println("----Expresiones de control---")


    println("try-catch")
    try {
        print("Ingresa tu edad: ")
        val edad: Int? = readlnOrNull()?.toInt()
        println("Tu edad es correcta y tienes $edad years")


    }catch (e: NumberFormatException){
        println ("Ingresa un numero entero $e")

    }

    println("try-catch-finally")
    try {
        print("Ingresa una segunda edad: ")
        val edad2: Int? = readlnOrNull()?.toInt()
        if (edad2 != null && edad2 >= 18) {
            println("Eres mayor de edad y tienes $edad2 years")
        }else{
            println("Eres menor de edad y tienes $edad2 years")
        }
    } catch (e: NumberFormatException) {
        println("Ingresa tu edad correctamente $e")
    } finally {
        println("Recuerda que puede registrar en la pagina sin importar tu edad")
    }

    println("Expresion de control (return)")
    fun firstReturn(): Int{
        return 40
    }

    println("Esta es una prueba del operador de control (fun) " +
            "el cual incluye retornar el numero entero ${firstReturn()}")

    println("Expresion de control (break)")

    for (i in 1..10){
        if(i == 5) break
        println(i)
    }

    println("Expresion de control (continue)")
    for (i in 1..10){
        if (i == 5) continue
        println(i)
    }



    println("Expresion de control (throw)")


    fun calcularPerimetro(num1: Double, num2: Double, num3: Double): Double {

        if (num1 > 900 || num2 >900 || num3 >900){
            throw numeroGrandes ("Los numeros son demasiados grandes reducelos")
        }else{
            return num1 + numero2 + num3
        }

    }

    fun useTriangulo(){
        try {
            print("Ingresa el priemr numero: ")
            val num1: Double? = readlnOrNull()?.toDouble()
            print("Ingresa el segundo numero: ")
            val num2: Double? = readlnOrNull()?.toDouble()
            print("Ingresa el tercero numero: ")
            val num3: Double? = readlnOrNull()?.toDouble()
            if (num1 != null && num2 != null && num3 != null) {
                println(calcularPerimetro(num1, num2, num3))
            }

        }catch (e: IllegalArgumentException) {
            println("Error: ${e.message}")
        }
    }

    useTriangulo()


    println ("Difucultad extra")

    println ("Todos los numeros comprendidos entre 10 y 55, pares, sin incluir el 16 y multiplos de 3")

    for (i in 10..55){
        if (i != 16 && i % 2 == 0 && i % 3 != 0){
            println (i)
        }
    }

}

