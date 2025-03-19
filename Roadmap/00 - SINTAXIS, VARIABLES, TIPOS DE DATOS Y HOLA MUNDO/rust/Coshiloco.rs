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


// URL del sitio web oficial del lenguaje de programación: https://www.rust-lang.org/

// Comentario de una línea

/*
Comentario 
Multilinea
*/

// Creación de una variable
let mut variable = 10;

// Creación de una constante 
const PI: f64 = 3.14159265358979323846264338327950288;

// Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...)
let cadena = "Hola, Rust!";
let entero = 42;
let booleano = true;
let flotante = 5.87;


fn main() {
    // Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    println!("{}", cadena);
}
