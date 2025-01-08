/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
44 CUENTA ATRÁS MOUREDEV PRO
------------------------------------

* EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente.
*/

use chrono::{DateTime, Utc, Duration};
use std::error::Error;
use std::fmt;
use std::thread;
use std::time::Duration as StdDuration;
use std::sync::{Arc, atomic::{AtomicBool, Ordering}};

#[derive(Debug)]
struct TimeComponents {
    days: i64,
    hours: i64,
    minutes: i64,
    seconds: i64,
}

#[derive(Debug)]
struct TimerError(String);

impl fmt::Display for TimerError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Timer error: {}", self.0)
    }
}

impl Error for TimerError {}

struct ReverseTimer {
    end_date: DateTime<Utc>,
    running: Arc<AtomicBool>,
}

impl ReverseTimer {
    fn new(end_date: &str) -> Result<Self, TimerError> {
        Ok(ReverseTimer {
            end_date: DateTime::parse_from_rfc3339(end_date)
                .map_err(|e| TimerError(format!("Invalid date format: {}", e)))?
                .with_timezone(&Utc),
            running: Arc::new(AtomicBool::new(true)),
        })
    }

    #[inline]
    fn time_remaining(&self) -> Duration {
        (self.end_date - Utc::now()).max(Duration::zero())
    }

    #[inline]
    fn get_time_components(remaining: Duration) -> TimeComponents {
        TimeComponents {
            days: remaining.num_days(),
            hours: remaining.num_hours() % 24,
            minutes: remaining.num_minutes() % 60,
            seconds: remaining.num_seconds() % 60,
        }
    }

    fn format_time(components: &TimeComponents) -> String {
        format!(
            "{} días, {} horas, {} minutos, {} segundos",
            components.days, components.hours, components.minutes, components.seconds
        )
    }

    fn display_time(&self) {
        print!("\x1B[2J\x1B[1;1H");
        let remaining = self.time_remaining();
        let components = Self::get_time_components(remaining);
        println!("Tiempo restante:");
        println!("{}", Self::format_time(&components));
    }

    fn start_countdown(self) -> thread::JoinHandle<()> {
        thread::spawn(move || {
            while self.running.load(Ordering::Relaxed) {
                let remaining = self.time_remaining();
                
                if remaining == Duration::zero() {
                    self.running.store(false, Ordering::Relaxed);
                    break;
                }

                self.display_time();
                thread::sleep(StdDuration::from_secs(1));
            }
            println!("¡Cuenta atrás finalizada!");
        })
    }

    fn stop(&self) {
        self.running.store(false, Ordering::Relaxed);
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let timer = ReverseTimer::new("2024-12-31T23:59:59.999999Z")?;
    let timer_thread = timer.start_countdown();

    // timer.stop();
    timer_thread.join().unwrap();
    Ok(())
}
