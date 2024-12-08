// Sitio Web Oficial de rust
// https://www.rust-lang.org

/*
    rust sigue la misma lógica de comentarios que c++ para los comentarios no documentales,
    por lo que para los comentarios multilínea se utiliza el mismo método.
    
    Para los documentales se utiliza otro formato pero a su vez siempre siguen la misma lógica
    de utilizar comentarios de una línea o multilínea.

    referencia:
    https://doc.rust-lang.org/reference/comments.html
*/

fn main(){
    // Variables
    let _x = "Hello, World!";
    let mut _y = 5;
    const _DOS_HORAS_EN_SEGUNDOS: u32 = 60 * 60 * 2;

    // Tipos de datos
    let _entero: i32 = 5;
    let _flotante: f32 = 3.14;
    let _booleano: bool = true;
    let _caracter: char = 'a';
    let _tupla: (i32, f64, u8) = (500, 6.4, 1);
    let _arreglo: [i32; 5] = [1, 2, 3, 4, 5];
    let string: String = String::from("rust");

    // Imprimir
    println!("¡Hola, {string}!");

}

