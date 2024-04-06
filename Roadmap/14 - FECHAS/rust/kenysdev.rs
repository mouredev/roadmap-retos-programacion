/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* FECHAS
-----------------------------------------
En Rust, la forma predeterminada de trabajar con fechas y horas es con crono.
Mas info: https://crates.io/crates/chrono

[dependencies]
chrono = "0.4.37"

_______________
* EJERCICIO 1
* Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
* - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
* - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
* Calcula cuántos años han transcurrido entre ambas fechas.
*/
use chrono::prelude::*;

fn date_diff(now: DateTime<Local>, birth_date: DateTime<Utc>) {
    let difference = now.signed_duration_since(birth_date);
    let years = difference.num_days() / 365;
    let months = (difference.num_days() % 365) / 30;
    let days = (difference.num_days() % 365) % 30;
    println!("Juanito tiene: {years} años, {months} meses y {days} días.");
}

/* 
_______________
* EJERCICIO 2
* Utilizando la fecha de tu cumpleaños, formatéala y muestra su 
  resultado de 10 maneras diferentes.
*/

fn others_format(birth_date: DateTime<Utc>) {
    println!("\n* 10 maneras diferentes:");
    println!("1. Predeterminado   -> {}", birth_date.format("%Y-%m-%d %H:%M:%S"));
    println!("2. Fecha larga      -> {}", birth_date.format("%A, %d de %B de %Y"));
    println!("3. dd-mm-yyyy       -> {}", birth_date.format("%d-%m-%Y"));
    println!("4. Nombre del mes   -> {}", birth_date.format("%B"));
    println!("5. Mes abreviado    -> {}", birth_date.format("%b"));
    println!("6. Nombre dia       -> {}", birth_date.format("%A"));
    println!("7. Dia abreviado    -> {}", birth_date.format("%a"));
    println!("8. Hora (12 horas)  -> {}", birth_date.format("%I:%M:%S %p"));
    println!("9. Hora (24 horas)  -> {}", birth_date.format("%H:%M:%S"));
    println!("0. Personalizado    -> {}", birth_date.format("Born on %A, %dth of %B %Y at %I:%M:%S %p"));
}

fn main() {
    let now: DateTime<Local> = Local::now();
    let birth_date = Utc.with_ymd_and_hms(1995, 10, 20, 12, 30, 0).unwrap(); 
    date_diff(now, birth_date);

    others_format(birth_date);
}
