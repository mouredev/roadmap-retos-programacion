
// https://www.rust-lang.org

/*
    Comments
*/

// single-line comment

/*
    this is a
    multi-line comment
*/


/// This Rust program declares variables of different types and prints a greeting message.
fn main(){

    /*
        Vars and Constants
    */

    // The variables that start with _ are not used

    let _x = "4"; // variable inmutable
    let mut _y = "5"; // variable mutable
    const _Z: &str = "6"; // const must have the type

    /*
        Primitive Types
    */

    let _number: u8 = 16; // unsigned 8-bits number, i8 for signed, there are 8, 16, 32, 64 and 128 bits
    let _boolean: bool = true;
    let _floating32: f32 = 2.5;
    let _floating64: f64 = 2.553;
    let _letter: char = 'a';

    println!("¡Hello, Rust!");
}