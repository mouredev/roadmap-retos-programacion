// Documentación en https://prev.rust-lang.org/es-ES/documentation.html

// Comentario en una linea

/*
  Comentario
  en varias
  lineas
*/

fn main() {
    // Declaración de variables y constantes
    let mut lenguaje = String::from("Rust"); // Variable
    let PI = 3.1415; // Constante

    // Tipos de datos primitivos
    let letra: char = 'A'; // Carácter
    let numero: i32 = -1; // Entero con signo de 32 bits
    let numerosinsigno: u64 = 1; // Entero sin signo de 64 bits
    let decimal: f64 = 3.1415; // Punto flotante de 64 bits
    let booleano: bool = true; // Booleano

    //Salida por pantalla
    println!("Hola {}!", lenguaje);
}
