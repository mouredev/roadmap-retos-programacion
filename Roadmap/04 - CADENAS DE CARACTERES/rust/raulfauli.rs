/// #04 CADENAS DE CARACTERES
///
/// Para compilar y ejecutar este código, ejecuta el siguiente comando desde el directorio principal:
///
/// `rustc ./Roadmap/04\ -\ CADENAS\ DE\ CARACTERES/rust/raulfauli.rs && ./raulfauli && rm raulfauli`
///
fn main() {
  let mut string = String::from("Hola");

  // Concatenar
  string.push_str(" Rust");
  println!("{}", string);

  // Longitud
  let length = string.len();
  println!("Longitud: {}", length);

  // Contiene
  let contains = string.contains("Rust");
  println!("Contiene 'Rust'? {}", contains);

  // Posición
  let position = string.find("Rust").unwrap();
  println!("Posición de 'Rust': {}", position);

  // Reemplazar
  let new_string = string.replace("Rust", "Mundo");
  println!("{}", new_string);

  // Iterar
  for c in string.chars() {
      println!("{}", c);
  }

  let chars: Vec<char> = string.chars().collect();
  println!("{}", chars[1]);

  // Convertir a mayúsculas
  println!("Mayúsculas: {}", string.to_uppercase());
  println!("Minúsculas: {}", string.to_lowercase());

  // Subcadenas
  let sub = &string[0..4];
  println!("{}", sub);

  // Split
  let split: Vec<&str> = string.split(" ").collect();
  println!("{:?}", split);

  // Join
  let join = split.join("-");
  println!("{}", join);

  // Trim
  let trimmed = "   Hola   ".trim();
  println!("{}", trimmed);

  // Convertir a número
  let number = "10".parse::<i32>().unwrap();
  println!("{}", number);

  // Formatear
  let formatted = format!("Mi nombre es {}! Ingeniero desde hace {} años", "Raúl", 12);
  println!("{}", formatted);

  // Multiplicar
  let multiplied = "Hola".repeat(3);
  println!("{}", multiplied);

  // Vaciar
  string.clear();
  println!("Está vacía? {}", string.is_empty());

  // EXTRA
  let palindrome = "anitalavalatina";
  println!("Es palíndromo '{}'? {}", palindrome, is_palindrome(palindrome));

  let not_palindrome = "Rust";
  println!("Es palíndromo '{}'? {}", not_palindrome, is_palindrome(not_palindrome));

  let anagram1 = "roma";
  let anagram2 = "amor";
  println!("Es anagrama '{}' y '{}'? {}", anagram1, anagram2, is_anagram(anagram1, anagram2));

  let not_anagram1 = "rust";
  let not_anagram2 = "dart";
  println!("Es anagrama '{}' y '{}'? {}", not_anagram1, not_anagram2, is_anagram(not_anagram1, not_anagram2));

  let isogram = "murcielago";
  println!("Es isograma '{}'? {}", isogram, is_isogram(isogram));

  let not_isogram = "murcielagoo";
  println!("Es isograma '{}'? {}", not_isogram, is_isogram(not_isogram));
}

fn is_palindrome(word: &str) -> bool {
  word.chars().eq(word.chars().rev())
}

fn is_anagram(word1: &str, word2: &str) -> bool {
  let mut chars1: Vec<char> = word1.chars().collect();
  chars1.sort_by(|a, b| b.cmp(a));

  let mut chars2: Vec<char> = word2.chars().collect();
  chars2.sort_by(|a, b| b.cmp(a));

  chars1 == chars2
}

fn is_isogram(word: &str) -> bool {
  let mut chars: Vec<char> = word.chars().collect();
  chars.sort_by(|a, b| b.cmp(a));

  let mut isogram = true;
  for i in 0..chars.len() - 1 {
      if chars[i] == chars[i + 1] {
          isogram = false;
          break;
      }
  }

  isogram
}

