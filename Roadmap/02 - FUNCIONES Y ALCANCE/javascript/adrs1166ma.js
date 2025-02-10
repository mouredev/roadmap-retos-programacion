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


// 🔥 Función sin parámetros ni retorno
function sinParametros() {
    console.log("Función sin parámetros ni retorno");
}
sinParametros();

// 🔥 Función con uno o varios parámetros
function conParametros(a, b) {
    console.log(`La suma de ${a} y ${b} es:`, a + b);
}
conParametros(5, 10);

// 🔥 Función con retorno
function conRetorno(a, b) {
    return a * b;
}
console.log("El producto de 4 y 6 es:", conRetorno(4, 6));

// 🔥 Funciones dentro de funciones
function externa() {
    console.log("Función externa ejecutada");
    function interna() {
        console.log("Función interna ejecutada");
    }
    interna();
}
externa();

// 🔥 Uso de funciones nativas del lenguaje
console.log("Longitud de la palabra 'JavaScript':", "JavaScript".length);

// 🔥 Variables globales y locales
let globalVar = "Soy una variable global";
function testScope() {
    let localVar = "Soy una variable local";
    console.log(globalVar);
    console.log(localVar);
}
testScope();
// console.log(localVar); // Esto generaría un error, ya que localVar es local

// 🔥 Extra
function contarNumeros(texto1, texto2) {
    let count = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(texto1 + texto2);
        } else if (i % 3 === 0) {
            console.log(texto1);
        } else if (i % 5 === 0) {
            console.log(texto2);
        } else {
            console.log(i);
            count++;
        }
    }
    return count;
}

let resultado = contarNumeros("Fizz", "Buzz");
console.log("Cantidad de números impresos en lugar de texto:", resultado);
