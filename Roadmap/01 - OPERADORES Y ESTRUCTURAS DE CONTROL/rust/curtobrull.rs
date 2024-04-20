// Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
// Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

fn aritmeticos() {
    let a: i32 = 25;
    let b: i32 = 5;
    let sum = a + b;
    let diff = a - b;
    let prod = a * b;
    let quot = a / b;
    let rem = a % b;
    println!("a = {}, b = {}", a, b);
    println!("Suma a + b: {}", sum);
    println!("Resta a - b: {}", diff);
    println!("Multiplicación a * b: {}", prod);
    println!("División a / b: {}", quot);
    println!("Módulo a % b: {}", rem);
}

fn incremento_decremento() {
    let mut a: i32 = 25;
    let mut b: i32 = 5;
    println!("a = {}, b = {}", a, b);
    a += 5;
    b -= 5;
    println!("En rust no existen los clásicos ++ o -- de otros lenguajes pero podemos simplemente usar += o -=");
    println!("Incremento (a += 5): {}", a);
    println!("Decremento (b -= 5): {}", b);
}

fn comparacion_relacion() {
    let a: i32 = 25;
    let b: i32 = 5;
    let equal: bool = a == b;
    let not_equal: bool = a != b;
    let greater_than: bool = a > b;
    let less_than: bool = a < b;
    let greater_than_or_equal_to: bool = a >= b;
    let less_than_or_equal_to: bool = a <= b;
    println!("a = {}, b = {}", a, b);
    println!("Igualdad a == b: {}", equal);
    println!("Desigualdad a != b: {}", not_equal);
    println!("Mayor que a > b: {}", greater_than);
    println!("Menor que a < b: {}", less_than);
    println!("Mayor o igual que a >= b: {}", greater_than_or_equal_to);
    println!("Menor o igual que a <= b: {}", less_than_or_equal_to);
}

fn logicos() {
    let bool_true: bool = true;
    let bool_false: bool = false;
    let and: bool = bool_true && bool_false;
    let or: bool = bool_true || bool_false;
    let not: bool = !bool_true;
    println!("AND lógico true && false: {}", and);
    println!("OR lógico true || false: {}", or);
    println!("NOT lógico !true: {}", not);
}

fn bitwise() {
    let a_binary = 1;
    let b_binary = 2;
    println!("Trabajo con bits");
    println!("a_binary = {:b}, b_binary = {:b}", a_binary, b_binary);
    println!("AND a_binary & b_binary: {:b}", a_binary & b_binary);
    println!("OR a_binary | b_binary {:b}", a_binary | b_binary);
    println!("XOR a_binary ^ b_binary: {:b}", a_binary ^ b_binary);
    println!("Desplazamiento a la derecha a_binary >> 1: {:b}", a_binary >> 1);
    println!("Desplazamiento a la izquierda a_binary << 1: {:b}", a_binary << 1);
}

fn condicion_if_else() {
    let number: i32 = 5;
    println!("Comparamos el número {} con 10 (if >, else if < y else), en éste caso entra en el else if", number);
    if number > 10 {
        println!("El número es mayor que 10");
    } else if number < 10 {
        println!("El número es menor que 10");
    } else {
        println!("El número es 10");
    }
}

fn loop_block() {
    let mut count: i32 = 0;
    println!("El contador empezará en 0 y se incrementa en 1 cada iteración, al llegar a 4 se realiza el break.");

    loop {
        println!("Looping con count = {}", count);
        if count == 4 {
            println!("Count ha llegado a 4, Loop terminado");
            break;
        }
        count += 1;
    }
}

fn while_block() {
    let mut count: i32 = 0;
    println!("El contador empezará en 0 y se incrementa en 1 cada iteración, al llegar a 4 ya no cumple la condición (count < 4).");
    while count < 4 {
        println!("While con count = {}", count);
        count += 1;
    }
}

fn for_block() {
    println!("For i in 0..5");
    for i in 0..5 {
        println!("i = {}", i);
    }
}

fn match_block() {
    let number: i32 = 3;
    println!("Comparamos el número {} con 1, 2, 3 o 4 (match number)", number);
    match number {
        1 => println!("El número es 1"),
        2 => println!("El número es 2"),
        3 => println!("El número es 3"),
        4 => println!("El número es 4"),
        _ => println!("El número no es 1, 2, 3 o 4"),
    }
}

fn extra_exercice() {
    println!("Números pares entre 10 y 55 incluidos que no sean ni el 16 ni múltiplos de 3:");
    for i in 10..56 {
        if i != 16 &&
            i % 2 == 0 &&
            i % 3 != 0 {
            print!("{} ", i);
        }
    }
}

fn main() {
    println!("Operadores aritméticos: ");
    aritmeticos();
    println!("------------------------");
    println!("Operadores de incremento y decremento: ");
    incremento_decremento();
    println!("------------------------");
    println!("Operadores de comparación o relacionales: ");
    comparacion_relacion();
    println!("------------------------");
    println!("Operadores lógicos: ");
    logicos();
    println!("------------------------");
    println!("Operadores de bits: ");
    bitwise();
    println!("------------------------");
    println!("--- Estructuras de control de flujo --- ");
    println!("Estructura if-else: ");
    condicion_if_else();
    println!("------------------------");
    println!("Estructura loop: ");
    loop_block();
    println!("------------------------");
    println!("Estructura while: ");
    while_block();
    println!("------------------------");
    println!("Estructura for: ");
    for_block();
    println!("------------------------");
    println!("Estructura match: ");
    match_block();
    println!("------------------------");
    println!("Ejercicio extra: ");
    extra_exercice();
}