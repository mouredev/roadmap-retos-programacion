// no advertencia
#![allow(unused_variables)]
#![allow(unused_assignments)]
#![allow(unused_mut)]
use std::collections::HashSet;
use std::borrow::Cow;
/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* CADENAS DE CARACTERES
-----------------------------------------
- Hay dos tipos principales: String y &str.
- son una colección de caracteres Unicode que pueden representar una
  amplia gama de idiomas y símbolos.
*/
fn main() {
    /*__________________________________
     * (&str)
     - Es una referencia a un segmento de memoria.
     - Son inmutables por naturaleza.
     - Representa una “sección” de una cadena de caracteres.
     - Pueden ser asociados con el tiempo de vida de otras referencias.
    */
    let name: &str = "Ken!"; // Su contenido sera estatico.
    
    // Concatenación
    let hello: &str = "¡Hola, ";
    let combined: String = hello.to_owned() + name; // o .to_string()
    println!("{combined}"); // ¡Hola, Ken!

    // Extracción de subcadenas (slicing)
    let sub: &str = &combined[0..6];
    println!("slicing: {sub}"); // ¡Hola

    // longitud
    println!("Longitud de 'name': '{}'", name.len());

    // Búsqueda de subcadenas
    if hello.contains("Ho") {
        println!("Si contiene 'Ho'");
    }

    // División en tokens
    let combined: &str = &combined; // tomar referencia de (combined: String).
    let tokens: Vec<&str> = combined.split(',').collect();
    println!("{:?}", tokens); // ["¡Hola", "Ken!"]

    // Conversión a otros tipo
    let num_str: &str = "12";
    let num: i8 = num_str.parse().unwrap();
    println!("Conversión a int: {num}");

    // Remoción de espacios en blanco
    let padded: &str = "   ¡Hola, mundo!   ";
    let trimmed: &str = padded.trim();
    println!("Remoción de espacios: '{trimmed}'");

    // Transformaciones de mayúsculas y minúsculas
    let upper: String = trimmed.to_uppercase();
    let lower: String = trimmed.to_lowercase();
    println!("upper: {upper}"); // ¡HOLA, MUNDO!
    println!("lower: {lower}"); // ¡hola, mundo! 

    // Iteración sobre caracteres
    for c in hello.chars() {
        println!("{c}");
    }

    /*__________________________________
     * (String)
     - Cadena de caracteres de propiedad (owned).
     - Son mutables por naturaleza.
     - Alojados en la memoria dinámica (Heap).
     - Están sujetas a las reglas de propiedad y vida útil de Rust.
    */
    let mut hi: String = String::from("¡Hola, "); // mutable
    let name: String = String::from("Ken!");      // inmutable

    // - Diferentes asignaciones
    let mut hello: String = hi;    // La propiedad de 'hi' se mueve a 'hello'
    // En este punto, 'hi' ya no es válido y no puede ser usado.

    let my_name: &String = &name; // Se crea una referencia inmutable de 'name'
    
    // Crear una referencia mutable
    let mut name2 = String::from("Ben");
    let mut my_name2: &mut String = &mut name2; 
    my_name2.push_str(" y Zoe");
    println!("{name2}"); // Veremos el cambio en la variable original.

    // - Formas de concatenar
    let mut result: String = String::new(); // declarar vacia
    result = format!("{}{}", hello, my_name);

    result.push_str(&hello); // Agregar texto
    result.push_str(&my_name);
    result.push('!'); // Agregar un caracter

    result = hello + &my_name; // hello ya no es utilizable.

    // Transformaciones de mayúsculas y minúsculas
    let upper: String = result.to_uppercase();
    let lower: String = result.to_lowercase();
    println!("upper: {upper}"); // ¡HOLA, KEN!
    println!("lower: {lower}"); // ¡hola, ken! 

    // - Reemplazo de subcadenas:
    result = result.replace("Ken", "Rust");
    println!("Reemplazo: {result}"); // ¡hola, Rust!

    // Búsqueda de subcadenas:
    if let Some(index) = result.find("Rust") {
        println!("Indice: {index}");
    }
    
    // Eliminación de espacios en blanco:
    let hi = String::from("   ¡Hola, mundo!   ");
    let trimed = hi.trim();
    println!("{trimed}");

    // Comprobación de vacío:
    let s = String::from("");
    if s.is_empty() {
        println!("La cadena está vacía");
    }

    /*__________________________________
     * Cow (Clone On Write)
     - 'Cow<'a, B>' es una estructura de datos que representa una cadena de caracteres y se 
       utiliza para evitar copias innecesarias de datos al trabajar con cadenas. 
     - Puede contener tanto una referencia prestada (&T) como datos de propiedad propia (T).
     - Si se necesita modificar los datos compartidos, se realiza una copia solo en ese momento. 
    */
    
    // Cuando se necesita una copia de la cadena, y esta se clona.
    let owned: Cow<str> = Cow::Owned(String::from("Hola"));
    //  Cuando se quiere trabajar con una referencia prestada.
    let borrowed: Cow<str> = Cow::Borrowed("Hello");

    // Ejemplo de uso
    fn add_greeting(mut s: Cow<str>) -> Cow<str> {
        match s {
            // Verificamos si la cadena es propia (String) o prestada (&str)
            Cow::Owned(ref mut owned_string) => {
                // Si es propia, podemos modificarla directamente
                owned_string.push_str(", mundo!");
                return s
            }
            Cow::Borrowed(_) => {
                // Si es prestada, necesitamos hacer una copia antes de modificarla
                s.to_mut().push_str(", mundo!");
                return s
            }
        }
    }

    // Ejemplo con una cadena propia (String)
    let mut owned_string: Cow<str> = Cow::Owned(String::from("Hola"));
    let result_owned = add_greeting(owned_string.clone());
    println!("Cadena modificada (own): {}", result_owned);

    // Ejemplo con una cadena prestada (&str)
    let borrowed_string: Cow<str> = Cow::Borrowed("Hola");
    let result_borrowed  = add_greeting(borrowed_string.clone());
    println!("Cadena modificada (borrowed): {}", result_borrowed);

    /*__________________________________
     * EJERCICIO:
     * Crea un programa que analice dos palabras diferentes y 
     * realice comprobaciones para descubrir si son:
     * - Palíndromos
     * - Anagramas
     * - Isogramas
    */
    println!("EJERCICIO:");
    analyze("reconocer", "vida");
    analyze("notas", "santo");
    analyze("héroe", "radar");
}

fn analyze(s1: &str, s2: &str) {
    let s1_is_palindrome: bool = s1.chars().eq(s1.chars().rev());
    let s2_is_palindrome: bool = s2.chars().eq(s2.chars().rev());

    let mut s1_chars: Vec<char> = s1.chars().collect();
    let mut s2_chars: Vec<char> = s2.chars().collect();
    s1_chars.sort();
    s2_chars.sort();   
    let is_anagram: bool =  s1_chars == s2_chars;

    let s1_set: HashSet<_> = s1.chars().collect();
    let s2_set: HashSet<_> = s2.chars().collect();
    let s1_is_isogram: bool = s1.len() == s1_set.len();
    let s2_is_isogram: bool = s2.len() == s2_set.len();

    println!("
__________________________________________
- {s1} es un palíndromo?: {s1_is_palindrome}
- {s2} es un palíndromo?: {s2_is_palindrome}

- {s1} es un anagrama de {s2}?: {is_anagram}

- {s1} es un isograma?: {s1_is_isogram}
- {s2} es un isograma?: {s2_is_isogram}
__________________________________________");
}
