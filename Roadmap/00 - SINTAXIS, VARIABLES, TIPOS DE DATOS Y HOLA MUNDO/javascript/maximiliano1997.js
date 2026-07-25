/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */


/* SOLUCION: */

// https://www.javascript.com/

/*
    Representacion de comentario en 
    varias lineas.
*/


var variable = 10
let variableLet = 10
const constante = 10

// Primitivos
let primitivo_number = 10
let primitivo_booleano_true = true
let primitivo_booleano_False = false
let primitivo_string = 'String'
let primitivo_null = null
let primitivo_undefined;
let primitivo_bigInt = 123456789012345678901234567890n
let primitivo_Symbol = Symbol('symbol')


console.log('¡Hola, Javascript!')







// comprobaciones en consola
console.log(`
    Variables y Constante: \n
    variable: ${variable}
    variableLet: ${variableLet} 
    constante: ${constante} 
    \n
    Primitivos:
    primitivo_number: ${primitivo_number}   <-- ${typeof primitivo_number}
    primitivo_booleano_true: ${primitivo_booleano_true} <-- ${typeof primitivo_booleano_true}
    primitivo_booleano_False: ${primitivo_booleano_False} <-- ${typeof primitivo_booleano_False}
    primitivo_string: ${primitivo_string} <-- ${typeof primitivo_string}
    primitivo_null: ${primitivo_null} <-- ${typeof primitivo_null} //Curiosa historia sobre porque null es marcado como object en javascript :D
    primitivo_bigInt: ${primitivo_bigInt} <-- ${typeof primitivo_bigInt}
    primitivo_undefined: ${primitivo_undefined} <-- ${typeof primitivo_undefined}
    primitivo_Symbol: ${primitivo_undefined} <-- ${typeof primitivo_Symbol}
    
    `)



// Gracias Mouredev #00
