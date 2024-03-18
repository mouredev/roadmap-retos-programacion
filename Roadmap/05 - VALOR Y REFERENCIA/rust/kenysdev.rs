// no advertencia
#![allow(unused_variables)]
#![allow(unused_assignments)]
use std::collections::HashSet;
/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* VALOR Y REFERENCIA
-----------------------------------------
- Un valor es simplemente un dato que ocupa un espacio de memoria.
- Los valores pueden ser de dos tipos principales(tipos primitivos y tipos compuestos).
- Los valores son propietarios de su propio espacio de memoria.

- Las referencias son una forma de "prestar" un valor sin transferir la propiedad del mismo.
- Una referencia simplemente "apunta" al valor original en la memoria de ese valor.
- Las referencias pueden ser Mutables o inmutables.
*/
fn main() {
    // _________________________________________________________________
    // * ASIGNAR POR VALOR
    // * Tipos con (trail 'copy') que se copian al asignarse.
    // * Tipos primitivos
    let num: u8 = 12; // ,i->n, u->n
    let assign_num: u8 = num;

    let float: f32 = 12.21; // ,f64
    let assign_float: f32 = float;

    let chr: char = 'a';
    let assign_chr: char = chr;

    let boolean: bool = true;
    let assign_boolean: bool = boolean;
    
    // * Tipos Compuestos
    // * los quee contienen tipos primitivos.
    let tuple: (u8, bool, char) = (num, boolean, chr);
    let assign_tuple: (u8, bool, char) = tuple;

    let array: [u8; 3] = [1, 2, 3];
    let assign_array: [u8; 3] = array;

    // _________________________________________________________________
    // * ASIGNAR EL VALOR MOVIENDO LA PROPIEDAD
    // * Son los tipos que no tienen (trail 'copy').
    // * Despues de moverse, la la variable original ya no sera válida.
    let original_string: String = String::from("Ken");
    let assign_string: String = original_string;
    //println!("{original_string}"); // ya no es valida

    let original_vector: Vec<u8> = vec![1, 2, 3];
    let assign_vector: Vec<u8> = original_vector;
    //println!("{:?}", original_vector); // ya no es valida

    let original_set: HashSet<u8> = vec![1, 2, 3].into_iter().collect();
    let assign_set: HashSet<u8> = original_set;
    //println!("{:?}", original_set); // ya no es valida

    // _________________________________________________________________
    // * ASIGNAR POR REFERENCIA INMUTABLE
    // * La mayoria de tipos pueden asignarse por referencia.
    // Se asigna usando '&'.
    let num: u8 = 12;
    let assign_num: &u8 = &num;

    let original_string: String = String::from("REFERENCIA INMUTABLE");
    let assign_string: &String = &original_string;
    println!("{original_string}"); // 'original_string' aun es valida.

    let array: [u8; 3] = [1, 2, 3];
    let assign_array: &[u8; 3] = &array;
    println!("{:?}", array); // 'array' aun es valida.

    // _________________________________________________________________
    // * ASIGNAR POR REFERENCIA MUTABLE
    // - Solo es posible con aquellos tipos que pueden mutar.
    // - se asigna usando '&mut' y se modifica aplicando desreferencia con '*'
    let mut num: u8 = 12;
    let assign_num: &mut u8 = &mut num;
    *assign_num = 77;
    println!("{num}"); // Los cambios afectaron a 'num'.

    let mut original_string: String = String::from("Ben");
    let assign_string: &mut String = &mut original_string;
    *assign_string = String::from("REFERENCIA MUTABLE");
    println!("{original_string}"); // Los cambios afectaron a 'original_string'.

    let mut original_vector: Vec<char> = vec!['a', 'b', 'c'];
    let assign_vector: &mut Vec<char> = &mut original_vector;
    assign_vector.push('d');
    println!("{:?}", original_vector); // Los cambios afectaron a 'original_vector'.

    // _________________________________________________________________
    // * DEMOSTRACIÓN EN FUNCIONES
    // Pasando por valor
    let original_bool: bool;

    original_bool = true;
    fn by_val(mut boolean: bool) {
        boolean = false;
    }
    by_val(original_bool);
    println!("Value: {original_bool}"); // no afecto a 'original_bool'

    // Pasando por referencia
    let mut original_bool: bool = true;

    fn by_ref( boolean: &mut bool) {
        *boolean = false;
    }
    by_ref(&mut original_bool);
    println!("Reference: {original_bool}"); // si afecto a 'original_bool'


/* _________________________________________________________________
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
* Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
* se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
* variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
* Comprueba también que se ha conservado el valor original en las primeras.
*/

let num1: i8 = 1;
let num2: i8 = 2;
let new_nums: (i8, i8) = by_value(num1, num2);
println!("Originales: {num1}, {num2}");
println!("Nuevas: {:?}", new_nums);

let mut vec1: Vec<char> = vec!['a', 'b'];
let mut vec2: Vec<char> = vec!['c', 'd'];
let new_vecs: (Vec<char>, Vec<char>) = by_reference(&mut vec1, &mut vec2);
println!("Originales: {:?}, {:?}", vec1, vec2);
println!("Nuevas: {:?}", new_vecs);
   
}

fn by_value(mut num1: i8,mut num2: i8) -> (i8, i8) {
    let tmp: i8 = num1;
    num1 = num2;
    num2 = tmp;
    return (num1, num2)
}

fn by_reference(vec1: &mut Vec<char>, vec2: &mut Vec<char>) -> (Vec<char>, Vec<char>) {
    let vec_1: Vec<char> = vec2.clone();
    let vec_2: Vec<char> = vec1.clone();
    return (vec_1, vec_2);
}
