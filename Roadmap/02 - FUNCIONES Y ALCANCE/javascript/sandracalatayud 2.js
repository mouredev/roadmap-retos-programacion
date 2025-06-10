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

// !  -------- EJERCICIO 1 --------

/*
    * 1. 
    * Crea ejemplos de funciones básicas que representen las diferentes
    * posibilidades del lenguaje:
    * Sin parámetros ni retorno, con uno o varios parámetros, con retorno... 
*/

//Función normal
function printConsola () {
    console.log("Hola");
}

printConsola();

//Función con parámetros
function printConsolaParam (mensaje) {
    console.log(mensaje);
}

printConsolaParam("Hola");

//Función con return
function suma (valor1, valor2) {
    return valor1 + valor2
}

console.log(suma(3,5));

/*
    * 2.
    * Comprueba si puedes crear funciones dentro de funciones.
*/

function printScores () {
    score1 = 3
    score2 = 4

    function formatScores(){
        return console.log("Puntuación 1: "+ score1 + "\n" + "Puntuación 2: "+ score2);
    }

    return formatScores();
}

printScores();

/*
    * 3.
    * Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
*/

console.log(Math.round(4.6654563));

/*
    * 4.
    * Pon a prueba el concepto de variable LOCAL y GLOBAL.
*/

let myStringGlobal = "Esta es una variable global"

function stringLocal(){
    let myStringLocal = "Esta es una variable local";
    return myStringLocal;
}

console.log(stringLocal());
//console.log(myStringLocal);     //No devuelve nada, no está definida
console.log(myStringGlobal);

// !  -------- EXTRA --------

/*
    * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    * La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function numbersExtra (str1, str2){

    let countPrintNum=0; 

    for (let i = 0; i <= 100; i++) {
        if ( i % 5 == 0 && i % 3 == 0){
            console.log(str1)
        } else if ( i % 5 == 0){
            console.log(str2)
        } else if ( i % 3 == 0){
            console.log(str1 + str2)
        } else {
            console.log(i);
            countPrintNum++;
        }
    }

     return countPrintNum
}

console.log(numbersExtra("Cadena 1", "Cadena 2"));