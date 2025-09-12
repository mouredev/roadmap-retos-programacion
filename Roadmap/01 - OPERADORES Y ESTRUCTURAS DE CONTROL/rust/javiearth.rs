//=========================================
// 01 - OPERADORES Y ESTRUCTURAS DE CONTROL
//=========================================

fn main(){
    
    println!("EJEMPLO DE TODOS LOS TIPOS DE OPERADORES");
    
    let mut a: u8 = 2;
    let b: u8 = 4;
    let c: u8 = 8;
    
    // Aritmeticos:
    println!("{} + {} = {}", a, b, a + b);
    println!("{} - {} = {}", b, a, b - a);
    println!("{} * {} = {}", a, b, a * b);
    println!("{} / {} = {}", b, a, b / a);
    println!("{} % {} = {}", a, b, a % b);
    
    // Logicos:
    println!("AND: a < b && c > b da {}", a < b && c > b);
    println!("OR: a < b || b > c da {}", a < b || b > c);
    println!("NOT: ! a < b da {}", ! a < b);
    
    // Comparacion:
    println!("{} es distinto de {}, es {}", a, b, a != b );
    println!("{} es igual que {}, es {}", a, b, a == b);
    println!("{} es mayor que {}, es {}", a, b, a > b );
    println!("{} es menor que {}, es {}", a, b, a < b );
    println!("{} es mayor o igual que {}, es {}", a, b, a >= b );
    println!("{} es menor igual de que {}, es {}", a, b, a <= b );
    
    // Asignacion:
    a += 1;
    println!("a += 1, ahora a vale {}", a);
    a -= 1;
    println!("a -= 1, ahora a vale {}", a);
    a *= 2;
    println!("a *= 2, ahora a vale {}", a);
    a /= 2;
    println!("a /= 2, ahora a vale {}", a);
    a %= 2;
    println!("a %= 2, ahora a vale {}", a);

println!("ESTRUCTURAS DE CONTROL");
 
    let mut acdc: u8 = 1;

    println!("LOOP");
    'counting_up: loop {
   
        if acdc < 4 {
        println!("{}", acdc);
        } else if acdc == 4 {
        println!("y {}", acdc);
        } else {
        break 'counting_up;
        }
        acdc = acdc + 1;
    }

    let mut acdc = 1;

    println!("WHILE");
    while acdc <= 4 {
    
        println!("{}", acdc);
        acdc = acdc + 1;
    }

    println!("FOR");
    for acdc in (1..5).rev() {
        println!("{}", acdc);
    }
    println!("FIN");
    
    println!("DIFICULTAD EXTRA");
    for metallica in 10..56 {
        if metallica % 2 == 0 {
            if metallica % 3 == 0 {
                if metallica != 16 {
                    println!("{}", metallica);
                }
            }
        }
    }

}