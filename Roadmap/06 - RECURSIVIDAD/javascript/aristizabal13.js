/*
Ejercicio
*/

function countdown(number){
    if (number >= 0) {
        console.log(number);
        countdown(number - 1);
    }
}

countdown(100);


/*
Extra
*/

function factorial(number){
    if(number < 0){
        console.log("No se puede calcular el factorial de un número negativo");
        return 0;
    } else if(number === 0){
        return 1;
    } else {
        return number * factorial(number - 1);
    }
}

console.log(factorial(-1));

function fibonacci(num){
    if (num < 0) {
        console.log("Los numeros negativos no son validos")
        return 0;
    } else if (num === 1){
        return 0;
    } else if (num === 2){
        return 1;
    } else {
        return fibonacci(num - 1) + fibonacci(num - 2);
    }
}

console.log(fibonacci(5));