#![allow(dead_code)]
/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* PRUEBAS UNITARIAS
-----------------------------------------
Mas info: https://doc.rust-lang.org/rust-by-example/testing/unit_testing.html
_______________
* EJERCICIO #1
* Crea una función que se encargue de sumar dos números y retornar
  su resultado.
* Crea un test, utilizando las herramientas de tu lenguaje, que sea
  capaz de determinar si esa función se ejecuta correctamente.

_______________
* EJERCICIO #2
* Crea un diccionario con las siguientes claves y valores:
  - "name": "Tu nombre"
  - "age": "Tu edad"
  - "birth_date": "Tu fecha de nacimiento"
  - "programming_languages": ["Listado de lenguajes de programación"]
* Crea dos test:
  - Un primero que determine que existen todos los campos.
  - Un segundo que determine que los datos introducidos son correctos.
*/

fn sum(a: i32, b: i32) -> i32 {
    a + b
}

use std::collections::HashMap;
use std::any::Any;

fn get_dict_user() -> HashMap<&'static str, Box<dyn Any>> {
    let mut dict_user: HashMap<&'static str, Box<dyn Any>> = HashMap::new();

    dict_user.insert("name", Box::new("Ken"));
    dict_user.insert("age", Box::new(121));
    dict_user.insert("birth_date", Box::new("1903-03-19"));
    dict_user.insert("prog_langs", Box::new(vec!["cs", "py", "vb", "rs", "js"]));

    return dict_user
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sum() {
        assert_eq!(sum(5, 2), 7);
        assert_eq!(sum(-2, 1), -1);
        assert_eq!(sum(0, 0), 0);
    }

    #[test]
    fn test_dict_key_existence() {
        let dict_user = get_dict_user();

        assert!(dict_user.contains_key("name"));
        assert!(dict_user.contains_key("age"));
        assert!(dict_user.contains_key("birth_date"));
        assert!(dict_user.contains_key("prog_langs"));
    }

    #[test]
    fn test_dict_value_types() {
        let dict_user = get_dict_user();

        assert!(dict_user["name"].is::<&str>());
        assert!(dict_user["age"].is::<i32>());
        assert!(dict_user["birth_date"].is::<&str>());
        assert!(dict_user["prog_langs"].is::<Vec<&str>>());
    }
}
