/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

 func Recursividad(num: Int){
    print(num)

    if(num == 0 ){
        print("xd")
    }

    if(num > 0){
        Recursividad(num: num-1)
    }
 }

 Recursividad(num: 100)

 //DIFICULTAD EXTRA
 func factorial(num: Int, numdes: Int){
    if (numdes == 0){
        print(num)
    }
    else{
        factorial(num: numdes * num, numdes: numdes - 1)
    }
 }

 factorial(num:1, numdes: 4)

 //El primer numero es el numero con el que siempre se inicia que es 1, y el 4 es como decir 4!, y de ahi se multiplica.

 //Calcular posicion fibonacci

 func fibonacci(num1: Int,num2: Int ,pos: Int){
    let aux = num1 + num2
    if (pos == 3){ //asi funciona, hice un error pequeño de calculo, antes pero bueno si sale mejor no moverlo xd
        print(aux)
    }
    else{
        
        fibonacci(num1: num2, num2: aux , pos: pos - 1)
    }
 }

 fibonacci(num1: 0, num2: 1, pos: 10)//Comienza siempre con 0 luego 1, y la posicion es la q queremos determinar.