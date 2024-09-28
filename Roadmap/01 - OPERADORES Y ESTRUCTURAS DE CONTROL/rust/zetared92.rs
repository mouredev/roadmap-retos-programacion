// RETO #01 OPERADORES Y ESTRUCTURAS DE CONTROL

fn main() {
    // Operadores aritméticos
    println!("Arithmetic Operators");

    let x = 15;
    let y = 5;
    println!("Addition: {}", x + y);
    println!("Subtraction: {}", x - y);
    println!("Multiplication: {}", x * y);
    println!("Division: {}", x / y);

    // Operadores de asignación
    println!("Assignment Operators");

    let mut z = 15;

    z += 5; // Equivalencia: z = z + 5;
    z -= 5: // Equivalencia: z = z - 5;
    z *= 5: // Equivalencia: z = z * 5;
    z /= 5: // Equivalencia: z = z / 5;
    z %= 5: // Equivalencia: z = z % 5;

    println!("X final value: {}", z);

    // Operadores de comparación
    println!("Comparison Operators");

    let x = 5;
    let y = 15;

    println!("Equal: {}", x == y);
    println!("Unequal: {}", x != y);
    println!("Less than: {}", x < y);
    println!("Greater than: {}", x > y);
    println!("Less Equal than: {}", x <= y);
    println!("Greater than: {}", x >= y);

    // Operadores lógicos
    println!("Logical Operators");

    let x = true;
    let y = false;

    println!("Logical AND: x && y -> {}", x && y);
    println!("Logical NOT: !y -> {}", !y);
    println!("Logical OR: x !! y -> {}", x || y);

    // Operadores binarios
    println!("Binary Operators");

    let x: u8 = 0b1010;
    let y: u8 = 0b1100;

    let and = x & b; // AND binario
    let or = x | y; // OR binario
    let xor = x ^ y; // XOR binario
    let not = !x // NOT binario
    let shift_left = x << 2; // Desplazamiento a la izquierda
    let shift_right = x >> 4; // Desplazamiento a la derecha

    println!("Binary AND: x & y -> {}", x & y);
    println!("Binary OR: x | y -> {}", x | y);
    println!("Binary XOR: x ^ y -> {}", x ^ y);
    println!("Binary NOT: !y -> {}", !y);
    println!("Shift Left: x << 2 -> {}", x << 2);
    println!("Shift Right: x >> 4 -> {}", x >> 4);

    // Operadores de identidad
    let a = "Hello";
    let b = "Hello";
    let c = "World";
    println!("Equal: {}", a == b);
    println!("Unequal: {}", a != c);

    // Operadores de pertenencia
    let nums = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
    let num_in = 0;
    println!("Membership operators: {}", nums.contains(&num_in));
}

// Estructuras de control: Condicionales
fn even_odd(num: i32) {
    if num % 2 == 0 {
        println!("The number {} is even", num);
    } else {
        println!("The number {] is odd", num);
    }
}

fn main() {
    let num1 = 10;
    let num2 = 5;

    even_odd(num1);
    even_odd(num2);
}

// Instrucción match
fn day_weekly(num: i32) -> String {
    match num {
        1 => String::from("Monday"),
        2 => String::from("Tuesday"),
        3 => String::from("Wednesday"),
        4 => String::from("Thrusday"),
        5 => String::from("Friday"),
        6 => String::from("Saturday"),
        7 => String::from("Sunday"),
        _ => String::from("Input a valid value (1-7)")
    }
}

// Iterativas: loop, while, for
// Loop
fn main() {
    let mut counter = 0;

    loop {
        println!("Counter is: {}", counter);
        counter += 1;

        if counter == 10{
            break;
        }
    }
}

// While
fn factorial(num: u32) -> u32 {
    let mut result = 1;
    let mut i: u32 = 1;

    while i <= num {
        result *= i;
        i += 1;
    }

    result
}

fn main() {
    let num = 5;
    let result_factorial = factorial(num);

    println!("Factorial of {} is: {}", num, result_factorial);
}

// For
fn main() {
    let num_list = [1, 2, 3, 4, 5];

    for num in num_list {
        println!("Number: {}", num);
    }
}

// Manejo de errores: Panic y Result
fn main() {
    let num_str = "15*";
    let num = match num_str.parse::<i32>() {
        Ok(num) => num,
        Err(_e) => -1,
    };
    println!("{}", num);
}

// Extra
fn main() {
    println!("🧩 DIFICULTAD EXTRA 🧩");
    for num in 10..=55{
        if num % 2 == 0 && num != 16 && num %3 !=0 {
            println!("{}", num);
        }
    }
}