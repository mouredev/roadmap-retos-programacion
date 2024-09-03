/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------------------
* 34 ÁRBOL GENEALÓGICO DE LA CASA DEL DRAGÓN
-----------------------------------------------------
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijos
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 *
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.

'_______
' NOTE Here Is the 'people.json' file with the data if you want to test it:
'      https://pastebin.com/29kWWgPU
'      Just paste it into the base folder.
*/

use std::fs;
use std::collections::{HashMap, HashSet};
use std::io::{self, Write};

/*
https://crates.io/crates/serde_json
[dependencies]
serde = { version = "1.0.197", features = ["derive"] }
serde_json = "1.0.115"
*/
use serde::{Serialize, Deserialize};

//_______________________________________
#[derive(Debug, Serialize, Deserialize, PartialEq, Eq)]
pub struct Person {
    id: i32,
    name: String,
    parents: HashSet<i32>,
    partners: HashSet<i32>,
    children: HashMap<i32, Vec<i32>>,
    deleted: bool,
}

impl Person {
    pub fn new(id: i32, name: String) -> Self {
        Self {
            id,
            name,
            parents: HashSet::new(),
            partners: HashSet::new(),
            children: HashMap::new(),
            deleted: false,
        }
    }

    pub fn id(&self) -> i32 { self.id }
    pub fn name(&self) -> &str { &self.name }
    pub fn parents(&self) -> &HashSet<i32> { &self.parents }
    pub fn parents_mut(&mut self) -> &mut HashSet<i32> { &mut self.parents }
    pub fn partners(&self) -> &HashSet<i32> { &self.partners }
    pub fn partners_mut(&mut self) -> &mut HashSet<i32> { &mut self.partners }
    pub fn children(&self) -> &HashMap<i32, Vec<i32>> { &self.children }
    pub fn children_mut(&mut self) -> &mut HashMap<i32, Vec<i32>> { &mut self.children }
    pub fn is_deleted(&self) -> bool { self.deleted }
    pub fn mark_as_deleted(&mut self) { self.deleted = true; }
}

impl std::fmt::Display for Person {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Person(id={}, name='{}')", self.id, self.name)
    }
}

//_______________________________________
pub mod input {
    use super::*;
    pub fn get_str(msg: &str) -> String {
        loop {
            print!("{}", msg);
            io::stdout().flush().unwrap();

            let mut input = String::new();
            io::stdin().read_line(&mut input).unwrap();
            let input = input.trim();

            if !input.is_empty() {
                return input.to_string();
            }

            println!("\n❌ This field cannot be empty.");
        }
    }

    pub fn get_int(msg: &str) -> i32 {
        loop {
            let input = get_str(msg);
            match input.parse() {
                Ok(num) => return num,
                Err(_) => println!("\n❌ Enter an integer."),
            }
        }
    }
}

//_______________________________________
pub struct People {
    people: Vec<Person>,
    filename: String,
}

impl People {
    pub fn new(filename: Option<&str>) -> Self {
        let filename = filename.unwrap_or("people.json").to_string();
        let mut people = Self { people: Vec::new(), filename };
        people.load_from_json();
        people
    }

    pub fn get_people(&self) -> &[Person] {
        &self.people
    }

    pub fn load_from_json(&mut self) {
        match fs::read_to_string(&self.filename) {
            Ok(json_string) => {
                match serde_json::from_str(&json_string) {
                    Ok(loaded_people) => {
                        self.people = loaded_people;
                        println!("✅ The file '{}' has been successfully loaded.", self.filename);
                    },
                    Err(e) => println!("⚠️ Error parsing JSON from '{}': {}", self.filename, e),
                }
            },
            Err(_) => {
                println!("⚠️ The file '{}' not found. Starting with an empty list.", self.filename);
                self.people = vec![Person::new(0, "unknown".to_string())];
            }
        }
    }

    pub fn save_to_json(&self) {
        match serde_json::to_string_pretty(&self.people) {
            Ok(json_string) => {
                match fs::write(&self.filename, json_string) {
                    Ok(_) => println!("✅ Data saved successfully to {}", self.filename),
                    Err(e) => println!("❌ An error occurred while saving to '{}': {}.", self.filename, e),
                }
            },
            Err(e) => println!("❌ Error serializing data: {}", e),
        }
    }

