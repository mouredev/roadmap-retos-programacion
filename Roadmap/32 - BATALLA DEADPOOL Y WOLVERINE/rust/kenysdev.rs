/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------------------
* BATALLA DEADPOOL Y WOLVERINE
-----------------------------------------------------

* EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
*/

// _____
// NOTA: Estoy intentando practicar los principios SOLID. XD 😂

// ________________________________________________

// [dependencies]
// rand = "0.8.5"
// https://crates.io/crates/rand
use rand::prelude::*;

use std::io::{self, Write};
use std::collections::HashMap;
use std::thread::sleep;
use std::time::Duration;

// ---------------------------------------
// INTERFACES
// ---------------------------------------

/// Contrato sobre la configuración global del juego.
pub trait IGlobalConfig {
    fn turn_interval(&self) -> i32;
    fn minimum_hp(&self) -> i32;
    /// Diccionario de personajes, con sus habilidades, Daño posible, Probabilidad de defensa.
    /// Fácil de adaptar a un Json de personajes.
    /// {"Character": {"attacks": ["Attack1", "Attack2"], "damage_range": (10, 100), "defense_chance": 0.25}}
    fn characters(&self) -> &HashMap<String, TCharacterConfig>;
    fn menu(&self) -> &str;
}

/// Clase que define la configuración del personaje
#[derive(Clone)]
pub struct TCharacterConfig {
    pub attacks: Vec<String>,
    pub damage_range: (i32, i32),
    pub defense_chance: f64,
}

pub trait IInput {
    /// # Returns
    /// Retorna un dato `entero` que no debe ser vacío.
    fn get_int(&self, msg: &str) -> i32;
}

/// Contrato para los datos y métodos de un personaje instanciado.
pub trait ICharacter {
    fn name(&self) -> &str;
    fn set_name(&mut self, name: String);
    fn hp(&self) -> i32;
    fn set_hp(&mut self, hp: i32);
    fn can_attack(&self) -> bool;
    fn set_can_attack(&mut self, can_attack: bool);
    fn attacks(&self) -> &Vec<String>;
    fn damage_range(&self) -> (i32, i32);
    fn defense_chance(&self) -> f64;
    fn add(&mut self, name: String, hp: i32, attributes: TCharacterConfig);
    /// Verifica si puede atacar, realiza un ataque y devuelve el daño infligido.
    fn attack(&self) -> i32;
    /// Determina si el personaje puede defenderse y lo retorna.
    fn defend(&self) -> bool;
}

/// Contrato para lógica de batalla.
pub trait IBattleStrategy {
    /// Ejecuta la estrategia de batalla entre el atacante y el defensor.
    /// # Returns
    /// Retorna verdadero si el defensor sigue en pie, falso si el atacante gana la batalla.
    fn execute(&self, attacker: &mut dyn ICharacter, defender: &mut dyn ICharacter) -> bool;
}

// ---------------------------------------
// IMPLEMENTACIÓN DE INTERFACES
// ---------------------------------------
pub struct DefaultConfig {
    characters: HashMap<String, TCharacterConfig>,
}

impl IGlobalConfig for DefaultConfig {
    fn turn_interval(&self) -> i32 { 1 }
    fn minimum_hp(&self) -> i32 { 200 }
    fn characters(&self) -> &HashMap<String, TCharacterConfig> { &self.characters }
    fn menu(&self) -> &str {
        "\nSIMULADOR DE BATALLAS:\n\
        -------------------------------------------\n\
        | 1. Simular una batalla |    2. Salir    |\n\
        -------------------------------------------"
    }
}

impl DefaultConfig {
    pub fn new() -> Self {
        let mut characters = HashMap::new();
        characters.insert("Deadpool".to_string(), TCharacterConfig {
            attacks: vec!["Con arma".to_string(), "Cuerpo a cuerpo".to_string(), "Ataque imprudente".to_string()],
            damage_range: (10, 100),
            defense_chance: 0.25,
        });
        characters.insert("Wolverine".to_string(), TCharacterConfig {
            attacks: vec!["Con garras de adamantium".to_string(), "Con arma".to_string(), "Cuerpo a cuerpo".to_string()],
            damage_range: (10, 120),
            defense_chance: 0.2,
        });
        DefaultConfig { characters }
    }
}

