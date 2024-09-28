use std::collections::HashSet;

/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
*/

fn checkwords(word1: String, word2: String) {
    // Saber si una palabra es palindroma -> Palabras que se leen igual de izquierda a derecha que de derecha a izquierda
    let invertedword1: String = word1.chars().rev().collect::<String>();
    let invertedword2: String = word1.chars().rev().collect::<String>();
    println!("La palabra {} es una palindroma? {}", word1, word1 == invertedword1);
    println!("La palabra {} es una palindroma? {}", word2, word2 == invertedword2);

    // Saber si una palabra en un anagrama -> Palabras que si cambiamos el orden de las letras, son palabras diferentes (Zara = Raza)
    let mut string1: Vec<char> = word1.chars().collect();
    let mut string2: Vec<char> = word2.chars().collect();
    string1.sort();
    string2.sort();
    println!("Son anagramas? {:?}", string1 == string2);

    // Saber si es un isograma -> Palabras que tienen letras repetidas
    let mut string1_set: HashSet<char> = HashSet::new();
    for c in word1.chars() {
        string1_set.insert(c);
    }
    let string1_fi: String = string1_set.into_iter().collect();

    let mut string2_set: HashSet<char> = HashSet::new();
    for c in word2.chars() {
        string2_set.insert(c);
    }
    let string2_fi: String = string2_set.into_iter().collect();

    println!("La palabra {} es un isograma? {}",word1 ,string1_fi.len() < word1.len());
    println!("La palabra {} es un isograma? {}", word2, string2_fi.len() < word2.len());
}

fn main(){
    let string1: String = String::from("hello");
    let string2: String = String::from("rust");
    let string3: String = String::from("  github    ");
    let string4: String = String::from("Mouredev esta en directo en twitch");
    let palabras: Vec<&str> = vec!["Juan", "se", "fue", "a", "comprar", "el", "pan"];

    // Formateo
    let saludo = format!("{string1}, {string2}");
    println!("{saludo}");

    // Convertir String a int
    let numero: String = String::from("34");
    println!("Pasamos una string un valor numerico: {:?}", numero.parse::<i32>().unwrap());
    
    // Ver si una cadena esta vacía
    println!("La cadena2 esta vacía? {}", string2.is_empty());

    // Obtener una referencia a los bytes que componen la cadena.
    println!("La cadena 2 representada en caracteres ASCII es: {:?}", string2.as_bytes());
    
    // Obtener posición
    let string2_vector: Vec<char> = string2.chars().collect();
    println!("La posición 2 de la cadena 2 es: {:?}", string2_vector[2]);
    
    // Concatenación
    let mut result: String = String::new();
    result.push_str(&string1);
    result.push_str(&string2);

    println!("Si concatenamos la string1 y la string2 sale: {}", result);

    // Repetición
    println!("String2 repetida 3 veces: {}", &string2.repeat(3));

    // Longitud
    println!("La longitud de la string 1 es de {} caracteres", string1.len());

    // Busqueda
    let incluye: bool = string2.contains("us");
    println!("La string 2 contiene 'us'? {incluye}");

    // Reemplazo
    println!("En la string 1, si remplazamos las 'l' por 'a' quedaria asi: {}", string1.replace("l", "a"));

    // Recorrido
    for character in string2.chars() {
        println!("{character}")
    }
    
    // División
    let text: Vec<&str> = string4.split("en").collect();
    println!("La string 4 dividida por 'en' es: {:?}", text);

    // Mayúsculas y minúsculas
    println!("String 2 toda en mayúsculas: {}", string2.to_uppercase());
    println!("String 2 toda en minúsculas: {}", string2.to_lowercase());

    // Eliminar espacio principio y final
    println!("La string sin espacios es: {}", string3.trim());

    // Búsqueda al principio y al final
    println!("La string 2 comienza por ru? {}", string2.starts_with("ru"));
    println!("La string 2 comienza por he? {}", string2.starts_with("he"));
    println!("La string 2 acabas por llo? {}", string2.ends_with("llo"));
    println!("La string 2 acabas por st? {}", string2.ends_with("st"));

    // Búsqueda de la primera posición
    println!("La primera letra 't' esta en la posición: {:?}", string4.find("t"));

    // Búsqueda de la ultima posición
    println!("La ultima letra 't' se encuentra en la posición: {:?}", string4.rfind("t"));

    // Búsqueda de ocurrencias
    println!("La string 4 tiene: {} caracteres", string4.chars().count());

    // Unión de vector
    println!("El vector unido mediante espacios es: {}", palabras.join(" "));
    
    checkwords(String::from("radar"), String::from("zara"));
}
