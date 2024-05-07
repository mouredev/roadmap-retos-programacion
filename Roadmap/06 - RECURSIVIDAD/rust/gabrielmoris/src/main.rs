/*
 * EXERCISE:
 * Understand the concept of recursion by creating a recursive function that
 * prints numbers from 100 to 0.
 *
 * EXTRA DIFFICULTY (optional):
 * Use the concept of recursion to:
 * - Calculate the factorial of a specific number (the function receives that number).
 * - Calculate the value of a specific element (according to its position) in the
 *   Fibonacci sequence (the function receives the position).
 */

fn main() {
    let mut n = 1;

    fn print_recursive(num: &mut i32) {
        if *num > 100 {
            return;
        }

        println!("{}", *num);

        let mut new_num = *num + 1;
        print_recursive(&mut new_num);
    }
    print_recursive(&mut n);
    let fac = factorial(4);
    println!("Factorial of 4 = {fac}");

    let fibo = fibonacci_possition(13);
    println!("Fibonacci position of 13 = {fibo}"); // should be 7
}

fn factorial(n: i32) -> i32 {
    if n == 0 {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

fn fibonacci_possition(n: u32) -> u32 {
    let mut position: u32 = 0;
    let fibonacci_calc = fibonacci(&position);

    if fibonacci_calc == n {
        return position;
    }

    while fibonacci_calc != n {
        position = position + 1;
        fibonacci(&position);
    }

    return position;
}

fn fibonacci(n: &u32) -> u32 {
    match n {
        0 => 1,
        1 => 1,
        _ => fibonacci_possition(n - 1) + fibonacci_possition(n - 2),
    }
}
