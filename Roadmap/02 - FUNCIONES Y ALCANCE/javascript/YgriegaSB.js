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

const arreglo = [];
// Llena el arreglo con números del 1 al 100
const fillArray = () => {
    for (let i = 1; i <= 100; i++) {
        arreglo.push(i);
    }
}

// Imprime "Fizz", "Buzz" o "FizzBuzz" en lugar de múltiplos de 3, 5 o ambos
const imprimirFizzBuzz = (cadena1, cadena2) => {
    for (let i of arreglo){
        console.log(
            (i % 3 === 0 && i % 5 === 0) ? `${cadena1}${cadena2}` :
            (i % 3 === 0) ? `${cadena1}` :
            (i % 5 === 0) ? `${cadena2}` : `${i}`
        );
    }
}

fillArray();
imprimirFizzBuzz('Fizz', 'Buzz');
