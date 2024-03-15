/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
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

fn webbrowser(){
    let mut tabs: Vec<String> = Vec::new();
    let mut input: String = String::new();
    let mut position = 0;
    
    println!("-------------------- BIENVENIDO AL NAVEGADOR --------------------");
    println!("-- -> Para añadir una nueva pestaña simplemente escriba el nombre --");
    println!("-- -> Si quieres ver todas las pestañas abiertas usa 'tabs' --");
    println!("-- -> Si deseas salir del programa escribe 'exit' --");

    loop {
        input.clear();
        std::io::stdin().read_line(&mut input).expect("Ha ocurrido un error leyendo");

        let input = input.trim();

        if input == "adelante" {
            if position == tabs.len() - 1{
                println!("No puedes ir mas hacia adelante. No hay mas pestañas.");
            } else {
                position += 1;
            }
        } else if input == "atras" {
            if position > 0 {
                position -= 1;
            } else {
                println!("No puede ir mas hacia atrás. No hay mas pestañas");
            }
        } else if input == "exit" {
            break;
        } else if input == "tabs" {
            println!("{:?}", tabs);
        } else {
            tabs.push(input.to_string());
            if tabs.len() > 1 {
                position += 1;
            }
        }

        println!("Te encuentras en la pestaña {}", tabs[position]);
    }

    println!("Se ha cerrado el navegador.");
}

fn printer(){
    let mut document_queue: Vec<String> = Vec::new();
    let mut input: String = String::new();

    println!("-------------------- BIENVENIDO AL PROGRAMA DE IMPRESIÓN --------------------");
    println!("------ -> Para añadir un nuevo documento simplemente escriba el nombre ------");
    println!("------ -> Para imprimir un documento escribe la palabra 'imprimir' ------");
    println!("------ -> Si deseas salir del programa escribe 'exit' ------");
    
    loop {
        input.clear();
        std::io::stdin().read_line(&mut input).expect("Ha ocurrido un error leyendo");

        let input = input.trim();
    
        if input == "imprimir" {
            if document_queue.len() > 0 {
                println!("Imprimiendo documento {}", document_queue[0]);
                document_queue.remove(0);
            } else {
                println!("No hay documentos para imprimir!");
            }
        } else if input == "exit" {
            break;
        } else {
            println!("El documento {} ha sido añadido a la cola de impresión", input);
            document_queue.push(input.to_string());
        }
    }

    println!("El programa de impresión finalizo");

}

fn main(){
    // LIFO (Last In First Out) STACKS
    let mut stack: Vec<u32> = Vec::new();
    // push
    stack.push(34);
    stack.push(45);
    stack.push(10);
    // Print stack
    println!("{:?}", stack);
    // Delete last element
    stack.pop();
    // Print stack
    println!("{:?}", stack);

    // FIFO (First In First Out) QUEUES
    let mut queue: Vec<u32> = Vec::new();
    // Push
    queue.push(89);
    queue.push(33);
    queue.push(13);
    // Print queue
    println!("{:?}", queue);
    // Remove first element
    queue.remove(0);
    // Print queue
    println!("{:?}", queue);

    // EXTRA EXERCISE PRINTER
    printer();
    // EXTRA EXERCISE WEB BROWSER
    webbrowser();
}