/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* SOLID: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
-----------------------------------------

* EJERCICIO:
* Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
* Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
* de forma correcta e incorrecta.
*/

// # SIN APLICAR EL PRINCIPIO:

pub struct Program {
    customers: Vec<String>,
    suppliers: Vec<String>,
}

impl Program {
    pub fn new() -> Self {
        Program {
            customers: Vec::new(),
            suppliers: Vec::new(),
        }
    }

    pub fn add_customer(&mut self, name: String) {
        self.customers.push(name);
    }

    pub fn add_supplier(&mut self, name: String) {
        self.suppliers.push(name);
    }

    pub fn remove_customer(&mut self, name: &str) {
        self.customers.retain(|x| x != name);
    }

    pub fn remove_supplier(&mut self, name: &str) {
        self.suppliers.retain(|x| x != name);
    }
}

// _______________________________________
// APLICANDO SRP:

pub struct Customers {
    customers: Vec<String>,
}

impl Customers {
    pub fn new() -> Self {
        Customers {
            customers: Vec::new(),
        }
    }

    pub fn add(&mut self, name: String) {
        self.customers.push(name);
    }

    pub fn remove(&mut self, name: &str) {
        self.customers.retain(|x| x != name);
    }
}

pub struct Suppliers {
    suppliers: Vec<String>,
}

impl Suppliers {
    pub fn new() -> Self {
        Suppliers {
            suppliers: Vec::new(),
        }
    }

    pub fn add(&mut self, name: String) {
        self.suppliers.push(name);
    }

    pub fn remove(&mut self, name: &str) {
        self.suppliers.retain(|x| x != name);
    }
}

//____________________________________
fn main() {
    let mut customers = Customers::new();
    let mut suppliers = Suppliers::new();

    customers.add(String::from("C A"));
    customers.add(String::from("C B"));

    suppliers.add(String::from("S X"));
    suppliers.add(String::from("S Y"));

    println!("Clientes: {:?}", customers.customers);
    println!("Proveedores: {:?}", suppliers.suppliers);

    customers.remove("C A");
    suppliers.remove("S X");

    println!("Clientes: {:?}", customers.customers);
    println!("Proveedores: {:?}", suppliers.suppliers);
    
}
