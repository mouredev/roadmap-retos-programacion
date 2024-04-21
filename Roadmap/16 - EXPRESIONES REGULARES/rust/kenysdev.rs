/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* EXPRESIONES REGULARES
-----------------------------------------
https://crates.io/crates/regex

[dependencies]
regex = "1.10.4"

* EJERCICIO #1:
* Utilizando tu lenguaje, explora el concepto de expresiones regulares,
* creando una que sea capaz de encontrar y extraer todos los números
* de un texto.
*/

use regex::Regex;

fn get_numbers(text: &str) {
    let pattern = Regex::new(r"\d+").unwrap();
    for number in pattern.find_iter(text) {
        println!("{}", number.as_str());
    }
}

/*
* EJERCICIO #2:
* Crea 3 expresiones regulares (a tu criterio) capaces de:
* - Validar un email.
* - Validar un número de teléfono.
* - Validar una url.
*/

fn is_email(text: &str) -> bool {
    let pattern = Regex::new(
        r"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$").unwrap();
    return pattern.is_match(text)
}

fn is_phone_number(text: &str) -> bool {
    let pattern = Regex::new(
        r"^(\d{3}-\d{3}-\d{4}|\d{10})$").unwrap();
    return pattern.is_match(text)
}

fn is_url(text: &str) -> bool {
    let pattern = Regex::new(
        r"^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/\S*)?$"
    ).unwrap();
    return pattern.is_match(text)
}

fn main() {
    println!("GetNumbers");
    get_numbers("abcdsfs1s(*&#}2. a3// 45sdf67");
    get_numbers("45sdf67");

    println!("\nis_email");
    println!("{}", is_email("ejm@dmn.com"));        // True
    println!("{}",is_email("e_jm-2+b@dmn.co.hn"));  // True
    println!("{}",is_email("ejm@dmn.com_"));        // False
    println!("{}",is_email("ejm@dmn"));             // False

    println!("\nis_email");
    println!("{}",is_phone_number("123-456-7890")); // True
    println!("{}",is_phone_number("1234567890"));   // True
    println!("{}",is_phone_number("123456-7890"));  // False
    println!("{}",is_phone_number("uno234567890")); // False

    println!("\nis_url");
    println!("{}",is_url("http://www.ejm.com"));    // True
    println!("{}",is_url("google.com"));            // True
    println!("{}",is_url("ejm.com/a/b/c"));         // True
    println!("{}",is_url("https://.ejm.com"));      // False
    println!("{}",is_url("https://.ejm.com/a b"));  // False

}