    pub fn print_people(&self) {
        println!("{}", "_".repeat(32));
        println!("|{:4}|{:-25}|", "id", "Name");
        println!("{}", "_".repeat(32));
        for person in self.people.iter().filter(|p| !p.is_deleted()) {
            println!("|{:4}|{:-25}|", person.id(), person.name());
        }
        println!("{}", "*".repeat(32));
    }

    pub fn get_person_by_id(&self, id: i32) -> Option<&Person> {
        self.people.iter().find(|p| p.id() == id)
    }
    
    pub fn get_person_by_id_mut(&mut self, id: i32) -> Option<&mut Person> {
        self.people.iter_mut().find(|p| p.id() == id)
    }

    pub fn add_person(&mut self) {
        println!("Add Person or 'x' to Exit");
        let name = input::get_str("Name: ");
        if name.eq_ignore_ascii_case("x") {
            println!("Exit");
            return;
        }
        let new_id = self.people.iter().map(|p| p.id()).max().unwrap_or(-1) + 1;
        let new_person = Person::new(new_id, name);
        println!("✅ Added: {}", new_person);
        self.people.push(new_person);
        self.save_to_json();
    }

    pub fn remove_person(&mut self) {
        self.print_people();
        println!("\nPerson ID to mark as deleted or a letter to exit.");
        let id_str = input::get_str("ID: ");
        match id_str.parse::<i32>() {
            Ok(id) => {
                if let Some(person) = self.people.iter_mut().find(|p| p.id() == id) {
                    if !person.partners().is_empty() || !person.parents().is_empty() {
                        println!("❌ You cannot delete a person who is linked to parents or partners.");
                        return;
                    }
                    person.mark_as_deleted();
                    println!("✅ '{}' is marked as deleted.", person.name());
                    self.save_to_json();
                } else {
                    println!("❌ ID not found.");
                }
            },
            Err(_) => println!("Exit"),
        }
    }

    pub fn count(&self) -> usize {
        self.people.len()
    }
}

//_______________________________________
pub mod partners {
    use super::*;

    fn add(people: &mut People, partners: &mut HashSet<i32>, id_person: i32) {
        println!("Select Partner ID");
        let id_partner = input::get_int("ID: ");
        if let Some(partner) = people.get_person_by_id_mut(id_partner) {
            if partner.is_deleted() {
                println!("❌ ID not found or the person is deleted.");
                return;
            }
            if partners.contains(&id_partner) {
                println!("❌ This partner is already added.");
                return;
            }

            partners.insert(id_partner);
            partner.partners_mut().insert(id_person);
            if let Some(person) = people.get_person_by_id_mut(id_person) {
                person.partners_mut().insert(id_partner);
            }

            println!("✅ Partner successfully added.");
            people.save_to_json();
        } else {
            println!("❌ ID not found or the person is deleted.");
        }
    }

    fn remove(people: &mut People, partners: &mut HashSet<i32>, id_person: i32) {
        println!("Select Partner ID to Delete");
        let id = input::get_int("ID: ");
        if !partners.contains(&id) {
            println!("❌ ID not found.");
            return;
        }
        if let Some(partner) = people.get_person_by_id_mut(id) {
            if !partner.children().is_empty() {
                println!("❌ Cannot delete a partner who has children.");
                return;
            }
            partners.remove(&id);
            partner.partners_mut().remove(&id_person);
            
            if let Some(person) = people.get_person_by_id_mut(id_person) {
                person.partners_mut().remove(&id);
            }
            
            println!("✅ Partner deleted");
            people.save_to_json();
        } else {
            println!("❌ Partner not found.");
        }
    }

    fn options(people: &mut People, partners: &mut HashSet<i32>, id_person: i32) {
        println!("\n1. Add partner | 2. Remove partner | 3. Exit");
        let option = input::get_int("\nOption: ");
        match option {
            1 => add(people, partners, id_person),
            2 => remove(people, partners, id_person),
            3 => return,
            _ => println!("❌ Invalid option."),
        }
    }

