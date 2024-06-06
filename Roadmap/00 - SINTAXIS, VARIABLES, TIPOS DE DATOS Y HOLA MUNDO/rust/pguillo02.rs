fn main(){
    println!("Hola mundo");

    //En rust podemos tener variables mutables e inmutables 

    let mut x = 5;

    let y = 5

    let entero_signed: i32 = -42; // Entero con signo de 32 bits
    let entero_unsigned: u64 = 42; // Entero sin signo de 64 bits

    let flotante_f32: f32 = 3.14; // Punto flotante de 32 bits
    let flotante_f64: f64 = 3.14159; // Punto flotante de 64 bits

    let verdadero: bool = true;
    let falso: bool = false;

    let caracter = 'a'; // Carácter Unicode, Rust infiere el tipo (char por defecto)

    let cadena_str = "Hola, mundo!"; // Cadena de texto en formato UTF-8 (tipo &str)
    let cadena_string = String::from("¡Hola, mundo!"); // Cadena de texto en formato UTF-8 mutable (tipo String)
}
