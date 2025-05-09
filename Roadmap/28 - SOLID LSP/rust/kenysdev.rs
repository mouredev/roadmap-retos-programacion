/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-------------------------------------------------
* SOLID: PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
-------------------------------------------------
*/

trait BaseT {
    fn method_base(&self);
}

// Implementación
struct Sub1;

impl BaseT for Sub1 {
    fn method_base(&self) {
        println!("Sub1");
    }
}

// Implementación
struct Sub2;

impl BaseT for Sub2 {
    fn method_base(&self) {
        println!("Sub2");
    }
}

/*
_______________
* EJERCICIO:
* Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
* cumplir el LSP.
* Instrucciones:
* 1. Crea la clase Vehículo.
* 2. Añade tres subclases de Vehículo.
* 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
* 4. Desarrolla un código que compruebe que se cumple el LSP.
*/

// Trait base
trait Vehicle {
    fn brand(&self) -> &str;
    fn model(&self) -> &str;
    fn accelerate(&self) -> String;
    fn brake(&self) -> String;
}

// ___________________________________________
// Implementación
struct Car {
    brand: String,
    model: String,
}

impl Car {
    fn new(brand: &str, model: &str) -> Car {
        Car {
            brand: brand.to_string(),
            model: model.to_string(),
        }
    }
}

impl Vehicle for Car {
    fn brand(&self) -> &str {
        &self.brand
    }

    fn model(&self) -> &str {
        &self.model
    }

    fn accelerate(&self) -> String {
        format!("Acelerando auto: {} - {}", self.brand, self.model)
    }

    fn brake(&self) -> String {
        format!("Frenando auto: {} - {}", self.brand, self.model)
    }
}

// ___________________________________________
// Implementación
struct Motorcycle {
    brand: String,
    model: String,
}

impl Motorcycle {
    fn new(brand: &str, model: &str) -> Motorcycle {
        Motorcycle {
            brand: brand.to_string(),
            model: model.to_string(),
        }
    }
}

impl Vehicle for Motorcycle {
    fn brand(&self) -> &str {
        &self.brand
    }

    fn model(&self) -> &str {
        &self.model
    }

    fn accelerate(&self) -> String {
        format!("Acelerando Motocicleta: {} - {}", self.brand, self.model)
    }

    fn brake(&self) -> String {
        format!("Frenando Motocicleta: {} - {}", self.brand, self.model)
    }
}

// ___________________________________________
// Implementación
struct Truck {
    brand: String,
    model: String,
}

impl Truck {
    fn new(brand: &str, model: &str) -> Truck {
        Truck {
            brand: brand.to_string(),
            model: model.to_string(),
        }
    }
}

impl Vehicle for Truck {
    fn brand(&self) -> &str {
        &self.brand
    }

    fn model(&self) -> &str {
        &self.model
    }

    fn accelerate(&self) -> String {
        format!("Acelerando Camión: {} - {}", self.brand, self.model)
    }

    fn brake(&self) -> String {
        format!("Frenando Camión: {} - {}", self.brand, self.model)
    }
}

// ___________________________________________
fn test_impls(vehicle: &dyn Vehicle) {
    println!("\nPropiedades:");
    println!("{} - {}", vehicle.brand(), vehicle.model());

    println!("\nMétodos:");
    println!("{}", vehicle.accelerate());
    println!("{}", vehicle.brake());
}

fn main() {
    let s1 = Sub1;
    let s2 = Sub2;

    s1.method_base();
    s2.method_base();

    // _______________________________________________
    // EXS
    let car = Car::new("Honda", "Civic");
    test_impls(&car);

    let motorcycle = Motorcycle::new("Kawasaki", "Ninja");
    test_impls(&motorcycle);

    let truck = Truck::new("Ford", "Raptor");
    test_impls(&truck);

}
