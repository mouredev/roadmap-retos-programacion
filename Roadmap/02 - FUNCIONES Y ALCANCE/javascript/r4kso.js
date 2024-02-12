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
 */

// Función sin parámetros ni retorno
function hello() {
    console.log("¡Hola Mundo! Soy r4kso")
}
hello()

// Función con un parámetro y sin retorno
function showNumber(number) {
    n = number;
    console.log(`El número es: ${n}`)
}
showNumber(69);

// Función con varios parámetros y sin retorno
function addNumbers(a, b) {
    let add = a + b;
    console.log(`La suma de ${a} (a) y ${b} (b) es: ${add}`)
}
addNumbers(34, 35)

// Función sin parámetros y con retorno
function getNumber() {
    return 7
}
console.log("El número obtenido es: " + getNumber())

// Función con un parámetro y con retorno
function getNumberByParam(a) {
    return a;
}
console.log("El número pasado por parámetro a la función es: " + getNumberByParam(13))

// Función con varios parámetros y con retorno
function substractionByParam(a, b) {
    return a - b;
}
console.log("La resta del primer parámetro menos el segundo parámetro es: " + substractionByParam(71, 2))

// Función dentro de una función (anidada)
function functionOne(a) {
    return function functionTwo(b) {
        return a + b;
    }
};
console.log("El resultado de la suma mediante funciones anidadas es: " + functionOne(40)(29));

// Variable global
var a = 10
function globalVariable() {
    console.log("El valor de la variable global es: " + a);
};

// Variable local
function localVariable() {
    var a = 20;
    console.log("El valor de la variable local es: " + a);
};

// Math.max y Math.min (máximo y mínimo de un conjunto de números)
var num1 = 10;
var num2 = 5;
var num3 = 8;
var maximo = Math.max(num1, num2, num3);
var minimo = Math.min(num1, num2, num3);
console.log("El máximo es: " + maximo + ", y el mínimo es: " + minimo);

// Math.abs (valor absoluto de un número)
var numeroNegativo = -7;
var valorAbsoluto = Math.abs(numeroNegativo);
console.log("El valor absoluto de " + numeroNegativo + " es: " + valorAbsoluto);

// Variable flecha
const noArgs = () => console.log("¡Hola Mundo! Mediante el uso de flechas");
noArgs();

/*
* DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function exercise(a, b) {
    let count = 0;

    for(let i = 1; i <= 100; i++) {
        let threeMultiple = i % 3 === 0;
        let fiveMultiple = i % 5 === 0;

        if (threeMultiple && fiveMultiple) {
            console.log(a + b);
        }else if (threeMultiple) {
            console.log(a);
        } else if (fiveMultiple) {
            console.log(b)
        } else {
            console.log(i);
            count++;
        }
    }
    
    return count;
}

console.log("Numero de veces que se ha impreso un número: " + exercise("Hola", "Mundo"));