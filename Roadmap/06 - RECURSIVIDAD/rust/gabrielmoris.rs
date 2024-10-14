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

use std::collections::HashMap;

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

    let mut memo = HashMap::new(); // Hashmap to save the recursive answers and save memory.
    let fib = fibonacci(7, &mut memo);
    println!("Fibonacci number in 7th possition = {fib}"); // should be 13

    // Own Challenge: Get the possition of a fibonacci number. Return 0 if it doesn't belong to fibonacci serie.
    let fibo = fibonacci_position(13);
    println!("Fibonacci position of 13 = {fibo}"); // should be 7
}

fn factorial(n: i32) -> i32 {
    if n == 0 {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

fn fibonacci(n: u32, memo: &mut HashMap<u32, u32>) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        n => {
            // Is it not in the memo? save it, otherwise get it from there.
            if !memo.contains_key(&n) {
                let fib_n_minus_1 = fibonacci(n - 1, memo);
                let fib_n_minus_2 = fibonacci(n - 2, memo);
                memo.insert(n, fib_n_minus_1 + fib_n_minus_2);
            }
            *memo.get(&n).unwrap()
        }
    }
}

fn fibonacci_position(n: u32) -> u32 {
    let mut position: u32 = 0;
    let mut memo = HashMap::new(); // Saving the data will allow me to dont fall in a stack overflow.
    let mut fibonacci_calc = fibonacci(position, &mut memo);

    while fibonacci_calc < n {
        position += 1;
        fibonacci_calc = fibonacci(position, &mut memo);
    }

    // I could throw an Error but I decide to return 0 when the number
    // doesn't belong to fibonacci serie.
    if fibonacci_calc != n {
        return 0;
    }

    position
}
