/*
EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y
"por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
*/

fn main() {
    // Asignación por valor
    let x: u8 = 5;
    let y;
    y = 14;

    println!("x: {}, y: {}", x, y);

    // Asignación por valor a un array
    let mut array: [u8; 5] = [1, 2, 3, 4, 5];
    println!("array: {:?}", array);
    array[0] = 4;
    println!("array1: {:?}", array);

    // Asignación por referencia
    let mut z = 2;
    let p = &mut z; // referencia
    let r = *p;
    *p = 4;
    println!("z: {}, r: {}", z, r);

    // Funciones
    /*
    // Una vez que se pasa una variable por referencia, la variable original no se puede usar más.
    // Lo comento porque no compila
    let mut value = String::from("hello");
    let ref1 = &mut value;
    let ref2 = &mut value;
    println!("{}, {}", ref1, ref2);
    */
    let mut s = String::from("hello");
    up(&mut s);
    println!("{}", s);

    // Extra
    // Funcion por parámetros
    println!("EXTRA");

    let a = 1;
    let b = 2;

    fn swap_v(a: i32, b: i32) -> (i32, i32) {
        (b, a)
    }
    println!("a:{}, b:{}", a, b);
    swap_v(a, b);
    println!("post swap_v\na:{}, b:{}", a, b);

    // Funcion por referencia
    let mut c = 3;
    let mut d = 4;

    fn swap_r(c: &mut i32, d: &mut i32) {
        let temp = *c;
        *c = *d;
        *d = temp;
    }

    println!("\nc:{}, d:{}", c, d);
    swap_r(&mut c, &mut d);
    println!("post swap_r\nc:{}, d:{}", c, d);
}

fn up(s: &mut String) {
    s.make_ascii_uppercase();
}
