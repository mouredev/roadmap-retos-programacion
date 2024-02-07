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
//Ejercicio

function recursividad(numero){
    if (numero<=100){
        console.log(numero)
    }
    else {
        return recursividad
    }
   
    recursividad (numero +1)

}

recursividad(0)




//Dificultad extra
const prompt=require('prompt-sync')()
function factorial (numero2){
    if (numero2==0){
        return 1
    }
    else {
        return numero2 * factorial(numero2-1)
    }
}

let numero2 = prompt("Por favor ingrese un número: ")

let resultado= factorial(numero2)
console.log(resultado)


function Fibonacci (posicion){
    if (posicion<=1){
        return posicion
    }
    else {
        return Fibonacci(posicion -1)+ Fibonacci(posicion-2)
    }
}
let posicion = prompt("Por favor ingrese la posición del número en la serie: ")
let resultado2 = Fibonacci(posicion)
console.log(resultado2)




