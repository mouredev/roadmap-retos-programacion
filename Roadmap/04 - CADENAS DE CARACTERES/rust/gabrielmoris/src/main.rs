/*
 * EXERCISE:
 * Show examples of all the operations you can perform with strings in your language.
 * Some of these operations might include (search for as many as you can):
 * - Accessing specific characters, substrings, length, concatenation, repetition,
 *   traversal, converting to uppercase and lowercase, replacement, splitting, joining,
 *   interpolation, verification...
 *
 * EXTRA CHALLENGE (optional):
 * Create a program that analyzes two different words and checks whether they are:
 * - Palindromes
 * - Anagrams
 * - Isograms
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
    // PUSH

    str_to_reverse.push_str("World");

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
}
