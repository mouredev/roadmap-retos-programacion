use std::collections::HashMap;
fn main() {
    // Vector, similar al ArrayList
    let mut v: Vec<i32> = vec![1, 3, 2, 5, 4, 7];

    v.remove(1);
    v.push(6);

    // Ordenar vector
    v.sort();

    // Para imprimir un vector se agrega :? al {}
    println!("Vector ordenado: {:?}", v);

    // String
    let _s: String = String::from("Hola, mundo!");
    // No se puede ordenar

    // Tupla
    let tup = (1, "hola", 3.0);
    // Una tupla no se puede modificar

    println!("Tupla: {:?}", tup);

    // HashMap,
    // guarda datos tipo Clave, Valor
    // importar los HashMap (Esto iría al principio del archivo)
    //use std::collections::HashMap;

    let mut scores = HashMap::new();
    // Insertar (Clave, Valor)
    scores.insert("Juan", 42);
    scores.insert("Maria", 30);

    println!("HashMap: {:?}", scores);
    scores.remove("Maria");
    println!("HashMap con Maria eliminada: {:?}", scores);

    // No se puede ordenar un HashMap ya se accede mediante la clave y no por posición de los
    // elementos.

    // HashSet,
    // guarda datos tipo Clave y no permite repetidos (Sin orden)
    // Para importar el HashSet
    use std::collections::HashSet;

    // Creación
    let mut unique_numbers = HashSet::new();
    // Insertar
    unique_numbers.insert(1);
    unique_numbers.insert(3);
    unique_numbers.insert(9);
    unique_numbers.insert(7);

    // Otra vez, no se puede ordenar un set ya que no es una estructura iterable.
    println!("HashSet: {:?}", unique_numbers);
    unique_numbers.insert(7);
    println!("HashSet con el 7 insertado dos veces: {:?}", unique_numbers);

    // VecDeque es una cola de doble extremo.
    use std::collections::VecDeque;
    let mut deque = VecDeque::new();
    deque.push_front(1);
    deque.push_back(2);
    deque.push_front(3);

    println!("Deque: {:?}", deque);

    println!("\n\nEXTRA EXTRA");
    extra();
}

use std::io::{self, BufRead, Write};
use std::process::Command;
//use std::time::Duration;
//use std::{i32, thread};

fn extra() {
    println!("Presiona Enter para ingresar a la funcionalidad extra...");
    // Leer una línea de entrada del usuario
    let stdin = io::stdin();
    let _ = stdin.lock().lines().next();

    // Hacer que el programa espere durante 2 segundos
    //thread::sleep(Duration::from_secs(2));
    let output = Command::new("clear")
        .status()
        .expect("Failed to clear terminal");

    if output.success() {
        let mut contacts: HashMap<String, u32> = HashMap::new();

        loop {
            println!("=== Agenda de Contactos ===");
            println!("1. Buscar contacto");
            println!("2. Insertar contacto");
            println!("3. Actualizar contacto");
            println!("4. Eliminar contacto");
            println!("5. Imprimir agenda");
            println!("6. Salir");

            print!("Ingrese el número de la operación que desea realizar: ");
            io::stdout().flush().unwrap();

            let mut opcion = String::new();
            io::stdin()
                .read_line(&mut opcion)
                .expect("Error al leer la entrada");

            // Verificación de que sea un número
            let numero: u32 = match opcion.trim().parse() {
                Ok(numero) => numero,
                Err(_) => {
                    opcion_invalida();
                    continue;
                }
            };

            match numero {
                1 => buscar_contacto(&contacts),
                2 => insertar_contacto(&mut contacts),
                3 => actualizar_contacto(&mut contacts),
                4 => eliminar_contacto(&mut contacts),
                5 => imprimir_agenda(&mut contacts),
                6 => break,
                _ => opcion_invalida(), // Si no es un número del 1 al 5
            }
        }
    } else {
        println!("Failed to clear terminal");
    }
}

fn buscar_contacto(agenda: &HashMap<String, u32>) {
    clear_terminal();

    println!("\nIngrese el nombre del contacto a buscar: ");
    let mut nombre: String = String::new();

    io::stdin()
        .read_line(&mut nombre)
        .expect("Error al leer la entrada");

    nombre = nombre.trim().to_string();
    match agenda.get(&nombre) {
        Some(telefono) => println!("El número del contacto {} es: {}", nombre, telefono),
        None => println!("No se encontro el contacto"),
    }
}

fn insertar_contacto(agenda: &mut HashMap<String, u32>) {
    clear_terminal();

    println!("\nIngrese el nombre del contacto a agregar: ");
    let mut nombre: String = String::new();
    io::stdin()
        .read_line(&mut nombre)
        .expect("Error al leer la entrada");

    nombre = nombre.trim().to_string();

    println!("Ingrese el número del contacto: ");
    let mut numero_s: String = String::new();
    io::stdin()
        .read_line(&mut numero_s)
        .expect("Error al leer la entrada");

    if numero_s.len() > 11 {
        println!("El número debe tener hasta 11 digitos");
        return;
    }

    let numero: u32 = match numero_s.trim().parse() {
        Ok(numero) => numero,
        Err(_) => {
            opcion_invalida();
            return;
        }
    };

    agenda.insert(nombre.clone(), numero);
    println!("Contacto agendado: {} \nCon el numero: {}", nombre, numero);
}

fn actualizar_contacto(agenda: &mut HashMap<String, u32>) {
    println!("\nIngrese el nombre del contacto a modificar: ");
    let mut nombre: String = String::new();
    io::stdin()
        .read_line(&mut nombre)
        .expect("Error al leer la entrada");
    nombre = nombre.trim().to_string();

    if agenda.contains_key(&nombre.clone()) {
        println!("Ingrese el nuevo número del contacto: ");
        let mut numero_s: String = String::new();
        io::stdin()
            .read_line(&mut numero_s)
            .expect("Error al leer la entrada");

        if numero_s.len() > 11 {
            println!("El número debe tener hasta 11 digitos");
            return;
        }

        let numero: u32 = match numero_s.trim().parse() {
            Ok(numero) => numero,
            Err(_) => {
                opcion_invalida();
                return;
            }
        };

        agenda.insert(nombre, numero);
    } else {
        println!("El contacto no existe");
    }
}

fn eliminar_contacto(agenda: &mut HashMap<String, u32>) {
    println!("\nIngrese el nombre del contacto a modificar: ");
    let mut nombre: String = String::new();
    io::stdin()
        .read_line(&mut nombre)
        .expect("Error al leer la entrada");
    nombre = nombre.trim().to_string();

    if agenda.contains_key(&nombre.clone()) {
        agenda.remove(&nombre);
        println!("Contacto {} eliminado", nombre);
    } else {
        println!("El contacto no existe");
    }
}

fn opcion_invalida() {
    clear_terminal();
    println!("Entrada inválida, por favor, ingresa una entrada válida.");
}

fn clear_terminal() {
    Command::new("clear")
        .status()
        .expect("Failed to clear terminal");
}

fn imprimir_agenda(agenda: &mut HashMap<String, u32>) {
    let multi_line = "
 ____________________________________________\n
/                                            \\\n
|              Agenda de Contactos           |\n
|____________________________________________|";
    println!("{}", multi_line);
    if !agenda.is_empty() {
        for (k, v) in agenda {
            println!("|   Nombre: {}, numero: {}             |", k, v);
        }
        println!("|____________________________________________|");
    } else {
        println!("Agenda vacia");
    }
}