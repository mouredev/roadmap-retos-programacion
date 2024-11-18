// Rust URL: https://www.rust-lang.org/

// Este es un comentario usando dos diagonales.

/*
*  Comentario en bloque
*
*/

// Variables
fn main() {
    let mut variable = "Esto es una variable con propiedad mutable";
    let variable = "Esta es una variable";
}

// Sombra (Shadowing)
fn main() {
    let x = 3;
    let x = "a";
}

// Constantes
const CONSTANTE: f32 = 1.0;

fn main() {
    // Datos primitivos
    // Enteros con signo
    let a_int: i8 = 1;
    let a_int_suffix = 1i8; // Notación con sufijo

    let a_int_2: i16 = 1;
    let a_int_3: i32 = 1;
    let a_int_4: i64 = 1;
    let a_int_5: i128 = 1;
    let a_uint_6: isize = 1;

    // Enteros sin signo
    let a_uint: u8 = 1;
    let a_uint_2: u16 = 1;
    let a_uint_3: u32 = 1;
    let a_uint_4: u64 = 1;
    let a_uint_5: u128 = 1;
    let a_uint_6: usize = 1;

    // Coma flotante
    let my_float: f32 = 1.0;
    let my_float_2: f64 = 1.0;

    // Caracteres UNICODE
    let my_char: char = 'a';

    // Booleanos
    let a_true: bool = true;
    let a_false: bool = false;

    // Unit (Tupla vacía)
    let my_unit = ();

    // Arrays y Tuplas
    let my_array: [i32; 5] = [1, 2, 3, 4, 5];
    let my_tuple: (i32, f64, u8) = (1, 3.0, 1);

    // Imprime por terminal "¡Hola, [y el nombre de tu lenguaje]!"
    println!("¡Hola, Rust!");
}
