// RETO 302 FUNCIONES Y ALCANCE


// Función sin parámetros/retorno
fn main() {
    println!("Hello, World!")
}

// Func con retorno y parámetros
fn addition(x: i32, y: i32) -> i32{
    x + y
}

// Func con varios parámetros y retorno
fn multiple_value() -> (&'static str, &'static str){
    ("Hello", "Rust")
}

// Func varios parámetros
fn mult_values(games: &[&str]) {
    for game in games {
        println!("{game}");
    }
}

// FUNCIONES DENTRO DE FUNCIONES
fn func_out() {
    fn func_in_func(){
        println!("Hello, Rust!")
    }
    func_in_func();
}

// VARIABLES LOCALES Y GLOBALES
fn hello_world() {
    let global_var: i32 = 15;
    fn hello_world() {
        let local_var: i32 = 55;
        println!("{}", local_var);
    }
    hello_rust();
    println!("{}", global_var);
}

// EXTRA
fn print_numbers(text_1: &str, text_2: &str) -> u8 {
    let mut count: u8 = 0;
    for x in 1..101 {
        if x % 3 == 0 && x % 5 == 0 {
            println!("{text_1}", "{text_2}");
        } else if x % 3 == 0 {
            println!("{text_1}");
        } else if x % 5 == 0 {
            println!("{text_2}")
        } else {
            println!("{x}");
            count += 1;
        }
    }
    count
}
println!(print_numbers("Fizz", "Buzz"));
