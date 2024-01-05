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

    //Operadores relacionales   https://www.develou.com/operadores-en-kotlin/
    //igualdad

    //diferente de...

    //menor que

    //mayor que

    //menos o igual que

    //mayor o igual que


    //Operadores lógicos



}