/*
Operators
*/

fn main(){
    println!("Aritmetic operators");
// Aritmetic operators
    println!("Suma: {}",1+20);
    println!("Resta: {}",1-20);
    println!("Multiplicación: {}",2*20);
    println!("División (flotante): {}",10.0/3.0);
    println!("Division entera: {}", 10/3);
    println!("Módulo: {}",10%3);
    println!("Potencia: {}",1_i32.pow(10));
    println!("Raíz cuadrada: {}",4.0_f64.sqrt());

    println!("\nLogical operators");
// Logical operators
    println!("AND: {}",true && false);
    println!("OR: {}",true || false);
    println!("NOT: {}",!true);

    println!("\nRelational operators");
// Relational operators
    println!("Equality: {}",1==1);
    println!("Nonequality comparison: {}",1!=1);
    println!("Greater than comparison: {}",1>2);
    println!("Less than comparison: {}",1<2);

    println!("\nBitwise operators");
// Bitwise operators
    println!("AND: {}",0b1010 & 0b1100);
    println!("OR: {}",0b1010 | 0b1100);
    println!("XOR: {}",0b1010 ^ 0b1100);
    println!("Left-shift: {}",0b1010 << 2);
    println!("Right-shift: {}",0b1010 >> 2);
    println!("Complement: {}",!0b1010);

    println!("\nAssignment operators");
// Assignment operators
    let mut a = 10;
    a += 10;
    println!("Addition assignment: {}",a);
    a -= 10;
    println!("Subtraction assignment: {}",a);
    a *= 10;
    println!("Multiplication assignment: {}",a);
    a /= 10;
    println!("Division assignment: {}",a);
    a %= 10;
    println!("Modulo assignment: {}",a);
    a &= 10;
    println!("AND assignment: {}",a);
    a |= 10;
    println!("OR assignment: {}",a);
    
    println!("\nTeranary operator");
// Ternary operator
    let a = 10;
    let b = 20;
    let c = if a > b {a} else {b};
    println!("Ternary operator: {}",c);

    println!("\nMembership operator");
// Membership operator
    let nums = vec![1, 2, 3, 4, 5];
    let num_to_check = 3;
    println!("Member?: {}", nums.contains(&num_to_check));

    println!("\nControl structures");
// Control structures

    println!("\nIf else");
    // if else
    let number = 42;
    if number > 30 {
        println!("The number is greater than 30");
    } else {
        println!("The number is less than or equal to 30");
    }

    println!("\nfor in");
    // for in
//  for num in 10..55  10 to 54
    for num in 10..=55 { // 10 to 55 inclusive
        if num % 2 == 0 && num != 16 && num % 3 != 0 {
            println!("{}", num);
        }
    }

    println!("\nLoop");
    // Infinite loop
    let mut count = 0u32;
    loop {
        count += 1;
        if count == 3 {
            println!("three");
            // Skip the rest of this iteration
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("OK, that's enough");
            // Exit this loop
            break;
        }
    }

    println!("\nWhile");
    // while loop
    let mut n = 1;
    while n < 20 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
        // Increment counter
        n += 1;
    }

    println!("\nMatch(Switch)");
    // match (Switch case in other languages)
    let number = 11;
    println!("Tell me about {}", number);
    match number {
        // Match a single value
        1 => println!("One!"),
        // Match several values
        2 | 3 | 5 | 7 | 11 => println!("This is a prime"),
        // Match an inclusive range
        13..=19 => println!("A teen"),
        // Handle the rest of cases
        _ => println!("Ain't special"),
    }

    println!("\n");
    extra();

}

fn extra(){
    println!("Extra");
    for num in 10..=55 {
        if num % 2 == 0 && num != 16 && num % 3 != 0 {
            println!("{}", num);
        }
    }
}