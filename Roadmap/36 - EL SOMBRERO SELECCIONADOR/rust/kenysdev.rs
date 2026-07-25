/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
36 EL SOMBRERO SELECCIONADOR
------------------------------------
* Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
* de programación de Hogwarts para magos y brujas del código.
* En ella, su famoso sombrero seleccionador ayuda a los programadores
* a encontrar su camino...
* Desarrolla un programa que simule el comportamiento del sombrero.
* Requisitos:
* 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
* 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
*    (Puedes elegir las que quieras)
* Acciones:
* 1. Crea un programa que solicite el nombre del alumno y realice 10
*    preguntas, con cuatro posibles respuestas cada una.
* 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
* 3. Una vez finalizado, el sombrero indica el nombre del alumno
*    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
*    pero indicándole al alumno que la decisión ha sido complicada).
*/

use std::collections::HashMap;
use std::io::{self, Write};

// [dependencies]
// rand = "0.8.5"
// https://crates.io/crates/rand
use rand::Rng;

const HOUSES: [&str; 4] = ["Frontend", "Backend", "Mobile", "Data"];

// NOTA: Preguntas y respuestas generadas por IA
const QUESTIONS: [&str; 10] = [
    "¿Qué te atrae más?",
    "¿Qué superhéroe de la programación te gustaría ser?",
    "En un proyecto de software, ¿qué rol te emociona más?",
    "Si tu código fuera una obra de arte, ¿qué estilo tendría?",
    "¿Qué animal de programación serías?",
    "En una hackathon, ¿qué tipo de proyecto propondrías?",
    "Si tu carrera en tech fuera una película, ¿de qué género sería?",
    "¿Qué herramienta de programación no puede faltar en tu caja de herramientas digital?",
    "Si pudieras resolver un gran problema en tech, ¿cuál elegirías?",
    "¿Qué tipo de equipo prefieres?",
];

const ANSWERS: [[&str; 4]; 10] = [
    ["Crear experiencias visuales.", "Solucionar problemas de funcionamiento.", "Innovar en dispositivos portátiles.", "Descubrir tendencias ocultas."],
    ["Diseñador de Interfaces, creando experiencias asombrosas", "Arquitecto de Sistemas, construyendo estructuras robustas", "Mago de Apps, conjurando soluciones móviles", "Explorador de Datos, descubriendo tesoros ocultos"],
    ["Director de UX, orquestando la sinfonía visual", "Ingeniero de Backend, dominando la lógica del servidor", "Desarrollador de Apps, llevando la potencia al bolsillo", "Científico de Datos, descifrando los secretos de la información"],
    ["Minimalismo elegante, como una landing page perfecta", "Arquitectura compleja, como un sistema distribuido", "Diseño adaptativo, fluyendo en diferentes dispositivos", "Visualización de datos, pintando historias con números"],
    ["Un camaleón, adaptándome a diferentes frameworks", "Un pulpo, manejando múltiples servicios a la vez", "Un colibrí, ágil y siempre en movimiento", "Una lechuza, analizando datos con sabiduría"],
    ["Una web app que revolucione la experiencia del usuario", "Un sistema de IA que optimice procesos backend", "Una app móvil que cambie la forma de interactuar con el mundo", "Un proyecto de big data que prediga tendencias futuras"],
    ["Comedia romántica con JavaScript y CSS", "Thriller de ciencia ficción con microservicios", "Aventura de acción en el mundo de las apps", "Documental profundo sobre el universo de los datos"],
    ["Un editor de código con plugins para diseño visual", "Una robusta suite de testing y depuración", "Un emulador multi-dispositivo de última generación", "Una plataforma de análisis de datos en tiempo real"],
    ["Hacer que la accesibilidad web sea universal", "Crear una arquitectura de software autorreparable", "Desarrollar una plataforma de AR/VR para educación móvil", "Construir un modelo de IA ético y transparente"],
    ["Creativos enfocados en diseño.", "Técnicos que construyen sistemas.", "Especialistas en aplicaciones móviles.", "Expertos en datos y análisis."],
];

struct SortingHat {
    scores: HashMap<String, i32>,
}

impl SortingHat {
    fn new() -> Self {
        let scores = HOUSES.iter().map(|&house| (house.to_string(), 0)).collect();
        SortingHat { scores }
    }

    fn ask_question(&mut self, q_num: usize, question: &str, answers: &[&str]) {
        println!("\n#{}: {}", q_num, question);
        for (i, answer) in answers.iter().enumerate() {
            println!("{}) {}", i + 1, answer);
        }

        loop {
            print!("Elige tu respuesta (1-4): ");
            io::stdout().flush().unwrap();
            
            let mut choice = String::new();
            io::stdin().read_line(&mut choice).unwrap();
            
            if let Ok(num) = choice.trim().parse::<usize>() {
                if num >= 1 && num <= 4 {
                    *self.scores.get_mut(HOUSES[num - 1]).unwrap() += 1;
                    break;
                }
            }
            println!("Por favor, elige un número entre 1 y 4.");
        }
    }

    fn select_house(&self) -> String {
        let max_score = self.scores.values().max().unwrap();
        let top_houses: Vec<_> = self.scores
            .iter()
            .filter(|(_, &score)| score == *max_score)
            .map(|(house, _)| house)
            .collect();

        if top_houses.len() > 1 {
            println!("\nLa decisión ha sido complicada.");
            top_houses[rand::thread_rng().gen_range(0..top_houses.len())].clone()
        } else {
            top_houses[0].clone()
        }
    }
}

fn main() {
    println!("EL SOMBRERO SELECCIONADOR");
    print!("¿Cuál es tu nombre? : ");
    io::stdout().flush().unwrap();
    
    let mut name = String::new();
    io::stdin().read_line(&mut name).unwrap();
    let name = name.trim();

    let mut hat = SortingHat::new();

    for (i, (&question, answers)) in QUESTIONS.iter().zip(ANSWERS.iter()).enumerate() {
        hat.ask_question(i + 1, question, answers);
    }

    let selected_house = hat.select_house();
    println!("\n'{}' pertenecerá a la casa '{}'\n", name, selected_house);
}
