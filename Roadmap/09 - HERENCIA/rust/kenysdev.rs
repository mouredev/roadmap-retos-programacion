/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* HERENCIA Y POLIMORFISMO
-----------------------------------------
- En Rust, no hay clases ni herencia como en lenguajes orientados a objetos tradicionales.
- Pero se puede lograr un diseño de código que se asemeja a la herencia y el polimorfismo
  utilizando traits y enums. 
*/
// Simulando una "Superclase"
trait Animal {
    fn make_sound(&self);
}

// Simulando una "Subclases"
struct Dog {
    name: String,
}

impl Dog {
    fn new(name: String) -> Self {
        Dog { name }
    }
}

impl Animal for Dog {
    fn make_sound(&self) {
        println!("{} hace: Woof", self.name);
    }
}
//_________
struct Cat {
  name: String,
}

impl Cat {
    fn new(name: String) -> Self {
        Cat { name }
    }
}

impl Animal for Cat {
    fn make_sound(&self) {
        println!("{} hace: Meow", self.name);
    }
}
fn main() {
    let dog = Dog::new("Max".to_string());
    let cat = Cat::new("Milo".to_string());

    dog.make_sound();
    cat.make_sound();

}
