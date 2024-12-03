/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
39 BATMAN DAY
------------------------------------

* RETO 1:
* Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta
* su 100 aniversario.

[dependencies]
chrono = "0.4.37"
*/

use chrono::{Datelike, NaiveDate, Weekday};
use std::cmp::Ordering;

fn third_saturday_of_september(year: i32) -> String {
    let mut date = NaiveDate::from_ymd_opt(year, 9, 15).unwrap();
    let days_to_add = ((Weekday::Sat.num_days_from_monday() as i32
        - date.weekday().num_days_from_monday() as i32
        + 7)
        % 7) as i64;
    date = date + chrono::Duration::days(days_to_add);
    date.format("%d-%m-%Y").to_string()
}

fn calculate_anniversary_dates(total_anniversaries: i32) {
    println!("Batman Day");
    const BATMAN_DAY_START: i32 = 2014;
    let current_year = chrono::Local::now().year();

    if current_year < BATMAN_DAY_START {
        println!("xd");
        return;
    }

    let past_anniversaries = current_year - BATMAN_DAY_START;
    println!("Aniversarios que ya han pasado: {}", past_anniversaries);

    for i in 0..(total_anniversaries - past_anniversaries) {
        let num = past_anniversaries + i + 1;
        let the_date = third_saturday_of_september(current_year + i as i32);
        println!("- Aniversario #{}: {}", num, the_date);
    }
}

/*
* RETO 2:
* Crea un programa que implemente el sistema de seguridad de la Batcueva.
* Este sistema está diseñado para monitorear múltiples sensores distribuidos
* por Gotham, detectar intrusos y activar respuestas automatizadas.
* Cada sensor reporta su estado en tiempo real, y Batman necesita un programa
* que procese estos datos para tomar decisiones estratégicas.
* Requisitos:
* - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
* - Cada sensor se identifica con una coordenada (x, y) y un nivel
*   de amenaza entre 0 a 10 (número entero).
* - Batman debe concentrar recursos en el área más crítica de Gotham.
* - El programa recibe un listado de tuplas representando coordenadas de los
*   sensores y su nivel de amenaza. El umbral de activación del protocolo de
*   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
* Acciones:
* - Identifica el área con mayor concentración de amenazas
*   (sumatorio de amenazas en una cuadrícula 3x3).
* - Si el sumatorio de amenazas es mayor al umbral, activa el
*   protocolo de seguridad.
* - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
*   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
* - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
*   sus amenazas, la distancia a la Batcueva y si se debe activar el
*   protocolo de seguridad.
*/

type Point = (i32, i32);
type Sensor = (i32, i32, i32);

fn create_map(
    size: Point,
    batcave: Point,
    sensors: &Vec<Sensor>,
    threats: &Vec<Point>,
) -> Vec<Vec<String>> {
    
    let mut gotham = vec![vec![String::from("| "); size.1 as usize]; size.0 as usize];

    gotham[batcave.0 as usize][batcave.1 as usize] = String::from("|B");

    for s in sensors {
        gotham[s.0 as usize][s.1 as usize] = String::from("|S");
    }

    for t in threats {
        gotham[t.0 as usize][t.1 as usize] = String::from("|T");
    }

    gotham
}

fn print_map(gotham: &Vec<Vec<String>>) {
    println!("\nMapa de Gotham:");
    for row in gotham {
        for cell in row {
            print!("{}", cell);
        }
        println!();
    }
}

fn scan_map(gotham: &Vec<Vec<String>>, sensors: &Vec<Sensor>, size: Point) {
    let mut danger_list: Vec<(usize, i32)> = Vec::new();

    for (c, s) in sensors.iter().enumerate() {
        let mut danger_counter = 0;

        for i in (s.0 - 1)..=(s.0 + 1) {
            for j in (s.1 - 1)..=(s.1 + 1) {
                if i >= 0 && i < size.0 && j >= 0 && j < size.1 {
                    if gotham[i as usize][j as usize] == "|T" {
                        danger_counter += s.2;
                    }
                }
            }
        }

        danger_list.push((c, danger_counter));
    }

    let max_danger = danger_list
        .iter()
        .max_by(|a, b| a.1.partial_cmp(&b.1).unwrap_or(Ordering::Equal))
        .unwrap();
    let location = sensors[max_danger.0];

    println!("\nInforme:");
    println!("Cuadrícula más amenazada: '{}, {}'", location.0, location.1);
    println!("Máximo nivel de alerta: '{}'", max_danger.1);

    if max_danger.1 >= 20 {
        println!("Protocolo de seguridad activado.");
        println!("Distancia: '{}'", location.0 + location.1);
    } else {
        println!("No hay amenazas relevantes.");
    }
}

fn main() {
    // Reto 1
    calculate_anniversary_dates(100);

    // Reto 2
    let size = (20, 20);
    let batcave = (0, 0);
    let sensors = vec![(2, 2, 10), (6, 8, 9), (10, 12, 8), (17, 15, 7)];
    let threats = vec![(2, 3), (2, 1), (6, 9), (17, 16), (15, 4)];

    let gotham = create_map(size, batcave, &sensors, &threats);
    print_map(&gotham);
    scan_map(&gotham, &sensors, size);
}
