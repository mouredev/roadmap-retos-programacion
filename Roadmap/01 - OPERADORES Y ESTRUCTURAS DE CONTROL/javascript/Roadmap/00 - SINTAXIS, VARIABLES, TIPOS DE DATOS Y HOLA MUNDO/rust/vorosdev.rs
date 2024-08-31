// Documentacion: https://www.rust-lang.org/ 

/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

fn main() {
    // variables
    let _immutable = 12;
    let mut _mutable = ":D";

    // constante
    const _CONSTANT: i32 = 20;

    // tipos de datos primitivos
    let _string: &str = "Rust";
    let _floating32: f32 = 4.1 ;
    let _floating64: f64 = 4.323;
    let _number: i32 = 24;
    let _boolean: bool = true;

    // hello world
    println!("Hola, {}!", _string);
}
