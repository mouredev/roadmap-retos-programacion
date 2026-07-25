/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */

function cuentaAtras(numero) {
    if(numero >= 0) {
        console.log(numero)
    cuentaAtras(numero -1)
    }
}
cuentaAtras(100)


 /*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 */

function calcuFactorial(nPositivo) {
    //let factorial = 1 

    if(nPositivo < 0) {
        return `¡${nPositivo} no es un dato válido! \n Tiene que ser un número positivo`
    }else if (nPositivo == 0) {
        return 1
    }

    /* for(let i = nPositivo; i > 1; i --) { 
       factorial *= i
       console.log(i)
    }
    return factorial*/ 

    return nPositivo * calcuFactorial (nPositivo - 1) // No hace falta guardar previamente el resultado en una variable que acumule el resultado de cada operación,
                                                      // ya que se acumula en la pila de llamadas. Primero se calcula la pila de llamadas de manera descendente
                                                      // y luego se realizan los cálculos de manera ascendente, acumulando el resultado de la operación anterior,
                                                      // ya que es necesario para realizar la siguiente operación.
}
console.log(calcuFactorial(5))

/*
* - Calcular el valor de un elemento concreto (según su posición) en la
*   sucesión de Fibonacci (la función recibe la posición).
*/

function valorPosicion(valor) {
    if(valor <= 0){
        return `¡${valor} no es un dato válido! \n Tiene que ser un número positivo`
    }else if(valor === 1) {
        return 0
    }else if( valor === 2) {
        return 1
    }else {
        return valorPosicion(valor -1) + valorPosicion(valor -2)
    }
}

console.log(valorPosicion(8))