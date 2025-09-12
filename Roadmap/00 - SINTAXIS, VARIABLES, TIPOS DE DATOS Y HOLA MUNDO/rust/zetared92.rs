// RETO #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

// La documentación de Rust la podemos encontrar en: https://doc.rust-lang.org/book/

/*
Esto es un comentario
en varias líneas
*/

// Declaración de variables y constantes
fn main() {
    let var = 15; // Variable
    let permittivity = 8.8541878176; // Constante (Permitividad) 


// Tipos de datos primitivos
let character: char = 'Z'; // Caracteres
let integer: i32 = 15; // Int 32bits
let intwithoutsign: u64 = 420; // Int 64bits
let float: f64 = 3.141592; // Flotante 64bits
let boolean: bool = false; // Booleano

// Strings
let str_1: &str = "Hello, Rust!" ;// Cadena de caracteres
let str_2: String = String::from("Hello, Ferris!"); // Cadena de caracteres mutable

// Prints
println!("Hello {}!", "Rust");
println!("Variable: {}", var);
println!("Permittivity Constant: {}", permittivity);
println!("Character: {}", character);
println!("Integer: {}", integer);
println!("Integer without sign: {}", intwithoutsign);
println!("Float: {}", float);
println!("Boolean: {}", boolean);
println!("Strings: {}", str_1);
println!("Mutable String: {}", str_2);
}
