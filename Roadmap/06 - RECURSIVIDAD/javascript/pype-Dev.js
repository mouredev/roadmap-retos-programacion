/**
 * EJERCICIO
 */

function cuentaAtras(num){
    if(num === 0){
        return 0;
    }

    console.log(num);
    return cuentaAtras(num - 1);
}

cuentaAtras(100);

/**
 * DIFICULTAD EXTRA
 */

function factorial(num){
    if(num < 0){
        console.log("Error. El factorial de número no puede ser negativo");
        return;
    } else if(num === 0){
        return 1;
    } else{
        return num * factorial(num - 1);
    }
}

factorial(5);

function fibonacci(posicion){
    if(posicion <= 0){
        console.log("LPara saber el valor correspondiente en la secuencia de Fibonacci, la posición debe ser mayor que cero.")
        return 0;
    } else if(posicion <= 2){
        return 1;
    } else{
        return fibonacci(posicion - 1) + fibonacci(posicion - 2);
    }
}

console.log(fibonacci(10));