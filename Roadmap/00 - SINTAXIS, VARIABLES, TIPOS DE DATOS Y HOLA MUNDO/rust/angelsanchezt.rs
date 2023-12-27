// URL del sitio web oficial de Rust: https://www.rust-lang.org

// Comentarios de una línea

/*
  Comentarios
  de
  varias
  líneas
*/

fn main() {
    // Declaración de variables y constantes
    let mut variable_mutable = 42; // Variable mutable
    let constante = 3.14; // Constante

    // Tipos de datos primitivos
    let caracter: char = 'A'; // Carácter
    let entero: i32 = -42; // Entero con signo de 32 bits
    let entero_sin_signo: u64 = 123; // Entero sin signo de 64 bits
    let flotante: f64 = 3.14159; // Punto flotante de 64 bits
    let booleano: bool = true; // Booleano

    // Cadenas de texto
    let cadena_texto: &str = "¡Hola, Rust!"; // Cadena de texto (inmutable)
    let cadena_texto_mut: String = String::from("¡Hola, Rust mutable!"); // Cadena de texto mutable

    // Imprimir por terminal
    println!("¡Hola, {}!", "Rust");
    println!("Valor de la variable mutable: {}", variable_mutable);
    println!("Valor de la constante: {}", constante);
    println!("Carácter: {}", caracter);
    println!("Entero con signo: {}", entero);
    println!("Entero sin signo: {}", entero_sin_signo);
    println!("Punto flotante: {}", flotante);
    println!("Booleano: {}", booleano);
    println!("Cadena de texto (inmutable): {}", cadena_texto);
    println!("Cadena de texto mutable: {}", cadena_texto_mut);
}