    pub fn edit_partners(people: &mut People) {
        people.print_people();
        println!("\nPerson ID to edit partners or a letter to exit.");
        let id_str = input::get_str("ID: ");
        let id = match id_str.parse::<i32>() {
            Ok(id) => id,
            Err(_) => {
                println!("Exit");
                return;
            }
        };

        if let Some(person) = people.get_person_by_id(id) {
            if person.is_deleted() {
                println!("❌ ID not found or the person is deleted.");
                return;
            }
            println!("You selected '{}'", person.name());
            let partners = person.partners().clone();
            if !partners.is_empty() {
                println!("Partners:");
                for &id_p in partners.iter() {
                    if let Some(partner) = people.get_person_by_id(id_p) {
                        println!("ID: {} -> {}", partner.id(), partner.name());
                    }
                }
            } else {
                println!("🚫 This person has no partners.");
            }
            
            let mut partners = partners;
            options(people, &mut partners, id);
            
            if let Some(person) = people.get_person_by_id_mut(id) {
                *person.partners_mut() = partners;
            }
        } else {
            println!("❌ ID not found or the person is deleted.");
        }
    }
}

//_______________________________________
pub struct Children {
    id_parent: i32,
    id_partner: i32,
    id_child: i32,
    children: HashMap<i32, Vec<i32>>,
}

impl Children {
    pub fn new() -> Self {
        Self {
            id_parent: 0,
            id_partner: 0,
            id_child: 0,
            children: HashMap::new(),
        }
    }

    fn select_partner(&self, people: &People, partners: &HashSet<i32>) -> Option<i32> {
        println!("Partners:");
        for &id_p in partners {
            if let Some(partner) = people.get_person_by_id(id_p) {
                println!("ID: {} -> {}", partner.id(), partner.name());
            }
        }

        println!("Select the ID of the partner with whom you have the child.");
        let id_partner = input::get_int("Id: ");
        if partners.contains(&id_partner) {
            return Some(id_partner);
        }

        println!("❌ ID not found or the person is deleted.");
        None
    }

    fn update_child_parent(&mut self, people: &mut People) -> Option<i32> {
        let id_child = input::get_int("Select Child ID: ");
        if let Some(child) = people.get_person_by_id(id_child) {
            if !child.parents().is_empty() {
                println!("❌ This person already has parents.");
                return None;
            }

            if self.children.is_empty() {
                self.children = HashMap::new();
            }

            let children_list = self.children.entry(self.id_partner).or_insert_with(Vec::new);
            if !children_list.contains(&id_child) {
                children_list.push(id_child);
            }

            if let Some(parent) = people.get_person_by_id_mut(self.id_parent) {
                parent.children_mut().clear();
                parent.children_mut().extend(self.children.clone());
            }

            if let Some(child) = people.get_person_by_id_mut(id_child) {
                child.parents_mut().clear();
                child.parents_mut().extend([self.id_parent, self.id_partner].iter().copied());
            }

            Some(id_child)
        } else {
            None
        }
    }

    fn update_child_partner(&self, partner: &mut Person) {
        let children_list = partner.children_mut().entry(self.id_parent).or_insert_with(Vec::new);
        if !children_list.contains(&self.id_child) {
            children_list.push(self.id_child);
        }
    }

    fn add(&mut self, people: &mut People) {
        let parent = match people.get_person_by_id(self.id_parent) {
            Some(p) => p,
            None => {
                println!("❌ Parent not found.");
                return;
            }
        };
    
        let partners = parent.partners();
        if partners.is_empty() {
            println!("❌ This person does not have a partner with whom to have children.");
            return;
        }
    
        let id_partner = match self.select_partner(people, &partners) {
            Some(id) => id,
            None => return,
        };
        
        self.id_partner = id_partner;
        let id_child = match self.update_child_parent(people) {
            Some(id) => id,
            None => {
                println!("❌ Failed to update child.");
                return;
            }
        };
    
        let partner = match people.get_person_by_id_mut(id_partner) {
            Some(p) => p,
            None => {
                println!("❌ Partner not found.");
                return;
            }
        };
    
        self.id_child = id_child;
        self.update_child_partner(partner);
    
        println!("✅ Child successfully added.");
        people.save_to_json();
    }

