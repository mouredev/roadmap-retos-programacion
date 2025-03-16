/** #06 - JavaScript ->Jesus Antonio Escamilla */
/**
 * La recursividad es un concepto que se llama la misma función asi misma,
    siempre y cuanto tenga donde llegar y donde iniciar, claro tener un punto de rotura
 */

function cuentaAtrás(numero) {
    if(numero <= 0){
        console.log("¡Cero!");
    }else{
        console.log(numero);
        cuentaAtrás(numero - 1);
    }
}

cuentaAtrás(100);

/**-----DIFICULTAD EXTRA-----*/

//-----FACTORIAL-----
function factorial(num) {
    if (num === 0) {
        return 1;
    } else if(num < 0){
        return 0;
    }else {
        return num * factorial(num - 1);
    }
}

console.log(factorial(5));



//-----FIBONACCI-----
function Fibonacci(a) {
    if(a <= 1){
        return a;
    }else{
        return Fibonacci(a - 1) + Fibonacci(a - 2);
    }
}

console.log(Fibonacci(4));

/**-----DIFICULTAD EXTRA-----*/