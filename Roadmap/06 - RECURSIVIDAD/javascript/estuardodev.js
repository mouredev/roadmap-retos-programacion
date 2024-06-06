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

function numeros(n){
    if(n<0){
        return;
    }

    console.log(n);
    numeros(n-1);
}

numeros(100);

function factorial(n){
    if (n < 0){
        return 0;
    } else if (n==0){
        return 1;
    } else{
        return n * factorial(n - 1);
    }
}

factorial(5);

function fibonacci(posicion){
    if (posicion <= 0){
        return 0;
    } else if (posicion == 1){
        return 0;
    } else if (posicion == 2){
        return 1;
    } else{
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
    }
}

fibonacci(5)