// Data structures in Rust: https://doc.rust-lang.org/std/collections/index.html
use std::collections::{BTreeMap, BTreeSet, BinaryHeap, HashMap, HashSet, LinkedList, VecDeque};
use std::io;

fn agenda_validate_phone(phone: &String) -> bool {
    if phone.len() == 0 || phone.len() > 11 {
        return false;
    }

    let mut phone_ok = true;

    for digit in phone.chars() {
        if ! ['0','1','2','3','4','5','6','7','8','9'].contains(&digit) {
            phone_ok = false;
            break;
        }
    }

    return phone_ok;
}

fn agenda_add(agenda_contacts: &mut HashMap<String, String>) {
    let mut name = String::new();
    let mut phone = String::new();

    println!("Name:");
    io::stdin()
        .read_line(&mut name)
        .expect("User does not provide the name");

    name = name.trim().to_string();
    
    println!("Phone:");
    io::stdin()
        .read_line(&mut phone)
        .expect("User does not provide the phone");

    phone = phone.trim().to_string();
    
    if ! agenda_validate_phone(&phone) {
        println!("Phone format is not correct!");
        return;
    }

    agenda_contacts.insert(name, phone);
}

fn agenda_search(agenda_contacts: &mut HashMap<String, String>) {
    let mut contact = String::new();

    println!("Contact to search: ");
    io::stdin()
        .read_line(&mut contact)
        .expect("User does not provide the contact");

    contact = contact.trim().to_string();
    let phone = agenda_contacts.get(&contact);

    if let Some(p) = phone {
        println!("Contact name: {}, contact phone {}", contact, p);
    } else {
        println!("Contact not found!");
    }

}

fn agenda_remove(agenda_contacts: &mut HashMap<String, String>) {
    let mut contact = String::new();

    println!("Contact to delete: ");
    io::stdin()
        .read_line(&mut contact)
        .expect("User does not provide the contact");

    contact = contact.trim().to_string();
    agenda_contacts.remove(&contact);
}


fn agenda_list(agenda_contacts: &mut HashMap<String, String>) {
    let mut entry = 1;
    if agenda_contacts.len() == 0 {
        println!("Agenda is empty");
        return;
    }
    
    for (name, phone) in agenda_contacts.iter() {
        println!("Entry {}: Name {}, Phone {}", entry, name, phone);
        entry += 1;
    }
}

fn agenda_update(agenda_contacts: &mut HashMap<String, String>) {
    let mut name = String::new();
    let mut phone = String::new();

    println!("Name:");
    io::stdin()
        .read_line(&mut name)
        .expect("User does not provide the name");

    name = name.trim().to_string();

    if let Some(_p) = agenda_contacts.get(&name) {
        println!("Phone:");
        io::stdin()
        .read_line(&mut phone)
        .expect("User does not provide the phone");

        phone = phone.trim().to_string();
    
        if ! agenda_validate_phone(&phone) {
            println!("Phone format is not correct!");
            return;
        }
        
        *agenda_contacts.get_mut(&name).unwrap() = phone;

    } else {
        println!("Contact not found!");
    }
}

fn agenda_clear(agenda_contacts: &mut HashMap<String, String>) {
    agenda_contacts.clear();
}

fn agenda(agenda_contacts: &mut HashMap<String, String>) -> bool {
    let mut command = String::new();
    let mut exit = false;
    println!("Next Agenda command: ");
    io::stdin()
        .read_line(&mut command)
        .expect("User does not provide the command");

    println!("User command: {}", command);
    match command.as_str().trim() {
        "add" => agenda_add(agenda_contacts),
        "list" => agenda_list(agenda_contacts),
        "remove" => agenda_remove(agenda_contacts),
        "search" => agenda_search(agenda_contacts),
        "update" => agenda_update(agenda_contacts),
        "clear" => agenda_clear(agenda_contacts),
        "help" => {
            println!("add: Add a new contact to the agenda");
            println!("list: List the agenda");
            println!("remove: Remove a contact from the agenda");
            println!("search: Search the phone number for a contact");
            println!("update: Update the phone number for a contact");
            println!("exit: Exit from the agenda app");
            println!("clear: Remove all contacts from agenda");
            println!("help: Show this help message");
        },
        "exit" => exit = true,
        _ => println!("Not recognized command: {}", command.as_str()),
    }

    return exit;
}

