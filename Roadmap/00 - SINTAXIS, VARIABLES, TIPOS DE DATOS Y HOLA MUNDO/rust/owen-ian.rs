////===========================================//
/// 00 - SINTAXIS, VARIABLES Y TIPOS DE DATOS // 
//===========================================//

// URL del sitio web oficial: https://www.rust-lang.org/

// Comentario de una sola línea en Rust

/* Y este es un
comentario de varias
líneas en Rust */

//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//
//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//

fn main() {
    let x = 10; // Variable
  
    let mut y = 5; // Esta es una
    y = 10; // Variable mutable

    const PI: f32 = 1.99; // Constante

    let x = x + 1; // Let let (shadowing) -----------------> 
    println!("Valor de x después del shadowing: {}", x); // Reemplaza el valor anterior de x

//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//
//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//_//
  
    // Cadenas de texto
    let texto: &str = "Cadena de texto"; // Cadena de texto
    let mut string: String = String::from("Cadena de texto mutable"); // Cadena de texto mutable

    // Enteros con signo (Signed)
    let a: i8 = 10; // Entero con signo de 8 bits, puede ser del -128 al 127
    let b: i16 = 10; // Entero con signo de 16 bits, puede ser del -32,768 al 32,767
    let c: i32 = 10; // Entero con signo de 32 bits, puede ser del -2,147,483,648 al 2,147,483,647 -->-->--> [VALOR POR DEFECTO] <--<--<--
    let d: i64 = 10; // Entero con signo de 64 bits, puede ser del -9,223,372,036,854,775,808 al 9,223,372,036,854,775,807
    let e: i128 = 10; // Entero con signo de 128 bits, puede ser del -170,141,183,460,469,231,731,687,303,715,884,105,727 al 170,141,183,460,469,231,731,687,303,715,884,105,727

    // Enteros sin signo (Unsigned)
    let f: u8 = 10; // Entero sin signo de 8 bits, puede ser del 0 al 255
    let g: u16 = 10; // Entero sin signo de 16 bits, puede ser del 0 al 65,535
    let h: u32 = 10; // Entero sin signo de 32 bits, puede ser del 0 al 4,294,967,295 -->-->--> [EL VALOR POR DEFECTO SIGUE SIENDO I32] <--<--<--
    let i: u64 = 10; // Entero sin signo de 64 bits, puede ser del 0 al 18,446,744,073,709,551,615
    let j: u128 = 10; // Entero sin signo de 128 bits, puede ser del 0 al 340,282,366,920,938,463,463,374,607,431,768,211,455

    // Flotantes
    let k: f32 = 3.141592; // Flotante de 32 bits, llega a 6 decimales
    let l: f64 = 3.1415926535897932; // Flotante de 64 bits, llega a 16 decimales

    // Por cierto, en Rust puedes escribir los números con _ cada que te resulte cómodo, por ejemplo:
    // 3.14159_26535_89793_23846_26433
    // 3.141_592_653_589_793_238_462_643_3
    // Ambos ejemplos siguen siendo iguales para la máquina, esto no afecta en absolutamente nada
    // Sino más bien que resulta ser una característica implementada para facilitar la lectura de números largos al desarrollador
    // Te recomiendo separar cada 3, 4 o 5 dígitos, depende tu región, idioma o normas de trabajo.

    let booleano: bool = true; // Verdadero
    let booleano2: bool = false; // Falso
    
    let caracter: char = 'A'; // Carácter

    // POO en Rust
    let tupla: (i32, f64, &str) = (c, l, texto); // Tupla, estructura que puede contener varios elementos con distintos tipos de datos
    let arreglo: [i32; 5] = [1, 2, 3, 4, 5]; // Arreglo (array), estructura que puede contener varios elementos pero un solo tipo de dato

    // Tanto las tuplas como arrays pueden ser variables, variables mutables, constantes, o let let (shadowing)
    // Por ultimo aclaro que si bien yo menciono let let, el termino correcto o al menos mas popular es Shadowing, let let es solo un chiste jajaja

    println!("¡Hola, Rust!"); // Imprimir por terminal
}
