/// https://www.rust-lang.org/

/*
This is a
multi-line
block comment
*/

fn main() {
    // Constant Variables
    let _string = "Hello";
    let _string2 = "Rust";
    // Mutables
    let mut _y = 10;
    _y = 20;

    // Strings
    let _str: &str = " This is a string";

    // Integers
    let _int: i32 = 42;

    // Floating points
    let _fl1: f64 = 3.1416;

    //Booleans
    let _bool: bool = false;

    // Characters
    let _char: char = '😂';

    // tuples
    let _tup: (i32, f64, bool) = (2, 1.5, false);

    // Arrays
    let _arr: [i32; 4] = [1, 5, 7, 9];

    // Objects: 1. define structure and create the instance.
    struct Person {
        _name: String,
        _age: u32,
    }

    let _person: Person = Person {
        _name: String::from("Alice"),
        _age: 30,
    };

    // Classes: 1. Define structure, add constructor and methods
    impl Person {
        // Constructor function
        fn _new(_name: &str, _age: u32) -> Person {
            Person {
                _name: String::from(_name),
                _age,
            }
        }

        // Method to greet the person
        fn _greet(&self) {
            println!("Hello, my name is {} and I'm {} years old.", self._name, self._age);
        }
    }

    let _person = Person::_new("Gabrielmoris", 34);

    println!("{_string}, {_string2}");
}
