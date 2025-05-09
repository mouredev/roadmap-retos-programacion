/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------------------
* RESCATANDO A MICKEY
-----------------------------------------------------
 * ¡Disney ha presentado un montón de novedades en su D23!
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
*/

use std::cell::RefCell;
use std::collections::HashMap;
use std::io::{self, Write};
use std::rc::Rc;

// [dependencies]
// rand = "0.8.5"
// https://crates.io/crates/rand
use rand::prelude::*;

//____________________________________________________________
struct Input;

impl Input {
    fn get(&self, msg: &str) -> String {
        print!("{}", msg);
        io::stdout().flush().expect("Error flushing output buffer.");
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Error reading input.");
        return input.trim().to_string();
    }
}

//____________________________________________________________
struct Data {
    maze: Vec<Vec<String>>,
    position_mouse: (usize, usize),
    exit_location: (usize, usize),
    width: usize,
    height: usize,
    title: String,
    obstacle_char: String,
    empty_char: String,
    mouse_char: String,
    exit_char: String,
}

impl Data {
    fn new(config: HashMap<&str, &str>) -> Rc<RefCell<Self>> {
        let size: Vec<&str> = config["size"].split(',').collect();
        let width = size[0].trim().parse().expect("Invalid width value");
        let height = size[1].trim().parse().expect("Invalid height value");

        Rc::new(RefCell::new(Data {
            maze: Vec::new(),
            position_mouse: (0, 0),
            exit_location: (0, 0),
            width,
            height,
            title: config["title"].to_string(),
            obstacle_char: config["obstacle"].to_string(),
            empty_char: config["empty"].to_string(),
            mouse_char: config["mouse"].to_string(),
            exit_char: config["exit"].to_string(),
        }))
    }

    fn print_maze(&self) {
        println!("--------------------------------------");
        for row in &self.maze {
            println!("{}", row.join(""));
        }
        println!("--------------------------------------");
    }

    fn print_config(&self) {
        println!(
            "{}\nSize: {}*{}\nObstacle: {}\nEmpty: {}\nMouse: {}\nExit: {}",
            self.title,
            self.width,
            self.height,
            self.obstacle_char,
            self.empty_char,
            self.mouse_char,
            self.exit_char
        )
    }
}

//____________________________________________________________
struct Moves {
    data: Rc<RefCell<Data>>,
}

impl Moves {
    fn new(data: Rc<RefCell<Data>>) -> Self {
        Moves { data }
    }

    fn can_move(&self, y: isize, x: isize, old_y: usize, old_x: usize) {
        let mut data_ref = self.data.borrow_mut();
        let rows = data_ref.maze.len();
        let cols = data_ref.maze[0].len();
        if y < 0 || x < 0 || y >= rows as isize || x >= cols as isize {
            println!("🚨I can't jump over the edges.🚨");
            return;
        }

        let y = y as usize;
        let x = x as usize;

        if data_ref.maze[y][x] == data_ref.obstacle_char {
            println!("🚨You pushed me against the wall.🚨");
            return;
        }

        data_ref.position_mouse = (y, x);
        println!("✅Correct move.✅");
        data_ref.maze[old_y][old_x] = data_ref.empty_char.clone();
        data_ref.maze[y][x] = data_ref.mouse_char.clone();
    }

    fn up(&self) {
        let (y, x) = self.data.borrow().position_mouse;
        self.can_move(y as isize - 1, x as isize, y, x);
    }

    fn down(&self) {
        let (y, x) = self.data.borrow().position_mouse;
        self.can_move(y as isize + 1, x as isize, y, x);
    }

    fn right(&self) {
        let (y, x) = self.data.borrow().position_mouse;
        self.can_move(y as isize, x as isize + 1, y, x);
    }

    fn left(&self) {
        let (y, x) = self.data.borrow().position_mouse;
        self.can_move(y as isize, x as isize - 1, y, x);
    }
}

//____________________________________________________________
struct Maze {
    data: Rc<RefCell<Data>>,
    moves: Moves,
}

impl Maze {
    fn new(data: Rc<RefCell<Data>>, moves: Moves) -> Self {
        Maze { data, moves }
    }

