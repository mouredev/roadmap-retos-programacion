/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
42 TORNEO DRAGON BALL
-------------------------------------
* EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.

[dependencies]
rand = "0.8.5"
*/

use rand::Rng;
use std::collections::HashMap;
use std::f64;

// __________________________________________________________
#[derive(Debug)]
struct Fighter {
    name: String,
    speed: i32,
    attack: i32,
    defense: i32,
    health: f64,
}

impl Fighter {
    fn new(name: &str, speed: i32, attack: i32, defense: i32) -> Self {
        Self {
            name: name.to_string(), speed, attack, defense, health: 100.0,
        }
    }

    fn execute_attack(&self, opponent: &mut Fighter) {
        println!("'{}' ataca a '{}'", self.name, opponent.name);

        let damage = if opponent.defense >= self.attack {
            self.attack as f64 * 0.1 // 10%
        } else {
            (self.attack - opponent.defense) as f64
        };

        if !Self::activate_defense() {
            opponent.health -= damage;
            println!("'{}' ha recibido '{}' de daño", opponent.name, damage);
            println!("Salud restante '{}'\n", opponent.health);
        } else {
            println!("'{}' ha esquivado el ataque.\n", opponent.name);
        }
    }

    fn activate_defense() -> bool {
        rand::thread_rng().gen_bool(0.2) // 20%
    }
}

// __________________________________________________________
struct Battle {fighter1: Fighter, fighter2: Fighter}

impl Battle {
    fn new(fighter1: Fighter, fighter2: Fighter) -> Self {
        println!("__'{} VS '{}'__\n", fighter1.name, fighter2.name);
        Self { fighter1, fighter2 }
    }

    fn combat(mut fighter_a: Fighter, mut fighter_b: Fighter) -> Fighter {
        loop {
            fighter_a.execute_attack(&mut fighter_b);
            if fighter_b.health <= 0.0 {
                println!("--> '{}' gana la batalla.__\n", fighter_a.name);
                return fighter_a;
            }

            fighter_b.execute_attack(&mut fighter_a);
            if fighter_a.health <= 0.0 {
                println!("--> '{}' gana la batalla.\n", fighter_b.name);
                return fighter_b;
            }
        }
    }

    fn start(self) -> Fighter {
        if self.fighter1.speed > self.fighter2.speed {
            Self::combat(self.fighter1, self.fighter2)
        } else {
            Self::combat(self.fighter2, self.fighter1)
        }
    }
}

// __________________________________________________________
#[derive(Clone, Debug)]
struct FighterStats {speed: i32, attack: i32, defense: i32,}

struct Tournament {fighters: HashMap<String, FighterStats>,}

impl Tournament {
    fn new(fighters: HashMap<String, FighterStats>) -> Self {
        Self { fighters }
    }

    fn is_power_of_2(&self) -> bool {
        self.fighters.len() > 1 && (self.fighters.len() as f64).log2().fract() == 0.0
    }

    fn get_random_pairs(&mut self) -> (Fighter, Fighter) {
        use rand::seq::SliceRandom;
        
        let selected_names: Vec<String> = self.fighters.keys()
            .cloned()
            .collect::<Vec<_>>()
            .choose_multiple(&mut rand::thread_rng(), 2)
            .cloned()
            .collect();
    
        let stats1 = self.fighters.remove(&selected_names[0]).unwrap();
        let stats2 = self.fighters.remove(&selected_names[1]).unwrap();
    
        (
            Fighter::new(&selected_names[0], stats1.speed, stats1.attack, stats1.defense),
            Fighter::new(&selected_names[1], stats2.speed, stats2.attack, stats2.defense)
        )
    }

    fn start_rounds(&mut self, round_num: i32) {
        if !self.is_power_of_2() {
            println!("El número de luchadores debe ser una potencia de 2.");
            return;
        }

        println!("\n__Ronda #{}__", round_num);
        let mut next_round = HashMap::new();

        loop {
            let (fighter1, fighter2) = self.get_random_pairs();
            let battle = Battle::new(fighter1, fighter2);
            let winner = battle.start();

            next_round.insert(
                winner.name.clone(),
                FighterStats {
                    speed: winner.speed,
                    attack: winner.attack,
                    defense: winner.defense,
                },
            );

            if self.fighters.is_empty() {
                if next_round.len() > 1 {
                    self.fighters = next_round;
                    self.start_rounds(round_num + 1);
                    break;
                } else {
                    println!("\n--> El vencedor del torneo es '{}'.", winner.name);
                    break;
                }
            }
        }
    }
}

// __________________________________________________________
fn main() {
    let fighters = HashMap::from([
        (String::from("Goku"), FighterStats { speed: 100, attack: 95, defense: 85 }),
        (String::from("Vegeta"), FighterStats { speed: 95, attack: 90, defense: 90 }),
        (String::from("Gohan"), FighterStats { speed: 85, attack: 95, defense: 85 }),
        (String::from("Freezer"), FighterStats { speed: 90, attack: 90, defense: 90 }),
        (String::from("Piccolo"), FighterStats { speed: 90, attack: 85, defense: 90 }),
        (String::from("Krillin"), FighterStats { speed: 85, attack: 75, defense: 75 }),
        (String::from("Cell"), FighterStats { speed: 90, attack: 95, defense: 85 }),
        (String::from("Majin Buu"), FighterStats { speed: 80, attack: 85, defense: 95 })
    ]);

    println!("Simulación del Torneo de Artes Marciales");
    let mut tournament = Tournament::new(fighters);
    tournament.start_rounds(1);
}
