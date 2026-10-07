use std::fmt;

trait Work {
    fn work(&self);
}

struct Employee {
    id: u32,
    name: String,
}

impl fmt::Display for Employee {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "id {} with name {}", self.id, self.name)
    }
}

impl Employee {
    fn new(id: u32, name: String) -> Self {
        Employee { id: id, name: name }
    }

    fn get_id(&self) -> u32 {
        return self.id;
    }

    fn get_name(&self) -> String {
        return self.name.clone();
    }
}

struct Manager<'a> {
    profile: Employee,
    employees: Vec<&'a Employee>,
}

impl<'a> Manager<'a> {
    fn add_employee(&mut self, e: &'a Employee) {
        self.employees.push(e);
    }
}

impl Work for Manager<'_> {
    fn work(&self) {
        println!("Managing employees...");
        for e in self.employees.iter() {
            println!("- {}", e);
        }
    }
}

struct ProjectManager {
    profile: Employee,
    projects: Vec<String>,
}

impl Work for ProjectManager {
    fn work(&self) {
        println!("Working in projects: {:?}", self.projects);
    }
}

impl ProjectManager {
    fn add_project(&mut self, project: String) {
        self.projects.push(project);
    }
}

struct Programmer {
    profile: Employee,
    prog_langs: Vec<String>,
}

impl Work for Programmer {
    fn work(&self) {
        println!("Coooooooooding!!!!");
        println!("Langs: {:?}", self.prog_langs);
    }
}

impl Programmer {
    fn add_language(&mut self, lang: String) {
        self.prog_langs.push(lang);
    }
}

trait Animal {
    fn emit_sound(&self);
}

struct Cat {
    name: String,
}

struct Dog {
    name: String,
}

impl Animal for Cat {
    fn emit_sound(&self) {
        println!("Cat {} says: Meow!", self.name);
    }
}

impl Animal for Dog {
    fn emit_sound(&self) {
        println!("Dog {} says: Guau!", self.name);
    }
}

fn main() {
    let dog1 = Dog {
        name: "Leo".to_string(),
    };
    let cat1 = Cat {
        name: "Milo".to_string(),
    };

    dog1.emit_sound();
    cat1.emit_sound();

    let employee1 = Employee::new(0, "Mike".to_string());
    let mut manager = Manager {
        profile: Employee::new(1, "John".to_string()),
        employees: Vec::new(),
    };
    let mut pmanager = ProjectManager {
        profile: Employee::new(2, "Mary".to_string()),
        projects: Vec::new(),
    };

    let mut programmer1 = Programmer {
        profile: Employee::new(3, "Peter".to_string()),
        prog_langs: Vec::new(),
    };

    manager.add_employee(&employee1);
    manager.add_employee(&programmer1.profile);
    manager.work();
    employee1.get_id();
    manager.profile.get_id();
    pmanager.add_project("wonder-project".to_string());
    pmanager.work();
    pmanager.profile.get_name();
    programmer1.add_language("Python".to_string());
    programmer1.work();
}
