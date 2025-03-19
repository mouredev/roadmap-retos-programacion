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
*/

fn main(){
    /*
        OPERADORES
    */
    
    // Operadores de asignación
    let numero1: i32 = 10;
    let numero2: i32 = 2;
    let mut numero3: i32 = 10;
    numero3 += 5;
    numero3 -= 5;
    numero3 *= 5;
    numero3 /= 5;
    numero3 %= 2;
    println!("El resultado final es {}", numero3);
    
    
    // Operadores aritméticos
    let suma: i32 = numero1 + numero2;
    let resta: i32 = numero1 - numero2;
    let multiplicacion: i32 = numero1 * numero2;
    let division: i32 = numero1 / numero2;
    let modulo: i32 = numero1 % numero2;

    println!("La suma de 10 + 2 = {suma}" );
    println!("La resta de 10 - 2 = {resta}");
    println!("La multiplicación de 10 * 2 = {multiplicacion}");
    println!("La division de 10 / 2 = {division}");
    println!("El modulo de 10 y 2 = {modulo}");

    // Operadores de comparación
    let igualdad: bool = 10 == 10;
    let desigualdad: bool = 23 != 24;
    let mayor_que: bool = 10 > 5;
    let mayor_o_igual_que: bool = 10 >= 10;
    let menor_que: bool = 80 < 69;
    let menor_o_igual_que: bool = 49 <= 50;

    println!("Igualdad de 10 == 10 es {}", igualdad);
    println!("23 es diferente de 24: {}", desigualdad);
    println!("10 es mayor que 5 {}", mayor_que);
    println!("10 es mas grande o igual a 10: {}", mayor_o_igual_que);
    println!("80 es menor a 69: {}", menor_que);
    println!("49 es menor o igual a 50: {}", menor_o_igual_que);

    // Operadores lógicos
    let my_or: bool = 10 == 10 || 3 > 1;
    let my_and: bool = 5 > 6 && 1 == 1;
    let my_not: bool = !(5 > 1);

    println!("10 == 10 || 3 > 1 es {}", my_or);
    println!("5 > 6 && 1 == 1 es {}", my_and);
    println!("!(5 > 1) es {}", my_not);

    // Operadores de pertenencia
    let usuario: &str = "Troleomotor10";
    println!("La letra O aparece en el nombre de usuario {}", usuario.contains('o'));

    // Operadores de bit
    let j = 1010;
    let k = 0011;
    
    let bit_and = j & k;
    let bit_or = j | k;
    let bit_xor = j ^ k;
    let bit_not = !k;
    let bit_move_right = j >> 1;
    let bit_move_left = j << 1;

    println!("j & k = {}", bit_and);
    println!("j | k = {}", bit_or);
    println!("j ^ k = {}", bit_xor);
    println!("!k = {}", bit_not);
    println!("j >> 1 = {}", bit_move_right);
    println!("j << 1 = {}", bit_move_left);

    /*
        ESTRUCTURAS DE CONTROL
    */

    // Condicionales
    // if
    if numero1 == numero2 {
        println!("Son el mismo numero!")
    }
    // if else
    if numero1 == numero2 {
        println!("Son el mismo numero!")
    } else {
        println!("Son números diferentes!")
    }
    // if else if else
    if numero1 == numero2 {
        println!("El numero 1 y el numero 2 tienen el mismo valor")
    } else if numero1 > numero2 {
        println!("El numero 1 es mas grande que el numero 2")
    } 
    else {
        println!("El numero 2 es mas grande que el numero 1")
    }
    
    // Iterativas
    // Bucle for
    let lista_notas: [i32; 8] = [4, 7, 10, 8, 2, 8, 8, 9];
    for x in lista_notas {
        println!("{x}");
    }

    // Bucle while
    let mut contador: i32 = 0;
    while contador <= 5 {
        println!("Numero {contador}");
        contador += 1;
    }

    // Control de errores y panic
    panic!("El programa finalizo!");
    
    let data_file = File::open("hello.txt");

    let file_result = match data_file {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file: {:?}", error),
    };
    

    // Ejemplos extra
    let mut contador2: i32 = 10;
    while contador2 <= 55 {
        if (contador2 % 2 == 0) && (contador2 != 16) && (contador2 % 3 != 0) {
            println!("{}", contador2);
        }
        contador2 += 1;
    }
        
}

