console.warn("----------(◉◉∖____/◉◉)---------- Recursividad ----------(OO∖____/OO)----------")
console.log("Imprimiendo del número 100 al número 0 usando Recursividad")
// Definimos la funcion con un parametro de tipo numero
function recursividad(numero) {
    // Le indicamos al programa hasta donde queremos que terminer la ejecusión
    if (numero >= 0) {
        // Imprimimos por consola el valor de la variable
        console.log(numero) // 10
        // Llamamos nuevamente a la funcion
        recursividad(numero-1) // Haciendo uso de la recursividad
    }
}
recursividad(100)

console.warn("----------(◉◉∖____/◉◉)---------- Ejercicio Extra ----------(OO∖____/OO)----------")
console.log("------------ Factorial de un número ------------")
function factorial(valor_factorial) {
    if (valor_factorial < 0) {
        return "No se aceptan números negativos"
    } else if(valor_factorial == 0 || valor_factorial == 1) {
        return 1
    } else {
        return valor_factorial * factorial(valor_factorial - 1)
    }
}
let num_factorial = 10
let resultado_factorial = factorial(num_factorial)
console.log(`Factorial de ${num_factorial}! = ${resultado_factorial}`)

console.log("------------ Fibonacci ------------")
function fibonacci(valor_fibonacci) {
    if (valor_fibonacci <= 0) {
        console.log("No se aceptan números negativos")
        return 0
    } else if (valor_fibonacci == 1) {
        return 0
    } else if (valor_fibonacci == 2) {
        return 1
    } else {
        return fibonacci(valor_fibonacci - 1) + fibonacci(valor_fibonacci - 2)
    }
}
let num_fibonacci = 10
let resultado_fibonacci = fibonacci(num_fibonacci)
console.log(`La posición ${num_fibonacci} en fibonacci es = ${resultado_fibonacci}`)
