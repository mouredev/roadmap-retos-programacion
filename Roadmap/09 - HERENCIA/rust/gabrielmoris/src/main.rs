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
    let dog = Animal::new("Laica", Dog);
    let cat = Animal::new("Felix", Cat);

    dog.print_sound(); // Prints "Laica says Guau!"
    cat.print_sound(); // Prints "Felix says Marramiau!"
}

/* EXTRA CHALLENGE (optional):
 * Implement the hierarchy of a development company consisting of Employees who
 * can be Managers, Project Managers, or Programmers.
 * Each employee has an identifier and a name.
 * Depending on their role, they have properties and functions exclusive to their
 * activity, and they store the employees under their supervision.
 */
