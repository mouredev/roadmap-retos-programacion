use std::collections::HashMap;
use std::io;

/*
 Ejercicio 04 - CADENAS DE CARACTERES
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
*/
fn main() {
    let mut s = String::new();

    // Concat
    s.push_str("Hello ");
    s.push_str("Rust!");
    println!("s: {}", s);

    // Length
    println!("Longitud: {}", s.len());

    // Contains
    let c = s.contains('R');
    println!("s contiene R?: {}", c);

    // Position
    println!("Posicion de e: {:?}", s.find('e'));

    // Replace
    let s2 = s.replace("Rust", "Rust 2023");
    println!("s2: {}", s2);

    // Iterate
    println!("s2 iteration: ");
    for c in s2.chars() {
        print!("{}", c);
    }
    println!();

    // To uppercase
    println!("s2 uppercase: {}", s2.to_uppercase());

    // To lowercase
    println!("s2 lowercase: {}", s2.to_lowercase());

    // Slice
    let s3 = &s2[0..5];
    println!("s3 = s2[0..5]: {}", s3);

    // Splite (Vector, not a String)
    println!("s2: {}", s2);
    let s4: Vec<_> = s2.split(' ').collect();
    println!("s4 : {:?}", s4);

    // Join
    println!("s4 join: {:?}", s4.join("-"));

    // Trim (remove " ")
    let s5 = "  Hello  ";
    println!("s5 trim: {}.", s5.trim());

    // format
    let formatted = format!("Mi nombre es {}! Estoy aprendiendo {}.", "Martin", "Rust");
    println!("{}", formatted);

    // Repetir
    println!("s3 ({}) * 3: {}", s3, s3.repeat(3));

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que analice dos palabras diferentes y realice comprobaciones
     * para descubrir si son:
     * - Palíndromos
     * - Anagramas
     * - Isogramas
     */
    println!("EXTRA EXTRA:\n");

    println!("Ingrese la primer palabra:");
    let mut palabra1 = String::new();
    match io::stdin().read_line(&mut palabra1) {
        Ok(_) => {}
        Err(error) => {
            println!("Ha ocurrido un error: {}", error)
        }
    };
    println!("Ingrese la segunda palabra:");
    let mut palabra2 = String::new();
    match io::stdin().read_line(&mut palabra2) {
        Ok(_) => {}
        Err(error) => {
            println!("Ha ocurrido un error: {}", error)
        }
    };
    palabra1 = palabra1.trim().to_string();
    palabra2 = palabra2.trim().to_string();
    extra(palabra1, palabra2);
}

fn extra(palabra1: String, palabra2: String) {
    if son_palindromos(palabra1.clone(), palabra2.clone()) {
        println!("Las dos palabras son palindromos");
    } else {
        println!("Las dos palabras no son palindromos\n")
    }

    if son_anagrama(palabra1.clone(), palabra2.clone()) {
        println!("Las dos palabras son anagramas");
    } else {
        println!("Las dos palabras no son anagramas\n")
    }

    if son_isograma(palabra1.clone(), palabra2.clone()) {
        println!("Ambas palabras son isogramas");
    } else {
        println!("Ambas palabras no son isogramas")
    }
}

fn son_palindromos(palabra1: String, palabra2: String) -> bool {
    let mut a = false;
    let mut b = false;
    if es_palindromo(palabra1.clone()) {
        println!("La palabra {} es palindromo", palabra1);
        a = true;
    }

    if es_palindromo(palabra2.clone()) {
        println!("La palabra {} es palindromo", palabra2);
        b = true;
    }

    if a && b {
        return true;
    }
    false
}

fn es_palindromo(palabra: String) -> bool {
    let mut palabra_r: Vec<char> = palabra.chars().collect();
    palabra_r.reverse();
    let palabra_r: String = palabra_r.iter().collect();
    if palabra == palabra_r {
        return true;
    }
    false
}

fn son_anagrama(palabra1: String, palabra2: String) -> bool {
    let mut palabra1_v: Vec<char> = palabra1.chars().collect();
    let mut palabra2_v: Vec<char> = palabra2.chars().collect();
    palabra1_v.sort();
    palabra2_v.sort();
    let palabra1_v: String = palabra1_v.iter().collect();
    let palabra2_v: String = palabra2_v.iter().collect();
    if palabra1_v == palabra2_v {
        return true;
    }
    false
}

fn son_isograma(palabra1: String, palabra2: String) -> bool {
    let mut a = false;
    let mut b = false;
    if es_isograma(palabra1.clone()) {
        println!("La palabra {} es un isograma", palabra1);
        a = true;
    }
    if es_isograma(palabra2.clone()) {
        println!("La palabra {} es un isograma", palabra2);
        b = true;
    }

    if a && b {
        return true;
    }
    false
}

fn es_isograma(palabra: String) -> bool {
    let palabra_v = palabra.chars();
    let mut caracteres: HashMap<char, u8> = HashMap::new();
    for c in palabra_v {
        *caracteres.entry(c).or_insert(0) += 1;
    }

    let values_equal = caracteres
        .values()
        .all(|&v| v == *caracteres.values().next().unwrap());

    values_equal
}