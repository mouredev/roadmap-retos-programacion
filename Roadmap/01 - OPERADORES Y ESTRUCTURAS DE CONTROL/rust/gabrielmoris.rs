// https://doc.rust-lang.org/rust-by-example/
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
    // "Arithmetic";
    let _addition = 5 + 3;
    let _substraction = 10 - 4;
    let _multiplication = 7 * 2;
    let _division = 15 / 3;
    let _module = 17 % 5;

    // "Logic";
    let _and = true && true;
    let _or = true || false;
    let _not = !false;

    // "Comparison";
    let _greather = 2 > 1;
    let _less = 1 < 2;
    let _greather_or_equal = 3 >= 2;
    let _les_or_equal = 2 <= 3;
    let _equal = 1 == 1;
    let _not_equal = 1 != 2;

    // "Identity"
    let mut x = 1;
    let _copy = x;
    let _shared_borrow = &x;
    let _mutable_borrow = &mut x;

    // "Bitwise"

    let _bit_and = 0b1010 & 0b1100;
    let _bit_or = 0b1010 | 0b1100;
    let _bit_xor = 0b1010 ^ 0b1100;
    let _bit_not = !0b1010;
    let _left_shift = 0b1010 << 2;
    let _right_shift = 0b1010 >> 1;

    // Dependency operators
    // let x: i32 = "123".parse()?;
    // It propagates errors by returning the error from the current function early.
    // It can only be used in functions that return a Result or Option type..

    flow_controls();
}

fn flow_controls() {
    print!("Conditionals\n");
    if 10 < 1 {
        return;
    } else if 11 == 10 {
        return;
    } else {
        print!("Hello If\n");
    }

    print!("Loops\n");

    let mut index = 10;

    loop {
        if index % 2 == 0 && index % 3 != 0 && index != 16 {
            print!("{},", index);
        }
        index += 1;
        if index > 55 {
            break;
        }
    }

    print!("\nWhile\n");
    index = 10;

    while index <= 55 {
        if index % 2 == 0 && index % 3 != 0 && index != 16 {
            print!("{},", index);
        }
        index += 1;
    }

    print!("\nFor and Range\n");

    for n in 10..=55 {
        if n % 2 == 0 && n % 3 != 0 && n != 16 {
            print!("{},", n);
        }
    }

    print!("\nMatch\n");

    let number = 13;

    match number {
        1 => println!("One!"),
        2 | 3 | 5 | 7 | 11 => println!("This is a prime"),
        13..=19 => println!("A teen"),
        _ => println!("Ain't special"),
    }

    print!("\nif let\n");
    // For some use cases, when matching enums, match is awkward.
    // All have type `Option<i32>`
    let number = Some(7);

    // The `if let` construct reads: "if `let` destructures `number` into
    // `Some(i)`, evaluate the block (`{}`).
    if let Some(i) = number {
        println!("Matched {:?}!", i);
    }
}
