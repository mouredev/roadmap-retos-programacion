/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------------------
* SIMULADOR JUEGOS OLÍMPICOS
-----------------------------------------------------

* EJERCICIO:
* ¡Los JJOO de París 2024 han comenzado!
* Crea un programa que simule la celebración de los juegos.
* El programa debe permitir al usuario registrar eventos y participantes,
* realizar la simulación de los eventos asignando posiciones de manera aleatoria
* y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
*/

// NOTA: Solo es un intento de practicar los principios SOLID. XD

// ________________________________________________
use std::io::{self, Write};
use std::sync::{Arc, Mutex};
use std::collections::HashMap;

// [dependencies]
// rand = "0.8.5"
// https://crates.io/crates/rand
use rand::prelude::*;

// ________________________________________________
// INTERFACES
/// Contrato para acceder a constantes globales.
trait IGlobalConfig {
    fn medals(&self) -> [&'static str; 3];
    fn menu(&self) -> &'static str;
}

/// Contrato de métodos requeridos para una tabla de datos.
trait IDataTable<T> {
    fn add(&mut self, item: T);
    fn count(&self) -> usize;
    fn get_list(&self) -> Vec<T>;
}

/// Contrato para implementar diferentes formas de almacenamiento de datos.
trait IData {
    fn events_table(&mut self) -> &mut dyn IDataTable<String>;
    fn participants_table(&mut self) -> &mut dyn IDataTable<(String, String, i32)>; // name, country, event_id 
    fn simulation_table( &mut self, //event_name, name, country, event_id, score, medal
    ) -> &mut dyn IDataTable<Vec<(String, Vec<(String, String, i32, i32, String)>)>>; 
}

/// Contrato sobre la entra de datos.
trait IInput {
    fn get(&self, msg: &str) -> String;
    fn get_int(&self, msg: &str) -> i32;
}

// ________________________________________________
// CONTRATOS sobre la comunicación entre la interacción del usuario y la capa de datos.
trait IEvents { fn add(&self); }

trait IParticipants {
    fn get_event_id(&self) -> i32;
    fn add(&self);
}

trait ISimulations { fn start(&self); }

trait IReports { fn generate(&self); }

// ________________________________________________
// IMPLEMENTAR CONTRATOS
struct GlobalConfig;

impl IGlobalConfig for GlobalConfig {
    fn medals(&self) -> [&'static str; 3] {
        static MEDALS: [&'static str; 3] = ["🥇 Oro", "🥈 Plata", "🥉 Bronce"];
        MEDALS
    }

    fn menu(&self) -> &'static str {
        r#"
SIMULADOR JUEGOS OLÍMPICOS:
--------------------------------------------------
| 1. Registrar evento        | 4. Crear informes |  
| 2. Registrar participante  | 5. Salir          |
| 3. Simulación de eventos   |                   |
--------------------------------------------------
"#
    }
}

struct EventsTable {
    dt: Vec<String>,
}

impl EventsTable {
    fn new() -> Self {
        EventsTable { dt: Vec::new() }
    }
}

impl IDataTable<String> for EventsTable {
    fn add(&mut self, sport: String) {
        self.dt.push(sport);
    }

    fn count(&self) -> usize {
        self.dt.len()
    }

    fn get_list(&self) -> Vec<String> {
        self.dt.clone()
    }
}

// _____________________
struct ParticipantsTable {
    dt: Vec<(String, String, i32)>,
}

impl ParticipantsTable {
    fn new() -> Self {
        ParticipantsTable { dt: Vec::new() }
    }
}

impl IDataTable<(String, String, i32)> for ParticipantsTable {
    fn add(&mut self, participant: (String, String, i32)) {
        self.dt.push(participant);
    }

    fn count(&self) -> usize {
        self.dt.len()
    }

