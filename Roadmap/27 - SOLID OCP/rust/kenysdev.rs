/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
-----------------------------------------

- Una entidad de software que está abierta a extensión, pero cerrada a modificación, 
  esto significa que debemos poder extender el comportamiento de una clase sin 
  necesidad de modificar su código fuente original.

_______________
* EJERCICIO #1:
* Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
* y crea un ejemplo simple donde se muestre su funcionamiento
* de forma correcta e incorrecta.
*/

// Trait base
trait Product {
    fn new(name: &str, price: f64) -> Self where Self: Sized;
    fn name(&self) -> &str;
    fn price(&self) -> f64;
    fn apply_discount(&self) -> f64;
    fn final_price(&self) -> f64 {
        self.price() - self.apply_discount()
    }
}
struct ElectronicsProduct {
    name: String,
    price: f64,
}

impl Product for ElectronicsProduct {
    fn new(name: &str, price: f64) -> Self {
        ElectronicsProduct {
            name: name.to_string(),
            price,
        }
    }

    fn name(&self) -> &str {
        &self.name
    }

    fn price(&self) -> f64 {
        self.price
    }

    fn apply_discount(&self) -> f64 {
        self.price * 0.05 // 5% discount
    }
}

//____________________________________
struct ClothingProduct {
    name: String,
    price: f64,
}

impl Product for ClothingProduct {
    fn new(name: &str, price: f64) -> Self {
        ClothingProduct {
            name: name.to_string(),
            price,
        }
    }

    fn name(&self) -> &str {
        &self.name
    }

    fn price(&self) -> f64 {
        self.price
    }

    fn apply_discount(&self) -> f64 {
        if self.price > 50.0 {
            10.0
        } else {
            0.0
        }
    }
}


//____________________________________
fn process_product<T: Product>(product: T) {
    println!(
        "Producto: {}, Precio final: {}",
        product.name(),
        product.final_price()
    );
}

/*
_______________
* EJERCICIO #2:
* Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
* Requisitos:
* - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
* Instrucciones:
* 1. Implementa las operaciones de suma, resta, multiplicación y división.
* 2. Comprueba que el sistema funciona.
* 3. Agrega una quinta operación para calcular potencias.
* 4. Comprueba que se cumple el OCP.
*/

// Trait base
trait Calculator {
    fn new(a: f64, b: f64) -> Self where Self: Sized;
    fn math_operation(&self) -> f64;
    fn a(&self) -> f64;
    fn b(&self) -> f64;
    fn operation_name(&self) -> &'static str;
    fn operation_symbol(&self) -> &'static str;
    
    fn print_result(&self) {
        println!("\n{} de {} {} {}:", 
            self.operation_name(), self.a(), self.operation_symbol(), self.b());
        println!("Es: {}", self.math_operation());
    }
}

// Estructuras concretas
struct Sum { a: f64, b: f64 }
struct Subtraction { a: f64, b: f64 }
struct Multiplication { a: f64, b: f64 }
struct Division { a: f64, b: f64 }
struct Pow { a: f64, b: f64 }

impl Calculator for Sum {
    fn new(a: f64, b: f64) -> Self { Self { a, b } }
    fn a(&self) -> f64 { self.a }
    fn b(&self) -> f64 { self.b }
    fn operation_name(&self) -> &'static str { "Suma" }
    fn operation_symbol(&self) -> &'static str { "+" }
    fn math_operation(&self) -> f64 { self.a + self.b }
}

impl Calculator for Subtraction {
    fn new(a: f64, b: f64) -> Self { Self { a, b } }
    fn a(&self) -> f64 { self.a }
    fn b(&self) -> f64 { self.b }
    fn operation_name(&self) -> &'static str { "Resta" }
    fn operation_symbol(&self) -> &'static str { "-" }
    fn math_operation(&self) -> f64 { self.a - self.b }
}

impl Calculator for Multiplication {
    fn new(a: f64, b: f64) -> Self { Self { a, b } }
    fn a(&self) -> f64 { self.a }
    fn b(&self) -> f64 { self.b }
    fn operation_name(&self) -> &'static str { "Multiplicación" }
    fn operation_symbol(&self) -> &'static str { "*" }
    fn math_operation(&self) -> f64 { self.a * self.b }
}

impl Calculator for Division {
    fn new(a: f64, b: f64) -> Self { Self { a, b } }
    fn a(&self) -> f64 { self.a }
    fn b(&self) -> f64 { self.b }
    fn operation_name(&self) -> &'static str { "División" }
    fn operation_symbol(&self) -> &'static str { "/" }
    fn math_operation(&self) -> f64 { self.a / self.b }
}

impl Calculator for Pow {
    fn new(a: f64, b: f64) -> Self { Self { a, b } }
    fn a(&self) -> f64 { self.a }
    fn b(&self) -> f64 { self.b }
    fn operation_name(&self) -> &'static str { "Potencia" }
    fn operation_symbol(&self) -> &'static str { "^" }
    fn math_operation(&self) -> f64 { self.a.powf(self.b) }
}

fn main() {
    let laptop = ElectronicsProduct::new("Laptop", 700.0);
    let pants = ClothingProduct::new("Pants", 55.0);

    process_product(laptop); // Output: Producto: Laptop, Precio final: 665
    process_product(pants);  // Output: Producto: Pants, Precio final: 45

    // _______________________________________________
    // exs 2

    let calculators: Vec<Box<dyn Calculator>> = vec![
        Box::new(Sum::new(2.0, 2.0)),
        Box::new(Subtraction::new(2.0, 2.0)),
        Box::new(Multiplication::new(2.0, 2.0)),
        Box::new(Division::new(2.0, 2.0)),
        Box::new(Pow::new(2.0, 2.0)),
    ];

    for calc in calculators.iter() {
        calc.print_result();
    }
}