    fn remove_and_update(&mut self, people: &mut People, id_parent: i32, id_partner: i32) {
        if let Some(parent) = people.get_person_by_id_mut(id_parent) {
            if let Some(children_with_partner) = parent.children_mut().get_mut(&id_partner) {
                children_with_partner.retain(|&child| child != self.id_child);
                if children_with_partner.is_empty() {
                    parent.children_mut().remove(&id_partner);
                }
            }
        }

        if let Some(child) = people.get_person_by_id_mut(self.id_child) {
            child.parents_mut().retain(|&parent_id| parent_id != id_parent);
        }

        println!("✅ Child deleted in parent: (ID: {})", id_parent);
        people.save_to_json();
    }

    fn remove(&mut self, people: &mut People) {
        self.id_child = input::get_int("Select Child ID to Delete: ");
        if let Some(child) = people.get_person_by_id(self.id_child) {
            if child.parents().len() != 2 {
                println!("❌ Child does not have two parents.");
                return;
            }

            let parent_ids: Vec<i32> = child.parents().iter().cloned().collect();
            let (id_p1, id_p2) = (parent_ids[0], parent_ids[1]);
            self.remove_and_update(people, id_p1, id_p2);
            self.remove_and_update(people, id_p2, id_p1);
        }
    }

    fn options(&mut self, people: &mut People) {
        println!("\n1. Add child | 2. Remove child | 3. Exit");
        let option = input::get_int("Option: ");

        match option {
            1 => self.add(people),
            2 => self.remove(people),
            3 => return,
            _ => println!("❌ Invalid option."),
        }
    }

    pub fn edit_children(&mut self, people: &mut People) {
        people.print_people();
        println!("\nPerson ID to edit Children or a letter to exit.");
        let id_str = input::get_str("id: ");
        if let Ok(id) = id_str.parse::<i32>() {
            if let Some(parent) = people.get_person_by_id(id) {
                if parent.is_deleted() {
                    println!("❌ ID not found or the person is deleted.");
                    return;
                }
    
                println!("You selected '{}'", parent.name());
                let children = parent.children().clone();
                if !children.is_empty() {
                    println!("Children:");
                    for (partner_id, child_ids) in children.iter() {
                        if let Some(partner) = people.get_person_by_id(*partner_id) {
                            let partner_name = partner.name();
                            println!("With ID: {} -> '{}':", partner_id, partner_name);
                            for &child_id in child_ids.iter() {
                                if let Some(child) = people.get_person_by_id(child_id) {
                                    println!("    ID: {} -> '{}'", child_id, child.name());
                                }
                            }
                        }
                    }
                } else {
                    println!("🚫 This person has no children.");
                }
    
                self.id_parent = id;
                self.children = children;
                self.options(people);
            } else {
                println!("❌ ID not found or the person is deleted.");
            }
        } else {
            println!("Exit");
        }
    }
}

//_______________________________________
pub mod tree {
    use super::*;
    use std::collections::HashSet;

