/* 
Sitio web oficial:
https://www.rust-lang.org/es
*/

// Sitio web oficial: 
// https://www.rust-lang.org/es

fn main(){
    let mut variable = "Esto es una variable"; // variable mutable
    let constante = "Esto es una constante"; // variable inmutable
    const PI: f32 = 3.1416; // const must be declared with a type

    // INT 
    let entero8: i8= 126; // -128 to 127
    let unsigned_entero: u8 = 254; // 0 to 255
    let entero16: i16 = 16; // -32768 to 32767
    let entero32: i32 = 32; // -2147483648 to 2147483647
    let entero64: i64 = 64; // -9223372036854775808 to 9223372036854775807
    let entero128: i128 = 128; // -170141183460469231731687303715884105728 to 170141183460469231731687303715884105727

    // Each type of integer can be either signed (positive and negative) or unsigned (just positive)
    // Signed: i8, i16, i32, i64, i128
    // Unsigned: u8, u16, u32, u64, u128
    
    // FLOAT
    let flotante32: f32 = 32.0; // 32-bit floating point
    let flotante64: f64 = 64.0; // 64-bit floating point

    // BOOLEAN
    let booleano: bool = true;

    // CHAR
    let caracter: char = 'a';

    // STRING
    let cadena: &str = "Hola, Rust!"; // Static
    let string1: String = String::from("Rust"); // Dynamic like a vector
    

    // ARRAY
    let arreglo: [i32; 5] = [1, 2, 3, 4, 5]; // [type; number of elements]

    // TUPLE
    let tupla: (i32, f64, u8) = (500, 6.4, 1); // (type, type, type)

    // PRINT
    println!("¡Hola, {}!", string1);

}