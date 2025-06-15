
 

// - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
//   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

function sinParametrosNiRetorno() {
    console.log("Esta función no tiene parámetros ni retorno.");
}
// Llamada a la función sin parámetros ni retorno
sinParametrosNiRetorno();

function conUnParametro(parametro: string) {
    console.log("Este es un parámetro: " + parametro);
}
// Llamada a la función con un parámetro
conUnParametro("Hola, soy un parámetro");

function conVariosParametros(param1: string, param2: number) {
    console.log("Primer parámetro: " + param1);
    console.log("Segundo parámetro: " + param2);
}
// Llamada a la función con varios parámetros
conVariosParametros("Hola", 42);

function conRetorno(): string {
    return "Este es el valor de retorno.";
}
// Llamada a la función con retorno
const retorno = conRetorno();
console.log("Valor de retorno: " + retorno);

// - Comprueba si puedes crear funciones dentro de funciones.
function funcionConFuncion() {
    function funcionInterna() {
        console.log("Soy una función interna.");
    }
    funcionInterna();
}
// Llamada a la función que contiene una función interna
funcionConFuncion();

// - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
function ejemploFuncionesYaCreadas() {
    const array = [1, 2, 3, 4, 5];
    const suma = array.reduce((acc, val) => acc + val, 0);
    console.log("Suma de los elementos del array: " + suma);
    const maximo = Math.max(...array);
    console.log("Máximo del array: " + maximo);
    const minimo = Math.min(...array);
    console.log("Mínimo del array: " + minimo);
}
// Llamada a la función que utiliza funciones ya creadas
ejemploFuncionesYaCreadas();

// - Pon a prueba el concepto de variable LOCAL y GLOBAL.
let variableGlobal = "Soy una variable global";

function pruebaVariables() {
    let variableLocal = "Soy una variable local";
    console.log(variableLocal);
    console.log(variableGlobal);
}
// Llamada a la función que prueba variables locales y globales
pruebaVariables();

// Dificultad extra
/*
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


//  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
function ejercicioReto(texto1: string, texto2: string): number {
    let contadorNumerosImpresos: number = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${texto1} ${texto2}`);
        } else if (i % 3 === 0) {
            console.log(texto1);
        } else if (i % 5 === 0) {
            console.log(texto2);
        } else {
            console.log(i);
            contadorNumerosImpresos++;
        }
    }

    return contadorNumerosImpresos;
}
// Llamada a la función de dificultad extra
const resultado = ejercicioReto("Oro", "Plata");
console.log("Número de veces que se imprimió un número:", resultado);