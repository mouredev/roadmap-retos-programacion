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
//
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

//funciones simples//

function saludar()  {
    console.log('Hola, Javascript!');
}
saludar();
// con retorno
function returnSaludar() {
    return console.log('Hola, Javascript!');
}
returnSaludar();

//con argumento

function arg_saludar(saludo) {
    return saludo;
}
let saludo = arg_saludar('Hola, Javascript!');
console.log(saludo);

//funciones dentro de funciones

function outherFunction() {
    function innerFunction() {
        console.log('Hola, Javascripts!');
        
    }innerFunction();
} outherFunction();

//funciones dentro del lenguaje
let a = 1;
console.log(a);

// variables locales y globales

variable_global = "Javascript";

console.log(variable_global);

function holaJavascript() {
    variable_local = "Hola";
    console.log(variable_local, variable_global);
}
holaJavascript();

