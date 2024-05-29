// https://doc.rust-lang.org/book/

// Comentario de una línea
/* Comentario de
varias líneas */

fn main() {
    let mut name = "Diego";
    let greeting = "Hello";

    //------- Integers

    // Unsigned
    let u8 = 20u8;
    let u16 = 20u16;
    let u32 = 20u32;
    let u64 = 20u64;
    let u128 = 20u128;

    // Signed
    let i8 = 20i8;
    let i16 = 20i16;
    let i32 = 20i32;
    let i64 = 20i64;
    let i128 = 20i128;

    //------- Floating
    let f64 = 3.0;
    let f32: f32 = 3.0;

    //------- Boolean
    let boolean = false;

    //------- Character
    let character = 'c';

    //------- Tuple
    let tuple: (i32, f64, u8) = (500, 3.0, 20);

    //------- Array
    let months = ["January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"];
    let a: [i32; 5] = [1, 2, 3, 4, 5];
    let a = [3; 5];

    println!("¡Hola, Rust!")
}