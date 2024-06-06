/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝

-----------------------------------------
* FUNCIONES
-----------------------------------------
*/ 
// - Basica
fn hello() {
    println!("hello, world!");
}

// _________________________
// - Con Parámetro:
//   "&" indica paso por referencia inmutable.
fn print(msg: &str) {
    println!("{}", msg);
}

// _________________________
// - Con retorno:
//   Funciona mediante expresiones las cuales
//   evalúan a un valor resultante.
fn sum(a: i32, b: i32) -> i32 {
    a + b
    // Las expresiones no finalizan con ";".
    // usar "return" es opcional.
}

// _________________________
// Función dentro de otra función
fn external(a: i32) -> String {
    fn internal(b: i32) -> i32 {
        b * 2
    }
    format!("Externa: {}", internal(a))
}

// _________________________
// * Ejemplo de funciones y métodos incorporados.
fn native_functions() {
    println!("len: {}", ("123").len());
    println!("lower: {}", ("ABC").to_lowercase());
    println!("upper: {}", ("abc").to_uppercase());
    println!("convert: {}", (12).to_string());
}

/* _________________________
* Ejercicio:
* Crea una función que reciba dos parámetros de tipo 
  cadena de texto y retorne un número.
* La función imprime todos los números del 1 al 100,
  teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de
  texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de 
  texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las  
  dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha 
  impreso el número en lugar de los textos.""")
*/

fn exs(str1: &str, str2: &str) -> i8 {
    let mut total: i8 = 0;
    for n in 1..=100 {
        match (n % 3 == 0, n % 5 == 0) {
            (true, false) => println!("- {str1}"),
            (false, true) => println!("- {str2}"),
            (true, true) => println!("- {str1} - {str2}"),
            _ => {println!("- {n}"); total += 1;}
        }
    }
    return total;
}

// _________________________
fn main() {
    hello();
    print("hello, Rust!");
    println!("Suma: {}", sum(2, 2));
    println!("{}", external(5));
    native_functions();
    println!("\nnúmero de veces: {}", exs("str1", "str2"))
}
