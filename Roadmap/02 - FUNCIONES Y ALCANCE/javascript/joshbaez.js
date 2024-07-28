/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// funcion sin parametros ni retorno 

function saludar() {
    console.log("hola mundo"); // hola mundo 

}

saludar(); // llamada a la funcion

// funcion con un parametro y sin retorno 

function saludo(name) {
     console.log("hola, " + name + "!");  // hola, josh!

} 

saludo("johs"); // llamada a la funcion con un argumento 
 
// funciones con varios parametros y sin retorno

function addAndPrint(a, b) {
    const sum = a + b;
    console.log("sum: " + sum); // sum: 8
}

addAndPrint(5, 3); // llamada a la funcion con dos argumentos

// funcion con un parametro y con retorno 

function cuadrado(numero) {
    return numero * numero;

} 
const resultado = cuadrado(4); // Llamada a la función y almacenando el valor de retorno
console.log(resultado); // imprime 16

// funcion con varios parametros y con retorno 
// esta funcion acepta varios parametros y devuelve un valor basado en esos parametros 

function multiply(a, b) {
    return a * b; 

    
}

const producto = multiply(6, 7);
console.log(producto); // imprime 42

// funcion anonima asignada a una variable 
// Una función anónima es una función sin nombre que se puede asignar a una variable

const greet = function (name) {
    return "hola, " + name + "!"

};

console.log(greet("josh")); // Llamada a la función anónima asignada a una variable 

// funcion de flecha (arrow function)
// Las funciones de flecha son una sintaxis más corta para escribir funciones anónimas.

const llamada = (apoodo) => {
    return "hello, " + apoodo + "!";

}; 

console.log(llamada("pepe")); // llamada a la fuction de flecha 

// Si la función de flecha tiene una sola expresión, se puede omitir el bloque {} y el return:\

const llama = apodo1 => "hola, " + apodo1 + "!";

console.log(llama("joshua")); // llama a la funcion de flecha simplificada 

// funcion con valor por defecto en los parametros 

function saludar2(name2 = "persona") {
    console.log("hola, " + name2 + "!");
}

saludar2(); // Llamada sin argumentos, utiliza el valor por defecto
saludar2("josue") // Llamada con un argumento

// funcion que utiliza el operador rest ...
// El operador Rest permite a una función aceptar un número indefinido de argumentos como un array.

function sum(...numbers) {
    return numbers.reduce((total, number) => total + number, 0);

}

console.log(sum(1, 2, 3)); // imprime: 6
console.log(sum(4, 5, 6, 7)); // imprime: 22

// function con manejo de exepciones (try-catch)
// Una función puede incluir manejo de excepciones para gestionar errores.

function divide(a, b) {
    try {
        if (b === 0) {
            throw new Error("division by zero");
        }
        return a / b;
    } catch (error) {
        console.log(error.message);
        return null;
    }
}

console.log(divide(10, 2)); // imprime: 5
console.log(divide(10, 0)); // imprime: division by zero y retorna null 

// DIFICULTA EXTRA 

function imprimirNumerosEspeciales(STR1, STR2) {
    let contador = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(STR1 + STR2);
        } else if (i % 3 === 0) {
            console.log(STR1);
        } else if (i % 5 === 0) {
            console.log(STR2);
        } else {
            console.log(i);
            contador++;
        }
    }

    return contador;
}

// Ejemplo de uso
const STR1 = "Fizz";
const STR2 = "Buzz";
const result = imprimirNumerosEspeciales(STR1, STR2);
console.log("Número de veces que se ha impreso un número en lugar de los textos:", resultado);