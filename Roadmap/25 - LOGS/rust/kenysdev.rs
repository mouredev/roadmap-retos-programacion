/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* LOGS
-----------------------------------------
Dependencia: https://crates.io/crates/log
             https://crates.io/crates/env_logger

[dependencies]
env_logger = "0.11.3"
log = "0.4.21"
*/

use log::{error, warn, info, debug, trace};

fn main() {
    /*
    * EJERCICIO #1:
    * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
    * un ejemplo con cada nivel de "severidad" disponible.
    */

    env_logger::Builder::from_default_env()
        .filter_level(log::LevelFilter::Trace)
        .init();
        
    debug!("msg {}", "debug");
    warn!("msg warn");
    info!("msg info");
    trace!("msg trace");
    error!("msg error");

    //____________________________________
    println!("EJERCICIO #2");

    let mut tasks = Program::new();

    tasks.add("a", "1");
    tasks.add("b", "2");
    tasks.add("c", "3");

    tasks.delete("a");
    tasks.show_list();

}

/*
* EJERCICIO #2:
* Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
* y listar dichas tareas.
* - Añadir: recibe nombre y descripción.
* - Eliminar: por nombre de la tarea.
* Implementa diferentes mensajes de log que muestren información según la 
* tarea ejecutada (a tu elección).
* Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
*/

struct Program {
    tasks: std::collections::HashMap<String, String>,
}

impl Program {
    fn new() -> Self {
        debug!("Se inició instancia.");
        Program {
            tasks: std::collections::HashMap::new(),
        }
    }

    fn add(&mut self, name: &str, description: &str) {
        self.tasks.insert(name.to_string(), description.to_string());
        info!("Se agregó una tarea.");
    }

    fn delete(&mut self, name: &str) {
        if self.tasks.remove(name).is_some() {
            info!("Tarea '{}' eliminada.", name);
        } else {
            println!();
            warn!("No se encontró la tarea '{}'.", name);
        }
    }

    fn show_list(&self) {
        info!("Lista de tareas");
        for (task, des) in &self.tasks {
            println!("{} -- {}", task, des);
        }
    }
}
