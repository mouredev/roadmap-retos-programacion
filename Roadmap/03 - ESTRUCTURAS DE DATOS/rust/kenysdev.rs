// no advertencia(variables no utilizadas)
#![allow(unused_variables)]
/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝

-----------------------------------------
* ESTRUCTURAS DE DATOS
-----------------------------------------
*/
use std::io::{self, Write};
use std::collections::HashSet;
use std::collections::HashMap;

fn main() {
    //_____________________________________________
    // * Tupla
    // - Para agrupar varios valores de distintos tipos.
    // - Tienen una longitud fija.
    let tuple: (i8, &str, bool) = (12, "abc", true);
    
    // Obtener los valores individuales
    let (a, b, c) = tuple;
    println!("tupla: {a}-{b}-{c}");
    
    // Acceder mediante índice
    println!("item-tupla: {}", tuple.2);

    //_____________________________________________
    // * Arreglo
    // - Cada elemento debe tener el mismo tipo.
    // - Tienen una longitud fija.
    let array = [1, 2, 3, 4];

    //  Inicializar para contener el mismo valor.
    let array = [3; 4]; // [3, 3, 3, 3]

    // Especificar tipo de un arreglo
    let array: [i32; 4] = [1, 2, 3, 4];

    // Acceder mediante índice
    println!("item-array: {}", array[3]);

    //_____________________________________________
    // * Vectores (Vec<T>)
    // - Solo valores del mismo tipo.
    // - Puede cambiar de tamaño.
    let vector: Vec<i32> = Vec::new();

    // Creará un nuevo vector con valores dados.
    // Rust puede inferir que el tipo.
    let mut vector = vec!["a", "b", "c"];

    // Agregar elementos
    vector.push("d");
    vector.push("e");

    // Acceder mediante índice o *get*
    println!("item-vector: {}", vector[1]);

    match vector.get(10) {
        Some(valor) => println!("item-vector: {valor}"),
        None => println!("indice en vector fuera de rango."),
    }
    
    // NOTE: 
    // - Si es por *indice* causará que el programa falle cuando
    //   intente acceder a un elemento que no existe.
    // - si es con *get* simplemente devuelve *None* sin entrar en pánico.
    // Modificar
    vector[4] = "z"; 
    println!("item-vector: {}", vector[4]);

    // Eliminar
    vector.remove(4);
    // Eliminar ultimo y obtener
    if let Some(last) = vector.pop() { 
        println!("delete-vector: {last}");
    }

    // Buscar
    // Devuelve el índice del primer elemento que cumple con la condición.
    let index = vector.iter().position(|&i| i == "c");
    match index {
        Some(idx) => println!("indice-vector: {idx}"),
        None => println!("no se encontró."),
    }
    
    // Devuelve una referencia al primer elemento que cumple con la condición.
    let item: Option<&&str> = vector.iter().find(|&&i| i == "c");
    match item {
        Some(&i) => println!("Elemento-vector: {i}"),
        None => println!("no se encontró."),
    }

    //_____________________________________________
    // * HashSet
    // - Debe contener elementos del mismo tipo.
    // - Puede cambiar de tamaño.
    // - No guarda duplicados.
    // - Sin indice ni orden.
    let mut set: HashSet<&str> = HashSet::new();

    // Agregar elementos
    set.insert("a"); 
    set.insert("b"); 
    set.insert("c");

    // Verificar
    if set.contains("b") {
        println!("El conjunto contiene 'b'");
    }
    
    // elimionar
    set.remove("c");

    //_____________________________________________
    // * HashMap
    // - De pares clave-valor
    let mut contacts: HashMap<String, u64> = HashMap::new();

    // Agregar elementos
    contacts.insert("Ben".to_string(), 111);
    contacts.insert("zoe".to_string(), 222);
    contacts.insert("Dan".to_string(), 333);

    // Acceder
    if let Some(value) = contacts.get("Dan") {
        println!("Valor de 'Dan' es: {value}");
    } 

    // Eliminar
    if let Some(value) = contacts.remove("c") {
        println!("Se eliminó clave 'Dan' y valor {value}");
    }
    
    // Iterar
    for (key, value) in &contacts {
        println!("Nombre: {key}, Numero: {value}");
    }
    
    /*_____________________________________________
    // * Ejercicio:
    * Crea una agenda de contactos por terminal.
    * - Debes implementar funcionalidades de búsqueda, inserción, 
        actualización y eliminación de contactos.
    * - Cada contacto debe tener un nombre y un número de teléfono.
    * - El programa solicita en primer lugar cuál es la operación 
        que se quiere realizar y a continuación los datos necesarios
        para llevarla a cabo.
    * - El programa no puede dejar introducir números de teléfono no
        númericos y con más de 11 dígitos.
    * - También se debe exister operación de finalización del programa.
    */

    contact_book(&mut contacts);
}

