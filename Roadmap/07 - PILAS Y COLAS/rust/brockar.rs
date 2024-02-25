use std::io;
fn main() {
    let mut array: Vec<i32> = vec![1, 2, 3];
    println!("pila: {:?}", array);
    pila_agregar(&mut array, 4);
    println!("pila_agregar, (4): {:?}", array);

    println!(
        "pila_quitar, quita {}, la pila queda: {:?}",
        pila_quitar(&mut array),
        array
    );

    println!("cola: {:?}", array);
    cola_agregar(&mut array, 5);
    println!("cola_agregar, (5): {:?}", array);

    let ultimo_valor = cola_quitar(&mut array);
    println!(
        "cola_quitar, quita {}, la cola queda: {:?}",
        ultimo_valor, array
    );

    println!("Presiona Enter para empezar con las funciones extras");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Error de lectura");
    clear_terminal().expect("Error al limpiar");
    extra1();
    extra2();
}

fn pila_agregar(vector: &mut Vec<i32>, add: i32) {
    vector.push(add);
}

fn pila_quitar(vector: &mut Vec<i32>) -> i32 {
    vector.pop().unwrap()
}

fn cola_agregar(vector: &mut Vec<i32>, add: i32) {
    vector.push(add);
}

fn cola_quitar(vector: &mut Vec<i32>) -> i32 {
    vector.remove(0)
}

use std::io::Write;
fn clear_terminal() -> io::Result<()> {
    // Enviamos el escape code para limpiar la pantalla y colocar el cursor en la esquina superior izquierda
    print!("\x1B[2J\x1B[1;1H");
    io::stdout().flush()?;

    Ok(())
}

fn extra1() {
    /*
        Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
        de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
        que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
        Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
        el nombre de una nueva web.
    */
    let mut historial: Vec<String> = Vec::new();
    let mut historial1: Vec<String> = Vec::new();
    let mut cadena: String = String::new(); // cadena = pagina actual
    let mut comando = String::new();
    loop {
        println!("-----------");
        println!("| EXTRA 1 |");
        println!("-----------");
        if !comando.is_empty() {
            println!("{}", comando);
            println!("----------------------------");
        }
        println!("Pagina actual: {}", cadena);

        println!("----------------------------");
        println!(
            "Historial: {:?} \nHistorialAdelante: {:?}",
            historial, historial1
        );
        println!("----------------------------");
        println!(
                "\"adelante\" para cambiar a una nueva pagina\n\"atras\" para ir a la página anteriores\n\"nombre-web\" para agregar una web\n\"salir\" para cerrar el programa"
            );
        comando = String::new();
        std::io::stdin().read_line(&mut comando).unwrap();
        comando = comando.trim().to_string();

        match comando.as_str() {
            "atras" => {
                if !historial.is_empty() {
                    if historial.len() > 1 {
                        pila_quitar_s(&mut historial);
                    }

                    pila_agregar_s(&mut historial1, cadena.clone());
                    cadena = pila_quitar_s(&mut historial);
                    comando = String::new();
                } else {
                    comando = "Historial vacio".to_string();
                }
            }
            "adelante" => {
                if !historial1.is_empty() {
                    pila_agregar_s(&mut historial, cadena.clone());
                    cadena = pila_quitar_s(&mut historial1);
                    comando = String::new();
                } else {
                    comando = "Estas en la última página".to_string();
                }
            }
            "salir" => {
                break;
            }
            _ => {
                if !comando.is_empty() {
                    cadena = comando.clone();
                    comando = String::new();
                    pila_agregar_s(&mut historial, cadena.clone());
                }
            }
        }
        clear_terminal().expect("Error al limpiar");
    }
}

fn pila_agregar_s(vector: &mut Vec<String>, add: String) {
    vector.push(add);
}

fn pila_quitar_s(vector: &mut Vec<String>) -> String {
    vector.pop().unwrap()
}

/*
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
*/

fn extra2() {
    clear_terminal().expect("Error al limpiar");
    let mut cola: Vec<String> = Vec::new();

    loop {
        println!("-----------");
        println!("| EXTRA 2 |");
        println!("-----------");
        println!("\"imprimir\" para imprimir\n\"papel\" para agregar un papel a la cola de impresion\n\"salir\" para cerrar el programa");
        let mut entrada: String = String::new();
        std::io::stdin().read_line(&mut entrada).unwrap();
        entrada = entrada.trim().to_string();
        if entrada == "imprimir" {
            if !cola.is_empty() {
                clear_terminal().expect("Error al limpiar");
                println!("Imprimiendo...");
                println!("{}", cola_quitar_s(&mut cola));
            } else {
                clear_terminal().expect("Error al limpiar");
                println!("No hay papeles");
            }
        } else if entrada == "salir" {
            break;
        } else {
            cola_agregar_s(&mut cola, entrada);
            clear_terminal().expect("Error al limpiar");
        }
    }
}

fn cola_agregar_s(vector: &mut Vec<String>, add: String) {
    vector.push(add);
}

fn cola_quitar_s(vector: &mut Vec<String>) -> String {
    vector.remove(0)
}
