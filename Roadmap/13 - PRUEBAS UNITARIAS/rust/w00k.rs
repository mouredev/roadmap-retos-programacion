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

//suma numeros
fn add_numbers(number1: u32, number2: u32) -> u32 {
    number1 + number2
}

//genera el HashMap -> clave valor
fn get_hashmap() -> HashMap<&'static str, &'static str> {
    let mut data = HashMap::new();
    data.insert("name", "w00k");
    data.insert("age", "41");
    data.insert("birth_date", "08/07/1982");
    data.insert("programming_languages", "Java, Go, Rust");
    return data;
}

fn main() {
    println!("Inicio");
    println!("{}", add_numbers(1, 2));
    println!("Fin");

    println!("\nDIFICULTAD EXTRA");
    let hash_map = get_hashmap();
    let iterator = hash_map.iter().count(); //cantidad de elementos del hash
    println!("The hash_map size equals {:?}", &iterator);
    for (key, value) in &hash_map { //imprimo el HashMap
        println!("{key}: {value}");
    }

}

//test
#[cfg(test)]
mod test {
    use crate::{add_numbers, get_hashmap};

    //test utilitario
    fn valid_key(value: &str) -> bool {
        if value.eq("name")
            || value.eq("age")
            || value.eq("birth_date")
            || value.eq("programming_languages") {
            return true;
        }
        return false;
    }

    //testcase
    #[test]
    fn it_works() {
        assert_eq!(add_numbers(2,2), 4);
    }
    #[test]
    fn other_works(){
        assert_eq!(add_numbers(1,1000000000), 1000000001);
    }
    //testcase DIFICULTAD EXTRA
    //valido datos no vacios
    #[test]
    fn validate_not_empty() {
        let hash = get_hashmap();
        let count = hash.iter().count();
        for (key, value) in &hash {
            assert_eq!(true, valid_key(&key));
            assert_ne!(0, value.len());
        }
        assert_eq!(4, count);
    }
    //valido nombre
    #[test]
    fn validate_name(){
        let hash = get_hashmap();
        let name = hash.get("name");
        match name {
            None => assert_eq!("none", ""),
            Some(&value) => assert_eq!("w00k", value),
        }
    }
    //valido edad
    #[test]
    fn validate_age(){
        let hash = get_hashmap();
        let age = hash.get("age");
        match age {
            None => assert_eq!("none",""),
            Some(&value) => {
                assert_ne!(0, value.len());
                assert_eq!("41", value);
            },
        }
    }
    //valido fecha nacimiento
    #[test]
    fn validate_birth_date(){
        let hash = get_hashmap();
        let birth_date = hash.get("birth_date");
        match birth_date {
            None => assert_eq!("none", ""),
            Some(&value) => assert_eq!("08/07/1982", value),
        }
    }
    //valido lenguajes de programación
    #[test]
    fn validate_languages(){
        let hash = get_hashmap();
        let lang = hash.get("programming_languages");
        match lang {
            None => assert_eq!("none", ""),
            Some(&value) => assert_eq!("Java, Go, Rust", value)
        }
    }
}