    struct FilteredGrandparents<'a> {
        grandparents: Vec<&'a Person>,
        no_partner: Vec<&'a Person>,
    }

    fn filtered_grandparents(people: &People) -> FilteredGrandparents {
        let mut grandparents = Vec::new();
        let mut no_partner = Vec::new();

        for person in people.get_people().iter().filter(|p| !p.is_deleted() && p.name() != "unknown") {
            if person.parents().is_empty() {
                if person.partners().is_empty() {
                    no_partner.push(person);
                } else {
                    let has_grandparent_partner = person.partners().iter().any(|&partner_id| {
                        people.get_person_by_id(partner_id)
                        .map_or(false, |partner| grandparents.iter().any(|gp: &&Person| gp.id() == partner.id()))
                    });

                    if !has_grandparent_partner {
                        grandparents.push(person);
                    }
                }
            }
        }

        FilteredGrandparents { grandparents, no_partner }
    }

    fn print_child(people: &People, children: &[i32], prefix: &str, is_last: bool, is_root: bool) {
        for (i, &child_id) in children.iter().enumerate() {
            let is_last_child = i == children.len() - 1;
            let new_prefix = if is_root {
                prefix.to_string()
            } else {
                let prefix_chars: Vec<char> = prefix.chars().collect();
                let new_prefix_chars = if prefix_chars.len() > 4 {
                    prefix_chars[0..prefix_chars.len() - 4].to_vec()
                } else {
                    Vec::new()
                };
                format!("{}{}", new_prefix_chars.into_iter().collect::<String>(), if is_last { "    " } else { "│   " })
            };

            print_family(
                people,
                child_id,
                &format!("{}{}", new_prefix, if is_last_child { "└── " } else { "├── " }),
                is_last_child,
                false,
            );
        }
    }

    fn print_parents(people: &People, id: i32, partners: &HashSet<i32>, prefix: &str, is_last: bool, is_root: bool) {
        for &partner_id in partners {
            if let Some(partner) = people.get_person_by_id(partner_id) {
                println!("{}💑 With: {} (ID: {})", prefix, partner.name(), partner.id());
                if let Some(children) = partner.children().get(&id) {
                    if !children.is_empty() {
                        print_child(people, children, prefix, is_last, is_root);
                    } else {
                        println!("{}└── 🚫 Without children", prefix);
                    }
                }
            }
        }
    }

    fn print_family(people: &People, id: i32, prefix: &str, is_last: bool, is_root: bool) {
        if let Some(person) = people.get_person_by_id(id) {
            println!("{}🙂 {} (ID: {})", prefix, person.name(), person.id());
    
            if !person.partners().is_empty() {
                let new_prefix = if !is_root {
                    let prefix_chars: Vec<char> = prefix.chars().collect();
                    let new_prefix_chars = if prefix_chars.len() > 4 {
                        prefix_chars[0..prefix_chars.len() - 4].to_vec()
                    } else {
                        Vec::new()
                    };
                    let new_prefix = new_prefix_chars.into_iter().collect::<String>();
                    format!("{}{}", new_prefix, if is_last { "    " } else { "│   " })
                } else {
                    prefix.to_string()
                };
    
                print_parents(people, id, person.partners(), &new_prefix, is_last, is_root);
                if !is_last {
                    println!("{}", new_prefix);
                }
            }
        }
    }

    pub fn print_tree(people: &People) {
        let FilteredGrandparents { grandparents, no_partner } = filtered_grandparents(people);

        if grandparents.is_empty() && no_partner.is_empty() {
            println!("⚠️ No users are registered.");
            return;
        }

        if !no_partner.is_empty() {
            println!("__________");
            println!("Parents unknown, without descendants and without a partner:");
            for p in &no_partner {
                println!("😐 {} (ID: {})", p.name(), p.id());
            }
        }

        println!();
        for (i, grandparent) in grandparents.iter().enumerate() {
            println!("__________");
            println!("Family #{}", i + 1);
            print_family(people, grandparent.id(), "", false, true);
        }
    }
}

//_______________________________________
const MENU: &str = r"
---------------------------------------------
| 1. Add person    | 4. Edit children       |
| 2. Remove person | 5. Print tree          |
| 3. Edit partners | 6. Exit                |
---------------------------------------------";

struct Program {
    people: People,
}

impl Program {
    fn new() -> Self {
        Program {
            people: People::new(None),
        }
    }

    fn run(&mut self) {
        loop {
            println!("{}", MENU);
            let option = input::get_int("\nOption: ");
            match option {
                1 => self.people.add_person(),
                2 => self.people.remove_person(),
                3 => partners::edit_partners(&mut self.people),
                4 => Children::new().edit_children(&mut self.people),
                5 => tree::print_tree(&self.people),
                6 => {
                    println!("Bye");
                    return;
                },
                _ => println!("❌ Invalid option."),
            }
        }
    }
}

fn main() {
    let mut program = Program::new();
    program.run();
}
