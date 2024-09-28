/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
*/

fn main(){
    // Función recursiva
    fn countdown(number: i32) {

        if number > 0 {
            println!("{}", number);
            countdown(number - 1)
        }
    }
    countdown(100);

    // EJERCICIO EXTRA
    // Numero factorial
    fn factorial(number: i32) -> i32 {
        if number < 0 {
            println!("Los números negativos no están permitidos");
            return 0;
        } else if number == 0 {
            return 1;
        }
        
        number * factorial(number - 1)
    }
    println!("El resultado de la factorial es: {}", factorial(5));

    // Sucesión Fibonacci
    fn fibonacci(position: i32) -> i32{
        if position <= 0 {
            println!("Los números negativos no están permitidos");
            return 0;
        } else if position == 1 {
            return 0;
        } else if position == 2 {
            return 1;
        } else {
            fibonacci(position - 1) + fibonacci(position - 2)
        }
    }
    println!("El numero en la sucesión de fibonacci es: {}", fibonacci(10));
}