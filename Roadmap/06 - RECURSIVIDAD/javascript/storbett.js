// Función contador en JavaScript
function contador(number) {
    if (number >= 0) {
        console.log(number);
        contador(number - 1);
    }
}

contador(100);

/*
    Extra 
*/

// Función factorial en JavaScript
function factorial(number) {
    if (number < 0) {
        console.log("Los números negativos no son válidos");
        return 0;
    } else if (number === 0) {
        return 1;
    } else {
        return number * factorial(number - 1);
    }
}

console.log(factorial(5));

// Función fibonacci en JavaScript
function fibonacci(number) {
    if (number <= 0) {
        console.log("La posición tiene que ser mayor que cero");
        return 0;
    } else if (number === 1) {
        return 0;
    } else if (number === 2) {
        return 1;
    } else {
        return fibonacci(number - 1) + fibonacci(number - 2);
    }
}

console.log(fibonacci(7));
