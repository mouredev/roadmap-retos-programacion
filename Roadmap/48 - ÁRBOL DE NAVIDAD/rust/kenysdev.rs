/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
#48 ÁRBOL DE NAVIDAD
------------------------------------

 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 * 
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 * 
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 * 
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).

[dependencies]
rand = "0.8.5"
*/

use std::io::{self, Write};
use std::thread;
use std::time::Duration;
use rand::seq::SliceRandom;

#[derive(Debug)]
struct ChristmasTree {
    size: usize,
    matrix: Vec<Vec<char>>,
    star: (usize, usize),
    tree_top: Vec<(usize, usize)>,
    balls: Vec<(usize, usize)>,
    lights: Vec<(usize, usize)>,
}

impl ChristmasTree {
    fn new(size: usize) -> Self {
        let cols = size * 2 - 1;
        let matrix = vec![vec![' '; cols]; size];
        let star = (0, size - 1);
        
        Self {
            size,
            matrix,
            star,
            tree_top: Vec::new(),
            balls: Vec::new(),
            lights: Vec::new(),
        }
    }

    fn print_tree(&self) {
        println!();
        for row in &self.matrix {
            println!("{}", row.iter().collect::<String>());
        }

        let spaces = (self.size * 2 - 4) / 2;
        println!("{}{}", " ".repeat(spaces), "|||");
        println!("{}{}", " ".repeat(spaces), "|||");
    }

    fn create_tree(&mut self) {
        let center = self.size - 1;
        for i in 0..self.size {
            let asterisks = "*".repeat(i * 2 + 1);
            for (j, c) in asterisks.chars().enumerate() {
                let col = center - i + j;
                self.matrix[i][col] = c;
                self.tree_top.push((i, col));
            }
        }
        self.tree_top.remove(0);
    }

    fn add_remove_star(&mut self) {
        let (row, col) = self.star;
        self.matrix[row][col] = if self.matrix[row][col] == '*' { '@' } else { '*' };
    }

    fn add_balls(&mut self) {
        if self.tree_top.len() < 2 {
            println!("Ya no hay espacio para poner bolas.");
            return;
        }
    
        let mut rng = rand::thread_rng();
        let count = std::cmp::min(2, self.tree_top.len());
    
        for _ in 0..count {
            if let Some(&pos) = self.tree_top.choose(&mut rng) {
                if let Some(idx) = self.tree_top.iter().position(|&x| x == pos) {
                    let removed_pos = self.tree_top.remove(idx);
                    self.balls.push(removed_pos);
                    self.matrix[removed_pos.0][removed_pos.1] = 'o';
                }
            }
        }
    }
    
    fn remove_balls(&mut self) {
        if self.balls.is_empty() {
            println!("No hay bolas que eliminar.");
            return;
        }
    
        let mut rng = rand::thread_rng();
        let count = std::cmp::min(2, self.balls.len());

        for _ in 0..count {
            if let Some(&pos) = self.balls.choose(&mut rng) {
                if let Some(idx) = self.balls.iter().position(|&x| x == pos) {
                    let removed_pos = self.balls.remove(idx);
                    self.tree_top.push(removed_pos);
                    self.matrix[removed_pos.0][removed_pos.1] = '*';
                }
            }
        }
    }
    fn add_lights(&mut self) {
        if self.tree_top.len() < 3 {
            println!("Ya no hay espacio para poner luces.");
            return;
        }
    
        let mut rng = rand::thread_rng();
        let count = std::cmp::min(3, self.tree_top.len());

        for _ in 0..count {
            if let Some(&pos) = self.tree_top.choose(&mut rng) {
                if let Some(idx) = self.tree_top.iter().position(|&x| x == pos) {
                    let removed_pos = self.tree_top.remove(idx);
                    self.lights.push(removed_pos);
                    self.matrix[removed_pos.0][removed_pos.1] = '+';
                }
            }
        }
    }
    
    fn remove_lights(&mut self) {
        if self.lights.is_empty() {
            println!("No hay luces que eliminar.");
            return;
        }
    
        let mut rng = rand::thread_rng();
        let count = std::cmp::min(3, self.lights.len());
    
        for _ in 0..count {
            if let Some(&pos) = self.lights.choose(&mut rng) {
                if let Some(idx) = self.lights.iter().position(|&x| x == pos) {
                    let removed_pos = self.lights.remove(idx);
                    self.tree_top.push(removed_pos);
                    self.matrix[removed_pos.0][removed_pos.1] = '*';
                }
            }
        }
    }

    fn on_off_lights(&mut self) {
        if self.lights.is_empty() {
            println!("No hay luces.");
            return;
        }

        for &(row, col) in &self.lights {
            self.matrix[row][col] = if self.matrix[row][col] == '*' { '+' } else { '*' };
        }
    }

    fn automatic_lights(&mut self) -> io::Result<()> {
        loop {
            print!("\x1B[2J\x1B[1;1H"); // Clear screen
            io::stdout().flush()?;
            
            for &(row, col) in &self.lights {
                self.matrix[row][col] = if self.matrix[row][col] == '*' { '+' } else { '*' };
            }
            
            self.print_tree();
            thread::sleep(Duration::from_secs(1));
        }
    }
}

const MENU: &str = r#"
1 - Agregar/Remover estrella.
2 - Agregar bolas.    | 3 - Quitar bolas.
4 - Agregar luces.    | 5 - Quitar luces.
6 - Encender/Apagar luces.
7 - Luces automáticas.| 8 - Salir
"#;

fn show_menu(tree: &mut ChristmasTree) -> io::Result<()> {
    loop {
        tree.print_tree();
        println!("{}", MENU);
        print!("Opción: ");
        io::stdout().flush()?;

        let mut option = String::new();
        io::stdin().read_line(&mut option)?;

        match option.trim() {
            "1" => tree.add_remove_star(),
            "2" => tree.add_balls(),
            "3" => tree.remove_balls(),
            "4" => tree.add_lights(),
            "5" => tree.remove_lights(),
            "6" => tree.on_off_lights(),
            "7" => tree.automatic_lights()?,
            "8" => break,
            _ => println!("Opción inválida."),
        }
    }
    Ok(())
}

fn get_size() -> io::Result<usize> {
    loop {
        print!("Tamaño: ");
        io::stdout().flush()?;

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;

        if let Ok(size) = input.trim().parse::<usize>() {
            if size % 2 != 0 && size >= 3 {
                return Ok(size);
            }
        }
        println!("Debe ser un número impar >= 3.");
    }
}

fn main() -> io::Result<()> {
    let size = get_size()?;
    let mut christmas_tree = ChristmasTree::new(size);
    christmas_tree.create_tree();
    show_menu(&mut christmas_tree)?;
    Ok(())
}
