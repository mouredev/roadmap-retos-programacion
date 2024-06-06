/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* PILAS Y COLAS
-----------------------------------------
- Son estructuras de datos comunes utilizadas para 
  organizar y manipular datos.
*/
use std::io::{self, Write};
use std::collections::VecDeque;
fn main() {
    // ______________________________________________________________
    // * PILAS (STACK - LIFO):
    // - Sigue el principio LIFO (last in, first out)
    // - El último elemento añadido, es el primero en ser retirado.

    let mut stack: Vec<i8> = Vec::new();
    // Agregar elementos.
    stack.push(1); 
    stack.push(2);
    stack.push(3);

    // Eliminar y obtener el elemento superior de la pila (pop):
    if let Some(top) = stack.pop() {
        println!("Eliminar y obtener: {top}");
    } else {
        println!("Pila vacia");
    }

    // Obtener el elemento superior de la pila sin eliminarlo (peek)
    if let Some(top) = stack.last() {
        println!("Obtener sin eliminar: {top}")
    } else {
        println!("Pila vacia")
    }

    // Verificar si la pila está vacía:
    if stack.is_empty() {
        println!("Pila vacia");
    } else {
        println!("Pila tiene elementos");
    }

    // Obtener el tamaño de la pila:
    println!("Total de elementos: {}", stack.len());

    // Verificar si existe
    let x: i8 = 5;
    if stack.contains(&x) {
        println!("{x} está en la pila.");
    } else {
        println!("{x} no está en la pila.");
    }

    // Imprimir todos
    println!("{:?}", stack);


    // ______________________________________________________________
    // * COLAS (QUEUE - FIFO)
    // - sigue el principio FIFO(First In, First Out)
    // - El primer elemento que se inserta es el primero en ser retirado.

    let mut queue: VecDeque<i8> = VecDeque::new();

    // Agregar elementos a la cola (enqueue):
    queue.push_back(1);
    queue.push_back(2);
    queue.push_back(3);

    // Obtener el elemento sin eliminarlo (peek):
    if let Some(front) = queue.front() {
        println!("Elemento en el frente de la cola: {front}");
    } else {
        println!("Cola vacía.");
    }

    // Eliminar y obtener el elemento (dequeue):
    if let Some(front) = queue.pop_front() {
        println!("Eliminar y obtener en cola: {front}");
    } else {
        println!("Cola vacía.");
    }

    // otros
    println!("Está vacía?: {}", queue.is_empty());
    println!("Total de elementos: {}", queue.len());
    println!("Verificar si existe 5: {}", queue.contains(&5));
    println!("Imprimir todos: {:?}", queue);

    // ______________
    // ejercicio
    home()

}
/* ______________________________________________________________
* * EJERCICIOS:
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.
* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
*/
const MSG_HOME: &str = "
-----------------------------------
- '1' -> simulador_navegador.
- '2' -> simulador_impresora.
- 'enter' -> SALIR
-----------------------------------
";

const MSG_NAV: &str = "
-----------------------------------
- '<' para página anterior.
- '>' para página adelante.
- 'h' Ver historial completo.
- 'x' para salir. 
Escribir web para agregar:
-----------------------------------
";

const MSG_PRINTER: &str = "
-----------------------------------
- 'p' Imprimir.
- 'l' Ver documentos pendientes.
- 'x' para salir.
Escribir nombre para enviar a cola:
-----------------------------------
";

fn home(){
    println!("{MSG_HOME}");
    let action: String = input("____________\nAcción: ");
    match action.as_str() {
        "1" => nav_history(),
        "2" => queue_printer(),
        _ => println!("Adios"),
    }
}

fn nav_history() {
    let mut history: Vec<String> = vec!["Inicio".to_string()]; 
    let mut back_history: Vec<String> = Vec::new(); 
    let mut forward_history: Vec<String> = Vec::new();
    println!("{}", MSG_NAV);
    loop { 
        println!("{} <-[{}]-> {}", 
        back_history.len(), history.last().unwrap(), forward_history.len());
        let action: String = input("____________\nAcción: ");
        match action.as_str() {
            "<" => {
                if back_history.len() > 0 {
                    forward_history.push(history.last().unwrap().clone()); 
                    history.push(back_history.pop().unwrap());
                } else {
                    println!("No hay página previa.")
                }
            },
            ">" => {
                if forward_history.len() > 0 {
                    back_history.push(history.last().unwrap().clone());
                    history.push(forward_history.pop().unwrap());
                } else {
                    println!("No hay página siguiente.")
                }
            },
            "h" => {
                if history.len() > 0 {
                    for web in &history { 
                        println!("{}", web); 
                    }
                } else {
                    println!("Historial vacío.")
                }
            },
            "x" => {
                home(); 
                break;
            },
            _ => {
                back_history.push(history.last().unwrap().clone());
                forward_history.clear();
                history.push(action); 
            },
        }
    }
}

fn queue_printer() {
    let mut doc_queue: VecDeque<String> = VecDeque::new();
    println!("{}", MSG_PRINTER);
    loop {
        let action: String = input("____________\nAcción: ");
        if action.len() > 0 {
            match action.as_str() {
                "p" => {
                    if doc_queue.len() > 0{
                        println!("{} -> ha sido impreso\n{} -> archivos faltantes.", 
                        doc_queue.pop_front().unwrap(), doc_queue.len());
                    } else {
                        println!("No hay archivos.");
                    }
                },
                "l" => {
                    if doc_queue.len() > 0 {
                        for doc in &doc_queue {
                            println!("{}", doc);
                        }
                    } else {
                        println!("No hay archivos.");
                    }
                },
                "x" => {
                    home();
                    break;
                },
                _ => {
                    doc_queue.push_back(action);
                    println!("Archivo agregado a cola de impresión.");
                }
            }
        } else {
            println!("xD");
        }
    }
}

fn input(msg: &str) -> String {
    print!("{msg}");
    io::stdout().flush().expect("Error al limpiar búfer");

    let mut input_txt: String = String::new();
    io::stdin()
        .read_line(&mut input_txt)
        .expect("Error al leer la entrada");

    input_txt.trim().to_string()
}

