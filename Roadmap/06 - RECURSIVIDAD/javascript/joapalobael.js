console.log('----- Recursividad -----');
function recursividad(num) {
    if (num < 0){
        return;
    }
    console.log(num)
    recursividad(num - 1);
}

recursividad(100);
/*
* DIFICULTAD EXTRA (opcional):
* Utiliza el concepto de recursividad para:
* - Calcular el factorial de un número concreto (la función recibe ese número).
* - Calcular el valor de un elemento concreto (según su posición) en la 
*   sucesión de Fibonacci (la función recibe la posición).
*/

console.log('----- Factorial -----');
function factorial(n) {
    if(n === 0){
        return 1; // 0! = 1 por definición
    }
    
    return(n*factorial(n-1));
}

console.log(factorial(9))

console.log('----- Fibonacci -----');

function fibonacci (f){
    if (f === 0){
        return 0;
    }
    if (f === 1){
        return 1;
    }
    if( f > 1){
        return fibonacci(f-1)+fibonacci(f-2);
    }
}
console.log(fibonacci(6));