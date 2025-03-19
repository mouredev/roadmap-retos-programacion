/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* ITERACIONES
-----------------------------------------

* EJERCICIO #1:
* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
* números del 1 al 10 mediante iteración.
*
* EJERCICIO #2:
* Escribe el mayor número de mecanismos que posea tu lenguaje
* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/

fn main() {
    //_____________________________
    println!("(1). for");
    for num in 1..=10 {
        println!("{}", num);
    }
    
    //_____________________________
    println!("\n(2). while");
    let mut num = 1;
    while num <= 10 {
        println!("{}", num);
        num += 1;
    }
    //_____________________________
    println!("\n(3). loop");
    let mut num = 1;
    loop {
        println!("{}", num);
        num += 1;
        if num > 10 {
            break;
        }
    }

    //_____________________________
    println!("\n(4). Método iter()");
    let numbers = vec![1, 2, 3, 4, 5];
    for num in numbers.iter() {
        println!("{}", num);
    }

    //_____________________________
    println!("\n(5). Método iter_mut()");
    // Devuelve un iterador mutable que permite modificar los elementos.
    let mut numbers = vec![1, 2, 3, 4, 5];
    for num in numbers.iter_mut() {
        *num *= 2;
        println!("{}", num);
    }

    //_____________________________
    println!("\n(6). Método filter()");
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8];
    for num in numbers.iter().filter(|&x| *x % 2 == 0) {
        println!("{}", num);
    }

    //_____________________________
    println!("\n(6). Método zip()");
    let numbers = vec![1, 2, 3];
    let letters = vec!['a', 'b', 'c'];
    for (num, letter) in numbers.iter().zip(&letters) {
        println!("Number: {}, Letter: {}", num, letter);
    }

    //_____________________________
    println!("\n(7). Método enumerate()");
    let numbers = vec![1, 2, 3, 4, 5];
    for (index, num) in numbers.iter().enumerate() {
        println!("Index: {}, Value: {}", index, num);
    }

    //_____________________________
    println!("\n(8). Método map()");
    let numbers = vec![1, 2, 3, 4, 5];
    let doubled_numbers: Vec<_> = numbers.iter().map(|&x| x * 2).collect();
    println!("{:?}", doubled_numbers);

}
