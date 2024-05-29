/*
 * EXERCISE:
 * Show examples of all the operations you can perform with strings in your language.
 * Some of these operations might include (search for as many as you can):
 * - Accessing specific characters, substrings, length, concatenation, repetition,
 *   traversal, converting to uppercase and lowercase, replacement, splitting, joining,
 *   interpolation, verification...
 *
 */

fn main() {
    // The two most used string types in Rust are String and &str.
    // A String is stored as a vector of bytes (Vec<u8>), but guaranteed to always be a valid UTF-8 sequence.
    // String is heap allocated, growable and not null terminated.
    // &str is a slice (&[u8]) that always points to a valid UTF-8 sequence,
    // and can be used to view into a String, just like &[T] is a view into Vec<T>.

    // CREATION
    let mut reversed: String = String::new();
    let str: &str = "Hello";
    let mut str_to_reverse: String = String::new();

    // ACCESS
    let third_character = str.chars().nth(2);
    assert_eq!(third_character, Some('l'));

    // PUSH
    str_to_reverse.push_str("World!!");

    // POP
    str_to_reverse.pop();

    // INSERT

    str_to_reverse.insert_str(5, "!!");

    // SPLIT
    let chars: Vec<_> = str_to_reverse.split("").collect();

    // ITERATION
    for word in chars.iter().rev() {
        reversed.push_str(word);
    }

    // CONCATENATION

    let weird = format!("{} {}", str, reversed);
    println!("Concatenated: {weird}");

    // SLICE
    let sliced = &weird[0..5];
    println!("Sliced: {sliced}");

    // REPLACING
    let say = String::from("I like dogs");
    let replace = say.replace("dog", "cat");
    println!("He says: {}", replace);

    // TRIMMING
    let string = String::from("   Hello, world!   ");
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("Trimmed: {}", trimmed_str);
    let string2 = String::from("         WHAT!!?      ");
    let trimmed = string2.trim();
    println!("Trimmed: {}", trimmed);

    // VIWEW INTO A STRING: The &str type allows you to view into a String without copying data
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    for word in pangram.split_whitespace() {
        println!("Word: {}", word);
    }

    challenge("a".to_owned(), "almendro".to_owned());
    challenge("manam".to_owned(), "maman".to_owned());
}

/*
 * EXTRA CHALLENGE (optional):
 * Create a program that analyzes two different words and checks whether they are:
 * - Palindromes
 * - Anagrams
 * - Isograms
 */

fn reverse_string(input: String) -> String {
    let mut input1_reversed = String::new();
    let chars: Vec<_> = input.split("").collect();
    for word in chars.iter().rev() {
        input1_reversed.push_str(word);
    }
    return input1_reversed;
}

fn sort_string(input: String) -> String {
    let sliced_str = &input[..];
    let mut chars: Vec<char> = sliced_str.chars().collect();
    chars.sort_by(|a, b| b.cmp(a));

    return String::from_iter(chars);
}

fn is_isogram(s: &str) -> bool {
    let mut sorted_chars: Vec<char> = s.chars().collect();
    sorted_chars.sort_by(|a, b| a.to_ascii_lowercase().cmp(&b.to_ascii_lowercase()));

    for i in 0..sorted_chars.len() - 1 {
        if sorted_chars[i] == sorted_chars[i + 1] {
            return false;
        }
    }

    true
}

fn challenge(input1: String, input2: String) {
    let cloned_input1 = input1.clone();
    let cloned_input2 = input2.clone();
    let reversed_input1 = reverse_string(input1);
    let reversed_input2 = reverse_string(input2);

    if reversed_input1 == cloned_input1 {
        println!("{cloned_input1} is a Palindrome.");
    }
    if reversed_input2 == cloned_input2 {
        println!("{cloned_input2} is a Palindrome.");
    }

    let recloned_input1 = cloned_input1.clone();
    let recloned_input2 = cloned_input2.clone();
    let sorted_str1 = sort_string(cloned_input1);
    let sorted_str2 = sort_string(cloned_input2);

    if sorted_str1 == sorted_str2 {
        println!("{recloned_input1} and {recloned_input2} are Anagrams");
    }

    let is_str1_isogram = is_isogram(&recloned_input1);
    let is_str2_isogram = is_isogram(&recloned_input2);

    if is_str1_isogram {
        println!("{recloned_input1} is a Isogram");
    }
    if is_str2_isogram {
        println!("{recloned_input2} is a Isogram")
    }
}
