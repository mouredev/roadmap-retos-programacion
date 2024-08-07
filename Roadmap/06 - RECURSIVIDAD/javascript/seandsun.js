/**
 * <-------------- Recursividad -------------->
 * Básicamente la recursión es una función llamándose a sí misma, hasta que llega un punto en que debe parar. Para indicarle a la función
 * recursiva que debe detenerse, le debemos definir un "caso base", o sea, una condición de salida o fin de la ejecución.
*/
function recursividad(numero) {
    if(numero < 0) { // Caso base, o sea que NO se produce ninguna llamada recursiva
        return
    }
    console.log(numero)
    recursividad(numero-1)
}

recursividad(100)

/**
 * Lo que está sucediendo dentro de la función "recursividad" es:
 * 1. La entrada actual es 100
 * 2. ¿ 100 es igual a 0 ? (este es el CASO BASE, o sea la condición que terminará la ejecución de la función)
 * 3. No, entonces imprime 100 por consola
 * 4. La función se llama a sí misma otra vez con el "numero - 1", o sea "100 - 1" = 99
 * 5. La nueva entrada principal es 99
 * 6. Nuevamente pregunta ¿ 99 es igual a 0 ?
 * 7. No, entonces imprime 99 por consola
 * 8. Y así se sigue repitiendo hasta que la entrada principal es 0, y de esa manera la función deja de llamarse a sí misma 
*/

/**
 * <-------------- Dificultad extra: factorial -------------->
 * Multiplicación de todos los números enteros positivos que hay entre ese número y el 1. El factorial de 0 es 1.
 * Ejemplo: 4! = 4 * 3 * 2 * 1 = 24
*/
function factorial(numero)  {
    if(numero === 0) { // Caso base, o sea que NO se produce ninguna llamada recursiva
        return 1
    } 
    return numero * factorial(numero-1)    
}

let resultado = factorial(num = 4)
console.log(`El factorial de ${num}! es: ${resultado}`) // 24

/*
Ejecución de la función factorial:
---------------------------------------------
 4! = 4 * 3! retorna 24  // Este es el primer proceso que se abre, pero es el último en ejecutarse ya que a partir de este se abren los otros
    --------------------------------------  
    3! = 3 * 2! retorna 6
        -------------------------------  
        2! = 2 * 1! retorna 2
            ------------------------ 
            1! = 1 * 0! retorna 1
                ----------------
                0! = 1 retorna 1  // Primero se resuelve este subproceso para pasarle el "resultado" al subproceso anterior
*/

/**
 * <-------------- Dificultad extra: fibonacci -------------->
 * Secuencia de números en la que después del 0 y del 1, cada numero de la serie se obtiene sumando los dos anteriores.
 * Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
*/
function fibonacci(posicion) {
    if(posicion < 2) { // Caso base, o sea que NO se produce ninguna llamada recursiva
        return posicion
    } 
    return fibonacci(posicion - 2) + fibonacci(posicion - 1)
}

let result = fibonacci(numPosicion = 4) 
console.log(`El valor de la posición ${numPosicion} en la secuencia Fibonacci es: ${result}`) // 3


/*
Ejecución de la función fibonacci:
---------------------------------------------
 pos4 = pos2(1) + pos3(2) retorna 3  // Este es el primer proceso que se abre, pero es el último en ejecutarse ya que a partir de este se abren los otros
    --------------------------------------  
    pos3 = pos1(1) + pos2(1) retorna 2
        -------------------------------  
        pos2 = pos0(0) + pos1(1) retorna 1 // Primero se resuelve este subproceso para pasarle el "resultado" al subproceso anterior
            ------------------------ 
            pos1 = 1 retorna 1
                ----------------
                pos0 = 0   retorna 0  
*/