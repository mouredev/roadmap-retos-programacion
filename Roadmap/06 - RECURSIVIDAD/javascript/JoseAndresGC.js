// recursividad javascript
// a grandes rasgos es una funcion que se llama a si misma

function countdown(numero) {
    console.log(numero); // imprime el numero
    if (numero > 0) { // si numero es mayor a 0
        countdown(numero - 1); // llama la funcion countdown y le resta 1 numero
    } else { // de lo contrario
        console.log("cuenta regresiva terminada") // imprime qie la cuenta regresiva ha terminado
    }
}
countdown(100); // numero vale ahora 100

// DIFICULTAD EXTRA

function factorial(numero) {
    if (numero < 0) {
        return "Error: No se permiten números negativos "; // si el numero es menor a 0 retorna que no se permiten numeros negativos
    } else if (numero === 0) {
        return 1; // si el numero es 0 retorna 1, ya que el factorial de 0 es 1
    } else {
        return numero * factorial(numero - 1); // si el numero es mayor a 0, se multiplica el numero por el factorial - 1
    }
}
console.log(factorial(5)); // 120
console.log(factorial(0)); // 1
console.log(factorial(-500)); // Error: No se permiten números negativos

function fibonacci(numero) {
    if (numero <= 0) {
        console.log("Error: La posició debe ser mayor a 0"); // si el numero es menor o igual a 0 retorna que los numeros negativos no son permitidos
        return 0;
    } else if (numero === 1 ) {
        return 0;
    } else if (numero === 2) {
        return 1;
    } else {
        return fibonacci(numero - 1) + fibonacci(numero - 2); // si el numero es mayor a 1, se suma el fibonacci del numero - 1 y el fibonacci del numero - 2
    }
}

console.log(fibonacci(5));