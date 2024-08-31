// progama para mostrar los tipos de operadores de rust

fn main() {

    // operadores de asignacion
    let mut a = 2;
    println!("ASIGNACIÓN:");
    println!("Mostramos el valor de la variable a = {}", a);
    a += 2;
    println!("Sumamos 2 a la variable a = {}", a);
    a -= 2;
    println!("Restamos 2 a la variable a = {}", a);
    a *= 2;
    println!("Multiplicamos por 2 a la variable a = {}", a);
    a /= 2;
    println!("Dividimos por 2 a la variable a = {}", a);
    a %= 2;
    println!("Hacemos el modulo 2 a la variable a = {}", a);
    a = 2;
    println!("Mostramos el valor de la variable a = {}", a);
    a <<= 1;
    println!("Desplazamos a la izquierda 1 bit a la variable a = {}", a);
    a >>= 1;
    println!("Desplazamos a la derecha 1 bit a la variable a = {}", a);
    a &= 1;
    println!("Hacemos un AND a la variable a = {}", a);
    a |= 1;
    println!("Hacemos un OR a la variable a = {}", a);
    a ^= 1;
    println!("Hacemos un XOR a la variable a = {}", a);
    println!();

    // operadores aritmeticos
    let a = 10;
    let b = 5;

    println!("OPERADORES ARITMÉTICOS:");
    println!("a = {}", a);
    println!("b = {}", b);
    println!("a + b = {}", a + b);
    println!("a - b = {}", a - b);
    println!("a * b = {}", a * b);
    println!("a / b = {}", a / b);
    println!("a % b = {}", a % b);
    println!();

    // operadores de comparacion
    let a = 10;
    let b = 5;

    println!("OPERADORES DE COMPARACIÓN:");
    println!("a = {}", a);
    println!("b = {}", b);
    println!("a == b = {}", a == b);
    println!("a != b = {}", a != b);
    println!("a > b = {}", a > b);
    println!("a < b = {}", a < b);
    println!("a >= b = {}", a >= b);
    println!("a <= b = {}", a <= b);
    println!();

    // operadores lógicos
    let a = true;
    let b = false;

    println!("OPERADORES LÓGICOS:");
    println!("a = {}", a);
    println!("b = {}", b);
    println!("a && b = {}", a && b);
    println!("a || b = {}", a || b);
    println!("!a = {}", !a);
    println!();

    // operadores binarios
    let a = 0b1010;
    let b = 0b1100;

    println!("OPERADORES BINARIOS:");
    println!("a = {:b}", a);
    println!("b = {:b}", b);
    println!("a & b = {:b}", a & b);
    println!("a | b = {:b}", a | b);
    println!("a ^ b = {:b}", a ^ b);
    println!("!a = {:b}", !a);
    println!("a << 1 = {:b}", a << 1);
    println!("a >> 1 = {:b}", a >> 1);
    println!();

    // Estructuras de control
    
    // Ejemplo if
    let a = 10;
    let b = 5;
    if a > b {
        println!("a es mayor que b");
    } else {
        println!("a es menor o igual que b");
    }

    // Ejemplo if anidado
    let a = 10;
    let b = 5;
    let c = 15;
    if a > b {
        if a > c {
            println!("a es mayor que b y c");
        } else {
            println!("a es mayor que b pero menor que c");
        }
    } else {
        println!("a es menor o igual que b");
    }
    // Ejemplo loop
    let mut a = 0;
    loop {
        println!("a = {}", a);
        a += 1;
        if a == 10 {
            break;
        }
    }
    // Ejemplo while
    let mut a = 0;
    while a < 10 {
        println!("a = {}", a);
        a += 1;
    }
    // Ejemplo for
    for a in 0..10 {
        println!("a = {}", a);
    }
    // Ejemplo match
    let a = 10;
    match a {
        0 => println!("a es 0"),
        1 => println!("a es 1"),
        2 => println!("a es 2"),
        3 => println!("a es 3"),
        4 => println!("a es 4"),
        5 => println!("a es 5"),
        6 => println!("a es 6"),
        7 => println!("a es 7"),
        8 => println!("a es 8"),
        9 => println!("a es 9"),
        10 => println!("a es 10"),
        _ => println!("a es otro valor"),
    }
    // Ejemplo match con if
    let a = 10;
    match a {
        0 => println!("a es 0"),
        1 => println!("a es 1"),
        2 => println!("a es 2"),
        3 => println!("a es 3"),
        4 => println!("a es 4"),
        5 => println!("a es 5"),
        6 => println!("a es 6"),
        7 => println!("a es 7"),
        8 => println!("a es 8"),
        9 => println!("a es 9"),
        10 => {
            println!("a es 10");
            if a > 5 {
                println!("a es mayor que 5");
            }
        },
        _ => println!("a es otro valor"),
    }
    // Ejemplo match con if anidado
    let a = 10;
    match a {
        0 => println!("a es 0"),
        1 => println!("a es 1"),
        2 => println!("a es 2"),
        3 => println!("a es 3"),
        4 => println!("a es 4"),
        5 => println!("a es 5"),
        6 => println!("a es 6"),
        7 => println!("a es 7"),
        8 => println!("a es 8"),
        9 => println!("a es 9"),
        10 => {
            println!("a es 10");
            if a > 5 {
                println!("a es mayor que 5");
            } else {
                println!("a es menor o igual que 5");
            }
        },
        _ => println!("a es otro valor"),
    }
    // Ejemplo match con if anidado y else if
    let a = 10;
    match a {
        0 => println!("a es 0"),
        1 => println!("a es 1"),
        2 => println!("a es 2"),
        3 => println!("a es 3"),
        4 => println!("a es 4"),
        5 => println!("a es 5"),
        6 => println!("a es 6"),
        7 => println!("a es 7"),
        8 => println!("a es 8"),
        9 => println!("a es 9"),
        10 => {
            println!("a es 10");
            if a > 5 {
                println!("a es mayor que 5");
            } else if a < 5 {
                println!("a es menor que 5");
            } else {
                println!("a es igual que 5");
            }
        },
        _ => println!("a es otro valor"),
    }

    // Extra

    println!("A continuación, el ejemplo extra");

    for a in 10..56 {
        if (a % 2 == 0) && (a != 16) && (a % 3 != 0)
        {
            println!("a = {}", a);
        }            
    }






    









   
}