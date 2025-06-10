/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */

let recursividad = (numero) =>{

    if (numero>=0){
        console.log(numero)
        recursividad(numero-1)
    }
}

recursividad(100);

/*

 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

let factorial =(n)=>{

    if(n===0){
         return 1
    } 
    else {
         return n*factorial(n-1)}
    }


console.log(factorial(1));


let fib = (number) =>{
    if (number<=0){
        console.log('Los numeros negativos no son validos');
        return 0
    }
    else if (number==1){
        return 0
    }
    else if (number==2) {
        return 1
    }
    else {
        return fib(number-1)+fib(number-2)
    }
}

console.log(fib(10));