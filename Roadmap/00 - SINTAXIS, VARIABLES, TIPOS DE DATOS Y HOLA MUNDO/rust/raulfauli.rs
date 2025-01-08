/// # Documentación en https://www.rust-lang.org/

// Comentario en una linea

/*
    Comentario
    en varias
    lineas
*/
fn main() {
    // Variables
    let y = 10; // Variable inmutable
    let z: i32 = 15; // Variable inmutable con tipo de dato especificado
    let mut x = 5; // Variable mutable

    // Constantes
    const PI: f32 = 3.1415; // Es necesario especificar el tipo de dato

    // Tipos primitivos
    let a: i8 = 127; // Entero de 8 bits
    let b: i16 = 32767; // Entero de 16 bits
    let c: i32 = 2147483647; // Entero de 32 bits
    let d: i64 = 9223372036854775807; // Entero de 64 bits
    let e: i128 = 170141183460469231731687303715884105727; // Entero de 128 bits
    let f: isize = 9223372036854775807; // Entero de 32 o 64 bits dependiendo de la arquitectura

    let g: u8 = 255; // Entero sin signo de 8 bits
    let h: u16 = 65535; // Entero sin signo de 16 bits
    let i: u32 = 4294967295; // Entero sin signo de 32 bits
    let j: u64 = 18446744073709551615; // Entero sin signo de 64 bits
    let k: u128 = 340282366920938463463374607431768211455; // Entero sin signo de 128 bits
    let l: usize = 18446744073709551615; // Entero sin signo de 32 o 64 bits dependiendo de la arquitectura

    let m: f32 = 3.1415; // Flotante de 32 bits
    let n: f64 = 3.1415926535898; // Flotante de 64 bits

    let o: bool = true; // Booleano
    let p: char = 'a'; // Caracter unicode
    let q: &str = "Hola Rust!"; // Cadena de caracteres

    let s: String = String::from("Hola Rust!"); // Cadena de caracteres dinamica

    println!("¡Hola, Rust!");
}
