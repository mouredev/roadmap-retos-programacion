use std::fs::File;

/*
 * Function to print the numbers between 10 and 55 that are even and are not multiple of 16 and 3.
 */
fn extra_fn() {
    for n in 10..=55 {
        let is_even = n % 2 == 0;
        let is_mult16 = n % 16 == 0;
        let is_mult3 = n % 3 == 0;
        if is_even && !is_mult16 && !is_mult3 {
            println!("{n}, (n % 2 = {}, n % 16 = {}, n % 3 = {})", is_even, is_mult16, is_mult3);
        }
    }
}

fn main() {
    println!("====================");
    println!("0. Extra task");
    println!("====================");
    extra_fn();

    println!("====================");
    println!("1. Arimetic operators");
    println!("====================");

    let num1 = 10;
    let num2 = 40;
    let mut res;

    res = num1 + num2;
    println!("{num1} + {num2} = {res}");

    res += 15;
    println!("+= 15 = {res}");

    res = num1 - num2;
    println!("{num1} - {num2} = {res}");

    res -= 3;
    println!("-= 3 = {res}");

    res = num1 * num2;
    println!("{num1} * {num2} = {res}");

    res *= 5;
    println!("*= 5 = {res}");

    res = num1 % num2;
    println!("{num1} % {num2} = {res}");

    res %= 6;
    println!("%= 6 = {res}");

    let num1 = 1.5;
    let num2 = 3.4;
    let mut res;
    res = num1 / num2;
    println!("{num1} / {num2} = {res}");

    res /= 2.5;
    println!("/= 2.5 = {res}");

    println!("====================");
    println!("2. Boolean operators");
    println!("====================");
    let cond1 = true;
    let cond2 = false;
    let mut cond_res;

    cond_res = !cond1;
    println!("!{cond1} = {cond_res}");

    cond_res = cond1 && cond2;
    println!("{cond1} && {cond2} = {cond_res}");

    cond_res = cond1 || cond2;
    println!("{cond1} || {cond2} = {cond_res}");

    cond_res = cond1 == cond2;
    println!("{cond1} == {cond2} = {cond_res}");

    cond_res = cond1 != cond2;
    println!("{cond1} != {cond2} = {cond_res}");

    cond_res = num1 < num2;
    println!("{num1} < {num2} = {cond_res}");

    cond_res = num2 > num1;
    println!("{num2} > {num1} = {cond_res}");

    cond_res = num1 >= num2;
    println!("{num1} >= {num2} = {cond_res}");

    cond_res = num2 <= num1;
    println!("{num2} <= {num1} = {cond_res}");

    println!("====================");
    println!("3. Range operators");
    println!("====================");
    let range = 2..9;
    println!("Range {range:?}");
    for r in range {
        println!("{r}");
    }
    let range = 3..=8;
    println!("Range {range:?}");
    for r in range {
        println!("{r}");
    }

    println!("====================");
    println!("4. Bitwise operators");
    println!("====================");
    let bits1 = 0b1010;
    let bits2 = 0b1100;
    let mut res_bits;

    res_bits = bits1 & bits2;
    println!("{bits1:04b} & {bits2:04b} = {res_bits:04b}");

    res_bits &= 0b0111;
    println!("&= 0b0111 = {res_bits:04b}");

    res_bits = bits1 | bits2;
    println!("{bits1:04b} | {bits2:04b} = {res_bits:04b}");

    res_bits |= 0b0001;
    println!("|= 0b0001 = {res_bits:04b}");

    res_bits = bits1 ^ bits2;
    println!("{bits1:04b} ^ {bits2:04b} = {res_bits:04b}");

    res_bits ^= 0b1100;
    println!("^= 0b1100 = {res_bits:04b}");

    res_bits = bits1 >> 1;
    println!("{bits1:04b} >> 1 = {res_bits:04b}");

    res_bits = bits2 << 2;
    println!("{bits2:04b} << 2 = {res_bits:04b}");

    res_bits >>= 1;
    println!(">>=1 = {res_bits:04b}");

    res_bits <<= 1;
    println!("<<=1 = {res_bits:04b}");

    println!("====================");
    println!("5. Array operators");
    println!("====================");

    let mut array1 = [1,2,3,4,5,6];
    let mut index = 0;

    for a in array1 {
        println!("Element: {a}");
        println!("Array[index={}]: {}",index, array1[index]);
        index +=1;
    }

    array1[2] = 5;
    println!("Array[2]: {}", array1[2]);

    println!("====================");
    println!("6. Control flow");
    println!("====================");

    if cond1 {
        println!("If statement executed");
    } else {
        println!("Else statement executed");
    }

    if ! cond1 {
        println!("If statement executed");
    } else {
        println!("Else statement executed");
    }

    if ! cond1 {
        println!("If statement executed");
    } else if ! cond2 {
        println!("Else if statement executed");
    } else {
        println!("Else statement executed");
    }

    let n1 = 4;

    match n1 {
        0 => println!("Zero"),
        4 => println!("Four"),
        _ => println!("Default case!")
    }

    let mut counter = 0;

    loop {
        if counter == 5 {
            println!("Break the loop!");
            break;
        }

        println!("Loooooping!");
        counter += 1;
    }

    while counter < 10 {
        println!("Inside the while");
        counter += 1;
    }

    for n in 1..=counter {
        println!("{n}");
    }

    println!("====================");
    println!("7. Error handling");
    println!("====================");

    let file_res = File::open("nofile.txt");

    match file_res {
        Ok(file) => println!("The file {file:?} exists"),
        Err(error) => println!("Error opening the file {error}")
    }

    panic!("Unrecoverable error.");
}
