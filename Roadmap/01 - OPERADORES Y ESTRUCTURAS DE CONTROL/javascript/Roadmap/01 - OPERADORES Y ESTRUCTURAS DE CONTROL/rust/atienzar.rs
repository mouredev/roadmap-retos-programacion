/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
use std::num::ParseIntError;

 fn main() {
    
    // asignar
    let x:i32 = 2;
    let y:i32 = 12;
    let mut z:i32;

    // aritmeticos.
    z = x + y;
    println!("Suma: {}", z);
    z = y - x;
    println!("Resta: {}", z);

    z = y / x;
    println!("Division: {}", z);

    z = y % x;
    println!("Modulo: {}", z);

    z += 2;
    println!("Incrementamos: {}", z);
    z -= 1;
    println!("Decrementamos: {}", z);


    //comparacion

    println!("{} Mayor(>) {} = {}",x,y, x > y);
    println!("{} Menor(<) {} = {}",x,y, x < y);
    println!("{} Igual(=) {} = {}",x,y, x == y);
    println!("{} Distinto(!=) {} = {}",x,y, x != y);
    println!("{} >= {} = {}",x,y, x >= y);
    println!("{} <= {} = {}",x,y, x <= y);

    //logicos

    let a = true;
    let b = false;

    if a && b{
        println!("Operador &&, las 2 verdaderas");
    }else{
        println!("Operador &&, 1 o las dos condiciones son falsas");
    }

    if a || b{        
        println!("Operador ||, 1 o las dos condiciones son verdaderas");
    }else{
        println!("Operador || las 2 son falsas");
    }

    if !a{
        println!("a es falsa");
    }else{
        println!("a es verdadera");
    }


    // operadores binarios

    let a: u8 = 0b1010;
    let b: u8 = 0b1100;

    let result_and = a & b;  // AND binario
    let result_or = a | b;   // OR binario
    let result_xor = a ^ b;  // XOR binario
    let result_shift_left = a << 2;   // Desplazamiento a la izquierda
    let result_shift_right = a >> 3;  // Desplazamiento a la derecha
    let result_not = !a;     // NOT binario

    println!("AND: {:b}", result_and);
    println!("OR: {:b}", result_or);
    println!("XOR: {:b}", result_xor);
    println!("Desplazamiento a la izquierda: {:b}", result_shift_left);
    println!("Desplazamiento a la derecha: {:b}", result_shift_right);
    println!("NOT: {:b}", result_not);


    // distintos tipos de base => binario, decimal, octal y  hexa

    let letra = 'A';
    let valor_numerico = letra as u8;

    println!("Carácter original: {}", letra);
    println!("Valor decimal: {}", valor_numerico);
    println!("Valor hexadecimal: {:X}", valor_numerico);
    println!("Valor octal: {:o}", valor_numerico);
    println!("Valor binario: {:b}", valor_numerico);


    // estructuras de control 

    let a:bool = true;

    if  a {
        println!("{} es Verdadero",a)
    }else if !a {
        println!("{} es Falso",a)
    }else{
        println!("Entramos  en el else")
    }

    let mut cont:i32 = 5; 

    while cont > 0{
        println!("Estamos dentro del While! ");
        cont -= 1;
    }
    
    cont = 0;
    loop {
        cont += 1;
        if cont == 5 {
           break;
        }
        println!("Paso {} dentro del loop",cont )
    }

    for n in 1..5{
        println!("Paso {} dentro del for", n);
    }

    let mut listado = vec!["juan", "pedro", "luis"];
    for name in listado.iter_mut(){
        println!("{:?}",name);
    }

    let num:i16 = 4;

    match num {
        1 | 2 | 3 => println!("Menor que cuantro"),
        4 => println!("Cuatro!"),
        5..=10 => println!("Mayor que cuatro"), 
        _=> println!("Otra cosa")
    }

    // Excepciones  => panic y Result
    let number_str = "10*";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        //Err(_e) => panic!("Problemas creando el entero: {:?}", _e),
        Err(e) => -1,
    };
    println!("{}", number);

    print_numbers();

}

/*
 Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

fn print_numbers(){
    for num in 10..=55{
        if num % 2 == 0  && num != 16 && num % 3 != 0  {
            println!("{}", num);
        }
    }
}