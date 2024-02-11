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


 fn main() {
    // Operadores Aritméticos
    let suma = 5 + 3; // 8
    let resta = 5 - 3; // 2
    let multiplicacion = 5 * 3; // 15
    let division = 5 / 3; // 1
    let modulo = 5 % 3; // 2

    // Operadores Lógicos
    let verdadero = true;
    let falso = false;

    // Operadores de Comparación
    let igual = 5 == 3; // false
    let no_igual = 5 != 3; // true
    let mayor_que = 5 > 3; // true
    let menor_que = 5 < 3; // false
    let mayor_o_igual = 5 >= 3; // true
    let menor_o_igual = 5 <= 3; // false

    // Operadores de Asignación
    let mut valor = 5;
    valor += 2; // 7
    valor -= 1; // 6
    valor *= 2; // 12
    valor /= 3; // 4
    valor %= 2; // 0

    // Operadores de Bit
    let bit_and = 5 & 3; // 1
    let bit_or = 5 | 3; // 7
    let bit_xor = 5 ^ 3; // 6
    let desplazamiento_izquierda = 1 << 2; // 4
    let desplazamiento_derecha = 8 >> 1; // 4

    // Estructuras de Control
    // Condicionales
    if suma > 5 {
        println!("Suma es mayor que 5");
    } else if suma < 5 {
        println!("Suma es menor que 5");
    } else {
        println!("Suma es 5");
    }

    // Iterativas: loop, while, for
    let mut contador = 0;
    loop {
        if contador >= 3 { break; }
        contador += 1;
    }

    while contador > 0 {
        contador -= 1;
    }

    for i in 0..3 {
        println!("Valor de i: {}", i);
    }

    // Manejo de Errores
    let resultado: Result<i32, &str> = Ok(10);
    match resultado {
        Ok(valor) => println!("Resultado exitoso: {}", valor),
        Err(e) => println!("Error: {}", e),
    }

    let opcion: Option<i32> = Some(5);
    match opcion {
        Some(valor) => println!("Tenemos un valor: {}", valor),
        None => println!("No hay valor"),
    }
    
    /* Crea un programa que imprima por consola todos los números comprendidos
     entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */
    
    ejercicioExtra();
    
}

fn ejercicioExtra() {
    /* Crea un programa que imprima por consola todos los números comprendidos
     entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */
    for i in 10..56 {
        if i % 2 == 0 && i != 16 && i % 3 != 0 {
            println!("{}", i);
        }
    }
}