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

//____________________________________
// Estructuras concretas
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

    fn name(&self) -> &str {&self.name}

    fn price(&self) -> f64 {self.price}

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

    fn name(&self) -> &str {&self.name}

    fn price(&self) -> f64 {self.price}

    fn apply_discount(&self) -> f64 {
        if self.price > 50.0 {
            10.0
        } else {
            0.0
        }
    }
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
    fn operation_result(&self);
}

// __________________________________________
// Estructuras concretas
struct Sum { a: f64, b: f64 }

impl Calculator for Sum {
    fn new(a: f64, b: f64) -> Sum {Sum { a, b }}
    
    fn operation_result(&self) {
        println!("\nSuma:");
        println!("{} + {} = {}", self.a, self.b, self.a + self.b);
    }
}

// __________________________________________
struct Subtraction { a: f64, b: f64 }

impl Calculator for Subtraction {
    fn new(a: f64, b: f64) -> Subtraction {Subtraction { a, b }}
    
    fn operation_result(&self) {
        println!("\nResta:");
        println!("{} - {} = {}", self.a, self.b, self.a - self.b);
    }
}

// __________________________________________
struct Multiplication { a: f64, b: f64 }

impl Calculator for Multiplication {
    fn new(a: f64, b: f64) -> Multiplication {Multiplication { a, b }}
    
    fn operation_result(&self) {
        println!("\nMultiplicación:");
        println!("{} * {} = {}", self.a, self.b, self.a * self.b);
    }
}

// __________________________________________
struct Division { a: f64, b: f64 }

impl Calculator for Division {
    fn new(a: f64, b: f64) -> Division {Division { a, b }}
    
    fn operation_result(&self) {
        println!("\nDivisión:");
        println!("{} / {} = {}", self.a, self.b, self.a / self.b);
    }
}

// __________________________________________
struct Pow { a: f64, b: f64 }

impl Calculator for Pow {
    fn new(a: f64, b: f64) -> Pow {Pow { a, b }}
    
    fn operation_result(&self) {
        println!("\nPotencia:");
        println!("{} ^ {} = {}", self.a, self.b, self.a.powf(self.b));
    }
}

fn main() {
    //____________________________________
    fn process_product<T: Product>(product: T) {
        println!(
            "Producto: {}, Precio final: {}",
            product.name(),
            product.final_price()
        );
    }

    process_product(ElectronicsProduct::new("Laptop", 700.0));
    process_product(ClothingProduct::new("Pants", 55.0));

    // _______________________________________________
    // exs 2

    Sum::new(2.0, 2.0).operation_result();
    Subtraction::new(2.0, 2.0).operation_result();
    Multiplication::new(2.0, 2.0).operation_result();
    Division::new(2.0, 2.0).operation_result();
    Pow::new(2.0, 2.0).operation_result();

}
