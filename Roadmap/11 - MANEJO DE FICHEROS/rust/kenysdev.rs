/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* MANEJO DE FICHEROS
-----------------------------------------
* EJERCICIO:
* Desarrolla un programa capaz de crear un archivo que se llame como
* tu usuario de GitHub y tenga la extensión .txt.
* Añade varias líneas en ese fichero:
* - Tu nombre.
* - Edad.
* - Lenguaje de programación favorito.
* Imprime el contenido.
* Borra el fichero.
*/

use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::fs;

fn write_all(the_path: &str, content: &str) {
    let path = Path::new(the_path);
    let display = path.display();

    let mut file = match File::create(&path) {
        Err(why) => panic!("No se pude crear {}: {}", display, why),
        Ok(file) => file,
    };

    match file.write_all(content.as_bytes()) {
        Err(why) => panic!("No se pude escribir en {}: {}", display, why),
        Ok(_) => println!("* Se escribió en {}", display),
    }
}

fn print_all(the_path: &str) {
    match fs::read_to_string(the_path) {
        Ok(content) => {
            println!("* Contenido de {}: \n{}", the_path, content);
        }
        Err(err) => {
            println!("Error al leer el archivo {}: {}", the_path, err);
        }
    }
}

fn delete_file(the_path: &str) {
    if let Err(err) = fs::remove_file(the_path) {
        println!("Error al eliminar {}: {}", the_path, err);
    } else {
        println!("* {} ha sido eliminado.", the_path);
    }
}

fn main(){
    write_all("kenysdev.txt", "- Ken\n- 121\n- Python");
    print_all("kenysdev.txt");
    delete_file("kenysdev.txt");    
}
