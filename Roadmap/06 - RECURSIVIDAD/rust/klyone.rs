fn fibo(n: u64) -> u64 {
    match n {
        0 => return 0,
        1 => return 1,
        pos => return fibo(pos - 1) + fibo(pos - 2),
    }
}

fn fact(n: u64) -> u64 {
    if n == 0 {
        return 1;
    } else {
        return n * fact(n - 1);
    }
}

fn print_numbers(n: u8) {
    println!("{n}");

    if n > 0 {
        print_numbers(n - 1);
    }
}

fn main() {
    print_numbers(100);
    println!(
        "fact(4): {}, fact(5): {}, fact(10): {}",
        fact(4),
        fact(5),
        fact(10)
    );
    println!(
        "fibo(0): {}, fibo(1): {}, fibo(2): {}, fibo(6): {}, fibo(8): {}",
        fibo(0),
        fibo(1),
        fibo(2),
        fibo(6),
        fibo(8)
    );
}
