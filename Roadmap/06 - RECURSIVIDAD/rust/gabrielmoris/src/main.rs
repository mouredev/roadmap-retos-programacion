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
}
