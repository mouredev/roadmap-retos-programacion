/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* CALLBACKS
-----------------------------------------

* EJERCICIO #1:
* Explora el concepto de callback en tu lenguaje creando un ejemplo
* simple (a tu elección) que muestre su funcionamiento.
*/

// (Opcional) ya que Rust puede inferir automáticamente 
// el tipo de la función de callback en la mayoría de los casos. 
type CallbackDelegate = fn(String, i32);

fn sum_numbers(a: i32, b: i32, callback: CallbackDelegate) {
    let result: i32 = a + b;
    callback(format!("{} + {}", a, b), result);
}

fn my_callback(summands: String, result: i32) {
    println!("La suma de {} es: {}", summands, result);
}

/*
* EJERCICIO #2:
* Crea un simulador de pedidos de un restaurante utilizando callbacks.
* Estará formado por una función que procesa pedidos.
* Debe aceptar el nombre del plato, una callback de confirmación, una
* de listo y otra de entrega.
* - Debe imprimir un confirmación cuando empiece el procesamiento.
* - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
*   procesos.
* - Debe invocar a cada callback siguiendo un orden de procesado.
* - Debe notificar que el plato está listo o ha sido entregado.
*/

use std::thread;
use std::time::Duration;

// [dependencies]
// rand = "0.8.5"
// https://crates.io/crates/rand
use rand::prelude::*;

fn process_order(name: &str, confirm: fn(&str), prepare: fn(&str), serving: fn(&str)) {
    println!("-----\n* Procesando: '{}' \n-----\n", name);
    confirm(name);
    prepare(name);
    serving(name);
}

fn time_random() -> u64 {
    let mut rng: ThreadRng = rand::thread_rng();
    rng.gen_range(1..=10)
}

fn confirm_order(name: &str) {
    let time: u64 = time_random();
    println!("* Confirmando {}, espere {} segundos.", name, time);
    thread::sleep(Duration::from_secs(time));
    println!("- '{}', ha sido confirmado.\n", name);
}

fn prepare_order(name: &str) {
    let time: u64 = time_random();
    println!("* Preparando, espere {} segundos.", time);
    thread::sleep(Duration::from_secs(time));
    println!("- '{}', esta Listo.\n", name);
}

fn serving_order(name: &str) {
    let time: u64 = time_random();
    println!("* Sirviendo, espere {} segundos.", time);
    thread::sleep(Duration::from_secs(time));
    println!("- '{}', ha sido entregado.\n", name);
}

fn order(dish_name: &str) {
    process_order(dish_name, confirm_order, prepare_order, serving_order);
}

fn main() {
    println!("EJERCICIO #1");
    sum_numbers(6, 6, my_callback);
    sum_numbers(5, 2, my_callback);

    println!("\nEJERCICIO #2");
    order("Baleadas");
    order("Tamales");
    order("Enchiladas");
}
