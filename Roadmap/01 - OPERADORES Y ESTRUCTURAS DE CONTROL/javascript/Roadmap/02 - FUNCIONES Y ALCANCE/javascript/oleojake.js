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


// FUNCIÓN SIN PARÁMETRO
function funcionSimple (){
    console.log ("Soy una función sin parámetros ni retorno");
}
funcionSimple();

// FUNCIÓN CON UN PARÁMETRO
function funcionOneParameter (message){
    console.log ("Soy una función con un parámetro y te lo imprimo por pantalla: " + message);
}
let myMessage = "OleojakeDEV"
funcionOneParameter(myMessage);

// FUNCIÓN CON DOS PARÁMETROS
function sumaNumbers (num1,num2){
    let suma = num1 + num2;
    console.log ("Te hago la suma de los dos números que me has pasado: " + num1 + " + " + num2 + " = " + suma);
}
sumaNumbers(3,5);

// FUNCIÓN CON RETORNO
function retornoMultiplicacion (num1,num2) {
    return num1 * num2;
}
let multiplicacion = retornoMultiplicacion(3,5);
console.log ("Después de haber llamado a retornoMultiplicacion() ahora mi variable multiplicación vale: " + multiplicacion);

// FUNCIÓN DENTRO DE OTRA FUNCIÓN
function printSumaNumbers (num1,num2){
    let suma = num1 + num2;
    function printResult (sumaResult){
        console.log ("El resultado de la suma que me has pasado: " + num1 + " + " + num2 + " = " + suma);
    }
    printResult(suma);    
}
printSumaNumbers (4,2);

// FUNCIÓN DEFINIDA YA EN JS
let myDecimal = 5.45;
console.log(parseInt(myDecimal)); // Devuelve un entero a partir de un decimal

// VARIABLE GLOBAL Y LOCAL
let numberGlobal = 50;
function changeMyNumber (){
    let numberLocal = 75;
    console.log (numberLocal); // Solo puedo acceder a su valor dentro de donde se ha declarado
    numberGlobal = 100; // En cambio puedo acceder a variables globales que se han definido fuera de la funcion
}
changeMyNumber();
console.log (numberGlobal);

// FUNCION ÁNONIMA, Se declaran sin nombre y se alojan dentro de una variable
const PI = function () {
    return 3.14;
}
console.log(PI); // Imprime la funcion
console.log(PI()); // Llamamos a la funcion dentro de la variable donde la hemos alojada

// ARROW =>
// También se pueden definir eliminando la palabra function y utilizando la flecha
const PI_FLECHA = () => {
    return "PI_flecha";
}
console.log(PI_FLECHA());
// A diferencia de las functions habituales que pueden ser llamadas antes o después de su declaración. Una función flecha no puede ser llamada antes de ser declarada.


/* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */

function myFizzBuzz (fizz,buzz) {
    let contador = 0;
    for (let i = 1; i <= 100; i++) {
        if ((i % 3 == 0) && (i % 5 != 0)){
            console.log(fizz);
        } else if ((i % 5 == 0) && (i % 3 != 0)){
            console.log(buzz);
        } else if ((i % 5 == 0) && (i % 3 == 0)){
            console.log(fizz+buzz);
        } else {
            console.log (i);
            contador ++;
        }
    }
    return contador;
}
console.log("Se han impreso números: " +myFizzBuzz ("Fizz", "Buzz") + " veces");