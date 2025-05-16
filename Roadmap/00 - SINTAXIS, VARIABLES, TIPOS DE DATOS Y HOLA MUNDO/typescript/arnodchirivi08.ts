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

//Url oficial https://www.typescriptlang.org/
/*
    Varias
    lineas
    comentarios
*/

//Variables y constantes
let firstName;
var lastName;
const nameLanguage= 'Typescript';

// Tipos de datos primitivos
let isEnabled: boolean = true;
let numberOne: number = 1;
let nameText: string = 'Carolina';
let valueNull: null = null;
let valueUndefined: undefined= undefined
const id = Symbol('id');
const numberBig: BigInt = 1234567890123456789012345678901234567890n;

// Tipos de datos adicionales
let nombres: string[] = ["Ana", "Juan", "María"];
let persona: [string, number, boolean] = ["Carlos", 35, true];
enum Color {
    Rojo, 
    Verde, 
    Azul
}

console.log("¡Hola, Typescript!");