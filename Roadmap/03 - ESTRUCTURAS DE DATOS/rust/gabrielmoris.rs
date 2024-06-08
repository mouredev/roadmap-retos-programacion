/*
 * EXERCISE:
 * - Provide examples of creating all default-supported structures in your language.
 * - Use insertion, deletion, updating, and sorting operations.
 *
 */

use std::io::{ self };
use std::collections::HashMap;

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
    let dramatic_fruits: Vec<String> = fruits
        .iter()
        .map(|x| format!("{}!", x))
        .collect();
    println!("{:?}", dramatic_fruits);
    let filter_fruits: Vec<String> = dramatic_fruits
        .iter()
        .filter(|x| x.contains("pp"))
        .cloned()
        .collect();
    // I need to clone and collect to actually send the filtered vector
    println!("{:?}", filter_fruits);

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
    // use std::collections::HashMap; It is already imported, but I note here as a cutiosity that it must be imported.
    let mut scores: HashMap<String, u32> = HashMap::new();
    scores.insert("Alice".to_string(), 90);
    scores.insert("Bob".to_string(), 85);
    let it_print = scores.get_key_value("Alice");
    println!("{:?}", it_print);
    challenge()
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

fn challenge() {
    let mut contacts: HashMap<String, String> = HashMap::new();

    loop {
        println!(
            "
            ===========================
            What would you like to do?
            1. Add a contact
            2. Delete a contact
            3. Search a contact
            4. Edit a contact
            5. Exit
            ===========================
            "
        );

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");

        let choice: u32 = input.trim().parse().expect("Invalid input");

        match choice {
            1 => add_contact(&mut contacts),
            2 => delete_contact(&mut contacts),
            3 => search_contact(&mut contacts),
            4 => edit_contact(&mut contacts),
            5 => {
                println!("Goodbye!");
                break;
            }
            _ => println!("Invalid choice. Please try again."),
        }

        println!();
    }
}

fn add_contact(contacts: &mut HashMap<String, String>) {
    println!("Enter the contact Name");
    let mut name: String = String::new();
    io::stdin().read_line(&mut name).expect("Failed to read name");
    let name: String = name.trim().to_string();
    println!("Enter the phone number");
    let mut phone: String = String::new();
    io::stdin().read_line(&mut phone).expect("Failed to read phone");
    let phone: String = phone.trim().to_string();

    if phone.len() > 11 {
        println!("The phone number must be shorter than 11 digits.")
    } else {
        contacts.insert(name, phone);
    }
}

fn delete_contact(contacts: &mut HashMap<String, String>) {
    println!("Enter the contact Name that you want to DELETE");
    let mut name: String = String::new();
    io::stdin().read_line(&mut name).expect("Failed to read name");
    let name: String = name.trim().to_string();

    contacts.remove(&name);
    println!("{name} has ben deleted.");
}

fn search_contact(contacts: &mut HashMap<String, String>) {
    println!("Enter the contact Name");
    let mut name: String = String::new();
    io::stdin().read_line(&mut name).expect("Failed to read name");
    let name: String = name.trim().to_string();
    let found_contact = contacts.get(&name);

    match found_contact {
        Some(phone) => println!("{}'s phone is {}", name, phone),
        None => println!("Contact not found."),
    }
}

fn edit_contact(contacts: &mut HashMap<String, String>) {
    println!("Enter the contact Name");
    let mut name = String::new();
    io::stdin().read_line(&mut name).expect("Failed to read name");
    let name = name.trim().to_string();

    // Separate scope for the immutable reference
    {
        let found_contact = contacts.get(&name);

        match found_contact {
            Some(existing_name) => {
                // Clone the existing name to avoid borrowing issues
                let existing_name_clone = existing_name.clone();
                contact_edition(contacts);
                contacts.remove(&existing_name_clone);
            }
            None => {
                println!(
                    "Contact not found. Do you want to add a new contact with this name? (y/n)"
                );
                let mut response = String::new();
                io::stdin().read_line(&mut response).expect("Failed to read response");
                let response = response.trim().to_lowercase();

                if response == "y" || response == "yes" {
                    add_contact(contacts);
                } else {
                    println!("No changes made.");
                }
            }
        }
    } // Immutable reference ends here

    // Now you can safely mutate `contacts` outside the inner scope
}

fn contact_edition(contacts: &mut HashMap<String, String>) {
    println!("Enter New Name");
    let mut new_name = String::new();
    io::stdin().read_line(&mut new_name).expect("Failed to read name");
    let new_name = new_name.trim().to_string();

    println!("Enter the new phone number");
    let mut phone = String::new();
    io::stdin().read_line(&mut phone).expect("Failed to read phone");
    let phone = phone.trim().to_string();

    if phone.len() > 11 {
        println!("The phone number must be shorter than 11 digits.");
    } else {
        // Insert the updated contact
        contacts.insert(new_name, phone);
    }
}
