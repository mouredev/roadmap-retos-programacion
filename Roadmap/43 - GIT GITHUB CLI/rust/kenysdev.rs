/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
43 GIT GITHUB CLI
-------------------------------------
* EJERCICIO:
 * ¡Me voy de viaje al GitHub Universe 2024 de San Francisco!
 *
 * Desarrolla un CLI (Command Line Interface) que permita 
 * interactuar con Git y GitHub de manera real desde terminal.
 * 
 * El programa debe permitir las siguientes opciones:
 * 1. Establecer el directorio de trabajo
 * 2. Crear un nuevo repositorio
 * 3. Crear una nueva rama
 * 4. Cambiar de rama
 * 5. Mostrar ficheros pendientes de hacer commit
 * 6. Hacer commit (junto con un add de todos los ficheros)
 * 7. Mostrar el historial de commits
 * 8. Eliminar rama
 * 9. Establecer repositorio remoto
 * 10. Hacer pull
 * 11. Hacer push
 * 12. Salir
 *
 * Puedes intentar controlar los diferentes errores.
*/

use std::env;
use std::io::{self, Write};
use std::path::Path;
use std::process::Command;

const MENU: &str = r#"
Comandos Git::
------------------------------------------------------------
| 1. Establecer directorio       | 7. Historial de commits |  
| 2. Crear repositorio           | 8. Eliminar rama        |
| 3. Crear rama                  | 9. Configurar remoto    |
| 4. Cambiar rama                | 10. pull                | 
| 5. Mostrar cambios pendientes  | 11. push                | 
| 6. 'add' + 'commit'            | 12. Salir               | 
------------------------------------------------------------"#;

const COMMANDS: &[GitCommand] = &[
    GitCommand { name: "Establecer directorio", command: "cd", prompt: Some("Ruta: ") },
    GitCommand { name: "Crear repositorio", command: "git init && git branch -M main", prompt: None },
    GitCommand { name: "Crear rama", command: "git branch -c", prompt: Some("Nombre: ") },
    GitCommand { name: "Cambiar rama", command: "git switch", prompt: Some("Nombre: ") },
    GitCommand { name: "Mostrar cambios", command: "git status -s", prompt: None },
    GitCommand { name: "Commit", command: "git add . && git commit -m", prompt: Some("Mensaje: ") },
    GitCommand { name: "Historial", command: "git log --oneline", prompt: None },
    GitCommand { name: "Eliminar rama", command: "git branch -d", prompt: Some("Nombre: ") },
    GitCommand { name: "Configurar remoto", command: "git remote add origin", prompt: Some("URL: ") },
    GitCommand { name: "Pull", command: "git pull origin", prompt: Some("rama: ") },
    GitCommand { name: "Push", command: "git push origin", prompt: Some("rama: ") },
];

fn run_command(command: &str) {
    let (program, args) = if cfg!(windows) {
        ("cmd", vec!["/C", command])
    } else {
        ("sh", vec!["-c", command])
    };

    match Command::new(program).args(&args).output() {
        Ok(output) => {
            if output.status.success() {
                println!("✅: {}", String::from_utf8_lossy(&output.stdout).trim());
            } else {
                println!("❌: {}", String::from_utf8_lossy(&output.stderr).trim());
            }
        }
        Err(e) => println!("❌: Error ejecutando el comando: {}", e),
    }
}

fn read_input(prompt: &str) -> String {
    print!("{}", prompt);
    io::stdout().flush().unwrap();
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    input.trim().to_string()
}

struct GitCommand {
    name: &'static str,
    command: &'static str,
    prompt: Option<&'static str>,
}

fn execute(cmd: &GitCommand) {
    println!("\n=> {}", cmd.name);
    println!("--------------------");
    match (cmd.command, cmd.prompt) {
        ("cd", Some(prompt)) => {
            let path = read_input(prompt);
            if Path::new(&path).is_dir() {
                env::set_current_dir(&path)
                    .unwrap_or_else(|_| println!("Error cambiando directorio"));
            } else {
                println!("Esta ruta no existe.");
            }
        },
        (cmd, Some(prompt)) => run_command(&format!("{} {}", cmd, read_input(prompt))),
        (cmd, None) => run_command(cmd),
    }
}

fn main() {
    loop {
        println!("{}", MENU);
        println!("Directorio actual: {}", env::current_dir().unwrap().display());
        println!("--------------------");
        match read_input("\nOpción: ").parse::<usize>().ok() {
            Some(n) if n == COMMANDS.len() + 1 => break,
            Some(n) if n > 0 && n <= COMMANDS.len() => execute(&COMMANDS[n - 1]),
            _ => println!("Opción inválida"),
        }
    }
}
