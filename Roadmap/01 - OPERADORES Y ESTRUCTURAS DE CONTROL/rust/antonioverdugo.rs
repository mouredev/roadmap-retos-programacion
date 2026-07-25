fn main() {
    // OPERADORES
    // OPERADORES ARITMETICOS
    let sum = 10 + 3;
    let substract = 34 - 70;
    let multiply = 12.7 * 3.0;
    let division = 23 / 2;
    let module = 20 % 5;

    println!("El operador de suma es + resultado = {sum}");
    println!("El operador de resta es - resultado = {substract}");
    println!("El operador de multiplicacion es * resultado = {multiply}");
    println!("El operador de division es / resultado = {division}");
    println!("El operador de modulo es % resultado = {module}");

    // OPERADORES DE COMPARACION
    let igual = "hola" == "hola";
    let distinto = "hola" != "adios";
    let mayor_que = 34.6 > 10.0;
    let menor_que = 3 < 5;
    let mayor_igual = 5 >= 5;
    let menor_igual = 3 <= 10;
    println!("El operador de igualdad es == resultado = {igual}");
    println!("El operador de desigualdad es != resultado = {distinto}");
    println!("El operador mayor que es > resultado = {mayor_que}");
    println!("El operador menor que es < resultado = {menor_que}");
    println!("El operador mayor o igual que es >= resultado = {mayor_igual}");
    println!("El operador menor o igual que es <= resultado = {menor_igual}");

    // OPERADORES LOGICOS
    let todo = 4 > 7 && 3 < 2;
    let uno = 5 > 10 || 8 < 10;
    let falso = !true;
    println!("El operador AND es && resultado = {todo}");
    println!("El operador OR es || resultado = {uno}");
    println!("El operador NOT es ! resultado = {falso}");

    // OPERADORES DE ASIGNACION
    let mut asign = 12;
    asign += 10;
    asign -= 5;
    asign *= 3;
    asign /= 3;
    asign %= 3;

    println!(
        "El operador de asignacion es = y todas las variaciones añadiendo los operadores aritmeticos\nEl valor de asign = {asign}"
    );

    // ESTRUCTURAS DE CONTROL
    // BUCLES
    let mut control = 0;
    loop {
        if control > 0 && control % 3 == 0 {
            println!("El número {control} es divisible entre 3");
            break;
        }
        control += 1;
    }
    println!("El valor de control = {control}");

    while control <= 10 {
        control += 1;
    }
    println!("El valor de contro = {control}");

    for num in 1..11 {
        println!("{num}");
    }

    // CONDICIONALES
    if control > 11 {
    } else if control < 20 {
        println!("Control es menor de 20");
    } else {
        println!("Control es mayor de 20 o menor o igual a 11");
    }
    match control {
        10 => println!("El valor de control es 10"),
        11 => println!("El valor de control es 11"),
        _ => println!("Es un valor distinto a 10 u 11"),
    }

    // * DIFICULTAD EXTRA (opcional):
    // * Crea un programa que imprima por consola todos los números comprendidos
    // * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

    for num in 10..=55 {
        if num % 2 == 0 && num != 16 && num % 3 != 0 {
            println!("{num}");
        }
    }
}
