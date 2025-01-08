// https://www.rust-lang.org/

// Esto es un comentario simple

// Si se desea escribir un comentario multilinea
// debemos colocar '//' en cada linea del mismo.

/// Para documentar items dentro de paquetes o crates podemos emplear '///', que aparecera 
/// a continuacion del item que queramos explicar. Ademas tiene soporte para Markdown 
/// enriqueciendo la documentacion con code snippets

//! Si se quisiera dar una explicacion general del paquete o create usariamos '//!'


// Variables (inmutables en Rust por defecto)
let my_variable = 5;
let mut my_variable_2 = 3; // Mutable

// Constantes
static LANG = "Rust"; // Imposible asignar otro valor despues de la def.
const INFO = "Dev"; // Variable que puede mutar dentro de un 'static lifetime

// Tipos Primitivos

// Enteros con signo
let my_int: i8 = 1;
let my_int_suffix = 1i8; // Notacion con sufijo

let my_int_2: i16 = 1;
let my_int_3: i32 = 1;
let my_int_4: i64 = 1;
let my_int_5: i128 = 1;

// Enteros sin signo
let my_uint_2: u16 = 1;
let my_uint_3: u32 = 1;
let my_uint_4: u64 = 1;
let my_uint_5: u128 = 1;

// Coma flotante
let my_float: f32 = 1.0;
let my_float_2: f64 = 1.0;

// Caracteres UNICODE
let my_char: char = 'a';

// Booleanos
let my_bool: bool = true;

// Unit(Tupla vacia)
let my_unit = ();

// Arrays y Tuplas
let my_array: [i32; 5] = [1, 2, 3, 4, 5];
let my_tuple: (i32, f64, u8) = (1, 3.0, 1);

println!("Hola, Rust!");
