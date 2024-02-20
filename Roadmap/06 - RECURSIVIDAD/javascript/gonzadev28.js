// Entiende el concepto de recursividad creando una función recursiva
// que imprima números del 100 al 0.

function recursividad(n){
    if (n < 0){
        return;
    }else{
        console.log(n);
        return recursividad(n -1);
    }
}
recursividad(100);

// DIFICULTAD EXTRA (opcional):

// Calcular el factorial de un número concreto (la función recibe ese número).

function factorial(fac){
    if (fac === 0){
        return 1;
    }else{
        return fac * factorial(fac - 1);
    }
}
console.log('---FACTORIAL---')
console.log(factorial(9)); //9x8x7x6x5x4x3x2x1 = 362.880

/* Calcular el valor de un elemento concreto (según su posición)
en la sucesión de Fibonacci (la función recibe la posición).*/

function fibonacci(num) {
    if(num < 1){
        console.log("Numero debe ser mayor o igual a 1");
    }else if(num === 1){
        return 0;
    }else if(num === 2){
        return 1;
    }else{
        return fibonacci(num - 1) + fibonacci(num - 2);
    }
}
console.log('---FIBONACCI---')
console.log(fibonacci(5)); //0, 1, 1, 2, '3'