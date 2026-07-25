//==========================
// 02 - FUNCIONES Y ALCANCE
//==========================

fn main() {
    // Función sin parámetros y sin retorno
    fn saludar() {
        println!("¡Hola, mundo!");
    }
    saludar();

    // Función con un parámetro y sin retorno
    fn saludar_persona(nombre: &str) {
        println!("¡Hola, {}!", nombre);
    }
    saludar_persona("Owen");

    // Función con múltiples parámetros y retorno
    fn suma(a: i32, b: i32) -> i32 {
        a + b
    }
    println!("Suma: {}", suma(10, 3));

    // Función con retorno implícito
    fn resta(a: i32, b: i32) -> i32 {
        a - b
    }
    println!("Resta: {}", resta(10, 3));

    // Función con retorno múltiple
    fn division(a: i32, b: i32) -> (i32, i32) {
        (a / b, a % b)
    }
    let (cociente, resto) = division(10, 3);
    println!("División: {} (cociente) y {} (resto)", cociente, resto);

    // Función con argumentos variables
    fn promedio(args: &[i32]) -> f64 {
        let sum: i32 = args.iter().sum();
        sum as f64 / args.len() as f64
    }
    let numeros = vec![1, 2, 3, 4, 5];
    println!("Promedio: {}", promedio(&numeros));

    // Variables LOCAL y GLOBAL
    let x: i32 = 5; // variable LOCAL
    fn usa_variable() {
        static Y: i32 = 10; // variable GLOBAL
        println!("Y: {}", Y);
    }
    usa_variable();
    println!("X: {}", x);

    // Función anidada
    fn funcion_externa() {
        println!("Función externa");

        fn funcion_interna() {
            println!("Función interna");
        }
        funcion_interna();
    }
    funcion_externa();

    // DIFICULTAD EXTRA
    fn imprimir_multiplos(param1: &str, param2: &str) -> i32 {
        let mut contador = 0;
        for i in 1..=100 {
            if i % 3 == 0 && i % 5 == 0 {
                println!("{}{}", param1, param2);
            } else if i % 3 == 0 {
                println!("{}", param1);
            } else if i % 5 == 0 {
                println!("{}", param2);
            } else {
                println!("{}", i);
                contador += 1;
            }
        }
        contador
    }
    let veces_impreso = imprimir_multiplos("Fizz", "Buzz");
    println!("Veces que se ha impreso el número en lugar de los textos: {}", veces_impreso);
}
