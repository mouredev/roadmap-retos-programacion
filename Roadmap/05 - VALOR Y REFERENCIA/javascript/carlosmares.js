/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

//Asignacion de variables

// Asignacion de variables por valor

/**
 * La Asignacion por valor sucede cuando a una variable le asignamos el valor de otra cuyo valor es un dato primitivo
*/

let variablePorValor = 10;
let variableTemporal = variablePorValor;
variablePorValor = 20;

console.log(variablePorValor);
console.log(variableTemporal);

//Asignacion de Variables por referencia

/**
 * La asignacion por referencia sucede cuando a una variable le asignamos el valor de otra cuyo valor es un dato complejo 
*/

let x = {
    a: 10,
    b: 5
};

let y = x;

x.a = 20;
x.b - 50;

console.log(x);

//Funciones que se pasen variables por valor y por referencia

//Funcion que se le pasa una variable por valor

/**
 * La diferencia entre pasar una variable por valor y por referencia es su relacion con lo que sucede dentro y fuera de la funcion
 * Cuando pasamos una variable por referencia lo que ocurre dentro de la funcion repercute fuera de ella
 * Mientas tanto cuando pasamos una variable por valor lo que ocurre dentro de la funcion se queda en la funcion, sin alterar el resto del codigo
 */

//paso por valor

let valor = 18;
const funcionValor = (value) =>{
    value = value * 10;
    console.log('Dentro de la funcion, value es: ', value);
}
funcionValor(valor);
console.log('Fuera de la funcion, valor es: ', valor);

//paso por referencia
let valor2 = 10;
const funcionValor2 = (value) =>{
    valor2 = valor2 * 10;
}
console.log('Valor de la variable valor2 antes de ejecutar la funcion es: ', valor2);
funcionValor2(30);
console.log('Valor de la variable valor2 despues de ejecutar la funcion es: ', valor2);