use std::result;

/* EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 */

fn main() {
    println!("Inicio");

// OK
div_result(10, 2);

// Error
div_result(10, 0);
}

fn div_result(first: u32, second: u32) {
    let result = div(first, second);
    if result.is_ok() {
    println!("{}", result.ok().unwrap());
    } else {
        println!("{}", result.err().unwrap());
    }
}

fn div(first: u32, second: u32) -> Result<u32, &'static str> {
    if second == 0 {
        Err("El divisor es igual a cero")
    } else {
        Ok(first / second)
    }
}