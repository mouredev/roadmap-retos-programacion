/*
 * EXERCISE:
 * - Provide examples of creating all default-supported structures in your language.
 * - Use insertion, deletion, updating, and sorting operations.
 *
 */

fn main() {
    // Arays: Are Fixed size. They are created with [T; N] there T is type and N is size
    let mut array: [i32; 5] = [1, 5, 2, 4, 3];
    array.sort(); // it doesnt return the sorted array, it justs sorts the original array;
    let found = array.binary_search(&5);
    array[3] = 5;
    println!("{:?}", found);

    // Vectors: Are dynamic in size
    let mut fruits: Vec<&str> = vec!["apple", "banana", "cherry"];
    fruits.push("orange");
    let fruits_to_string = fruits.join("/");
    print!("{fruits_to_string}\n");

    // Tuples: Are fixed size and can handle different types
    let tup = (71, "a", false);
    let first = tup.0.to_owned();
    print!("{:?}\n", first);

    // Structs: User-defined data types that can hold data of different types
    struct Person {
        name: String,
        age: u32,
        is_student: bool,
    }
    let gabriel = Person {
        name: String::from("Gabriel"),
        age: 34,
        is_student: false,
    };
    let student_status = if gabriel.is_student { "" } else { "not " };
    print!(
        "my name is {}, I have {} years old and I am {}a student\n",
        gabriel.name,
        gabriel.age,
        student_status
    );

    // Enums: User-defined data types that represent a fixed set of possibilities
    #[derive(Debug)]
    enum Color {
        _Red,
        Green,
        _Blue,
    }
    let my_color = Color::Green;
    println!("{:?}", my_color);

    // HashMaps: unordered collections of key-value pairs
    use std::collections::HashMap;
    let mut scores: HashMap<String, u32> = HashMap::new();
    scores.insert("Alice".to_string(), 90);
    scores.insert("Bob".to_string(), 85);
    let it_print = scores.get_key_value("Alice");
    println!("{:?}", it_print)
}
/*
 * EXTRA CHALLENGE (optional):
 * Create a terminal-based contact agenda.
 * - Implement functionalities for searching, inserting, updating, and deleting contacts.
 * - Each contact should have a name and a phone number.
 * - The program first prompts the user to choose the desired operation,
 *   and then collects the necessary data to carry it out.
 * - The program should not allow non-numeric phone numbers with more than
 *   11 digits (or the number of digits you prefer).
 * - Additionally, propose an operation to exit the program.
 */
