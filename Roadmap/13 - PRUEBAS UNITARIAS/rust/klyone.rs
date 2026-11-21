/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */

use std::collections::HashMap;

enum HashData {
    HSTR(String),
    HVEC(Vec<String>),
}

fn sum(a: u32, b: u32) -> u32 {
    a + b
}

fn create_hashmap() -> HashMap<String, HashData> {
    let mut m = HashMap::<String, HashData>::new();

    m.insert("name".to_string(), HashData::HSTR("Miguel".to_string()));
    m.insert("age".to_string(), HashData::HSTR("36".to_string()));
    m.insert(
        "birth_date".to_string(),
        HashData::HSTR("01/01/1990".to_string()),
    );
    m.insert(
        "programming_languages".to_string(),
        HashData::HVEC(Vec::from(["C, Python".to_string()])),
    );
    return m;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_hashmap1() {
        let m = create_hashmap();

        assert!(matches!(m.get("name").unwrap(), HashData::HSTR(s) if s == "Miguel"));
        assert!(matches!(m.get("age").unwrap(), HashData::HSTR(s) if s == "36"));
        assert!(matches!(m.get("birth_date").unwrap(), HashData::HSTR(s) if s == "01/01/1990"));
        assert!(matches!(
            m.get("programming_languages").unwrap(),
            HashData::HVEC(v) if v == &vec!["C, Python".to_string()]
        ));
    }

    #[test]
    fn test_hashmap2() {
        let m = create_hashmap();

        assert!(m.get("name").is_some());
        assert!(m.get("age").is_some());
        assert!(m.get("birth_date").is_some());
        assert!(m.get("programming_languages").is_some());
    }

    #[test]
    fn test_add() {
        assert_eq!(sum(1, 2), 3);
    }
}

fn main() {
    let _m = create_hashmap();
}
