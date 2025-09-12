// URL: https://www.rust-lang.org/

// This is a one line comment

/*
    This is a multi line comment
*/

fn main() {
    // This is a variable
    let mut my_varianble = 5;
    println!("The value of my_varianble is: {}", my_varianble);
    my_varianble = 6;
    println!("The value of my_varianble is: {}", my_varianble);
    // This is a constant
    let my_constant = 7;
    println!("The value of my_constant is: {}", my_constant);

    // Data types
    // Integer
    // Signed
    // i8, i16, i32, i64, i128, isize
    // Unsigned
    // u8, u16, u32, u64, u128, usize
    let my_integer = 8;
    println!("The value of my_integer is: {}", my_integer);
    // Floating point
    // f32, f64
    let my_float = 9.0;
    println!("The value of my_float is: {}", my_float);
    // Boolean
    let my_boolean = true;
    println!("The value of my_boolean is: {}", my_boolean);
    // Character
    let my_char = '🤡';
    println!("The value of my_char is: {}", my_char);
    // String
    let my_string = "¡Hola, Rust!";
    println!("{}", my_string);
}
