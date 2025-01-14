/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* EXCEPCIONES 
-----------------------------------------
- Rust no tiene excepciones. En cambio, tiene el tipo Result<T, E> para errores recuperables y 
  el macro panic! que detiene la ejecución cuando el programa encuentra un error irrecuperable.

- Mas info: https://www.rustlang-es.org/rust-book-es/ch09-00-error-handling.html

* Errores recuperables (Result<T, E>) 
- 'T' representa el tipo del valor que será devuelto en un caso de éxito dentro de la variante Ok
- 'E' representa el tipo del error que será devuelto en un caso de fallo dentro de la variante Err.
*/

fn main() {
    /* ________________________________________________________________________
    * EJERCICIO 1
    * Fuerza un error en tu código, captura el error, imprime dicho error
      y evita que el programa se detenga de manera inesperada.
    - Prueba a dividir "10/0".
    - Acceder a un índice no existente.
    */
    println!("EJERCICIO 1");

    divide(10, 0);

    // _________________
    let vector = vec![1, 2, 3];
    match index_access(&vector, 7) {
        Ok(valor) => println!("El valor es: {}", valor),
        Err(err) => println!("Error: {}", err),
    }

    /* ________________________________________________________________________
    * EJERCICIO 2
    * Crea una función que sea capaz de procesar parámetros, pero que también
    * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
    * corresponderse con un tipo de excepción creada por nosotros de manera
    * personalizada, y debe ser lanzada de manera manual) en caso de error.
    * - Captura todas las excepciones desde el lugar donde llamas a la función.
    * - Imprime el tipo de error.
    * - Imprime si no se ha producido ningún error.
    * - Imprime que la ejecución ha finalizado. 
    */
    println!("\nEJERCICIO 2");

    divide(10, 0);
    divide(10, 5);
    divide(10, -2);
    divide(10, 2);

}
enum DivisionError {
    DivisionByZero,
    OddNumber,
    NegativeNumber,
}

fn division(a: i32, b: i32) -> Result<f32, DivisionError> {
    match b {
        0 => Err(DivisionError::DivisionByZero),
        n if n % 2 != 0 => Err(DivisionError::OddNumber),
        n if n < 0 => Err(DivisionError::NegativeNumber),
        _ => Ok(a as f32 / b as f32),
    }
}

fn index_access(vector: &Vec<i8>, index: usize) -> Result<i8, &'static str> {
    if index < vector.len() {
        Ok(vector[index])
    } else {
        Err("Índice fuera de rango")
    }
}

fn divide(a: i32, b: i32) {
    match division(a, b) {
        Ok(resultado) => println!("\n- El resultado es: {} \n- No ocurrió ningún error.", resultado),
        Err(error) => match error {
            DivisionError::DivisionByZero => println!("\nError: No es posible dividir entre 0."),
            DivisionError::OddNumber => println!("\nError: No dividir entre impares."),
            DivisionError::NegativeNumber => println!("\nError: No se permiten divisores negativos."),
        }
    }
    println!("- Operación terminada.");
}
