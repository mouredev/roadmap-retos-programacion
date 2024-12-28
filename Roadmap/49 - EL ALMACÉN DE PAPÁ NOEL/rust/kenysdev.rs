/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
#49 EL ALMACÉN DE PAPÁ NOEL
------------------------------------

 * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 * 
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 * 
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y 
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 * 
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.

[dependencies]
rand = "0.8.5"
*/

use rand::seq::SliceRandom;
use std::io;

fn verify_allowed_char(code_entry: &str) -> bool {
    for ch in code_entry.chars() {
        if !"abc123".contains(ch) {
            println!("Uno de los caracteres no está entre los permitidos.\n");
            return false;
        }
    }
    true
}

fn get_entry() -> String {
    loop {
        println!("Código: ");
        let mut code_entry = String::new();
        io::stdin().read_line(&mut code_entry).unwrap();
        let code_entry = code_entry.trim();

        if code_entry.len() != 4 {
            println!("El código debe ser de 4 dígitos.\n");
            continue;
        }

        if verify_allowed_char(code_entry) {
            return code_entry.to_string();
        }
    }
}

fn is_open(code: &str) -> bool {
    let code_entry = get_entry();

    if code_entry == code {
        return true;
    }

    println!("Código inválido.\n");

    for (i, ch) in code_entry.chars().enumerate() {
        if code.chars().nth(i).unwrap() == ch {
            println!("'{}' está en la posición correcta.", ch);
        } else if code.contains(ch) {
            println!("'{}' está en el código, pero en otra posición.", ch);
        } else {
            println!("'{}' no está presente en el código.", ch);
        }
    }

    false
}

fn main() {
    println!("
* Papá Noel tiene que comenzar a repartir los regalos...
* ¡Pero ha olvidado el código secreto de apertura del almacén!

- Tienes 10 intentos para adivinar el código que abre el almacén.
- Código de 4 caracteres. Permitidos: a, b, c, 1, 2, 3.
- Nota: No hay dígitos repetidos.");

    let characters = ["a", "b", "c", "1", "2", "3"];
    let mut rng = rand::thread_rng();
    let code: String = characters
        .choose_multiple(&mut rng, 4)
        .cloned()
        .collect::<String>();

    for attempts in 1..11 {
        println!("\n___________\nIntento #{}", attempts);
        if is_open(&code) {
            println!("Código correcto, almacén abierto.");
            println!("Papá Noel ahora podrá entregar los regalos.");
            break;
        }

        if attempts == 10 {
            println!("\n___________\nHas perdido.");
            println!("Papá Noel ya no podrá entregar los regalos.");
        }
    }
}
