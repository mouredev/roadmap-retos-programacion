// * EJERCICIO:
//  * - Crea ejemplos de funciones básicas que representen las diferentes
//  *   posibilidades del lenguaje:
//  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
//  * - Comprueba si puedes crear funciones dentro de funciones.
//  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

//  * - Debes hacer print por consola del resultado de todos los ejemplos.
//  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

//  * - Ejemplo de función sin parámetros ni retorno
function saludar() {
    console.log('Hola, ¿cómo estás?');
}
saludar();

//  * - Ejemplo de función con un parámetro y sin retorno
function saludarPersona(nombre) {
    console.log('Hola, ' + nombre);
}
saludarPersona('Elianis');

//  * - Ejemplo de función con un parámetro y con retorno
function sumar(a, b) {
    return a + b;
}
console.log(sumar(2, 3));

//  * - Ejemplo de función con varios parámetros y con retorno
function multiplicar(a, b, c) {
    return a * b * c;
}
console.log(multiplicar(2, 3, 4));

//  * - Ejemplo de función con retorno y función dentro de función
function calcular(a, b) {
    function sumar(a, b) {
        return a + b;
    }
    return sumar(a, b);
}
console.log(calcular(2, 3));

//  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
console.log(Math.random());

//  * - Crea una función que reciba un número y devuelva si es par o impar.
function parImpar(numero) {
    if (numero % 2 === 0) {
        return 'El número es par';
    } else {
        return 'El número es impar';
    }
}
console.log(parImpar(2));


function imprimirTexto(texto1, texto2) {
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(texto1 + texto2);
        } else if (i % 3 === 0) {
            console.log(texto1);
        } else if (i % 5 === 0) {
            console.log(texto2);
        } else {
            console.log(i);
        }
    }

}
imprimirTexto('Hola', 'Mundo');







