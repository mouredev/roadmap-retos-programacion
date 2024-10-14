// Url oficial de Rust: https://www.rust-lang.org/es

// Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...)

// Esto es un comentario de una una línea

/*
Los comentarios de multiples líneas
van entre /* */
*/

/// Con una triple barra antes de una función, estructura, etc... se crea la documentación
///
/// Al colocarnos sobre el nombre de la funcion (suma en este caso)
/// aparecerán los comentarios de la documentación
///
/// Esta es una función para sumar 2 números
fn suma(a: i32, b: i32) -> i32 {
    return a + b
}

/*
Una forma especial de "comentar" un bloque de código podría ser el que se declara con
#[cfg(never)]
No es un comentario como tal pero se puede usar de forma similar.
Útil para probar algo desactivando una parte del codigo sin tener que borrarlo
 */

fn reto00() {
    // Crea una variable (y una constante si el lenguaje lo soporta)
    // Las variables se declaran con let y las constantes con const
    let number: i8 = 1;
    const LANGUAGE: &str = "Rust";

    // Crea variables representando todos los tipos de datos primitivos
    let text: &str = "Hello, World!";
    // Aquí llamamos al metodo from de la clase String
    let text2: String = String::from("Hello, World!");

    let boolean: bool = false;
    let character: char = 'A';

    let float: f64 = 3.14;
    let integer_unsigned: u8 = 255;
    let integer: i32 = -10;
    let isize_unsigned: usize = 255;
    let isize: isize = 42;

    let _tuple: (i8, &str, &str, String, bool, char, f64, u8, i32, usize, isize) = (number, LANGUAGE, text, text2, boolean, character, float, integer_unsigned, integer, isize_unsigned, isize);
    let _array: [i8; 10] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let mut _vector: Vec<i8> = Vec::new();
    _vector.push(1);
    _vector.push(2);

    println!("¡Hola, {}!", LANGUAGE);

    let result = suma(1,2);
    println!("La suma es: {}", result);
}

fn main() {
    reto00();
}


