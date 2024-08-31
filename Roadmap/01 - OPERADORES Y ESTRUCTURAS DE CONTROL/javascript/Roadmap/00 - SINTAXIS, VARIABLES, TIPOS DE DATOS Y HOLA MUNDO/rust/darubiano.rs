/*
    EJERCICIO:
    1) Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    2) Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    3) Crea una variable (y una constante si el lenguaje lo soporta).
    4) Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    5) Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

// 1) https://www.rust-lang.org/es/

// 2) Comentario de una linea y varias

/*
Comentario de varias lineas
*/
fn main() {
    // 3) Variables son (inmutables en Rust por defecto) y constante
    let variable: &str = "variable";
    let mut variable_mutable: &str = "variable_mutable";
    // Constantes
    const MY_CONST: &str = "constante";

    // 4) Tipos de variables primitivas https://doc.rust-lang.org/rust-by-example/primitives.html
    //Tipos numericos
    // Enteros con signo
    let int: i8 = 1;
    let int_suffix = 1i8;
    let int_i16: i16 = 1;
    let int_i32: i32 = 1;
    let int_i64: i64 = 1;
    let int_i128: i128 = 1;
    // Enteros sin signo
    let uint_u16: u16 = 1;
    let uint_u32: u32 = 1;
    let uint_u64: u64 = 1;
    let uint_u128: u128 = 1;
    // Coma flotante
    let float_f32: f32 = 1.0;
    let float_f64: f64 = 1.0;

    // Tipo de dato texto
    let caracter: char = 'a';
    let variable: &str = "variable";
    let mut texto_mutable: String = String::from("¡Hola, ");

    // Tipos boleanos
    let verdadero: bool = true;
    let falso: bool = false;

    // Tipos arreglos,slices, tuplas y unidad
    let array: [i32; 3] = [1, 2, 3];
    let slice: &[i32] = &array[1..3];
    let tupla: (i32, f64, char) = (42, 3.14, 'A');
    let unidad: () = ();

    // 5) print() hola Go
    println!("¡Hola, Rust!");
}
