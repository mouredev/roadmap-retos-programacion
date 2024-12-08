/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
47  CALENDARIO DE ADVIENTO
------------------------------------

 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 * 
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño 
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *   
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
*/

use std::io::{self, Write};

fn main() {
    let mut mtx: [[String; 6]; 4] = Default::default();
    for i in 0..4 {
        for j in 0..6 {
            mtx[i][j] = format!("*{:02}*", i * 6 + j + 1);
        }
    }

    let ln = "**** ".repeat(6).trim_end().to_string();

    loop {
        for i in 0..4 {
            println!("{}", ln);
            let current_row = i;

            for j in 0..6 {
                print!("{} ", mtx[current_row][j]);
            }
            println!("\n{}\n", ln);
        }

        print!("Día a descubrir: ");
        io::stdout().flush().unwrap();
        let mut day = String::new();
        io::stdin().read_line(&mut day).unwrap();
        let day = day.trim();

        let day_int: i32 = match day.parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Entrada inválida. Debe ser un número.");
                continue;
            }
        };

        if day_int < 1 || day_int > 24 {
            println!("Día inválido, debe ser entre 1 y 24.");
            continue;
        }

        let r = (day_int - 1) / 6;
        let c = (day_int - 1) % 6;

        if mtx[r as usize][c as usize] == "****" {
            println!("El día {} ya está descubierto.", day);
            continue;
        }

        mtx[r as usize][c as usize] = "****".to_string();
    }
}
