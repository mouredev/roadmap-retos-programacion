use std::{thread, time};

fn is_mult3(n: u8) -> bool {
    return n % 3 == 0;
}

fn is_mult5(n: u8) -> bool {
    return n % 5 == 0;
}

fn fn_extra(str1: &str, str2: &str) -> u8 {
    let mut ret = 0;

    println!("Running extra task");

    for n in 1..=100 {
        let mult3: bool = is_mult3(n);
        let mult5: bool = is_mult5(n);

        if mult3 && mult5 {
            println!("{n}: {}", [str1, str2].concat());
        } else if mult5 {
            println!("{n}: {str2}");
        } else if mult3 {
            println!("{n}: {str1}");
        } else {
            println!("{n}");
            ret += 1;
        }
    }

    return ret;
}

fn fn_no_args_no_ret() {
    println!("Function without arguments and without return value");
}

fn fn_no_args_with_ret() -> u8 {
    println!("Function without arguments and with return value");
    return 10;
}

fn fn_single_arg_no_ret(x: u8) {
    println!("Function with a single argument {x} and without return value");
}

fn fn_single_arg_with_ret(x: u8) -> u8 {
    println!("Function with a single argument {x} and with return value {x}");
    return x;
}

fn fn_args_no_ret(x: u8, y: u8) {
    println!("Function with arguments {x} and {y} and without return value");
}

fn fn_args_with_ret(x: u8, y: u8) -> u8 {
    println!(
        "Function with arguments {x} and {y} and with return value {}",
        x + y
    );
    return x + y;
}

fn fn_recursive(counter: u8) {
    println!("{counter}");
    let c = counter - 1;

    if c != 0 {
        fn_recursive(c)
    }
}

fn fn_with_inner_fn() {
    fn my_print(msg: &str) {
        println!("My message is {msg}");
    }

    my_print("Hello world");
}

static GLOBAL: &str = "global-content";

fn fn_with_local_and_global_vars() {
    let local = "local-content";

    println!("Local: {local}, Global: {GLOBAL}");
}

fn main() {
    let nums_printed = fn_extra("hi", "world");
    println!("Nums printed {nums_printed}");

    let r = fn_no_args_no_ret();
    println!("Ret {r:?}");

    let r = fn_no_args_with_ret();
    println!("Ret {r}");

    let r = fn_single_arg_no_ret(99);
    println!("Ret {r:?}");

    let r = fn_single_arg_with_ret(101);
    println!("Ret {r}");

    let r = fn_args_no_ret(10, 20);
    println!("Ret {r:?}");

    let r = fn_args_with_ret(11, 44);
    println!("Ret {r}");

    fn_recursive(15);
    fn_with_inner_fn();

    println!("Global: {GLOBAL}");
    fn_with_local_and_global_vars();

    println!("Time to sleep during 5s... zzzz");
    let five_secs = time::Duration::from_millis(5000);
    thread::sleep(five_secs);
}
