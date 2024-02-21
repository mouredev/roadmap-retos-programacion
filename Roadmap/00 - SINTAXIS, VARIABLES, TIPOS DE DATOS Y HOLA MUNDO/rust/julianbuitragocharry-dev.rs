use std::io;

// https://www.rust-lang.org/
// Sintaxis de comentario en una linea
/* Sintaxis de comentario multilinea*/

fn main() {
    println!(r#"Do you want to know about Rust? 🦀
    1) Mutability
    2) Primitive Variables
    3) Constant
    4) Say Hello to me
    5) Exit
    "#);

    let mut option = String::new();
    io::stdin().read_line(&mut option).expect("Failed to read line");

    let option: u32 = option.trim().parse().expect("Please enter a number");

    match option {
        1 => mutability(),
        2 => primitive_variables(),
        3 => constant(),
        4 => hi(),
        5 => println!("See you soon..."),
        _ => {
            println!("Choose the right option...\n");
            main();
        }
    }
}

fn mutability() {
    println!(r#"What is a mutable variable
    1) let mut exit: bool = true;
    2) let exit: bool = true; 
    "#);
        
    let mut option = String::new();
    io::stdin().read_line(&mut option).expect("Failed to read line");

    let option: u32 = option.trim().parse().expect("Please enter a number");
    
    if option == 1 {
        println!("Correct Option...\n");
        main();
    } else {
        println!("Wrong Option... Repeat mutability test");
        mutability();
    }
}

fn primitive_variables() {
    let logical: bool = true;

    println!(r#"Boolean
    let logical: bool = true;
    {}
    "#, logical);

    let unsigned_integer: u32 = 1024;
    println!(r#"Unsigned Integer  
    let unsigned_integer: i32 = 1024;
    {}
    "#, unsigned_integer);

    let integer: i32 = -1024;
    println!(r#"Integer
    let integer: i32 = -1024;
    {}
    "#, integer);

    let float: f64 = 100.0;
    println!(r#"Float 
    let float: f64 = 100.0;
    {}
    "#, float);

    let chart: char = 'D';
    println!(r#"Char
    let chart: char = 'D';
    {}
    "#, chart);
    
    let empty = ();
    println!(r#"Tuple Empty 
    let empty = ();
    {:?}
    "#, empty);
    
    main();
}

fn constant() {
    const PI: f64 = 3.1416; 

    println!(r#"Constant
    const PI: f64 = 3.1416;
    {}
    "#, PI);
    
    main();
}

fn hi() {
    let language: &str = "Rust";
    println!("Hello, {}\n", language);

    main();
}