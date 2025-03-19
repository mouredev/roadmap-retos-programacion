// ** EJERCICIO

function recursividad(n) {
    if (n >= 0) {
        console.log(n);
        recursividad(n - 1);
    }
}

recursividad(100)

// ** DIFICULTAD EXTRA ** --------------------------------------------------------------------------------------------------------------------------------------------

//  Calcula el factorial de un número concreto

function factorial(n) { // La función recibe el número a factorizar
    if (n <= 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

factorial(5) // 120

// Calcula el valor de un elementos concreto en la sucesión de Fibonacci

function fibonacci() { // La función recibe la posición del número
    
}


function fibonacci(n) { 
    if (n === 0) {
        return 0;
    } else if (n === 1) {
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

console.log(fibonacci(5)) // La función empieza a contar desde el 0 como primera posición de la serie de Fibonacci