    fn create_paths(&self, x: usize, y: usize) {
        let mut data_ref = self.data.borrow_mut();
        data_ref.maze[y][x] = data_ref.empty_char.clone();

        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut rng = rand::thread_rng();
        let mut directions: Vec<_> = directions.iter().copied().collect();
        directions.shuffle(&mut rng);

        let width = data_ref.width;
        let height = data_ref.height;

        for (dx, dy) in directions {
            let nx = x as isize + dx * 2;
            let ny = y as isize + dy * 2;
            if 0 < nx && nx < width as isize - 1 && 0 < ny && ny < height as isize - 1 {
                let nx = nx as usize;
                let ny = ny as usize;

                if data_ref.maze[ny][nx] == data_ref.obstacle_char.clone() {
                    let mid_x = (x as isize + dx) as usize;
                    let mid_y = (y as isize + dy) as usize;

                    if mid_x < width && mid_y < height {
                        data_ref.maze[mid_y][mid_x] = data_ref.empty_char.clone();
                        drop(data_ref);
                        self.create_paths(nx, ny);
                        data_ref = self.data.borrow_mut();
                    }
                }
            }
        }
    }

    fn create(&self) {
        let mut data_ref = self.data.borrow_mut();

        if data_ref.width % 2 == 0 {
            data_ref.width += 1;
        }
        if data_ref.height % 2 == 0 {
            data_ref.height += 1;
        }

        data_ref.maze = vec![vec![data_ref.obstacle_char.clone(); data_ref.width]; data_ref.height];

        let height = data_ref.height;
        let width = data_ref.width;
        data_ref.maze[0][1] = data_ref.mouse_char.clone();
        data_ref.maze[height - 1][width - 2] = data_ref.exit_char.clone();
        data_ref.position_mouse = (0, 1);
        data_ref.exit_location = (height - 1, width - 2);

        let mut rng = rand::thread_rng();
        let initial_x = rng.gen_range(1..width - 1) | 1;
        let initial_y = rng.gen_range(1..height - 1) | 1;

        drop(data_ref);
        self.create_paths(initial_x, initial_y);
    }

    fn verify_win(&self) -> bool {
        let data = self.data.borrow();
        let (y, x) = data.exit_location;
        return data.maze[y][x] == data.mouse_char;
    }
}

//____________________________________________________________
struct Game {
    input: Input,
    maze: Maze,
}

impl Game {
    fn new(input: Input, maze: Maze) -> Self {
        Game { input, maze }
    }

    fn restart_or_exit(&self) -> bool {
        loop {
            match self.input.get("Y/N: ").as_str() {
                "y" => return true,
                "n" => return false,
                _ => println!("❌Invalid key.❌"),
            }
        }
    }

    fn play(&self) {
        self.maze.data.borrow().print_config();

        self.maze.create();
        loop {
            self.maze.data.borrow().print_maze();
            println!("Use the keys: (W, S, A, D).\nTo restart: R. To exit: 9.");

            match self.input.get("Key: ").as_str() {
                "w" => self.maze.moves.up(),
                "s" => self.maze.moves.down(),
                "d" => self.maze.moves.right(),
                "a" => self.maze.moves.left(),
                "r" => {
                    println!("😮Do you want to restart?😮");
                    if self.restart_or_exit() {
                        self.maze.create();
                    }
                }
                "9" => {
                    println!("😮Do you want to exit?😮");
                    if self.restart_or_exit() {
                        return;
                    }
                }
                
                _ => println!("❌Invalid key.❌"),
            }

            if self.maze.verify_win() {
                println!("🏆Congratulations, you managed to get me out.🏆");
                println!("🤔Do you want to play again?🤔");
                if self.restart_or_exit() {
                    self.maze.create();
                } else {
                    println!("Bye");
                    return;
                }
            }
        }
    }
}

//____________________________________________________________
fn main() {
    // These are the default values. You can change them here.
    let config: HashMap<&str, &str> = [
        ("title", "RESCUING MICKEY"),
        ("size", "7, 7"),
        ("empty", "⬜️"),
        ("obstacle", "⬛️"),
        ("mouse", "🐭"),
        ("exit", "🚪"),
    ]
    .iter()
    .cloned()
    .collect();

    let input = Input;
    let data = Data::new(config);
    let moves = Moves::new(data.clone());
    let maze = Maze::new(data.clone(), moves);
    let game = Game::new(input, maze);
    game.play();
}
