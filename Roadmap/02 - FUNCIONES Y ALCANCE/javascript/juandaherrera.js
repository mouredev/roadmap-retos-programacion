/*
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
 *
*/

function myFunction(text1, text2) {
    let counter = 0;
    for (let number = 1; number <= 100; number++) {
        if (number % 3 === 0 && number % 5 === 0) {
            console.log(text1 + text2);
        } else if (number % 3 === 0) {
            console.log(text1);
        } else if (number % 5 === 0) {
            console.log(text2);
        } else {
            console.log(number);
            counter++;
        }
    }
    return counter;
}

// Ejemplo de uso:
const myVar = myFunction("Hola", "Mundo");
console.log("----------------------------");
console.log(myVar);
