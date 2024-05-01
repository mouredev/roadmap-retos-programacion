/*EXERCISE:
* Provide examples of variable assignment "by value" and "by reference" based on their data type.
* Demonstrate functions with variables passed "by value" and "by reference," and how they behave when modified in each case.
(Understanding these concepts is essential in the majority of programming languages)
*/

fn main() {
    // ================= Assignment by Value: =================
    //  When a variable is assigned by value, the actual value is copied from one variable to another.
    // Ownership of the value is transferred.
    let x = 42; // x is an integer
    let _y = x; // y receives a copy of the value in x

    // ================= Assignment by Reference (Borrowing): =================
    //When a variable is assigned by reference, we create a reference (or borrow) to the original value.
    // The original value remains owned by the original variable. References are denoted by the & symbol.
    let s1 = String::from("hello");
    let _len = calculate_length(&s1); // The &s1 syntax creates a reference to the value of s1 without taking ownership.

    fn calculate_length(s: &String) -> usize {
        // calculate_length takes a reference to a String as its parameter (&String).
        s.len()
        // The value pointed to by the reference (s) is not dropped when the reference goes out of scope.
    }

    // ================= Modifying Borrowed Values: =================
    // When modifying a borrowed value, Rust enforces strict rules
    // 1. Immutable Borrow: If a value is borrowed immutably (using &), it cannot be modified.
    // 2. Mutable Borrow: If a value is borrowed mutably (using &mut), it can be modified.

    let mut str = String::from("hello");

    modify_string(&mut str);
    fn modify_string(s: &mut String) {
        //  takes a mutable reference (&mut String).
        s.push_str(", world!"); // We can modify the borrowed s by appending “, world!” to it.
    }
    // The original str is updated after the function call.
    println!("{str}");

    // ================= Lifetime Parameters: =================
    // Rust uses lifetimes to manage memory safety and ensure that references remain valid.
    // When you see 'a in a function signature or struct definition, it indicates that the function or struct is generic over a specific lifetime.
    // You can annotate references with lifetimes using the 'a syntax. For example, &'a str denotes a reference to a string with a lifetime 'a.
    // Person has a lifetime parameter 'a, indicating that the name field must live at least as long as 'a
    struct _Person<'a> {
        name: &'a str,
    }

    /*EXTRA CHALLENGE (optional):
Create two programs that receive two parameters each, defined as previously assigned variables.
* In one case, the programs receive two parameters by value, and in the other case, by reference.
* Inside the programs, swap the values of these parameters, return them, and assign the returned values to 
* two different variables from the originals.
* Finally, print the values of the original variables and the new ones, verifying that the values have been inverted in the latter.
* Also, confirm that the original values are preserved in the former.
*/

    let value1 = String::from("Value1");
    let value2 = String::from("Value2");

    let (value_changed1, value_changed2) = swap_by_value(value1, value2);

    // println!("Original value1: {}", value1); // Because the reference is lost affter sending it to the function, is no longer accessible
    // println!("Original value2: {}", value2); // Because the reference is lost affter sending it to the function, is no longer accessible
    println!("Swapped value1: {}", value_changed1); // Should print "Value2"
    println!("Swapped value2: {}", value_changed2); // Should print "Value1"

    let reference1 = String::from("Reference1");
    let reference2 = String::from("Reference2");
    let (new_reference1, new_reference2) = swap_by_reference(&reference1, &reference2);

    println!("Original reference1: {}", reference1);
    println!("Original reference2: {}", reference2);
    println!("Swapped reference1: {}", new_reference1); // Should print "eference2"
    println!("Swapped reference2: {}", new_reference2); // Should print "reference1"

    fn swap_by_value(mut str1: String, mut str2: String) -> (String, String) {
        let temporal = str1.clone();
        str1.clear(); // Clear str1
        str1.push_str(&str2); // Assign str2 to str1
        str2.clear(); // Clear str2
        str2.push_str(&temporal); // Assign the clone of str1 (temporal) to str2

        (str1, str2)
    }

    // 'a represents a lifetime parameter. It indicates that the function or struct is generic over a specific lifetime.
    // For example, &'a str denotes a reference to a string with a lifetime 'a.
    fn swap_by_reference<'a>(str1: &'a str, str2: &'a str) -> (&'a str, &'a str) {
        (str2, str1)
    }
}
