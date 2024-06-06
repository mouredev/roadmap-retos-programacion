// no advertencia(variables no utilizadas)
#![allow(unused_variables)] 

/* Comentario de bloque
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝

Web: https://www.rust-lang.org/es/
*/
// Comentarios de una línea

/// * Comentarios de documentación (Doc comments)
/// - genera documentación automáticamente con rustdoc.
/// - Genera la documentación en formato HTML.
/// - https://doc.rust-lang.org/cargo/commands/cargo-doc.html

fn main(){
  // * Variables
  // - Las variables por defecto son inmutables.
  let my_str1 = "Dejar que el compilador infiera el tipo.|";
  let my_str2: &str = "Especificar el tipo.|";
  let mut my_str3 = "variable mutable.|";
  
  /* Constante
  - No se permite usar *mut* con constantes.
  - El tipo del valor debe  especificarse.
  - Se pueden declarar en cualquier ámbito. */
  const MY_CONSTANT: i32 = 12; 

  /* Shadowing
  - Es redefinir una variable existente con el mismo nombre.
  - Permite cambios en el valor y tipo de la variable original
    sin necesidad de mutabilidad. */
  let x = 10;
  let x = x + 10;
  println!("Resultado: {}", x);

  // _________________________________________
  // * Tipos de datos primitivos
  // - Enteros (Decimal, Hex, Octal, Binario)
  let hex = 0x2A;
  let binary = 0b101010;

  // NOTA: se permite '_' en la asignación para más claridad.

  // - Enteros con signo
  let integer: i8 = -128; // a 127
  let integer: i16 = -32_768; // a 32,767
  let integer: i32 = -2_147_483_648; // a .,.,647
  let integer: i64 = 9_223_372_036_854_775_807;
  let integer: i128 = 170; // ...
  let integer: isize = 0; // Conforme a la arquitectura.

  // - Enteros sin signo
  let integer: u8 = 255;
  let integer: u16 = 65_535;
  let integer: u32 = 4_294_967_295;
  let integer: u64 = 18_446_744_073_709_551_615;
  let integer: u128 = 340; // ...
  let integer: usize = 0; // Conforme a la arquitectura.

  // _________________________________________
  // - Tipos de punto flotante
  //   De precisión simple y mas eficiencia.
  let y: f32 = 4.0;

  // De precisión doble pero ligeramente más lento.
  let x = 2.0; // f64
  let x: f64 = 3.0;

  // _________________________________________
  // - El tipo booleano
  let t = true;
  let f: bool = false;

  // _________________________________________
  // - Tipo de dato texto
  //   char: tamaño de cuatro bytes y representa un valor escalar Unicode
  //   (Letras acentuadas, Caracteres chinos, japoneses y coreanos; Emojis).
  let my_char: char = 'a';

  // "slice de cadena" y solo puede ser inmutable.
  let my_str: &str = "variable";

  // cadena de texto dinámica.
  let mut _my_string: String = String::from("abc");

  // _________________________________________
  println!("{} {} {} {}", 
  my_str1, my_str2, my_str3, MY_CONSTANT);

  my_str3 = "¡Hola, Rust!";
  println!("{my_str3}");

}
