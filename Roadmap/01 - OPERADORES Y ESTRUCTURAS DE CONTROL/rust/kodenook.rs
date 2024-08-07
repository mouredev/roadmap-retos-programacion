fn main() {
    /*
        Arithmetic Operators
    */

    println!("Arithmetic Operators");
    println!("2 + 2 = {}", 2 + 2);
    println!("2 - 2 = {}", 2 - 2);
    println!("2 * 2 = {}", 2 * 2);
    println!("2 / 2 = {}", 2 / 2);
    println!("2 % 2 = {}", 2 % 2);

    /*
        Bitwise Operators
    */

    println!("Bitwise Operators");
    println!("&: 5 & 2 = {}", 5 & 2);
	println!("|: 5 | 2 = {}", 5 | 2);
	println!("^: 5 ^ 2 = {}", 5 ^ 2);
	println!(">>: 5 >> 2 = {}", 5 >> 2);
	println!("<<: 5 << 2 = {}", 5 << 2);

    /*
        Assignment Operators
    */

    println!("Assignment Operators");
    println!("x = 5");
    println!("x += 5, x = x + 5");
    println!("x -= 5, x = x - 5");
    println!("x *= 5, x = x * 5");
    println!("x /= 5, x = x / 5");
    println!("x ~/= 5, x = x ~/ 5");
    println!("x %= 5, x = x % 5");
    println!("x &= 5, x = x & 5");
    println!("x |= 5, x = x | 5");
    println!("x ^= 5, x = x ^ 5");
    println!("x >>= 5, x = x >> 5");
    println!("x <<= 5, x = x << 5");
    println!("x >>>= 5, x = x >>> 5");

    /*
        Comparison Operators
    */

    println!("Comparison Operators");
    println!("Equal to 4 == 5, {}", 4 == 5);
    println!("Not Equal to 4 != 5, {}", 4 != 5);
    println!("Grater Than 4 > 5, {}", 4 > 5);
    println!("Less Than 4 < 5, {}", 4<= 5);
    println!("Grater Than Or Equal to 4 >= 5, {}", 4 >= 5);
    println!("Less Than Or Equal to 4 <= 5, {}", 4 <= 5);

    /*
        Logical Operators
    */

    println!("Logical Operators");
    println!("&&, 3 < 5 && 3 < 10, {}", 3 < 5 && 3 < 10);
    println!("||, 3 < 5 || 3 < 10, {}", 3 < 5 || 3 < 10);
    println!("!, !(4 < 5), {}", !(4 < 5));

    /*
        If
    */

    if 6 > 5 {
        println!("6 is grater than 5");
    } else if 5 < 6 {
        println!("5 is less than 6");
    } else {
        println!("Good Bye");
    }

    /*
        Loop
    */

    let mut _idx: u8 = 0;

    loop {
        println!("{_idx}");
        _idx += 1;
        if _idx == 5 {
            break;
        }
    }

    /*
        While
    */

    while _idx > 0 {
        println!("{_idx}");
        _idx -= 1;
    }

    /*
        For
    */

    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }

    /*
        Exercise
    */

    for element in 10..56 {
        if element % 2 != 0 || element % 2 != 0 || element == 16 {
            continue;
        }

        println!("{element}")
    }
}