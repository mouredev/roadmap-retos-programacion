// The Rust Language doc: http://rust-lang.org 

// This is a single line comment

/* This is a multi line comment
 * that continues here 
 */

fn main() {
    // Variable declaration
    let name : &str = "John";
    println!("Variable declaration -> {name}");

    // Const declaration
    const COLOR : &str = "red";
    println!("Constant declaration -> {COLOR}");

    // Unsigned integers
    let u8_var : u8 = 10;
    println!("u8_var -> {u8_var}");

    let u16_var : u16 = 300;
    println!("u16_var -> {u16_var}");

    let u32_var : u32 = 100000;
    println!("u32_var -> {u32_var}");

    let u64_var : u64 = 100000000;
    println!("u64_var -> {u64_var}");

    let u128_var : u128 = 10000000000000;
    println!("u128_var -> {u128_var}");

    let usize_var : usize = 10000;
    println!("usize_var -> {usize_var}");

    // Signed integers
    let i8_var : i8 = -10;
    println!("i8_var -> {i8_var}");

    let i16_var : i16 = -2300;
    println!("i16_var -> {i16_var}");

    let i32_var : i32 = -70000;
    println!("i32_var -> {i32_var}");

    let i64_var : i64 = -5000000;
    println!("i64_var -> {i64_var}");

    let i128_var : i128 = -1000000000000;
    println!("i128_var -> {i128_var}");

    let isize_var : isize = -10000;
    println!("isize_var -> {isize_var}");

    // Floating point numbers 
    
    let f32_var : f32 = 0.75;
    println!("f32_var -> {f32_var}");

    let f64_var : f64 = 0.79999995;
    println!("f64_var -> {f64_var}");

    // Boolean type
    let bool_var : bool = true;
    println!("bool_var -> {bool_var}");

    // String type
    let string_var : &str = "Hello world";
    println!("string_var -> {string_var}");

    // Char type
    let char_var : char = 'Z';
    println!("char_var -> {char_var}");

    // Array type
    let array_var1 : [u32;4] = [1,2,3,4];
    println!("array_var1 -> {array_var1:?}");
    let array_var2 : [&str;2] = ["Hello", "World"];
    println!("array_var2 -> {array_var2:?}");

    // Slice type
    let slice_var1 : &[u32] = &array_var1[1..3]; 
    println!("slice_var1 -> {slice_var1:?}");
    let slice_var2 : &[&str] = &array_var2[1..];
    println!("slice_var2 -> {slice_var2:?}");

    // Tuple type
    let tuple_var : (u32, &str, bool) = (32, "Bye", false);
    println!("tuple_var -> {tuple_var:?}");

    // Unit type (void)
    let unit_var : () = ();
    println!("unit_var -> {unit_var:?}");

    // Finally send the greet message
    println!("¡Hola, Rust!");
}
