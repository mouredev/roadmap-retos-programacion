

fun main() {
    var a= 20
    val b= 10

    //Operadores en Kotlin
    println("-a = ${-a}")//Operadores de signos

    //Operadores Aritmeticos
    println("a + b = ${a+b}")//Suma
    println("a - b = ${a-b}")//Resta
    println("a * b = ${a*b}")//Multiplicacion
    println("a / b = ${a/b}")//Division
    println("a % b = ${a%b}")//Resto

    //Operadores de Asignacion compuesta
    a += b
    println("+= $a")
    a -= b
    println("-= $a")
    a *= b
    println("*= $a")
    a /= b
    println("/= $a")
    a %=b
    println("%= $a")

    //Operadores de incremento y decremento
    a++
    println("a++ = $a")//Incremento
    a--
    println("a-- =$a")//Decremento

    //Operadores relacionales (devuelven un Boolean)
    println("a = b = ${a==b}")//igualdad
    println("a != b = ${a != b}")//diferente
    println("a < b = ${a<b} ")//menor que
    println("a > b = ${a>b}")//mayor que
    println("a <= b = ${a <= b}")//menor o igual
    println("a >= b = ${a >=b}")//mayor o igual

    //Operadores lógicos
    var result : Boolean
    val greater = b>0
    val isEven = b%2 ==0
    result= greater && isEven //Y
    println("La variable b es par y mayor que 0 $result")
    result= greater || isEven //0
    println("La variable b es par O mayor que 0 $result")
    result = !greater
    println("La variable b es menor que 0 $result")

    //Operadores a nivel de bits
    println("a and b = ${a and b}")//and bit a bit
    println (" a or b = ${a or b}")// or bit a bit
    println(" a xor b = ${a xor b}")// xor bit a bit
    println("a.inv()= ${a.inv()}")// not bit a bit
    println("a shl b = ${a shl b}")// Desplazamiento de bits a la izquierda
    println("a shr b = ${a shl b}")//Desplazamiento de bits a la derecha
    println("a ushr b = ${a ushr b}")// Desplazamiento de bits a la derecha sin signo

    //Estructuras de control
    //Condicionales
    val name = "Adrian"
    if(name.contains("a")){
        println("Tu nombre contiene una A")
    }else{
        println("Tu nombre no contiene ninguna A")
    }

    val x= 3
    when (x){
        1 -> println("x = 1")
        2 -> println(" x =2")
        else -> println("x no es ni 1 ni 2")
    }

    //Bucles
    for (i in 1..5){
        println(i)//Imprime del 1 al 5
    }

    var z=0
    while (z<6){
        println("El valor de la variable z es $z")
        z++
    }

    do{
        println("El nuevo valor de z es $z")
        z--
    }while (z>0)

    //De salto
    for(i in 1..10){
        if(i==5)break
        println(i)
    }

    for(i in 1..10){
        if(i%2==0)continue
        println(i)
    }

    eReturn()

    //Control de excepciones
    try{
        val resultado =10/0
    }catch (e:ArithmeticException){
        println("Error: Division por 0")
    }finally {
        println("Este bloque siempre se ejecuta")
    }

    //Control de ambito
    val list= mutableListOf(1, 2, 3)
    with(list){
        add(4)
        println(this)
    }

    list.run {
        add(5)
        println(this)
    }

    name?.let {
        println(name.length)
    }

    list.apply {
        add(4)
        add(5)
    }
    println(list)

    list.also {
        it.add(8)
    }
    println(list)

    exercise()
}

fun eReturn():Boolean{
    val name= "Adrian"
    val control: Boolean
    if(name.contains("b")){
        control=true
    }else{
        control=false
    }
    return control
}

fun exercise(){
    for (i in 10..55){
        if(i %2==0 && i !=16 && i %3!=0){
            println(i)
        }
    }
}