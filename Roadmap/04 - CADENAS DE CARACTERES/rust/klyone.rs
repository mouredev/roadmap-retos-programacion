use std::collections::HashMap;

fn check_words(word1: &str, word2: &str) {
    let word1_rev: String = word1.to_lowercase().chars().rev().collect();
    let word1_lower: String = word1.to_lowercase().to_string();

    let word2_rev: String = word2.to_lowercase().chars().rev().collect();
    let word2_lower: String = word2.to_lowercase().to_string();

    if word1_rev == word1_lower {
        println!("{word1} is a palindrome");
    }

    if word2_rev == word2_lower {
        println!("{word2} is a palindrome");
    }

    let mut hm1 = HashMap::new();
    let mut hm2 = HashMap::new();

    for c1 in word1_lower.chars() {
        if let Some(entry1) = hm1.get_mut(&c1) {
            *entry1 += 1;
        } else {
            hm1.insert(c1, 1);
        }
    }
    println!("Char distribution for {word1} = {hm1:?}");

    for c2 in word2_lower.chars() {
        if let Some(entry2) = hm2.get_mut(&c2) {
            *entry2 += 1;
        } else {
            hm2.insert(c2, 1);
        }
    }

    println!("Char distribution for {word2} = {hm2:?}");

    let mut anagram_str = "NOT";

    if (hm1.len() == hm2.len()) && (!hm1.is_empty() && !hm2.is_empty()) {
        anagram_str = "";
        for c1 in hm1.iter() {
            if let Some(entry2) = hm2.get(c1.0) {
                if *entry2 != *c1.1 {
                    anagram_str = "NOT";
                    break;
                }
            } else {
                anagram_str = "NOT";
                break;
            }
        }
    }
    println!("{} is {} an anagram of {}", word1, anagram_str, word2);

    let mut isogram_str = "";
    let mut first_char = false;
    let mut first_amount = 0;
    if !hm1.is_empty() {
        for c1 in hm1.iter() {
            if !first_char {
                first_amount = *c1.1;
                first_char = true;
            } else {
                if *c1.1 != first_amount {
                    isogram_str = "NOT";
                }
            }
        }
    }
    println!("{} is {} an isogram", word1, isogram_str);

    isogram_str = "";
    first_char = false;
    first_amount = 0;
    if !hm2.is_empty() {
        for c2 in hm2.iter() {
            if !first_char {
                first_amount = *c2.1;
                first_char = true;
            } else {
                if *c2.1 != first_amount {
                    isogram_str = "NOT";
                }
            }
        }
    }
    println!("{} is {} an isogram", word2, isogram_str);
}

fn main() {
    let mut string1 = String::new();
    let mut string2 = String::from("Hello world");

    println!("string1 capacity {}", string1.capacity());
    println!("string1 length {}", string1.len());
    println!("string1 is empty {}", string1.is_empty());
    println!("string2 capacity {}", string2.capacity());
    println!("string2 length {}", string2.len());
    println!("string2 is empty {}", string2.is_empty());
    string2.clear();
    println!("string2 capacity {}", string2.capacity());
    println!("string2 length {}", string2.len());
    println!("string2 is empty {}", string2.is_empty());

    string2 = String::from("Bye Bye World");
    string1 = string2.split_off(4);
    println!("{string1}");
    println!("{string2}");

    string2.push('x');
    string2.push_str("John");
    println!("{string2}");
    println!("bytes: {:?}", string2.clone().into_bytes());

    string2.truncate(4);
    println!("{string2}");
    string2.remove(1);
    println!("{string2}");
    println!("pop: {}", string2.pop().unwrap());
    println!("pop: {}", string2.pop().unwrap());
    println!("pop: {}", string2.pop().unwrap());
    println!("final length: {}", string2.len());

    for c in string1.chars() {
        println!("string1 char={}", c);
    }

    if string1.contains("Bye") {
        println!("Bye found!");
    }

    string1.make_ascii_uppercase();
    println!("{string1}");
    string1.make_ascii_lowercase();
    println!("{string1}");
    string2 = string1.replace("bye", "hello");
    println!("{string2}");
    let pos = string2.find("world");
    if let Some(p) = pos {
        println!("world found in char {}", p);
    } else {
        println!("world not found");
    }

    let string3 = String::from("Today is ");
    println!("{string3}");
    println!("concat: {}", string3 + "sunny");
    string1 = format!("Tomorrow will be {} with {} degrees", "cloudy", 19);
    println!("{string1}");
    let string1_rev: String = string1.chars().rev().collect();
    println!("reverse: {}", string1_rev);
    println!("slice: {}", &string1[0..23]);

    if string1.starts_with("Tomorrow") {
        println!("string1 starts with Tomorrow");
    }

    if string1.ends_with("degrees") {
        println!("string1 ends with degrees");
    }

    check_words(&String::from("kayak"), &String::from("Racecar"));
    check_words(&String::from("listen"), &String::from("SiLent"));
}
