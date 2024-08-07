/// #06 RECURSIVIDAD
///
/// `rustc ./Roadmap/06\ -\ RECURSIVIDAD/rust/raulfauli.rs && ./raulfauli && rm raulfauli`
///

fn main() {

    print_numbers(100);

    // Extra
    println!("Factorial 5: {}", factorial(5));
    println!("Fibonacci 10: {}", fibonacci(10));

    // Extra, extra: Con notación científica
    println!("Valor máximo: {:e}", u128::MAX); // 10^38
    println!("Factorial 30: {:e}", factorial(30)); // 10^32
    println!("Fibonacci 150: {:e}", fibonacci_memoization(150)); // 10^31
}

fn print_numbers(n: u32) {
    println!("{n}");

    if n > 0 {
        print_numbers(n - 1);
    }
}

fn factorial(n: u128) -> u128 {
    if n <= 1 {
        return 1;
    }

    if n > 30 {
        panic!("¡Factorial demasiado largo!");
    }

    n * factorial(n - 1)
}

fn fibonacci(n: u64) -> u64 {
    if n <= 1 {
        return n;
    }

    fibonacci(n - 1) + fibonacci(n - 2)
}

fn fibonacci_memoization(n: usize) -> u128 {
    let mut memo: Vec<u128> = vec![0; n + 1];

    fibonacci_memoization_aux(n, &mut memo)
}

fn fibonacci_memoization_aux(n: usize, memo: &mut Vec<u128>) -> u128 {
    if n <= 1 {
        return n as u128;
    }

    if memo[n] == 0 {
        memo[n] = fibonacci_memoization_aux(n - 1, memo) + fibonacci_memoization_aux(n - 2, memo);
    }

    memo[n]
}
