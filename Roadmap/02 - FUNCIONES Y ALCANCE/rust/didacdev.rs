// https://doc.rust-lang.org/book/ch03-03-how-functions-work.html

// Funciones con parámetro
fn print_hello(name: &str) {
    println!("Hello {name}")
}

fn suma_dos(number1:i32, number2:i32) {
    let result = number1 + number2;
    println!("{result}")
}

// Funciones con return
fn five() -> i32 {
    return 5
}

fn print_numbers(word1: &str, word2: &str) -> i32 {
    let mut n = 0;

    for number in 1..=100 {
        if number % 3 == 0 && number % 5 == 0 {
            println!("{}", word1.to_owned() + word2)
        } else if number % 5 == 0 {
            println!("{word2}")
        } else if number % 3 == 0 {
            println!("{word1}")
        } else {
            n += 1;
            println!("{number}")
        }
    }

    return n;
}

fn main() {
    // print_hello("Diego");
    // suma_dos(1, 2);
    // println!("{}", five())
    println!("Se ha impreso un número {} veces", print_numbers("Hola", "Mundo"));
}