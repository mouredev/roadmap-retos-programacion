/*
    Funciones definidas por el user
*/

// Función simple

function hello(){
    console.log("Hola Señor!");
}

hello();

// con parámetros

function suma(a, b){
    console.log(a+b);
}

suma(1, 2);

// con parámetros y retorno

function resta(a, b){
    return a - b;
}

console.log(resta(5, 2));

// funciones anidadas

function operacionesMatematicas(a, b){
    function suma(a, b){
        console.log(a+b)
    }
    function multiply(a, b){
        console.log(a*b)
    }

    suma(a,b);
    multiply(a,b);
}

operacionesMatematicas(4,4); // 8 y 16

// Función que venga predeterminada en el lenguaje
// push() Agrega un elemento a un array
let array = ['Juan', 'Diego'];
array.push('Alfredo');
console.log(array);

// Concepto variable local y global
const pi = 3.14; // Global
    function division(){
        const pi = 20; //Local
        console.log(pi);
    }
console.log(pi);
console.log(division());

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */

function printNumbers(text1, text2){
    let count = 0;
    for(let i = 1; i <= 100; i++){
        if(i%3 === 0 && i%5 === 0){
            console.log(text1 + text2);
        } else if(i%3 === 0){
            console.log(text1);
        } else if(i%5 === 0){
            console.log(text2);
        } else {
            console.log(i);
            count++;
        }

    }
    console.log(`Se han impreso ${count} números`);
}
printNumbers('Fizz', 'Buzz');