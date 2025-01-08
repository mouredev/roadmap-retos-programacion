/*
 * EJERCICIO:
 * 1- Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * 2- Comprueba si puedes crear funciones dentro de funciones.
 * 3- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * 4- Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * 5- Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */


/* Soluciones */

// 1- 5- Funciones Basicas

function saludo() {
    console.log("Hola Gente!!");
}

saludo();


function saludoConNombre(nombre) {
    console.log("Hola" + " " + nombre + "!!" );
}

saludoConNombre("Daniel");


function suma(num1, num2) {
    return num1 + num2;
}

console.log(suma(1, 5));

function funcionQueSaluda() {
    return "Hola!! soy una funcion!!";
}

console.log(funcionQueSaluda());


// 2- 5- Funcion dentro de otra funcion

function llamada() {
    return `Hola funcion estas ahi?? - ${funcionQueSaluda()}`;
}

console.log(llamada());


// 3- 5- Funciones preexistentes

// Esta funcion toma una cadena como parametro y devuelve su longitud utilizando length.
function obtenerLongitud(cadena) {
    return cadena.length;
}

console.log(obtenerLongitud("Javascript"));

// Esta linea convierte la cadena "123" a un numero entero utilizando parseInt.
let cadenaNumero = "123";
let numero = parseInt(cadenaNumero);

console.log(numero);


// 4- 5- Variables locales y globales

// Ejemplo de variable global
var variableGlobal = "Soy una variable global";

function pruebaVariables() {
    // Ejemplo de variable local dentro de una funcion
    let variableLocal = "Soy una variable local";

    console.log(variableLocal);
    console.log(variableGlobal);
}

pruebaVariables();

// Intentando acceder a la variable local fuera de la funcion resultara en un error
// console.log(variableLocal);

// Accediendo a la variable global fuera de la funcion funciona
console.log(variableGlobal);


// Opcional
function opcional(palabra1, palabra2) {
    let numeros = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0) {
            console.log(palabra1);
        } 
        if (i % 5 == 0) {
            console.log(palabra2);
        }
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(palabra1 + " " + palabra2);
        } else {
            numeros++;
            console.log(i);
        }
    }
    return numeros;
}

console.log(opcional("Varios", "Numeros"));