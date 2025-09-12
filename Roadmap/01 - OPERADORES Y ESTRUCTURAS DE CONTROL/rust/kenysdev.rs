/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝

-----------------------------------------
* OPERADORES Y ESTRUCTURAS DE CONTROL
-----------------------------------------
*/ 
#[allow(unused_assignments)] // no advertencia de asignaciones. 
fn main() {
    let a: i8 = 10;
    let b: i8 = 2;
    let mut r: i8;
    // ______________________________________
    // * OPERADORES
    // - Operadores aritmeticos
    r = a + b; // addition
    r = a - b; // subtraction
    r = a * b; // multiplication
    r = a / b; // division
    r = a % b; // remainder
    r = (4 + 2) * 3 / 2; // Combined
    println!("Aritmetico: {}", r);

    // ______________________________________
    // - Operadores de Asignación
    r = a;  // 10
    r += b; // 12
    r -= b; // 10
    r *= b; // 20
    r /= b; // 10
    r %= b; // 0
    println!("Asignación: {}", r);

    // ______________________________________
    // - Operadores de Comparación
    let mut boolean: bool;
    boolean = a == b; // igual a
    boolean = a != b; // diferente de
    boolean = a < b;  // menor que
    boolean = a > b;  // mayor que
    boolean = a <= b; // menor o igual
    boolean = a >= b; // mayor o igual
    println!("Comparación: {}", boolean);

    // ______________________________________
    // - Operadores Lógicos
    boolean = a == b && 5 != 6; // and
    boolean = a > b || 6 < 5;  // or
    boolean = !(a == b);       // not 
    println!("Logicos: {}", boolean);

    // ______________________________________
    // - Operadores Bit a Bit
    r = a & b;  // AND   
    r = a | b;  // OR
    r = a ^ b;  // XOR
    r = !a;     // NOT
    r = a << b; // izquierda
    r = a >> b; // derecha
    println!("Logicos: {}", r);

    // ______________________________________
    // * ESTRUCTURAS DE CONTROL
    // - Condicinales
    if a > b {
        boolean = true;
    }

    // con else
    if a > b {
        boolean = true;
    } else{
        boolean = false;
    }

    // con múltiples condiciones
    let mut st = "";
    if a > b {
        st = "a > b";
    } else if a < b {
        st = "a < b";
    } else if a == b{
        st = "a = b";
    } else {
        st = "xD"
    }
    println!("{}", st);

    // condicional boolean
    if boolean {
        println!("condicional: true");
    } else{
        println!("condicional: false");
    }

    // Usando if en una declaración let
    let mut num = if boolean {10} else {2};
    println!("{}", num);

    // ______________________________________
    // - Construcción de ramificación (match)
    // mas: https://doc.rust-lang.org/book/ch06-02-match.html
    num = 12;
    match num {
        0 => st = "Es cero",
        1 | 2 => st = "Uno o dos",
        3..=10 => st = "Entre 3 y 10",
        11..=50 if num % 2 == 0 => {
            st = "Entre 11 - 50 y es par"
        }
        _ => st = "Ningun patron",
    }
    println!("{}", st);

    // ______________________________________
    // - Bucles (loop, while y for)
    // loop (una y otra vez para siempre o hasta detener.)
    num = 0;
    loop {
        num += 1;
        println!("{}", num);
        if num == 3 {
            break;
        }
    }
    
    // Devolviendo valores de los bucles
    num = 0;
    let r = loop {
        num += 1;
        if num == 3 {
            break num;
        }
    };
    println!("retorno: {}", r);

    // Etiquetas de bucle
    let mut a = 0;
    'external: loop {
        a += 1;
        println!("external: {}", a);

        let mut b = 0;
        'internal: loop {
            b += 1;
            println!("internal: {}", b);
            if b == 2 {
                break 'internal;
            }
        }
        if a == 3 {
            break 'external;
        }
    }

    // ______________________________________
    // while (Mientras sea true, el bucle se ejecuta).
    // Elimina mucho anidamiento necesario en *loop*.
    num = 0;
    while num < 3 {
        num += 1;
        println!("while: {}", num);
    }

    // ______________________________________
    // for (Iterar y repeticiones específicas).
    let items = [10, 20, 30];
    for i in items {
        println!("item: {}", i);
    }

    // Usando rango específico.
    for n in 0..=3{
        println!("rango: {}", n);
    }

    // para invertir el rango
    for n in (1..4).rev(){
        println!("invertir: {}", n);
    }

    /* ______________________________________
    * Ejercicio:
    ------------
    - Crea un programa que imprima por consola todos
      los números comprendidos entre 10 y 55 (incluidos),
      pares, y que no son ni el 16 ni múltiplos de 3.
    */

    for num in 10..=55{
        if (num % 2 == 0) && (num != 16) && (num % 3 != 0) {
            println!("- {}", num);
        }
    }
}
