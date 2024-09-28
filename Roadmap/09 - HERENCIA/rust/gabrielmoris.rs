/*
 * EXERCISE:
 * Explore the concept of inheritance in your language. Create an example that
 * implements a superclass Animal and a pair of subclasses Dog and Cat,
 * along with a function that prints the sound each Animal makes.
 */

//  Rust does not have traditional inheritance like in object-oriented languages such as C++, Java, or Python.
//  Instead, Rust uses trait objects and trait implementations to achieve polymorphism and code reuse.
// Traits in Rust are similar to interfaces in other languages. They define a set of methods that a type must implement.
// Types can implement multiple traits, and traits can inherit from other traits (called "supertrait" in Rust terminology)
trait Sound {
    fn make_sound(&self) -> &str;
}

struct Animal<T: Sound> {
    name: String,
    make_sound: T,
}

impl<T: Sound> Animal<T> {
    fn new(name: &str, make_sound: T) -> Self {
        Animal {
            name: name.to_string(),
            make_sound,
        }
    }

    fn print_sound(&self) {
        println!("{} says {}", self.name, self.make_sound.make_sound());
    }
}

struct Dog;

impl Sound for Dog {
    fn make_sound(&self) -> &str {
        "Guau! Guau!"
    }
}

// Define the `Cat` struct and implement the `Sound` trait
struct Cat;

impl Sound for Cat {
    fn make_sound(&self) -> &str {
        "Marramiau!"
    }
}

fn main() {
    // EXERCISE
    let dog = Animal::new("Laica", Dog);
    let cat = Animal::new("Felix", Cat);
    dog.print_sound(); // Prints "Laica says Guau!"
    cat.print_sound(); // Prints "Felix says Marramiau!"

    // CHALLENGE
    let mut manager = Employee::new("Gabriel", Manager, "Manager");
    let mut project_manager = Employee::new("Jorge", ProjectManager, "Project_Manager");
    let developer_1 = Employee::new("Juan", Developer, "Frontend");
    let developer_2 = Employee::new("Julio", Developer, "Backend");

    project_manager.add_dev(developer_1);
    project_manager.add_dev(developer_2);
    project_manager.manage();
    manager.add_pm(project_manager);
    manager.manage();
}

/* EXTRA CHALLENGE (optional):
 * Implement the hierarchy of a development company consisting of Employees who
 * can be Managers, Project Managers, or Programmers.
 * Each employee has an identifier and a name.
 * Depending on their role, they have properties and functions exclusive to their
 * activity, and they store the employees under their supervision.
 */

trait Work {
    fn do_work(&self) -> &str;
}

struct Employee<T: Work> {
    name: String,
    identifier: String,
    do_work: T,
    supervise: Vec<Employee<ProjectManager>>,
    dev_team: Vec<Employee<Developer>>,
}

impl<T: Work> Employee<T> {
    fn new(name: &str, do_work: T, identifier: &str) -> Self {
        Employee {
            name: name.to_string(),
            identifier: identifier.to_string(),
            do_work,
            supervise: Vec::new(),
            dev_team: Vec::new(),
        }
    }

    fn show_is_working(&self) -> String {
        self.do_work.do_work().to_string()
    }

    fn get_name(&self) -> String {
        self.name.clone()
    }

    fn manage(&self) {
        if self.identifier == "Manager" {
            for n in &self.supervise {
                for dev in &n.dev_team {
                    println!(
                        "{} asks what is {} doing: he is helping {} {}",
                        self.name,
                        n.get_name(),
                        dev.get_name(),
                        n.show_is_working()
                    );
                }
            }
        } else if self.identifier == "Project_Manager" {
            for n in &self.dev_team {
                println!(
                    "{} tries to help {} with his current task: {}",
                    self.name,
                    n.get_name(),
                    n.show_is_working()
                );
            }
        }
    }

    fn add_dev(&mut self, employee: Employee<Developer>) {
        if self.identifier == "Project_Manager" {
            self.dev_team.push(employee);
        }
    }

    fn add_pm(&mut self, employee: Employee<ProjectManager>) {
        if self.identifier == "Manager" {
            self.supervise.push(employee);
        }
    }
}

struct Manager;

impl Work for Manager {
    fn do_work(&self) -> &str {
        "managing"
    }
}

struct Developer;

impl Work for Developer {
    fn do_work(&self) -> &str {
        "drinking a coffee"
    }
}

struct ProjectManager;

impl Work for ProjectManager {
    fn do_work(&self) -> &str {
        "making his coffee"
    }
}
