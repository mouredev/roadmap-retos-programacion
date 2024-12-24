/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
__________________________________________
#50 PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO
------------------------------------------
* EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 * 
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado 
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *   
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
*/

use std::collections::HashMap;
use std::io::{self, Write};
use std::process::Command;
use chrono::Local;
use std::fs::File;

#[derive(Debug)]
struct Goal {
    name: String,
    quantity: i32,
    units: String,
}

struct ObjectivePlanner {
    goals: Vec<Goal>,
    months: Vec<String>,
    pending_monthly: HashMap<usize, Vec<i32>>,
}

impl ObjectivePlanner {
    fn new() -> Self {
        let months = vec![
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ].iter().map(|&s| s.to_string()).collect();

        ObjectivePlanner {
            goals: Vec::new(),
            months,
            pending_monthly: HashMap::new(),
        }
    }

    fn read_line(prompt: &str) -> String {
        print!("{}", prompt);
        io::stdout().flush().unwrap();
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        input.trim().to_string()
    }

    fn add(&mut self) -> io::Result<()> {
        if self.goals.len() >= 10 {
            println!("\nMáximo de 10 objetivos alcanzado.");
            return Ok(());
        }

        println!("Ingrese los detalles del objetivo:");
        let name = Self::read_line("Meta: ");
        
        let quantity = match Self::read_line("Cantidad: ").parse::<i32>() {
            Ok(n) if n > 0 => n,
            _ => {
                println!("\nError: Ingrese una cantidad válida.");
                return Ok(());
            }
        };

        let units = Self::read_line("Unidades: ");

        let months = match Self::read_line("Plazo (en meses): ").parse::<i32>() {
            Ok(n) if (1..=12).contains(&n) => n,
            _ => {
                println!("\nError: Ingrese un plazo válido (1-12 meses).");
                return Ok(());
            }
        };

        if !name.is_empty() && !units.is_empty() {
            let goal = Goal {
                name,
                quantity,
                units,
            };

            let goal_id = self.goals.len();
            let monthly = quantity / months;
            let extra = quantity % months;

            let monthly_quantities: Vec<i32> = (0..months)
                .map(|m| monthly + if m < extra { 1 } else { 0 })
                .collect();

            self.pending_monthly.insert(goal_id, monthly_quantities);
            self.goals.push(goal);
            println!("\nObjetivo añadido exitosamente.");
        } else {
            println!("\nDatos inválidos.");
        }

        Ok(())
    }

    fn calculate_plan(&self) -> Option<HashMap<String, Vec<String>>> {
        if self.goals.is_empty() {
            return None;
        }

        let mut plan: HashMap<String, Vec<String>> = HashMap::new();

        for (goal_id, goal) in self.goals.iter().enumerate() {
            if let Some(monthly_quantities) = self.pending_monthly.get(&goal_id) {
                for (month, &quantity) in monthly_quantities.iter().enumerate() {
                    if quantity > 0 {
                        let month_name = &self.months[month];
                        let task = format!(
                            "[ ] {} ({} {}/mes). Total: {}.",
                            goal.name, quantity, goal.units, goal.quantity
                        );
                        plan.entry(month_name.clone())
                            .or_insert_with(Vec::new)
                            .push(task);
                    }
                }
            }
        }

        if plan.is_empty() {
            None
        } else {
            Some(plan)
        }
    }

    fn write_ordered_plan<W: Write>(&self, mut writer: W) -> io::Result<()> {
        if let Some(plan) = self.calculate_plan() {
            for month in &self.months {
                if let Some(tasks) = plan.get(month) {
                    writeln!(writer, "{}:", month)?;
                    for task in tasks {
                        writeln!(writer, "  {}", task)?;
                    }
                    writeln!(writer)?;
                }
            }
        }
        Ok(())
    }

    fn save_plan(&self) -> io::Result<()> {
        if self.calculate_plan().is_none() {
            println!("\nNo hay planificación para guardar.");
            return Ok(());
        }

        let filename = format!(
            "plan_{}.txt",
            Local::now().format("%Y%m%d_%H%M")
        );

        let file = File::create(&filename)?;
        self.write_ordered_plan(file)?;
        println!("\nPlan guardado en {}.", filename);
        Ok(())
    }

    fn display_plan(&self) {
        if self.calculate_plan().is_none() {
            println!("\nNo hay objetivos planificados.");
            return;
        }

        self.write_ordered_plan(io::stdout())
            .expect("Error al mostrar el plan");
    }

    fn clear_screen() {
        if cfg!(target_os = "windows") {
            Command::new("cmd").args(["/c", "cls"]).status().unwrap();
        } else {
            Command::new("clear").status().unwrap();
        }
    }

    pub fn run(&mut self) -> io::Result<()> {
        Self::clear_screen();

        loop {
            println!("\nGestor de Objetivos:");
            println!("1. Añadir objetivo");
            println!("2. Calcular plan detallado");
            println!("3. Guardar planificación");
            println!("4. Salir");

            match Self::read_line("\nSeleccione una opción: ").as_str() {
                "1" => self.add()?,
                "2" => self.display_plan(),
                "3" => self.save_plan()?,
                "4" => {
                    println!("\n¡Adiós!");
                    break;
                }
                _ => println!("\nOpción inválida."),
            }
        }
        Ok(())
    }
}

fn main() -> io::Result<()> {
    let mut planner = ObjectivePlanner::new();
    planner.run()
}