    fn get_list(&self) -> Vec<(String, String, i32)> {
        self.dt.clone()
    }
}

// _____________________
struct SimulationTable { // event_name, name, country, event_id, score, medal
    dt: Vec<Vec<(String, Vec<(String, String, i32, i32, String)>)>>,
}

impl SimulationTable {
    fn new() -> Self {
        SimulationTable { dt: Vec::new() }
    }
}

impl IDataTable<Vec<(String, Vec<(String, String, i32, i32, String)>)>> for SimulationTable {
    fn add(&mut self, simulation: Vec<(String, Vec<(String, String, i32, i32, String)>)>) {
        self.dt.push(simulation);
    }

    fn count(&self) -> usize {
        self.dt.len()
    }

    fn get_list(&self) -> Vec<Vec<(String, Vec<(String, String, i32, i32, String)>)>> {
        self.dt.clone()
    }
}

// _____________________
/// Aplicando interfaz para Datos en memoria.
struct DataInMemory {
    events_table: Box<dyn IDataTable<String>>,
    participants_table: Box<dyn IDataTable<(String, String, i32)>>,
    simulation_table: Box<dyn IDataTable<Vec<(String, Vec<(String, String, i32, i32, String)>)>>>,
}

impl DataInMemory {
    fn new() -> Self {
        DataInMemory {
            events_table: Box::new(EventsTable::new()),
            participants_table: Box::new(ParticipantsTable::new()),
            simulation_table: Box::new(SimulationTable::new()),
        }
    }
}

impl IData for DataInMemory {
    fn events_table(&mut self) -> &mut dyn IDataTable<String> {
        &mut *self.events_table
    }

    fn participants_table(&mut self) -> &mut dyn IDataTable<(String, String, i32)> {
        &mut *self.participants_table
    }

    fn simulation_table(
        &mut self,
    ) -> &mut dyn IDataTable<Vec<(String, Vec<(String, String, i32, i32, String)>)>> {
        &mut *self.simulation_table
    }
}

// ________________________________________________

/// Muestra un mensaje al usuario y devuelve su entrada.
struct ConsoleInput;

impl IInput for ConsoleInput {
    fn get(&self, msg: &str) -> String {
        loop {
            print!("{}", msg);
            io::stdout().flush().expect("Error: limpiar búfer");

            let mut input = String::new();
            io::stdin()
                .read_line(&mut input)
                .expect("Error al leer la entrada");

            let trimmed_input = input.trim().to_string();
            if !trimmed_input.is_empty() {
                return trimmed_input;
            }

            println!("La entrada no puede estar vacía.");
        }
    }
    
    fn get_int(&self, msg: &str) -> i32 {
        loop {
            let input: String = self.get(msg);
            
            match input.trim().parse::<i32>() {
                Ok(number) => {
                    return number
                },
                Err(_) => {
                    println!("Se requiere un número entero.");
                }
            }
        }
    }
}

// ________________________________________________
/// 1. Registrar eventos deportivos.
struct Events {
    data: Arc<Mutex<Box<dyn IData>>>,
    input: Arc<dyn IInput>,
    constants: Arc<dyn IGlobalConfig>,
}

impl Events {
    fn new(
        data: Arc<Mutex<Box<dyn IData>>>,
        input: Arc<dyn IInput>,
        constants: Arc<dyn IGlobalConfig>,
    ) -> Self { Events { data, input, constants, } }
}

impl IEvents for Events {
    fn add(&self) {
        println!("AGREGAR EVENTO DEPORTIVO:");
        let sport = self.input.get("Deporte: ");
        let mut data = self.data.lock().unwrap();
        data.events_table().add(sport.clone());
        println!("\n{} fue agregado", sport);
        println!("{}", self.constants.menu());
    }
}

// ________________________________________________
/// 2. Registrar participantes por nombre y país.
struct Participants {
    data: Arc<Mutex<Box<dyn IData>>>,
    input: Arc<dyn IInput>,
    constants: Arc<dyn IGlobalConfig>,
}

impl Participants {
    fn new(
        data: Arc<Mutex<Box<dyn IData>>>,
        input: Arc<dyn IInput>,
        constants: Arc<dyn IGlobalConfig>,
    ) -> Self { Participants { data, input, constants, } }
}

impl IParticipants for Participants {
    fn get_event_id(&self) -> i32 {
        println!("Seleccionar el evento donde participará:");
        let mut data = self.data.lock().unwrap();
        let events = data.events_table().get_list();
        
        for i in 0..events.len() {
            println!("{}: {}", i, events[i]);
        }

        loop {
            let index: i32 = self.input.get_int("d de evento: ");
            if index < 0 || index >= events.len().try_into().unwrap() {
                println!("Id no encontrada.");
            } else {
                return index;
            }
        }
    }

