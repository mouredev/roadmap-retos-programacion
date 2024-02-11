//=====================================================
// 00 - Sintaxis, variales, tipos de datos y hola mundo
//=====================================================

// 1. WEB  OFICIAL
// Rust official documentation: https://www.rust-lang.org

// 2. COMENTARIOS EN RUST
// One line comment
/* Multiple line comments
just like C!!
*/

// CREANDO UNA VARIALE Y UNA CONSTANTE

// Variable
let a = 5;

// Creando una constante:
const GRAVEDAD_TERRESTRE: 9.81;

// CREA VARIABLES REPRESENTANDO TODOS LOS TIPOS DE DATOS

// NOTA: el compilador infiere el tipo de dato y no es necesatio indicarlo, pero se puede hacer.

// Tipo escalar:
  // Tipos integer, pueden ser con signo (i) o sin signo (u): i8, i16, i32, i64, i128, isize, u8, u16, u32, u64, u128, usize.
  let entero_8bits i8 = -128;
  let positivo_8bits u8 = 255;
  let entero_16bits i16 = =-32768;
  let positivo_16bits u16 = 62535;
  let entero_32bits i32 = 42;
  let positivo_32bits u32 = 73;
  let entero_64bits i64 = 137;
  let positivo_64bits u64 = 20000000;
  let entero_128bits i128 = 1;
  let positivo_128bits u128 = 345;
  let entero_arquitectura isize = 546236;
  let positivo_arquitectura usize = 243653426;
  // Tipos integer literals: son enteros en otras notaciones(0x, 0o, 0b)
  let moure_dev = 1_987; //Decimal, sin prefijo, se puede usar _ para leerlo mejor sin que afecte en nada.
  let que_champu = 0x7C3; //Hexadecimal (todos los numeros hexadecimales empiezan por 0x, 7C3 es 1987 en hexadecimal)
  let usas_para = 0o3703; //Octal (notacion octal empieza por 0o)
  let la_barba = 0b11111000011; //Binario (0b indica binario)
  
// Coma flotante (f32 y f64, IEEE-754 standard)
  let x f32 = 1.234;
  let y f64 = -1.23456789;

//Tipo boolean:
let delicioso = true;
let love: = 0; // notacion explicita

// Tipo character (ocupan 4 bytes y represaentan valores Unicode):
let g = 'j';
let v: char = 'B';
let heart = 💓;

// Tipos compuestos: Tupla. almacena varios datos de diferente tipo.
let tuplita: (i32, f64, u8) = (500, 6.4, 1);
// Tipos compuestos: array. Almacena varios valores del mismo tipo.
let array = [1,2,3,4,5];

 //Cadenas de caracteres: para este caso hay que usar la funcion String::from o el metodo .to_string().
 let mi_cadena: String = String::from("mi casa");
 let mi_otra_cadena: String = "mi otra casa".to_string();
 // Seria incorrecto escribir algo como let mi-cadena: String = "mi casa".

 // IMPREME POR PANTALLA "HOLA MUNDO"

 fn main() {
    println("Hola, mundo");
 }