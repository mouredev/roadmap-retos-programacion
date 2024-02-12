/// 01 - OPERADORES Y ESTRUCTURAS DE CONTROL
fn main() {
    // Variables
    let a = 10;
    let b = 4;

    // Operadores aritméticos
    println!("Suma {a} + {b} = {}", a + b);
    println!("Resta {a} - {b} = {}", a - b);
    println!("Multiplicación {a} * {b} = {}", a * b);
    println!("División {a} / {b} = {}", a / b);
    println!("Módulo {a} % {b} = {}", a % b);

    // Operadores de comparación
    println!("¿{a} es == {b}? {}", a == b);
    println!("¿{a} es != {b}? {}", a != b);
    println!("¿{a} es > {b}? {}", a > b);
    println!("¿{a} es < {b}? {}", a < b);
    println!("¿{a} es >= {b}? {}", a >= b);
    println!("¿{a} es <= {b}? {}", a <= b);

    // Operadores lógicos
    println!("AND: ¿{a} es > 0 y {b} es > 0? {}", a > 0 && b > 0);
    println!("OR: ¿{a} es > 0 o {b} es > 0? {}", a > 0 || b > 0);
    println!("NOT: ¿{a} es lo contrario < 0? {}", !(a > 0));

    // Operadores de asignación
    let mut number = 4;
    println!("{number}");
    number += 1;
    println!("{number}");
    number -= 1;
    println!("{number}");
    number *= 2;
    println!("{number}");
    number /= 2;
    println!("{number}");
    number %= 2;
    println!("{number}");

    // Operadores de bits
    println!("AND: {a} & {b} = {}", a & b); // 1010 & 0100 = 0000
    println!("OR: {a} | {b} = {}", a | b); // 1010 | 0100 = 1110
    println!("XOR: {a} ^ {b} = {}", a ^ b); // 1010 ^ 0100 = 1110
    println!("NOT: !{a} = {}", !a); // ~1010 = 0101

    println!("Desplazamiento izquierda 10 << 2 = {}", a << 2); // 1010 << 2 = 101000
    println!("Desplazamiento derecha 10 >> 2 = {}", a >> 2); // 1010 >> 2 = 0010

    // Condicionales
    if a > b {
        println!("{a} es mayor que {b}");
    } else if a < b {
        println!("{a} es menor que {b}");
    } else {
        println!("{a} es igual que {b}");
    }

    // Ternario
    let max = if a > b { a } else { b };
    println!("{max}");

    // Match
    let a = 3;
    match a {
        1 | 2 => println!("Es 1 o 2"),
        3 => println!("Es 3"),
        4 => println!("Es 4"),
        _ => println!("Es otro número"),
    }

    // Bucles
    let mut i = 0;
    while i < 5 {
        println!("{i}");
        i += 1;
    }

    for i in 0..5 {
        println!("{i}");
    }

    // Dibuja el rango 0 a 5 inclusive
    for i in 0..=5 {
        println!("{i}");
    }

    // Bucle for-each
    let numbers = [1, 2, 3, 4, 5];
    for number in numbers.iter() {
        println!("{number}");
    }

    // Bucle infinito
    let mut i = 0;
    loop {
        if i == 5 {
            break;
        }
        println!("{i}");
        i += 1;
    }

    // Extra
    println!("Extra:");
    for i in 10..=55 {
        if i == 16 || i % 2 != 0 || i % 3 == 0 {
            continue;
        }
        println!("{i}");
    }
}
