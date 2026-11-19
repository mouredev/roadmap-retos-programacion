/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

use std::collections::HashMap;
use std::fs::remove_file;
use std::fs::File;
use std::io;
use std::io::Read;
use std::io::Write;

#[derive(Debug)]
struct ProductLine {
    name: String,
    qty: u32,
    price: f32,
}

fn save_file(products: &HashMap<String, ProductLine>) {
    println!("");
    println!("Saving products...");
    println!("");
    let mut file = File::create("sales.txt").unwrap();
    for (_k, v) in products {
        println!("{},{},{}", v.name.as_str(), v.qty, v.price);
        let _ = writeln!(file, "{},{},{}", v.name.as_str(), v.qty, v.price);
    }
    println!("");
}

fn get_product_total_sale(products: &HashMap<String, ProductLine>) {
    let mut total: f32 = 0.0;

    print!("Product: ");
    io::stdout().flush().unwrap();
    let mut prod = String::new();
    io::stdin()
        .read_line(&mut prod)
        .expect("Failed reading the product");
    prod = prod.trim().to_string();

    let pl = products.get(&prod).unwrap();
    total += pl.qty as f32 * pl.price;

    println!("Total price for {} is: {}$", prod, total);
    println!("");
}

fn get_total_sale(products: &HashMap<String, ProductLine>) {
    let mut total: f32 = 0.0;
    for (_k, v) in products {
        total += v.qty as f32 * v.price;
    }

    println!("Total price is: {}$", total);
    println!("");
}

fn _show_file() {
    let mut file = File::open("sales.txt").unwrap();
    let mut content = String::new();

    let _ = file.read_to_string(&mut content);
    println!("{}", content);
}

fn add_product(products: &mut HashMap<String, ProductLine>) {
    print!("Product: ");
    io::stdout().flush().unwrap();
    let mut prod = String::new();
    io::stdin()
        .read_line(&mut prod)
        .expect("Failed reading the product");
    prod = prod.trim().to_string();

    print!("Qty: ");
    io::stdout().flush().unwrap();
    let mut buffer = String::new();
    io::stdin()
        .read_line(&mut buffer)
        .expect("Failed to read line");
    let qty: u32 = buffer.trim().parse().expect("Input not an integer");

    print!("Price: ");
    io::stdout().flush().unwrap();
    buffer = String::new();
    io::stdin()
        .read_line(&mut buffer)
        .expect("Failed to read line");
    let price: f32 = buffer.trim().parse().expect("Input not an float");

    let new_product = ProductLine {
        name: prod.clone(),
        qty: qty,
        price: price,
    };

    if !products.contains_key(&prod) {
        products.insert(prod, new_product);
    } else {
        let elem = products.get_mut(&prod).unwrap();
        elem.qty = qty;
        elem.price = price;
    }

    save_file(&products);
}

fn modify_product(products: &mut HashMap<String, ProductLine>) {
    add_product(products);
}

fn remove_product(products: &mut HashMap<String, ProductLine>) {
    print!("Product: ");
    io::stdout().flush().unwrap();
    let mut prod = String::new();
    io::stdin()
        .read_line(&mut prod)
        .expect("Failed reading the product");
    prod = prod.trim().to_string();

    products.remove(&prod);
    println!("");
}

fn sales_app() {
    let mut products = HashMap::<String, ProductLine>::new();

    loop {
        let mut cmd = String::new();

        print!("Introduce the command: ");
        io::stdout().flush().unwrap();
        io::stdin()
            .read_line(&mut cmd)
            .expect("Failed reading the user command");
        cmd = cmd.trim().to_string();

        if cmd == "exit" {
            break;
        }

        match cmd.as_str() {
            "add" => add_product(&mut products),
            "modify" => modify_product(&mut products),
            "remove" => remove_product(&mut products),
            "total" => get_total_sale(&products),
            "prod_total" => get_product_total_sale(&products),
            _ => println!("Command not found"),
        }
    }
    products.clear();
    remove_file("sales.txt").expect("Failed removing file");
}

fn main() {
    let mut file = File::create("klyone.txt").unwrap();
    writeln!(file, "Miguel J.").unwrap();
    writeln!(file, "36").unwrap();
    writeln!(file, "Rust").unwrap();

    let mut file2 = File::open("klyone.txt").unwrap();
    let mut file_content = String::new();
    file2.read_to_string(&mut file_content).unwrap();

    println!("File content:");
    println!("{}", file_content);

    remove_file("klyone.txt").expect("Failed removing file");

    sales_app();
}
