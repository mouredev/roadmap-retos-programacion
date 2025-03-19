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

// FUNCIONES SIN PARÁMETROS

function greet() {
    console.log('Hello there!');
}

const arrowGreet = () => console.log('Hello there from arrow function!');

// FUNCIONES CON PARÁMETROS

function greetUser(name, surname) {
    console.log(`Hello ${name} ${surname}!`);
}

const arrowGreetUser = (name, surname) => console.log(`Hello ${name} ${surname}!`);

// FUNCIONES CON RETORNO

function addTwo(numOne, numTwo) {
    return numOne + numTwo;
}

const arrowAddTwo = (numOne, numTwo) => numOne + numTwo;

// FUNCIONES CON FUNCIONES DENTRO

function greetUserWithInner (name, surname) {
    const getFullName = () => `${name} ${surname}`;

    console.log(`Hello ${getFullName()}!`);
}

// BUILT IN FUNCTIONS

const stringNumber = '11';
const number = parseInt(stringNumber);
console.log(`stringNumber is ${typeof stringNumber}, but number is ${typeof number}`);
// stringNumber is string, but number is number

// LLAMADA A LAS FUNCIONES

greet();
arrowGreet();

greetUser('Naia', 'Larrea');
arrowGreetUser('Naia', 'Larrea');

console.log(addTwo(2, 3));      // 5
console.log(arrowAddTwo(2, 3)); // 5

greetUserWithInner('Naia', 'Larrea');


/* DIFICULTAD EXTRA (opcional):
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

function printNumbers(textOne, textTwo) {
    let counter = 0;

    for (let num=1; num<=100; num++) {
        if (num % 3 === 0 && num % 5 === 0) {
            console.log(`${textOne}${textTwo}`);
        } else if (num % 3 === 0) {
            console.log(textOne);
        } else if (num % 5 === 0) {
            console.log(textTwo);
        } else {
            console.log(num);
            counter++;
        }
    }

    return counter;
}

console.log(printNumbers('fizz', 'buzz'));  // 53