fn main() {
    // Tuple
    let tuple1: (i32, f64, &str) = (500, 1.5, "Hello world");
    println!("{tuple1:?}");
    let (x, _, z) = tuple1;
    println!("x = {x}, z = {z}");
    println!(
        "tuple1.0: {}, tuple1.1: {}, tuple1.2: {}",
        tuple1.0, tuple1.1, tuple1.2
    );

    // Array (static/fixed)
    let mut array1 = [3, 4, 5, 6, 4, 5, 9, 11, 0];
    let mut array2 = ['a', 'c', 'e', 'b', 'd'];
    let array3 = [1.2, 1.4, 1.5];

    println!(
        "array1[2]: {}, array2[1]: {}, array3[0]: {}",
        array1[2], array2[1], array3[0]
    );

    for a in array1 {
        println!("{}", a);
    }

    println!("{array1:?}");
    println!("{array2:?}");

    array1.sort();
    array2.sort();

    println!("{array1:?}");
    println!("{array2:?}");

    // Array (dinamic), Vector
    let mut vector1 = vec![10, 20, 30, 1, 2, 99, 101];
    println!("vector1: {:?}, size {}", vector1, vector1.len());
    vector1.push(55);
    println!("vector1: {:?}, size {}", vector1, vector1.len());
    println!(
        "vector1 {:?}, elem[3] {}, size {}",
        vector1,
        vector1[3],
        vector1.len()
    );
    println!("vector1 pop: {}", vector1.pop().unwrap());

    for v in vector1.iter() {
        println!("{}", v);
    }

    for (index, value) in vector1.iter().enumerate() {
        println!("vector1[{}]: {}", index, value);
    }

    vector1.sort();

    for (index, value) in vector1.iter().enumerate() {
        println!("vector1[{}]: {}", index, value);
    }

    // Queue or VecDeque
    let mut queue1 = VecDeque::from([1]);
    println!("{queue1:?}");
    queue1.push_back(10);
    println!("{queue1:?}");
    queue1.push_back(33);
    println!("{queue1:?}");
    queue1.push_back(55);
    println!("{queue1:?}");
    println!("pop {}", queue1.pop_front().unwrap());
    println!("{queue1:?}");
    println!("pop {}", queue1.pop_front().unwrap());
    println!("{queue1:?}");
    println!("pop {}", queue1.pop_front().unwrap());
    println!("{queue1:?}");

    // LinkedList
    let mut llist1 = LinkedList::from(["John", "Peter"]);
    let mut llist2 = LinkedList::from(["Mary", "Lisa"]);
    println!("{llist1:?}");
    println!("{llist2:?}");
    llist1.append(&mut llist2);
    println!("{llist1:?}");
    println!("{llist2:?}");
    println!("llist2 is empty={}", llist2.is_empty());
    llist2.push_back("Chris");
    llist2.push_back("Robert");
    println!("{llist1:?}");
    println!("{llist2:?}");

    for node in llist1.iter() {
        println!("Node for llist1: {}", node);
    }
    println!("llist1 contains Lisa={}", llist1.contains(&"Lisa"));
    println!("llist1 contains Robert={}", llist1.contains(&"Robert"));

    println!("Front for llist2: {}", llist2.front().unwrap());

    // HashMap
    let mut dict1 = HashMap::new();

    dict1.insert("Apples", 3);
    println!("{dict1:?}");
    dict1.insert("Bananas", 5);
    println!("{dict1:?}");

    if dict1.contains_key("Cherries") {
        println!("I have {} cherries", dict1.get("cherries").unwrap());
    } else {
        println!("I have to buy cherries");
    }

    dict1.remove("Bananas");
    println!("{dict1:?}");

    for (item, amount) in dict1.iter() {
        println!("{item} -> {amount}");
    }

    println!("{dict1:?}");

    // BTreeMap
    let mut pets = BTreeMap::new();

    pets.insert("dogs", 4);
    pets.insert("cats", 2);
    pets.insert("fishes", 5);

    println!("{pets:?}");
    pets.remove("cats");
    println!("{pets:?}");

    if pets.contains_key("dogs") {
        println!("I have {} dogs", pets.get("dogs").unwrap());
    }

    for (pet, amount) in pets.iter() {
        println!("{pet} -> {amount}");
    }

    // HashSet
    let mut set1 = HashSet::new();

    set1.insert(4);
    set1.insert(5);
    if !set1.insert(4) {
        println!("key 4 exists");
    }
    set1.insert(7);

    if !set1.contains(&9) {
        println!("set does not contain 9");
    }

    println!("{set1:?}");
    set1.remove(&5);
    println!("{set1:?}");

    for element in set1.iter() {
        println!("Element: {}", element);
    }

    // BTreeSet
    let mut bset1 = BTreeSet::from([1, 2, 3, 4]);
    println!("{bset1:?}");
    bset1.insert(8);
    bset1.remove(&3);
    println!("{bset1:?}");

    if bset1.contains(&4) {
        println!("bset1 contains 4");
    }

    for (index, element) in bset1.iter().enumerate() {
        println!("bset1[{index}] = {element}");
    }

    // BinaryHeap
    let mut heap = BinaryHeap::from([1, 3, 6]);

    println!("{heap:?}");

    println!("peek: {}", heap.peek().unwrap());
    heap.pop();
    println!("peek: {}", heap.peek().unwrap());
    heap.push(5);
    println!("peek: {}", heap.peek().unwrap());
    heap.pop();
    println!("peek: {}", heap.peek().unwrap());

    for elem in heap.iter() {
        println!("{elem}");
    }

    // Extra: agenda
    let mut agenda_contacts = HashMap::new();

    loop {
        let end = agenda(&mut agenda_contacts);

        if end {
            break;
        }
    }
}
