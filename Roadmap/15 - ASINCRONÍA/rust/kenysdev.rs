
/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* ASINCRONÍA
-----------------------------------------
https://crates.io/crates/tokio

[dependencies]
tokio = { version = "1.37.0", features = ["full"] }

* EJERCICIO #1:
* Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
* asíncrona una función que tardará en finalizar un número concreto de
* segundos parametrizables. También debes poder asignarle un nombre.
* La función imprime su nombre, cuándo empieza, el tiempo que durará
* su ejecución y cuando finaliza.
*/

use tokio::time::{sleep, Duration};

async fn process(name: &str, time: u64) {
    println!("* Iniciar función: {} -> Duración: {}", name, time);
    sleep(Duration::from_secs(time)).await;
    println!("- Función {} finaliza.", name);
}

async fn test() {
    tokio::join!(
        process("Test 2", 3),
        process("Test 1", 1)
    );
}

/*
* EJERCICIO #2:
* Utilizando el concepto de asincronía y la función anterior, crea
* el siguiente programa que ejecuta en este orden:
* - Una función C que dura 3 segundos.
* - Una función B que dura 2 segundos.
* - Una función A que dura 1 segundo.
* - Una función D que dura 1 segundo.
* - Las funciones C, B y A se ejecutan en paralelo.
* - La función D comienza su ejecución cuando las 3 anteriores han
*   finalizado.
*/

async fn in_parallel() {
    tokio::join!(
        process("C", 3),
        process("B", 2),
        process("A", 1)
    );
}

#[tokio::main]
async fn main() {
    test().await;
    in_parallel().await;
    process("D", 1).await;
}
