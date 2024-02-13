// #06 RECURSIVIDAD

function imprimirNumeros(contador) {
    if (contador < 0) {
        return;
    } else {
        console.log(contador);
        contador--;
        imprimirNumeros(contador);
    }
}

imprimirNumeros(100);

// Dificultad Extra

function factorial(numero) {
    if (numero === 0) {
        return 1;
    } else {
        return numero * factorial(numero - 1);
    }
}
console.log(factorial(5)); // 120

function fibonacci(numero) {
    if (numero < 1) {
        console.log("El número debe ser mayor o igual a 1");
    } else if (numero === 1) {
        return 0;
    } else if (numero === 2) {
        return 1;
    } else {
        return fibonacci(numero - 1) + fibonacci(numero - 2);
    }
}

console.log(fibonacci(8)); // 13