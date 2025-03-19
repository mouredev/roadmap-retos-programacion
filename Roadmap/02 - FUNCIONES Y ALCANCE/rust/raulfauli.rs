/// #02 FUNCIONES Y ALCANCE
///
/// Para compilar y ejecutar este código, ejecute el siguiente comando desde el directorio principal:
///
/// ```bash
///   rustc ./Roadmap/02\ -\ FUNCIONES\ Y\ ALCANCE/rust/raulfauli.rs && ./raulfauli
/// ```
///
fn main() {
    hello();
    say_hello("Raúl");

    say_hello_engineer("Raül", Some(10));
    say_hello_engineer("Raül", None);

    let sum = sum(5, 5);
    println!("Sum: {sum}");

    let (hello, world) = return_multiple_values();
    println!("{hello} {world}");

    let tuple = return_multiple_values();
    println!("{} {}", tuple.0, tuple.1);

    let media = average(&[1, 2, 3, 4, 5]);
    println!("Media: {media}");

    exterior_function();
    // interior_function(); // Error

    builtin_functions();

    local_global_variable();

    let count = extra_difficulty("Fizz", "Buzz");
    println!("Count: {count}");
}

// Función sin parámetro
fn hello() {
    println!("¡Hola mundo!");
}

// Función con parámetro
fn say_hello(name: &str) {
    println!("Hola, {name}!");
}

// Función con parámetro opcional Todo: revisar este punto
fn say_hello_engineer(name: &str, years: Option<i32>) {
    match years {
        Some(years) => {
            println!("Mi nombre es {name}, soy ingeniero de software hace más de {years} años")
        }
        None => println!("Mi nombre es {name}"),
    }
}

// Función con 2 parámetros y retorno
fn sum(a: i32, b: i32) -> i32 {
    // return a + b;
    a + b
}

// También podría haber devuelto -> (&'static str, &'static str)
fn return_multiple_values() -> (String, String) {
    (String::from("Hello"), String::from("World"))
}

fn average(numbers: &[i32]) -> f64 {
    let sum: i32 = numbers.iter().sum();
    sum as f64 / numbers.len() as f64
}

fn exterior_function() {
    fn interior_function() {
        println!("¡Hola desde la función interior!");
    }

    interior_function();
}

fn local_global_variable() {
    let global_variable = 10;
    let v = {
        // Este bloque de código nos permite obtener un resultado
        // sin tener que definir una función
        let a = 1;
        let b = 2;
        let global_variable = 20; // Shadowing
        a + b + global_variable
    };

    // println!("Local: {a}"); // Error

    fn interior_function(local_variable: i32) {
        // println!("Global: {global_variable}"); // Error
        println!("Local: {}", local_variable);
    }

    interior_function(v);

    println!("Global: {global_variable}");
}

fn builtin_functions() {
    let variable: &str = "github";
    println!("Longitud de \"{variable}\" {}", variable.len());

    let variable: String = "gitlab".to_string();

    println!("Longitud de \"{variable}\" {}", variable.len());
}

fn extra_difficulty(first: &str, second: &str) -> u8 {
    let mut count: u8 = 0;
    for x in 1..100 {
        if x % 3 == 0 && x % 5 == 0 {
            println!("{first} {second}");
        } else if x % 3 == 0 {
            println!("{first}");
        } else if x % 5 == 0 {
            println!("{second}");
        } else {
            println!("{x}");
            count += 1;
        }
    }

    count
}
