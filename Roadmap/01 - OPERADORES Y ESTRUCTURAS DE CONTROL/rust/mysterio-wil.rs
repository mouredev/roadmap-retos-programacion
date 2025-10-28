/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

fn main() {
    println!("### OPERADORES ###");

    // Operadores Aritméticos
    println!("\n--- Aritméticos ---");
    let (a, b) = (10, 3);
    println!("Suma: 10 + 3 = {}", a + b);
    println!("Resta: 10 - 3 = {}", a - b);
    println!("Multiplicación: 10 * 3 = {}", a * b);
    println!("División: 10 / 3 = {}", a / b);
    println!("Módulo: 10 % 3 = {}", a % b);

    // Operadores Lógicos
    println!("\n--- Lógicos ---");
    println!("AND (true && false): {}", true && false);
    println!("OR (true || false): {}", true || false);
    println!("NOT (!true): {}", !true);

    // Operadores de Comparación
    println!("\n--- Comparación ---");
    println!("Igualdad (10 == 3): {}", 10 == 3);
    println!("Desigualdad (10 != 3): {}", 10 != 3);

    // Operadores de Asignación
    println!("\n--- Asignación ---");
    let mut x = 5;
    x += 2;
    println!("Suma y asignación: x += 2 -> x = {}", x);

    // Operadores de Bits
    println!("\n--- Bits ---");
    let p = 10; // 1010
    let q = 3;  // 0011
    println!("AND a nivel de bits (10 & 3): {}", p & q);
    println!("OR a nivel de bits (10 | 3): {}", p | q);

    /*
     * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
     *   que representen todos los tipos de estructuras de control que existan
     *   en tu lenguaje:
     *   Condicionales, iterativas, excepciones...
     */

    println!("\n### ESTRUCTURAS DE CONTROL ###");

    // Condicionales
    println!("\n--- Condicionales (if, else) ---");
    let edad = 18;
    if edad < 18 {
        println!("Eres menor de edad.");
    } else {
        println!("Eres mayor de edad.");
    }

    // Iterativas
    println!("\n--- Iterativas (for) ---");
    for i in 1..=3 {
        println!("{}", i);
    }

    println!("\n--- Iterativas (while) ---");
    let mut contador = 3;
    while contador > 0 {
        println!("{}", contador);
        contador -= 1;
    }
    
    println!("\n--- Iterativas (loop) ---");
    let mut loop_contador = 0;
    loop {
        println!("Loop infinito (iteración {})", loop_contador);
        if loop_contador == 1 {
            break;
        }
        loop_contador += 1;
    }

    // Manejo de errores (Result y Option)
    println!("\n--- Manejo de errores (match con Result) ---");
    fn dividir(a: f64, b: f64) -> Result<f64, String> {
        if b == 0.0 {
            Err("No se puede dividir por cero".to_string())
        } else {
            Ok(a / b)
        }
    }
    match dividir(10.0, 0.0) {
        Ok(resultado) => println!("Resultado: {}", resultado),
        Err(e) => println!("Error: {}", e),
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que imprima por consola todos los números comprendidos
     * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
     */

    println!("\n### DIFICULTAD EXTRA ###");
    for numero in 10..=55 {
        if numero % 2 == 0 && numero != 16 && numero % 3 != 0 {
            println!("{}", numero);
        }
    }
}
