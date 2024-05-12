/*
* EXERCISE:
* Explore the concept of exception handling according to your language.
* Force an error in your code, capture the error, print the error
* and prevent the program from stopping unexpectedly.
* Try dividing "10/0" or accessing a non-existent index
* of a list to try to cause an error.
*/

fn main() {
    recoverable_error();
    println!("Program still works");
    let result_error = another_recoverable_err();
    println!("{:?}", result_error);
    println!("Program still works this second time as well.");
    err_handling_clojures();
    println!("Program still works this third time as well.");
    hard_error();
    println!("Program stopped wrking before. This Log wont be Printed!")
}

fn hard_error() {
    panic!("Fire and chaos.")
}

fn recoverable_error() {
    let result = match infinite() {
        Ok(value) => value,
        Err(error) => {
            println!("Error: {}", error);
            0
        }
    };
    println!("{result}")
}

fn infinite() -> Result<i32, String> {
    // I am handling manually the error
    let denominator = 0;
    let result = match denominator {
        0 => Err("Division by zero".to_string()),
        _ => Ok(10 / denominator),
    };
    result
}

fn another_recoverable_err() -> Result<(), String> {
    let greeting_file = infinite()?;
    println!("{:?}", greeting_file);
    Ok(())
}

fn err_handling_clojures() {
    let greeting_file = infinite().unwrap_or_else(|error| {
        if error.to_string() == "Division by zero" {
            println!("I break softly:: {}", error.to_string());
            return 0;
        } else {
            println!("It Worked! : {:?}", infinite());
            return 0;
        }
    });

    println!("{greeting_file}")
}

/* EXTRA DIFFICULTY (optional):
* Create a function that can process parameters, but also
* can throw 3 different types of exceptions (one of them has to
* correspond to a custom exception type created by us
* manually) in case of an error.
* Capture all exceptions from where you call the function.
* Print the type of error.
* Print if no error has occurred.
* Print that execution has finished.
*/

fn parameter_processor(x: i32, y: i32) -> Result<i32, String> {
    if y < 1 {
        panic!("This can't be possible")
    }

    let x_must_be_bigger =x_is_Smaller(x,y)? ;

    let division = match x {
        0 => Err("Please, Divide for a bigger number".to_string()),
        _ => Ok(x / y),
    };

    println!("tis Worked Fine {:?}", division);
    return division;
}

fn x_is_Smaller(x: i32, y: i32) -> Result<bool, String> {
    let result = match x > y {
        false => Err("Sorry, x is smaller!".to_string()),
        _ => Ok(true),
    };
    result
}
