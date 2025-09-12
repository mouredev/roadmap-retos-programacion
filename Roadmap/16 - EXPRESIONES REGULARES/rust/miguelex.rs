use regex::Regex;

fn reg_expr(cadena: &str) {
    let patron = Regex::new(r"-?\d+(\.\d+)?").unwrap();
    let numeros: Vec<&str> = patron.find_iter(cadena).map(|m| m.as_str()).collect();

    println!("Números encontrados:");
    for numero in numeros {
        println!("{}", numero);
    }
    println!("\n");
}

fn email_validation(email: &str) {
    let patron = Regex::new(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$").unwrap();
    if patron.is_match(email) {
        println!("El email {} es válido.", email);
    } else {
        println!("El email {} no es válido.", email);
    }
}

fn phone_validation(phone: &str) {
    let patron = Regex::new(r#"^\+?(\d{2,3})?[-. ]?\d{9}$"#).unwrap();
    if patron.is_match(phone) {
        println!("El teléfono {} es válido.", phone);
    } else {
        println!("El teléfono {} no es válido.", phone);
    }
}

fn url_validation(url: &str) {
    let patron = Regex::new(r#"^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"#).unwrap();
    if patron.is_match(url) {
        println!("La URL {} es válida.", url);
    } else {
        println!("La URL {} no es válida.", url);
    }
}

fn main() {
    let texto = "Este es un texto con números como 123, 45.6, -7 y 1000.";
    println!("Vamos a analizar el siguiente texto:");
    println!("'{}'\n", texto);
    reg_expr(texto);

    let texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456";
    println!("Vamos a analizar el siguiente texto:");
    println!("'{}'\n", texto);
    reg_expr(texto);

    email_validation("correo@correo.com");
    email_validation("correo@correo");

    phone_validation("+34 123456789");
    phone_validation("123456789");

    url_validation("http://www.google.com");
    url_validation("www.google.com");
}
