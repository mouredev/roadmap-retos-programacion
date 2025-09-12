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


/* Soluciones */


// Primitivos
let numero1 = 10;
let numero2 = numero1; // Se copia el valor de numero1 a numero2

numero1 = 20; // Modificar numero1 no afecta a numero2

console.log(numero1); // 20
console.log(numero2); // 10

// String
let nombre1 = "Ana";
let nombre2 = nombre1; // Se copia el valor de nombre1 a nombre2

nombre1 = "María"; // Modificar nombre1 no afecta a nombre2

console.log(nombre1); // María
console.log(nombre2); // Ana


// Objetos
let persona1 = { nombre: "Ana", edad: 30 };
let persona2 = persona1; // Se asigna la referencia al mismo objeto

persona1.nombre = "María"; // Modificar persona1 afecta a persona2

console.log(persona1); // { nombre: "María", edad: 30 }
console.log(persona2); // { nombre: "María", edad: 30 }

// Arrays
let numeros1 = [1, 2, 3];
let numeros2 = numeros1; // Se asigna la referencia al mismo array

numeros1[0] = 4; // Modificar numeros1 afecta a numeros2

console.log(numeros1); // [4, 2, 3]
console.log(numeros2); // [4, 2, 3]


/* Extra - Opcional */


let apellido = "Benzatto";

let apellido1 = "Corbo";


function intercambio1(param1, param2) {
    let apellido3 = param1;
    let apellido2 = param2;

    return { apellido2, apellido3 };
}

let resultado = intercambio1(apellido, apellido1);

let { apellido2, apellido3 } = resultado;

    // Las variables originales no se modifican
    console.log(apellido); // Valor original
    console.log(apellido1); // Valor original
    console.log(apellido2); // "Corbo"
    console.log(apellido3); // "Benzatto"


    let fruta1 = { nombre: "Manzana", color: "Rojo" };

    let fruta2 = { nombre: "Pera", color: "Amarillo" };


function intercambio2(param1, param2) {
    let fruta3 = param2;
    let fruta4 = param1;
    
    return { fruta3, fruta4 };
}

let resultado1 = intercambio2(fruta1, fruta2);

let { fruta3, fruta4 } = resultado1;

    // Las variables originales no se modifican
    console.log(fruta1); // Valor original
    console.log(fruta2); // Valor original
    console.log(fruta3); // "Pera"
    console.log(fruta4); // "Manzana"