const MSG: &str  = "
Agenda de contactos
╔═══════════════════════════╗
║ 1. Nuevo      4. Editar   ║
║ 2. Buscar     5. Eliminar ║
║ 3. Lista      6. Salir    ║
╚═══════════════════════════╝
";

fn contact_book(contacts: &mut HashMap<String, u64>) {
    println!("{MSG}");
    let option: String = input("Escriba opción: ");
    
    match option.trim() {
        "1" => create(contacts),
        "2" => search(contacts),
        "3" => list(contacts),
        "4" => edit(contacts),
        "5" => delete(contacts),
        "6" => println!("Adiós"),
        _ => {
            println!("Número 1 -> 6");
            contact_book(contacts);
        }
    }
}

fn create(contacts: &mut HashMap<String, u64>) {
    println!("Crear contacto o '6' para Salir");
    let name: String = input("Escriba el nombre: ");
    
    if name.is_empty() {
        create(contacts);
    } else if name == "6" {
        contact_book(contacts);
    } else if !contacts.contains_key(&name) {
        add_num(name, contacts);
    } else {
        println!("El nombre ya existe.\n");
        create(contacts);
    }
}

fn add_num(name: String, contacts: &mut HashMap<String, u64>) {
    let num: String = input("Escriba el número: ");
    if num == "6" {
        contact_book(contacts);
    } else if !num.is_empty() && num.len() < 12 && is_integer(&num) {
        contacts.insert(name.clone(), num.parse::<u64>().unwrap());
        println!("Guardado");
        contact_book(contacts);
    } else {
        println!("Ingrese un número con menos de 11 dígitos.");
        add_num(name, contacts)
    }
}

fn search(contacts: &mut HashMap<String, u64>) {
    println!("Buscar contacto o '6' para Salir");
    let name: String = input("Escriba el nombre: ");
    if name == "6" {
        contact_book(contacts);
    } else if let Some(value) = contacts.get(&name) {
        println!("{name} - {value}\n");
        search(contacts);
    } else {
        println!("Contacto no encontrado.\n");
        search(contacts);
    }
}

fn list(contacts: &mut HashMap<String, u64>) {
    for (name, number) in &mut *contacts {
        println!("{name} - {number}");
    }
    contact_book(contacts);
}

fn edit(contacts: &mut HashMap<String, u64>) {
    println!("Editar contacto o '6' para Salir");
    let name: String = input("Escriba el nombre: ");
    if name == "6" {
        contact_book(contacts);
    } else if contacts.contains_key(&name) {
        add_num(name, contacts);
    } else {
        println!("Contacto no encontrado.\n");
        edit(contacts)
    }
}

fn delete(contacts: &mut HashMap<String, u64>) {
    println!("Eliminar contacto o '6' para Salir");
    let name: String = input("Escriba el nombre: ");
    if name == "6" {
        contact_book(contacts);
    } else if let Some(value) = contacts.remove(&name) {
        println!("{name} - {value} fue eliminado.");
        contact_book(contacts);
    } else {
        println!("Contacto no encontrado.\n");
        delete(contacts);
    }
}

fn is_integer(var: &str) -> bool {
    if let Ok(numero) = var.parse::<u64>() {
        true
    } else {
        false
    }
}

fn input(msg: &str) -> String {
    print!("{msg}");
    io::stdout().flush().expect("Error: limpiar búfer");

    let mut input_txt: String = String::new();
    io::stdin()
        .read_line(&mut input_txt)
        .expect("Error al leer la entrada");

    input_txt.trim().to_string()
}
