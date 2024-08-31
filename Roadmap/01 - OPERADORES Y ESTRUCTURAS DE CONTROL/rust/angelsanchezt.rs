/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

fn main() {
    // Operadores aritméticos
    let a = 10;
    let b = 5;
    println!("Suma: {}", a + b);
    println!("Resta: {}", a - b);
    println!("Multiplicación: {}", a * b);
    println!("División: {}", a / b);
    println!("Módulo: {}", a % b);

    // Operadores lógicos
    let x = true;
    let y = false;
    println!("AND lógico: {}", x && y);
    println!("OR lógico: {}", x || y);
    println!("NOT lógico: {}", !x);

    // Operadores de comparación
    let c = 15;
    let d = 20;
    println!("Igualdad: {}", c == d);
    println!("Desigualdad: {}", c != d);
    println!("Mayor que: {}", c > d);
    println!("Menor que: {}", c < d);

    // Operadores de asignación
    let mut e = 25;
    e += 5;
    println!("Operador de asignación: {}", e);

    // Operadores de identidad
    let f = "Hola";
    let g = "Hola";
    let h = "Mundo";
    println!("Igualdad de referencias: {}", f == g);
    println!("Desigualdad de referencias: {}", f != h);

    // Operadores de pertenencia
    let nums = vec![1, 2, 3, 4, 5];
    let num_to_check = 3;
    println!("Pertenencia: {}", nums.contains(&num_to_check));

    // Operadores de bits
    let i = 0b1100; // Representación binaria de 12
    let j = 0b1010; // Representación binaria de 10
    println!("AND a nivel de bits: {:b}", i & j);
    println!("OR a nivel de bits: {:b}", i | j);
    println!("XOR a nivel de bits: {:b}", i ^ j);
    println!("Desplazamiento a la derecha: {:b}", i >> 1);
    println!("Desplazamiento a la izquierda: {:b}", i << 1);

    // Estructuras de control condicionales
    let number = 42;
    if number > 30 {
        println!("El número es mayor que 30");
    } else {
        println!("El número es menor o igual a 30");
    }

    // Estructuras de control iterativas
    for num in 10..=55 {
        if num % 2 == 0 && num != 16 && num % 3 != 0 {
            println!("{}", num);
        }
    }
}
