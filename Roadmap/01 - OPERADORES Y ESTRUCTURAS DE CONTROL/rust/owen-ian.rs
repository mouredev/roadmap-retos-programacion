//=========================================
// 01 - OPERADORES Y ESTRUCTURAS DE CONTROL
//=========================================

fn main() {
    // Operadores Aritméticos
    let a: i32 = 10;
    let b: i32 = 3;
    println!("Suma: {}", a + b);
    println!("Resta: {}", a - b);
    println!("Multiplicación: {}", a * b);
    println!("División: {}", a / b);
    println!("Módulo: {}", a % b);
    println!("Exponenciación: {}", a.pow(b));

    // Operadores Relacionales (Comparación)
    println!("Igual a: {}", a == b);
    println!("Diferente de: {}", a != b);
    println!("Menor que: {}", a < b);
    println!("Mayor que: {}", a > b);
    println!("Menor o igual que: {}", a <= b);
    println!("Mayor o igual que: {}", a >= b);
    
    // Operadores Lógicos
    let x = true;
    let y = false;
    println!("AND lógico: {}", x && y);
    println!("OR lógico: {}", x || y);
    println!("NOT lógico: {}", !x);
    
    // Operadores de Bits
    let c: i32 = 2;
    let d: i32 = 3;
    println!("AND binario: {}", c & d);
    println!("OR binario: {}", c | d);
    println!("XOR binario: {}", c ^ d);
    println!("Desplazamiento a la izquierda: {}", c << 1);
    println!("Desplazamiento a la derecha: {}", c >> 1);

    // Operadores de Pertenencia
    let lista = vec![1, 2, 3, 4, 5];
    println!("Pertenece a la lista: {}", lista.contains(&3));
    println!("No pertenece a la lista: {}", !lista.contains(&6));
    
    // Operadores de Asignación
    let mut e: i32 = 5;
    e += 2;
    println!("Suma y asignación: {}", e);
    e -= 2;
    println!("Resta y asignación: {}", e);
    e *= 2;
    println!("Multiplicación y asignación: {}", e);
    e /= 2;
    println!("División y asignación: {}", e);
    e %= 2;
    println!("Resto y asignación: {}", e);
    
    // Operadores de Asignación de Bits
    let mut f: i32 = 2; // 0b0010
    f &= 3; // 0b0011
    println!("AND a nivel de bits y asignación: {}", f); // 0b0010
    f |= 1; // 0b0001
    println!("OR a nivel de bits y asignación: {}", f);  // 0b0011
    f ^= 1; // 0b0001
    println!("XOR a nivel de bits y asignación: {}", f); // 0b0010
    f <<= 1;
    println!("Desplazamiento a la izquierda y asignación: {}", f); // 0b0100
    f >>= 1;
    println!("Desplazamiento a la derecha y asignación: {}", f); // 0b0010
    
    // Otros Operadores
    let vec = vec![1, 2, 3, 4, 5];
    println!("Acceso a miembro: {}", vec[0]);
    let range = 1..5;
    println!("Rango: {:?}", range);
    let range_inclusivo = 1..=5;
    println!("Rango inclusivo: {:?}", range_inclusivo);
    let valor = Some(42);
    println!("Operador de resultado: {:?}", valor.ok_or("Error"));
    
    // Operadores adicionales
    println!("Separador de elementos en listas: {:?}", [1, 2, 3]);
    println!("Terminador de sentencias: semicolon es requerido en Rust");
    println!("Especificador de tipo: let x: i32 = 10");
    println!("Operador de resolución de alcance: Vec::new()");
    println!("Closure: let suma = |a, b| a + b;");
    println!("Patrones de vinculación: let Some(x) = Some(42);");

    // Loop infinito y de uso cotidiano, se ejecuta hasta el break
    let mut i = 0;
    loop {
        if i == 5 {
            break;
        }
        println!("{i}");
        i += 1;
    }
        
    // Loop que ejecuta código mientras una condición sea verdadera
    let mut i = 0;
    while i < 5 {
        println!("{i}");
        i += 1;
    }
        
    // Bucle for que itera sobre un rango
    for i in 0..5 {
        println!("{i}");
    }

    // Loop que permite romper otros bucles internos o externos que sean etiquetados
    let mut a = 0;
    'external: loop {
        a += 1;
        println!("external: {}", a);
        
        let mut b = 0;
        'internal: loop {
            b += 1;
            println!("internal: {}", b);
            if b == 2 {
                break 'internal;
            }
        }
        if a == 3 {
            break 'external;
        }
    }
}
