/*COMENTARIOS MULTLINEA
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
 * - Representa las diferentes sintaxis que existen de crear comentarioss
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
*/
// URL del sitio web oficial de Rust
// https://www.rust-lang.org/
// Comentario de una línea
/*
 * Comentario
 * Multilínea
 */

 fn main() {
    // Las variables en Rust son inmutables por defecto
    // Para hacerlas mutables se debe agregar la palabra reservada mut
    // Para declarar una variable se utiliza la palabra reservada let
    //Rust puede inferir el tipo de dato de la variable, pero también se puede especificar el tipo de dato

    // Variables

    let variable = 10; //i32 es el tamaño de la variable
                       // variable = 20; //Error, la variable es inmutable por defecto
    let mut variable_mut = 20; //Se puede cambiar el valor de la variable
    variable_mut = 30; //Ahora sí se puede cambiar el valor de la variable

    // Constante
    const PI: f32 = 3.1416; //Las constantes se declaran con la palabra reservada const y se debe especificar el tipo de dato

    // Tipos de datos primitivos

    //Enteros con signo
    let entero: i8 = -10; //i8, i16, i32, i64, i128, isize
    let _entero_i64: i64 = 1_000_000_000; // Se pueden usar guiones bajos para mejorar la legibilidad

    //Enteros sin signo
    let entero_sin_signo: u8 = 10; //Igualmente se pueden usar u16, u32, u64, u128, usize

    //Punto flotante
    let flotante: f32 = 10.5; //f32, f64

    //Booleano
    let booleano = true; //false

    //Valores unicode
    let caracter = 'a'; //Se pueden usar comillas simples para representar un solo caracter

    //Cadena de texto
    let cadena: &str = "¡Hola, Rust!"; //Las cadenas de texto son inmutables por defecto

    // Imprimir por terminal
    println!("Constante: {}", PI);
    println!("Variable mutable: {}", variable_mut);
    variable_mut = 40; //Se puede cambiar el valor de la variable
    println!("Variable mutable: {}", variable_mut);
    println!("Variable: {}", variable);
    println!("¡Hola, Rust!"); //Se puede imprimir una cadena de texto directamente
    println!("{}", cadena); //También se puede imprimir una variable, los {} son marcadores de posición en esa posición se imprimirá el valor de la variable
    println!("Entero con signo: {}", entero);
    println!("Entero sin signo: {}", entero_sin_signo);
    println!("Punto flotante: {}", flotante);
    println!("Booleano: {}", booleano);
    println!("Caracter: {}", caracter);
}
