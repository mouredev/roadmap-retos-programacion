fun main(){

    //Definicion de variables
    val a = 4
    val b = 2

    //Tipos de operadores en kotlin

    println("Operadores aritmeticos")

    println(a + b) //Suma
    println(a - b) //Resta
    println(a * b) //Multiplicacion
    println(a / b) //Division
    println(a % b)  //Modulo

    println("Operadores de comparacion")

    val c = 10
    val d = 20

    println(c == d) //Igual
    println(c != d) //Desigual
    println(c < d) //Menor
    println(c <= d) //Menor igual
    println(c > d) //Mayor
    println(c >= d) //Mayor igual

    println("Operadores logicos")

    val isRaining =  true
    val isCold = false
    val canGoOut = true

    println(!isRaining && !isCold)
    println(isRaining || isCold)
    println(!canGoOut)

    println("Operadores de asignacion")

    var e = 5 //Asignacion simple
    println(e)

    e += 1 //Suma y asignacion
    println(e)

    e -= 2 //Resta y asignacion
    println(e)

    e *= 3 //Multiplica y asignacion
    println(e)

    e /= 1 //Divide y asignacion
    println(e)

    e %= 4 //Modulo y asignacion
    println(e)

    println("Incremento y decremento")

    var counter = 0

    println(counter)
    counter++
    println(counter)
    ++counter
    println(counter)
    counter--
    println(counter)
    --counter
    println(counter)

    println("Operadores de rango")

    val numbers = 1..10 //Incluyendo 1 y 10
    println(numbers)
    val letters = 'a'..'z' //Letras de la 'a' a la 'z'
    println(letters)
    val even_numbers = 2 until 10 //Numeros pares del 2 al 9 (excluyendo el 10)
    println(even_numbers)

    println("Operadores de bits")

    val bin_1 = 10 //1010 en binario
    val bin_2 = 5  //0101 en binario

    println(a and b) // Resultado es 1 cuando ambos bits son 1
    println(a or b) //Resultado es 1 si al menos un bit es 1
    println(a xor b) //Resultado es 1 si los bits son diferentes
    println(a shl 2) //Desplaza los bits a la izquierda, rellenando con ceros a la derecha
    println(a shr 2) //Desplaza los bits a la derecha, rellenando con el bit de signo a la izquierda
    println(a ushr 2) // Desplaza los bits a la derecha, rellenando con ceros a la izquierda

    println("Estructuras de control")

    println("If:")

    val age = 18

    if(age >= 18){
        println("Eres mayor de edad")
    } else {
        println("Eres menor de edad")
    }

    println("When:")

    val day = "Monday"

    when(day) {
        "Monday" -> println("It's monday")
        "Tuesday" -> println("It's tuesday")
        "Wednesday" -> println("It's wednesday")
        "Thursday" -> println("It's thursday")
        "Friday" -> println("It's friday")
        else -> println("Weekend!")
    }

    println("for")

    for(i in 1..3){
        print(i)
    }

    println()

    println("while:")
    var w_i = 0

    while(w_i < 3){
        print(w_i)
        w_i++
    }

    println()

    println("do-while")

    var j = 0
    do {
        print(j)
        j++
    }while(j < 3)

    println()

    println("break")

    for (i in 1..10) {
        if (i == 5) {
            break
        }
        print(i)
    }

    println()

    println("continue")

    for (i in 1..10) {
        if (i % 2 == 0) {
            continue
        }
        print(i)
    }

    println()
    
    println("Ejercicio extra!:")

    for(i in 10..55){
        if(i % 2 == 0 && i % 3 != 0) {
            print("$i ")
        }
       if(i == 16){
            continue
        }
    }

}