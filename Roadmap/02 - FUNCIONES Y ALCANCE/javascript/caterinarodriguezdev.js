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

console.log('--------------------FUNCIONES----------------------------');

const funcionSinParams = () => {
    console.log('función sin params');
}

const funcionConUnParam = (x) => {
    console.log(`función con 1 param - la raíz cuadrada de ${x} es: ${Math.sqrt(x)}`);
}

const funcionConVariosParams = (x, y) => {
    console.log(`función con varios params - el número mayor entre ${x} y ${y} es ${Math.max(x, y)}`);
}

const funcionConRetorno = (str) => {
    return str.toUpperCase();
}

const funcionConUnaFuncion = () => {
    const funcionDeDentro = (arr) => {
        return arr.map(el => el * 2);
    }
    console.log('la función de dentro multiplica el array por 2', funcionDeDentro([2, 4, 8]));
}

funcionSinParams();
funcionConUnParam(64);
funcionConVariosParams(5, 10);
console.log('función con retorno - el texto en mayúsculas será:', funcionConRetorno('boom'));
funcionConUnaFuncion(); 

console.log('--------------------LOCAL Y GLOBAL----------------------------');

let global = 'global';

const scope = () => {
    let local = 'local';

    console.log('ejecutando dentro de una función ->', global);

    global = 'He sido cambiada dentro de scope';
}

try {
    console.log(local);
} catch {
    console.error('Error: No puedes acceder a una variable local fuera de su scope');
}

scope();

console.log('global ha cambiado? ', global);



console.log('--------------------DIFICULTAD EXTRA----------------------------');

const dificultadExtra = (str1, str2) => {
    let numberPrinted = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(str1.toString() + str2.toString());
        } else if (i % 3 === 0) {
            console.log(str1);
        } else if (i % 5 === 0) {
            console.log(str2);
        } else {
            numberPrinted++;
            console.log(i);
        }
    }

    return numberPrinted;
}

console.log(`El número se ha imprimido ${dificultadExtra('Fizz', 'Buzz')} veces`);

