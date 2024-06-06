
static MYGLOBAL: &str = "global";

fn main() {
    name();
    full_name("my", "lname");
    let mut age: u8 = 20;
    age_addition(&mut age);
    println!("{age}");

    first();
    scope();

    println!("number of times it was a number and not words: {}", exercise("hello", "rust"));
}

/// The function `name` in Rust prints "kodenook" when called.
fn name() {
    println!("kodenook");
}

fn full_name(fname: &str, lname: &str) -> () {
    println!("{fname} {lname}");
}

fn age_addition(age: &mut u8) {
    *age += 5;
}

fn first() -> () {
    println!("First");

    fn second() -> () {
        println!("Second");
    }

    second();
}

fn scope() -> () {
    let local: &str = "local";

    println!("{}", MYGLOBAL);
    println!("{}", local);
}

/*
    Exercise
*/

fn exercise(word1: &str, word2: &str) -> u8 {
    let mut count_numbers: u8 = 0;

    for x in 1..=100 {
        if x % 3 == 0 && x % 5 == 0 {
            println!("{} {}", word1, word2);
        } else if x % 3 == 0 {
            println!("{word1}");
        } else if x % 5 == 0 {
            println!("{word2}")
        } else {
            count_numbers += 1;
        }
    }

    return count_numbers;
}