pub struct ConsoleInput;

impl IInput for ConsoleInput {
    fn get_int(&self, msg: &str) -> i32 {
        loop {
            print!("{}", msg);
            io::stdout().flush().expect("Error: limpiar búfer");

            let mut input = String::new();
            io::stdin()
                .read_line(&mut input)
                .expect("Error al leer la entrada");

            match input.trim().parse() {
                Ok(num) => return num,
                Err(_) => println!("Ingresa un número entero."),
            }
        }
    }
}

pub struct DefaultCharacter {
    name: String,
    hp: i32,
    can_attack: bool,
    attacks: Vec<String>,
    damage_range: (i32, i32),
    defense_chance: f64,
}

impl Default for DefaultCharacter {
    fn default() -> Self {
        DefaultCharacter {
            name: "Unknown".to_string(),
            hp: 200,
            can_attack: true,
            attacks: vec!["Basic Attack".to_string()],
            damage_range: (5, 90),
            defense_chance: 0.25,
        }
    }
}

impl ICharacter for DefaultCharacter {
    fn name(&self) -> &str { &self.name }
    fn set_name(&mut self, name: String) { self.name = name; }
    fn hp(&self) -> i32 { self.hp }
    fn set_hp(&mut self, hp: i32) { self.hp = hp; }
    fn can_attack(&self) -> bool { self.can_attack }
    fn set_can_attack(&mut self, can_attack: bool) { self.can_attack = can_attack; }
    fn attacks(&self) -> &Vec<String> { &self.attacks }
    fn damage_range(&self) -> (i32, i32) { self.damage_range }
    fn defense_chance(&self) -> f64 { self.defense_chance }

    fn add(&mut self, name: String, hp: i32, attributes: TCharacterConfig) {
        self.name = name;
        self.hp = hp;
        self.attacks = attributes.attacks;
        self.damage_range = attributes.damage_range;
        self.defense_chance = attributes.defense_chance;
        self.can_attack = true;
    }

    fn attack(&self) -> i32 {
        if self.can_attack {
            let mut rng = rand::thread_rng();
            let damage = rng.gen_range(self.damage_range.0..=self.damage_range.1);
            let selected_attack = &self.attacks[rng.gen_range(0..self.attacks.len())];
            println!("|'{}'ataca '{}' causando un: '-{}' 👊|", self.name, selected_attack, damage);
            damage
        } else {
            println!("|'{}' se está regenerando y no puede atacar. 😴|", self.name);
            0
        }
    }

    fn defend(&self) -> bool {
        let defended = rand::thread_rng().gen_bool(self.defense_chance);
        if defended {
            println!("|'{}' logró defenderse. 🛡️|", self.name);
        } else {
            println!("|'{}' no pudo bloquear el ataque. 🤕|", self.name);
        }
        defended
    }
}

pub struct DefaultBattleStrategy;

impl IBattleStrategy for DefaultBattleStrategy {
    fn execute(&self, attacker: &mut dyn ICharacter, defender: &mut dyn ICharacter) -> bool {
        let damage = attacker.attack();
        if damage == attacker.damage_range().1 {
            println!("|'{}' 🚨Recibió un ataque crítico y no podrá atacar.🚨|", defender.name());
            defender.set_can_attack(false);
        }
        if attacker.can_attack() {
            if !defender.defend() {
                defender.set_hp(defender.hp() - damage);
            }
        } else {
            attacker.set_can_attack(true);
        }
        if defender.hp() <= 0 {
            println!("\n____________________________");
            println!("|'{}' 🏆Gana la batalla. 🏆|", attacker.name());
            return false;
        }
        true
    }
}


// ---------------------------------------
// INYECCIÓN DE DEPENDENCIAS
// ---------------------------------------

