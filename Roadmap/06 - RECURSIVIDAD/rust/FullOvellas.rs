use std::collections::HashMap;

fn print_to_100(num: i32) {
    if num <= 100 {
        println!("{}", num);
        print_to_100(num + 1);
    }
}

fn factorial(num: i32) -> i32 {
    if num == 1 {
        return 1;
    }

    num * factorial(num - 1)
}

fn fib_at(n: i32, memo: &mut HashMap<i32, i32>) -> i32 {
    match n {
        0 => 0,
        1 | 2 => 1,
        3.. => {
            (if let Some(num) = memo.get(&(n - 1)) {
                *num
            } else {
                let fib = fib_at(n - 1, memo);
                memo.insert(n - 1, fib);
                fib
            }) + (if let Some(num) = memo.get(&(n - 2)) {
                *num
            } else {
                let fib = fib_at(n - 2, memo);
                memo.insert(n - 2, fib);
                fib
            })
        }
        _ => panic!("Invalid position"),
    }
}

fn main() {
    print_to_100(0);

    println!("{}", factorial(5));

    println!("{}", fib_at(5, &mut HashMap::new()));
}
