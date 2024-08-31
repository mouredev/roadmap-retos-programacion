/*
    * EJERCICIO:
    * Entiende el concepto de recursividad creando una función recursiva que imprima
    * números del 100 al 0.

    ** QUE ES LA RECURSIVIDAD?
    ** La recursividad en la programacion es una tecnica de una funcion que se llama a si misma durante su ejecucion. Este proceso
    ** se repite hasta que se cumpla una condicion base que evita que la funcion se llame recursivamente.
*/

function funcionRecursiva(number) {
    // Si el numero es 0 entonces, imprimimos el numero y luego retornamos
    if (number === 0) {
        console.log(number);
        return;
    }
    // Imprimir el numero actual, luego llamamos a la funcion con el numero - 1
    console.log(number);
    funcionRecursiva(number - 1);
}

funcionRecursiva(100)

/* 
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
*/

function factorialRecursivo(number) {
    // Si el numero es 0 o 1 retornar 1
    if (number === 0 || number === 1) {
        return 1;
    }
    // Retonar el valor del numero multiplicado por su factorial del numero - 1
    return number * factorialRecursivo(number - 1);
}

let resultadoDelFactorialRecursivo = factorialRecursivo(6);
console.log(`Este es el resultado de un factorial de 6 por una funcion recursiva: ${resultadoDelFactorialRecursivo}`)

// Creando la sucesion de Fibonacci
function sucesionDeFibonacci(number, diccionarioDeValores = {}) {
    // Si el numero es menor a 0 retonar null
    if (number < 0) {
        return null;
    }
    // Si es el numero es 0 retornar 0
    else if (number === 0) {
        return 0;
    }
    // Si el numero es 1 retornar 1
    else if (number === 1) {
        return 1;
    }
    // Si el numero existe en el diccionario de valores de la sucesion de Fibonacci entonces, retornar el valor del numero en la sucesion.
    else if (number in diccionarioDeValores) {
        return diccionarioDeValores[number];
    }
    /* Si ninguna de las condiciones anteriores se cumple, entonces vamos a conseguir el resultado del numero en la sucesion de fibonacci
    llamandola recursivamente hasta que se cumpla una condicion base */
    else {
        // Resultado:
        let resultado = sucesionDeFibonacci(number - 1, diccionarioDeValores) + sucesionDeFibonacci(number - 2, diccionarioDeValores);
        // Guardar el resultado con su respectivo numero en el diccionario de valores de la sucesion de fibonacci
        diccionarioDeValores[number] = resultado;
        // Retonar el resultado
        return resultado;
    }
}

let resultadoDeLaSucesionDeFibonacci = sucesionDeFibonacci(15);
console.log(`Este es el resultado de la sucesion de fibonacci: ${resultadoDeLaSucesionDeFibonacci}`);