pub struct Features {
    global_config: Box<dyn IGlobalConfig>,
    input: Box<dyn IInput>,
    strategy: Box<dyn IBattleStrategy>,
    player1: Box<dyn ICharacter>,
    player2: Box<dyn ICharacter>,
}

impl Features {
    fn new() -> Self {
        Features {
            global_config: Box::new(DefaultConfig::new()),
            input: Box::new(ConsoleInput),
            strategy: Box::new(DefaultBattleStrategy),
            player1: Box::new(DefaultCharacter::default()),
            player2: Box::new(DefaultCharacter::default()),
        }
    }
}

pub struct Simulation {
    features: Features,
}

impl Simulation {
    pub fn new(features: Features) -> Self {
        Simulation { features }
    }

    pub fn show_hp(&self) {
        println!("____________________________");
        println!(
            "|{}: ❤️ {}| |{}: ❤️ {}|",
            self.features.player1.name(),
            self.features.player1.hp(),
            self.features.player2.name(),
            self.features.player2.hp()
        );
    }

    fn init_battle(&mut self) {
        let mut turn = 1;
        loop {
            println!("\n----------------------------");
            println!("Turno #{}", turn);
            println!("----------------------------");

            self.show_hp();
            // Ataque de personaje #1 hacia #2
            if !self.features.strategy.execute(&mut *self.features.player1, &mut *self.features.player2) {
                break;
            }

            self.show_hp();
            // Ataque de personaje #2 hacia #1
            if !self.features.strategy.execute(&mut *self.features.player2, &mut *self.features.player1) {
                break;
            }

            turn += 1;
            sleep(Duration::from_secs(self.features.global_config.turn_interval() as u64));
        }

        self.show_hp();
    }

    fn add(&mut self, msg: &str, player: &str) {
        loop {
            let index = self.features.input.get_int(msg);
            let keys: Vec<String> = self.features.global_config.characters().keys().cloned().collect();
            if index < 0 || index >= keys.len() as i32 {
                println!("Número de personaje incorrecto.");
                continue;
            }
            let name = &keys[index as usize];
            if name == self.features.player1.name() {
                println!("El personaje ya fue utilizado.");
                continue;
            }
            let attributes: TCharacterConfig =self.features.global_config.characters().get(name).unwrap().clone();
            let hp = loop {
                let hp = self.features.input.get_int(&format!("Establecer una vida >= que '{}': ",self.features.global_config.minimum_hp()));
                if hp >= self.features.global_config.minimum_hp() {
                    break hp;
                }
                println!("La vida debe ser mayor o igual que '{}'.", self.features.global_config.minimum_hp());
            };

            if player == "player1" {
                self.features.player1.add(name.clone(), hp, attributes);
            } else if player == "player2" {
                self.features.player2.add(name.clone(), hp, attributes); 
            }
            
            break;
        }
    }

    pub fn start(&mut self) {
        println!("Personajes disponibles:");
        let characters: Vec<String> = self.features.global_config.characters().keys().cloned().collect();
        for (i, character) in characters.iter().enumerate() {
            println!("{}: {}", i, character);
        }

        self.add("'Primer' personaje: ", "player1");
        self.add("'Segundo' personaje: ", "player2");

        self.init_battle();

        // Restablecer para iniciar nueva simulación
        self.features.player1.set_name("Unknown".to_string());
        self.features.player2.set_name("Unknown".to_string());
        println!("{}", self.features.global_config.menu());
    }
}

pub struct Program {
    features: Features,
}

impl Program {
    pub fn new(features: Features) -> Self {
        Program { features }
    }

    fn run(&mut self) {
        println!("{}", self.features.global_config.menu());
        let mut simulation = Simulation::new(Features::new());

        loop {
            let option = self.features.input.get_int("\nOpción: ");
            match option {
                1 => {
                    simulation.start();
                },
                2 => {
                    println!("Adiós");
                    return;
                }
                _ => println!("Seleccionar de '1 o 2'"),
            }
        }
    }
}

fn main() {
    let mut program = Program::new(Features::new());
    program.run();
}

// _____
// NOTA: Estoy intentando practicar los principios SOLID. XD 😂

