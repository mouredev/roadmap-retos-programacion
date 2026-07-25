/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
38 MOUREDEV PRO
------------------------------------
* He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 
[dependencies]
csv = "1.3.0"
rand = "0.8.5"
*/

use std::collections::HashMap;
use std::error::Error;
use std::fs::File;
use csv::Reader;
use rand::seq::SliceRandom;
use rand::thread_rng;

#[derive(Debug, Clone)]
struct Entry {
    id: String,
    email: String,
    status: String,
}

fn read_csv(file_path: &str) -> Result<Vec<Entry>, Box<dyn Error>> {
    let file = File::open(file_path)?;
    let mut reader = Reader::from_reader(file);
    let mut entries = Vec::new();

    for result in reader.deserialize() {
        let record: HashMap<String, String> = result?;
        entries.push(Entry {
            id: record.get("id").unwrap_or(&String::new()).to_string(),
            email: record.get("email").unwrap_or(&String::new()).to_string(),
            status: record.get("status").unwrap_or(&String::new()).to_string(),
        });
    }

    Ok(entries)
}

fn get_active_entries(entries: &[Entry]) -> Vec<Entry> {
    entries
        .iter()
        .filter(|entry| entry.status.to_lowercase() == "active")
        .cloned()
        .collect()
}

fn select_winners(active_entries: &[Entry], num_winners: usize) -> Vec<Entry> {
    let mut rng = thread_rng();
    let mut indices: Vec<usize> = (0..active_entries.len()).collect();
    indices.shuffle(&mut rng);
    indices.into_iter()
        .take(num_winners.min(active_entries.len()))
        .map(|i| active_entries[i].clone())
        .collect()
}

fn distribute_prizes(winners: &[Entry], prizes: &[&str]) {
    let mut rng = thread_rng();
    let mut shuffled_prizes = prizes.to_vec();
    shuffled_prizes.shuffle(&mut rng);

    for (winner, prize) in winners.iter().zip(shuffled_prizes.iter()) {
        println!("{:<11} -> Id({}): {}", prize, winner.id, winner.email);
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    println!("Usuarios ganadores de 'MOUREDEV PRO:'");
    let csv_file = "users.csv";
    let prizes = vec!["Suscripción", "Descuento", "Libro"];

    match read_csv(csv_file) {
        Ok(entries) => {
            let active_entries = get_active_entries(&entries);
            let winners = select_winners(&active_entries, 3);
            distribute_prizes(&winners, &prizes);
        }
        Err(e) => println!("No se encontraron entradas activas: {}", e),
    }

    Ok(())
}
