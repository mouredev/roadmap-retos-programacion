/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
35 REPARTIENDO LOS ANILLOS DE PODER
------------------------------------
¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
¿Qué pasaría si tuvieras que encargarte de repartir los anillos
entre las razas de la Tierra Media?
Desarrolla un programa que se encargue de distribuirlos.
Requisitos:
1. Los Elfos recibirán un número impar.
2. Los Enanos un número primo.
3. Los Hombres un número par.
4. Sauron siempre uno.
Acciones:
1. Crea un programa que reciba el número total de anillos
   y busque una posible combinación para repartirlos.
2. Muestra el reparto final o el error al realizarlo.
*/

use std::io::{self, Write};

fn get_total_rings() -> u32 {
    loop {
        print!("Cantidad de anillos: ");
        io::stdout().flush().unwrap();
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        match input.trim().parse() {
            Ok(n) if n >= 1 => return n,
            _ => println!("Debe ser un valor entero '>= 1'."),
        }
    }
}

fn is_prime(n: u32) -> bool {
    if n < 2 {
        return false;
    }
    (2..=(n as f64).sqrt() as u32).all(|i| n % i != 0)
}

fn standard_deviation(tup: &(u32, u32, u32)) -> f64 {
    let values = [tup.0 as f64, tup.1 as f64, tup.2 as f64];
    let avg = values.iter().sum::<f64>() / values.len() as f64;
    let variance = values.iter().map(|&x| (x - avg).powi(2)).sum::<f64>() / (values.len() - 1) as f64;
    variance.sqrt()
}

fn the_most_balanced(combinations: &[(u32, u32, u32)]) -> Option<(u32, u32, u32)> {
    combinations.iter()
        .min_by(|&a, &b| standard_deviation(a).partial_cmp(&standard_deviation(b)).unwrap())
        .cloned()
}

fn recording_more_accurate_results(mut combinations:Vec<(u32, u32, u32)>) -> Vec<(u32, u32, u32)> {
    if combinations.len() > 2{
        let distribution = the_most_balanced(&combinations);
        combinations.clear();
        combinations.extend(distribution);
    }
    combinations
 }

fn distribute(total: u32) -> Vec<(u32, u32, u32)> {
    let mut combinations = Vec::new();
    for elves in (1..total).step_by(2) {
        for men in (2..total).step_by(2) {
            let dwarves = total.saturating_sub(men + elves);
            if dwarves > 0 && is_prime(dwarves) {
                combinations.push((elves, men, dwarves));
                combinations = recording_more_accurate_results(combinations.clone())
            }
        }
    }
    combinations
}

fn print_result(distribution: Option<(u32, u32, u32)>, sauron: u32) {
    match distribution {
        Some((elves, men, dwarves)) => {
            println!("_________________________");
            println!("🧝 Elfos   -> {} : # Impar", elves);
            println!("🧔 Enanos  -> {} : # Primo", dwarves);
            println!("👨 Hombres -> {} : # Par", men);
            println!("👁️  Sauron  -> {} : # Fijo", sauron);
            println!("-------------------------");
        }
        None => println!("Error en la selección equitativa."),
    }
}

fn main() {
    println!("REPARTIENDO LOS ANILLOS DE PODER");
    let mut total = get_total_rings();
    let sauron = 1;
    total -= sauron;

    let combinations = distribute(total);
    if combinations.is_empty() {
        println!("No existe una combinación posible.");
        return;
    }

    let distribution = the_most_balanced(&combinations);
    print_result(distribution, sauron);
}
