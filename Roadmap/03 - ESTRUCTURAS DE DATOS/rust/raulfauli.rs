/// #03 ESTRUCTURAS DE DATOS
///
/// Para compilar y ejecutar este código, ejecuta el siguiente comando desde el directorio principal:
///
/// `rustc ./Roadmap/03\ -\ ESTRUCTURAS\ DE\ DATOS/rust/raulfauli.rs && ./raulfauli && rm raulfauli`
///
use std::io;

fn main() {
    // Array de tamaño fijo
    let mut languages: [&str; 4] = ["Rust", "Java", "Kotlin", "Swift"];

    // Iterar sobre un array
    languages.iter().for_each(|lang| println!("{}", lang));

    // languages.push("Python"); // Error: no se puede modificar un array
    languages[0] = "Rust Lang"; // Ok

    let length = languages.len();
    println!("Número de lenguajes: {}", length);

    let first = languages[0]; // También languages.get(0);
    println!("First lenguage: {first}");

    let first = languages.first().unwrap();
    println!("First lenguages: {first}");

    let last = languages[length - 1];
    println!("Last lenguage: {last}");

    let last = languages.last().unwrap();
    println!("Last lenguages: {last}");

    let contains = languages.contains(&"Dart");
    println!("Languages: {:?} contains Dart? {}", languages, contains);

    // Vector
    let mut numbers: Vec<i32> = vec![1, 2, 3, 4, 5];
    numbers.push(6);
    numbers.remove(0);
    numbers.extend([7, 8, 9].iter().cloned());

    let contains = numbers.contains(&3);
    println!("Numbers: {:?} contains 3? {}", numbers, contains);

    // Tuplas (2 maneras de declararlas)
    let location = (10, 20);
    println!("Location: ({}, {}) type (i32, i32)", location.0, location.1);

    let x = Location(10, 20);
    println!("Location: ({}, {}) type Location", x.0, x.1);

    // Estructuras
    let person = Person {
        name: String::from("Raúl"),
        phone: 123_456_789,
    };

    println!("{}: {}", person.name, person.phone);

    // Estructura con implementación
    let person2 = Person::new("Fayu", 777_777_777);
    println!("{}: {}", person2.name, person2.phone);

    // Extra
    let mut agenda: Vec<Person> = vec![person, person2];
    loop {
        println!(r#"
        1. Añadir contacto
        2. Eliminar contacto
        3. Buscar contacto
        4. Listar contactos
        5. Salir "Crtl + C"
        "#);

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        match input.trim() {
            "1" => add_contact(&mut agenda),
            "2" => delete_contact(&mut agenda),
            "3" => find_contacts(&agenda),
            "4" => list_contacts(&agenda),
            "5" => break,
            _ => println!("Opción no válida"),
        }
    }
}

struct Location(i32, i32);

struct Person {
    name: String,
    phone: u64,
}

impl Person {
    fn new(name: &str, phone: u64) -> Person {
        Person {
            name: String::from(name),
            phone,
        }
    }
}

fn add_contact(agenda: &mut Vec<Person>) {
    let name = input_name();
    let phone = input_phone();

    let person = Person::new(&name, phone);
    agenda.push(person);
}

fn delete_contact(agenda: &mut Vec<Person>) {
    let name = input_name();

    let index = agenda.iter().position(|person| person.name == name).unwrap();
    if Some(index).is_some() {
        agenda.remove(index);
    }
}

fn find_contacts(agenda: &Vec<Person>) {
    let name = input_name();

    agenda.iter().for_each(|person| {
        if person.name == name {
            println!("{}: {}", person.name, person.phone);
        }
    });
}

fn list_contacts(agenda: &Vec<Person>) {
    agenda.iter().for_each(|person| {
        println!("{}: {}", person.name, person.phone);
    });
}

fn input_name() -> String {
    println!("Nombre:");

    let name = loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        input = input.trim().to_string();

        if input.is_empty() {
            println!("Nombre es requerido");
        } else {
            break input;
        }
    };

    return name;
}

fn input_phone() -> u64 {
    println!("Teléfono:");

    let phone = loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        input = input.trim().replace(" ", "");
        if input.len() > 11 {
            println!("Teléfono no válido");
            continue;
        }

        let phone: u64 = match input.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Teléfono debe ser un número");
                continue;
            }
        };

        break phone;
    };

    return phone;
}



