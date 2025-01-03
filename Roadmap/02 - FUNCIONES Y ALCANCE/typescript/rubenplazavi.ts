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

// Sin parámetros ni retorno
function noParametersNoReturnFunction(): void {
    console.log('No Parameters No Return');
}

// con uno o varios parámetros, con retorno
function oneOrMoreParametersFunction(a: number, b: number): void {
    console.log(a+b);
}

// con retorno
function returnFunction(parameter: string): string {
    return `this is the parameter you have introduced ${parameter}`;
}

// crear funciones dentro de funciones
function exteriorFunction(): void {
    function insideFunction(): void {
        console.log('this is a function inside a function');
    }
    insideFunction();
}

exteriorFunction();

// Funciones ya creadas en el lenguaje
console.log(Math.max(1, 2, 3, 4, 5));
console.log(Math.min(1, 2, 3, 4, 5));

// Variable LOCAL y GLOBAL
const globalVariable: string = 'this is a global variable';

function localVariableFunction(): void {
    let localVariable: string = 'this is a local variable';
    console.log(globalVariable);
    console.log(localVariable);
}
localVariableFunction();
console.log(globalVariable);
//console.log(localVariable);  // al ser local scope no la reconoce
/*

Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 * */

function numberOfNonMultiplesOfThreeOrFive(parameter1: string, parameter2: string): number{
    let count: number = 0;

    for(let i=1; i<=100; i++){
        if( i%3 === 0 && i%5 === 0){
            console.log(parameter1 + parameter2);
            continue;
        }
        if(i%3 === 0){
            console.log(parameter1);
            continue;
        }
        if(i%5 === 0){
            console.log(parameter2);
            continue;
        }
        count++;
    }

    return count;
}

const counterOfTimes: number = numberOfNonMultiplesOfThreeOrFive('multiplo de 3', 'multiplo de 5');

console.log('\ncounterOfTimes ---->\n',counterOfTimes);