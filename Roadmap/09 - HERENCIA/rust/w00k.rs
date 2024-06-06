
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

trait Animal {
    fn sound(&self) -> &str;
}

struct Dog {
    name: String,
    breed_of_dog: String,
    sound: String,
}
struct Cat {
    name: String,
    breed_of_cat: String,
    sound: String,
}

impl Animal for Dog {
    fn sound(&self) -> &str {
        return &self.sound;
    }
}

impl Animal for Cat {
    fn sound(&self) -> &str {
        return &self.sound;
    }
}

fn main() {
    println!("Start.");

    let dog = Dog{
        name: "Pepe".parse().unwrap(),
        breed_of_dog: "German Shepherd".parse().unwrap(),
        sound: "Guau".parse().unwrap(),
    };

    let cat = Cat{
        name: "Lala".parse().unwrap(),
        breed_of_cat: "Domestic Shorthair".parse().unwrap(),
        sound: "Miauuuuuu".parse().unwrap(),
    };

    println!("type of animal: {}, name: {}, sound: {}", dog.breed_of_dog, dog.name, dog.sound());
    println!("type of animal: {}, name: {}, sound: {}", cat.breed_of_cat, cat.name, cat.sound());

    println!("End.");
}

