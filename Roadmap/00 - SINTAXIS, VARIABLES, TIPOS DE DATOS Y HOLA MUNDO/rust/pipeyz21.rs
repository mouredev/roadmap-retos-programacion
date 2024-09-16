// Sitio web Rust: https://www.rust-lang.org/

// Comentario de una línea

/*  
    Comentario 
    de
    multiples
    lineas 
*/

fn main() {
    // Crear una variable
    let var_inmutable = 50;      // variable inmutable
    let mut var_mutable: u8 = 5;  // variable mutable
    const NUM_EULER = 2.71  // constante

    // Crear variables representado los tipos primitivos
    // Variables númericas enteras -> existen de 8, 16, 32 y 64 bits
    let num: u8 = 1;        // u: negativos y positivos 
    let num_neg: i8 = -1;   // i: solo toma valores positivos

    // variables númericas flotantes -> existen de 32 y 64 bits
    let num_pi = 3.1416;

    // variables booleanas
    let verdadero = true;
    let falso = false;

    // variables de cadena de texto
    let a: char = 'a';      // caracter
    let b: &str = "cadena de caracteres";
    let c: String = String::from("¡Hola Rust!"); 

    println!("{}", c)
}