    fn add(&self) {
        println!("AGREGAR PARTICIPANTE:");
        let mut data = self.data.lock().unwrap();
        let events = data.events_table().get_list();
                
        if !(events.len() > 0) {
            println!("No existe evento en cuál participar.");
            return;
        }

        drop(data);
        let event_id: i32 = self.get_event_id();
        let name = self.input.get("Nombre: ");
        let country = self.input.get("País: ");

        let mut data = self.data.lock().unwrap();
        data.participants_table()
            .add((name.clone(), country.clone(), event_id));
        println!("\n{} fue agregado", name);

        println!("{}", self.constants.menu());
    }
}
// ________________________________________________
/// 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
/// 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
struct Simulation {
    data: Arc<Mutex<Box<dyn IData>>>,
    constants: Arc<dyn IGlobalConfig>,
}

impl Simulation {
    fn new(data: Arc<Mutex<Box<dyn IData>>>, constants: Arc<dyn IGlobalConfig>) -> Self {
        Simulation { data, constants }
    }

    fn qualify_participants(&self, event_id: i32) -> Vec<(String, String, i32, i32, String)> {
        let mut rng = rand::thread_rng();
        let medals = self.constants.medals();

        let participants_list = {
            let mut data = self.data.lock().unwrap();
            data.participants_table().get_list()
        };

        // Seleccionar solo los participantes que tienen el ID del evento.
        let participants_of_event: Vec<_> = participants_list
        .iter()
        .filter(|p| p.2 == event_id)
        .collect();

        let mut participants: Vec<_> = participants_of_event
            .iter()
            .map(|(name, country, event_id)| (
                name.clone(), country.clone(), event_id.clone(), rng.gen_range(1..=100)))
            .collect();

        participants.sort_by(|a, b| b.3.cmp(&a.3));

        participants
            .into_iter()
            .take(3)
            .enumerate()
            .map(|(i, (name, country, event_id, score))| (
                name, country, event_id, score, medals[i].to_string()))
            .collect()
    }

    fn add_result_events(&self) {
        let mut data = self.data.lock().unwrap();
        let events = data.events_table().get_list();
        drop(data);
         
        let simulation: Vec<_> = events
            .into_iter()
            .enumerate()
            .map(|(index, event)| (event, self.qualify_participants(index
                .try_into()
                .unwrap())))
            .collect();

        let mut data2 = self.data.lock().unwrap();
        data2.simulation_table().add(simulation);
    }
}

impl ISimulations for Simulation {
    fn start(&self) {
        let mut data = self.data.lock().unwrap();
        if data.events_table().count() >= 1 && data.participants_table().count() >= 3 {
            drop(data);
            self.add_result_events();
            let total_simulation = self.data.lock().unwrap().simulation_table().count();
            println!("\nSimulación '#{:?}' creada.", total_simulation);
            println!("Puedes ver el resultado con opción: '4. Crear informes.'");
            println!("{}", self.constants.menu());
        } else {
            println!("\nDebe haber al menos un evento y al menos 'tres' participantes.");
        }
    }
}

// ________________________________________________
/// 5. Mostrar los ganadores por cada evento.
/// 6. Mostrar el ranking de países según el número de medallas.

struct Reports {
    data: Arc<Mutex<Box<dyn IData>>>,
    constants: Arc<dyn IGlobalConfig>,
}

impl Reports {
    fn new(data: Arc<Mutex<Box<dyn IData>>>, constants: Arc<dyn IGlobalConfig>) -> Self {
        Reports { data, constants }
    }

