//01 - OPERADORES Y ESTRUCTURAS DE CONTROL

//https://kotlinlang.org/docs/keyword-reference.html#modifier-keywords
//http://www.androidcurso.com/index.php/99-kotlin/912-estructuras-de-control-en-kotlin
//https://kotlin.desarrollador-android.com/basico/control-de-flujo/

fun main(): Unit {
    //OPERADORES ARITMÉTICOS
    var ope1 = 5
    var ope2 = 4
    var ope3 = 1
    //Suma
    println("Con operador + " + (ope1 + ope2))
    println("Con función equivalente sumar "+ ope1.plus(ope2))
    ope3+=ope1
    println("Suma asignación compuesta "+ ope3)

    //Restar
    println("Con operador - " + (ope1 - ope2))
    println("Con función equivalente restar "+ ope1.minus(ope2))
    ope3-=ope1
    println("Resta asignación compuesta "+ ope3)

    //Múltiplicación
    println("Con operador * " + (ope1 * ope2))
    println("Con función equivalente multiplicación "+ ope1.times(ope2))
    ope3*=ope1
    println("Multiplicación asignación compuesta "+ ope3)

    //División
    println("Con operador / " + (ope2 / ope1))
    println("Con función equivalente división "+ ope2.div(ope1))
    ope3/=ope1
    println("División asignación compuesta "+ ope3)

    //residuo
    println("Con operador % " + (ope1 % ope2))
    println("Con función equivalente multiflicación "+ ope1.rem(ope2))
    ope3%=ope1
    println("Residuo asignación compuesta "+ ope3)


    //Incremento: puede ir como prefijo o sufijo
    println("Incremento "+ (ope1++))

    //Decremento: puede ir como prefijo o sufijo
    println("Decremento "+ (ope1--))

    //Operadores relacionales
    //igualdad
    println("los númenos 2 y 2 son iguales: "+ (2==2))

    //diferente de...
    println("los númenos 2 y 1 son diferentes: "+ (2!=1))

    //menor que
    println("2 es menor que 3: "+ (2<3))

    //mayor que
    println("4 es menor que 3: "+ (4>3))

    //menos o igual que
    println("2 es menor o igual que 3: "+ (2<=3))

    //mayor o igual que
    println("3 es mayor o igual que 3: "+ (2>=3))


    //Operadores lógicos
    var num1 = 1
    var num2 = 4
    //AND
    println("num1 and num2: ${num1 and num2}")
    //OR
    println("num1 or num2: ${num1 or num2}")
    //XOR
    println("num1 xor num2: ${num1 xor num2}")

    //NOT
    println("num1.inv(): ${num1.inv()}")

    //DESPLAZAMIENTO DE BITS A LA IZQUIERDA
    println("num1 shl num2: ${num1 shl num2}")
    //DESPLAZAMIENTO DE BITS A LA DERECHA
    println("num1 shr num2: ${num1 shr num2}")
    //DESPLAZAMIENTO DE BITS A LA DERECHA SIN SIGNO
    println("num1 ushr num2: ${num1 ushr num2}")


    //ESTRUCTURAS DE CONTROL
    //IF
    if (2<3){
        println("2 es menor a 3")
    }

    //IF ELSE
    if ("agua" != "cafe"){
        println("El café es mejor que el agua")
    } else{
        println("Hay que beber agua para estar sano")
    }

    //WHEN
    when("Agua"){
        "Agua" -> print("sanito")
        "zumo" -> print("Mejor come fruta natural")
        else -> { println("mejora tu dieta")
        }
    }


    //BUCLE FOR
    for (i in 0..5){
        println("contador for: "+ i)
    }

    //BUCLE WHILE
    while (num2 > 0){
        println("contador while: "+ num2)
        num2--
    }
    num2 = 6
    //BUCLE DO WHILE
    do {
        println("contador do while: "+ num2)
        num2--
    }while(num2 > 0)

    //se pueden usar controladores para salir de la estructura
    //return : retornamos de la función actual (o función anónima).
    //break : terminamos el bucle más cercano.
    //continue : continuamos con el siguiente paso en el bucle más cercano.

}