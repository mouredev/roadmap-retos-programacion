// Página oficial de TypeScript: https://www.typescriptlang.org

// tipos de comentarios:

// comentario: una línea.
/* comentario: múltiples línea
    línea 1
    línea 2
    línea 3
    línea 4
    línea 5
    línea 6
*/

// variables:

var variable: string = 'es una variable tipo string'; // el uso de var no es aconsejable y no se aconseja
const constante: string = 'este tipo de variable es una constante'; // en este tipo el valor es constante, no puede ser modificado.
let variableLet: string = 'es una variable let tipo string'; // este tipo de variable si admite se modificado su valor

// tipos primitivos de las variables:

let variableNumero: number = 10; // variable tipo número, es de punto flotante o entero, de 64bits
let variableString: string = 'esto es un string'; // variable tipo string, representa una o una secuencia de caracteres.
let variableBoolean: boolean = true; // variable de valor booleano: puede tomar los valores de verdadero o falso.
let variableNull: null = null; // variable con valor nulo
let variableundefined: undefined = undefined; // Variable

// impresión por consola del texto "¡Hola, [nombre del lenguaje]"

console.log("¡Hola, TypeScript!")