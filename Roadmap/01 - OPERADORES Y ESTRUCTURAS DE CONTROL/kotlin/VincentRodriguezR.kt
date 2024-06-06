fun main(){

    // Punto #1 -> Operaciones con diferentes tipos de operadores

    //Operadores Aritmeticos
    val suma = 5 + 5 //Operador de suma
    val resta = 8 - 5 //Operador de resta
    val multi = 10 * 10 //Operador de multiplicacion
    val divi = 100 / 30 //Operador de division
    val perc = 100 % 3 //Operador modulo, devuelve el resto de la division


    //Operadores de asignacion
    val asigna = "Asignacion" //el = asigna un valor a la variable
    var resultado = 0
    resultado += suma //la combinacion de un operador con = devuelve la operacion directa, en este caso -> resultado = resultado + suma


    //Operadores de comparacion
    val igualdad = (5 == 5) //Igualdad ==
    val diferente = (8 != 9) //Desigualdad o diferente !=
    val mayorMenor = (9 > 10) //Comparadores >, <, >=, <=


    //Operadores logicos
    val and = (true && false) //Operador and &&
    val or = (true || true) //Operador or ||
    val not = !true //Operador Nor !


    //Operadores de incremento y decremento
    var incremento = 5
    incremento++ //Operador de incremento ++ el valor final es 6 ya que se incrementa en 1
    var decremento = 5
    decremento-- //Operador de decremento -- el valor final es 4 ya que se decrementa en 1


    //Punto #2 -> Ejercicios con estructuras de control existentes

    //Condicionales

    //if
    var condicional = true
    if (condicional == true)
        println("Codigo a ejecutar si se cumple la condicion (Si son varias instrucciones ponerlas entre {})")

    //if else
    if (condicional == true)
        println("Codigo a ejecutar si se cumple la condicion (Si son varias instrucciones ponerlas entre {})")
    else
        println("Codigo a ejecutar si no se cumple la condicion (Si son varias instrucciones ponerlas entre {})")

    //When
    val conmutador = 4
    when (conmutador){
        1 -> println("esta instruccion no se ejecutara ya que el valor no es igual al dado en al condicion osea en la variable conmutador")
        2, 3 -> println("esta instruccion no se ejecutara ya que el valor no es igual al dado en al condicion osea en la variable conmutador, se pueden concatenar varios resultados en un solo caso")
        4 -> println("esta instruccion se ejecutara ya que el conmutador contiene el valor de este caso cumpliendo la condicion del when")
        else -> println("esta instruccion se ejecutaria en caso de que ninguno de los valores definidos cumpla con la condicion del when")
    }

    //do while
    do{
        println("Instrucciones que se ejecutan mientras la condicion del while se cumpla, en este caso primero se ejecutan las acciones y luego se evalua la condicion")
        condicional = false
    } while(condicional == true)

    //while
    while(condicional == false){
        println("esta instruccion se ejecutara mientras la condicion del while se cumpla, en este caso se evalua primero la condicion y luego se ejecutan als acciones")
        condicional = true
    }

    //for + break
    val arreglo: Array<Int> = arrayOf(1,2,3)
    for(i in arreglo){
        println("Se ejecutan estas acciones hasta que se reccorra todo el arreglo en este caso son 3 posiciones que contiene el array")
        break //con Break se rompe el bucle haciendolo parar
    }

    //Punto Extra -> Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3

    for(i in 10 .. 55){
        if(i != 16 && i%3 != 0 ){
            println(i)
        }
    }
}