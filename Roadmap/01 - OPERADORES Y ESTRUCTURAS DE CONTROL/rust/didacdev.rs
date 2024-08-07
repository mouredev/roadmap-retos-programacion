// https://doc.rust-lang.org/book/appendix-02-operators.html
// https://doc.rust-lang.org/book/ch03-05-control-flow.html


fn print_numbers() {

    for number in 10..=55{

        if number % 2 == 0 {
            if !(number != 16 && number % 3 == 0) {
                println!("{}", number);
            }
        }
    }
}

fn main() {

    // Igualdad
    // println!("{}", 1 == 1);
    // println!("{}", 1 != 1);
    // println!("{}", 1 > 1);
    // println!("{}", 1 < 1);
    // println!("{}", 1 <= 1);
    // println!("{}", 1 >= 1);

    // Aritméticos
    // println!("{}", 2 % 2);
    // println!("{}", 2 * 2);
    // println!("{}", 2 + 2);
    // println!("{}", 2 - 2);
    // println!("{}", 2 / 2);

    // Lógicos
    // println!("{}", true && false);
    // println!("{}", true || false);

    // Condicional
    /*if 5 > 0 {
        println!("5 es mayor que 0");
    } else if 5 == 0{
        println!("5 es igual que 0");
    } else {
        println!("5 es menor que 0");
    }*/

    // let _number = if true { 5 } else { 0 };

    /*match _number {
        1 => println!("{}", 1),
        5 => println!("{}", 5),
        _ => println!("Resto"),
    }*/

    // loops
    // let mut number = 0;
    /*loop {
        println!("Hello Rust!");
        number += 1;

        if number == 2 {
            break;
        }
    }*/

    /*'first_loop: loop {
        let mut loops = 0;

        'second_loop: loop {
            loops += 1;
            println!("2");

            if loops == 2 {
                break 'second_loop;
            }
        }

        break 'first_loop;
    }*/

    /*while number != 0 {
        println!("{}", number);
        number -= 1;
    }*/

    // let a = [1, 2, 3, 4];
    /*for number in a {
        println!("{number}");
    }*/

    /*for number in 1..4{
        println!("{number}")
    }*/

    /*for number in (1..4).rev(){
        println!("{number}")
    }*/

    print_numbers();
}