    fn generate_top_countries(&self, ranking_countries: &mut HashMap<String, (i32, i32)>) {
        let mut vec: Vec<_> = ranking_countries.iter().collect();
        vec.sort_by(|a, b| b.1.0.cmp(&a.1.0).then(b.1.1.cmp(&a.1.1)));

        for (i, (country, (medals, score))) in vec.iter().take(10).enumerate() {
            println!("🔵 {:<2} | {:<12} | 🏅 {:<3} | 🧮 {:>4}", i + 1, country, medals, score);
        }
    }

    fn update_country_ranking(
        ranking_countries: &mut HashMap<String, (i32, i32)>,
        country: String,
        score: i32
    ) {
        match ranking_countries.get_mut(&country) {
            Some((medals, current_score)) => {
                *medals += 1;
                *current_score += score;
            },
            None => {
                ranking_countries.insert(country, (1, score));
            }
        }
    }

    fn iterate_participants(
        &self,
        participants: &[(String, String, i32, i32, String)],
        ranking_countries: &mut HashMap<String, (i32, i32)>,
    ) {
        for (i, (name, country, _event_id, score, medal)) in participants.iter().enumerate() {
            println!("🟢 '{:<1}' | {:<7} | {:<12} -> 🔢 {:<3}, | {:<3}", i + 1, name, country, score, medal
            );
            Self::update_country_ranking(ranking_countries, country.clone(), score.clone());
        }
    }

    fn iterate_events(
        &self,
        simulation: &Vec<(String, Vec<(String, String, i32, i32, String)>)>,
        ranking_countries: &mut HashMap<String, (i32, i32)>,
    ) {
        for (event_name, results) in simulation {
            println!("\nEvent: {}:", event_name);
            if results.len() < 3 {
                println!("Evento cancelado por falta de participantes.");
                continue;
            }

            self.iterate_participants(results, ranking_countries);
        }
    }
}

impl IReports for Reports {
    fn generate(&self) {
        let simulations = self.data.lock().unwrap().simulation_table().get_list();
        if simulations.is_empty() {
            println!("Aún no hay simulaciones creadas.");
            return;
        }

        for (i, simulation) in simulations.iter().enumerate() {
            println!("\n______________\nSimulation {}", i + 1);
            let mut ranking_countries: HashMap<String, (i32, i32)> = HashMap::new();
            self.iterate_events(simulation, &mut ranking_countries);

            println!("\nRanking de países, según el número de medallas:");
            self.generate_top_countries(&mut ranking_countries);
        }

        println!("{}", self.constants.menu());
    }
}

// ________________________________________________
struct Program {
    events: Box<dyn IEvents>,
    participants: Box<dyn IParticipants>,
    simulation: Box<dyn ISimulations>,
    reports: Box<dyn IReports>,
    input: Arc<dyn IInput>,
    constants: Arc<dyn IGlobalConfig>,
}

impl Program {
    fn new() -> Self {
        let data: Arc<Mutex<Box<dyn IData>>> = Arc::new(Mutex::new(Box::new(DataInMemory::new())));
        let input: Arc<dyn IInput> = Arc::new(ConsoleInput);
        let constants: Arc<dyn IGlobalConfig> = Arc::new(GlobalConfig);

        Program {
            events: Box::new(Events::new(data.clone(), input.clone(), constants.clone())),
            participants: Box::new(Participants::new(data.clone(), input.clone(), constants.clone(),)),
            simulation: Box::new(Simulation::new(data.clone(), constants.clone())),
            reports: Box::new(Reports::new(data, constants.clone())),
            input,
            constants,
        }
    }

    fn run(&self) {
        println!("{}", self.constants.menu());

        loop {
            let option = self.input.get("\nOpción: ");

            match option.as_str() {
                "1" => self.events.add(),
                "2" => self.participants.add(),
                "3" => self.simulation.start(),
                "4" => self.reports.generate(),
                "5" => {
                    println!("Adios");
                    break;
                }
                _ => println!("Seleccionar de '1 a 5'"),
            }
        }
    }
}

//____________________________________
fn main() {
    let program = Program::new();
    program.run();
}

// NOTA: Solo es un intento de practicar los principios SOLID. XD

