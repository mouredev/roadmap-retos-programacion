/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */

use std::fs::{self, File};
use std::io::Write;

/* XML example
<xml>
   <name>Miguel J.</name>
   <age>36</age>
   <birth>01/01/1990</birth>
   <languages>C,Rust,Python</languages>
</xml>
*/
fn create_xml_file(name: &String, age: u32, birth: &String, lang: &Vec<String>) {
    let mut f = File::create("klyone.xml").unwrap();

    let _ = write!(f, "<xml>\n");
    let _ = write!(f, "<name>{}</name>\n", name);
    let _ = write!(f, "<age>{}</age>\n", age);
    let _ = write!(f, "<birth>{}</birth>\n", birth);
    let _ = write!(f, "<languages>{}</languages>\n", lang.join(","));
    let _ = write!(f, "</xml>\n");
}

fn parse_xml_file(name: &mut String, age: &mut u32, birth: &mut String, lang: &mut Vec<String>) {
    for line in fs::read_to_string("klyone.xml").unwrap().lines() {
        let start = line.find(">").unwrap();
        let end = line.rfind("<").unwrap();
        if line.contains("<name>") {
            *name = String::from(&line[start + 1..end]);
        } else if line.contains("<age>") {
            *age = line[start + 1..end].parse::<u32>().unwrap();
        } else if line.contains("<birth>") {
            *birth = String::from(&line[start + 1..end]);
        } else if line.contains("<languages>") {
            let l = String::from(&line[start + 1..end]);
            *lang = l.split(",").map(|s| s.trim().to_string()).collect();
        }
    }
}

/* JSON example
 {
    "name" : "Miguel J.",
    "age" : 36,
    "birth" : "01/01/1990",
    "languages": ["C", "Rust", "Python"]
 }
*/
fn create_json_file(name: &String, age: u32, birth: &String, lang: &Vec<String>) {
    let mut f = File::create("klyone.json").unwrap();

    let lang2: Vec<String> = lang.into_iter().map(|x| format!("\"{}\"", x)).collect();

    let _ = write!(f, "{{\n");
    let _ = write!(f, "\"name\": \"{}\",\n", name);
    let _ = write!(f, "\"age\": {},\n", age);
    let _ = write!(f, "\"birth\": \"{}\",\n", birth);
    let _ = write!(f, "\"languages\": [{}]\n", lang2.join(","));
    let _ = write!(f, "}}\n");
}

fn parse_json_file(name: &mut String, age: &mut u32, birth: &mut String, lang: &mut Vec<String>) {
    for line in fs::read_to_string("klyone.json").unwrap().lines() {
        let l: Vec<&str> = line.split(":").collect();

        if l.len() != 2 {
            continue;
        }

        let n = l[0].trim().replace("\"", "").replace(",", "");
        let mut v = l[1].trim().replace("\"", "");

        if n == "name" {
            v = v.strip_suffix(",").unwrap().to_string();
            *name = String::from(v);
        } else if n == "age" {
            v = v.strip_suffix(",").unwrap().to_string();
            *age = v.parse::<u32>().unwrap();
        } else if n == "birth" {
            v = v.strip_suffix(",").unwrap().to_string();
            *birth = String::from(v);
        } else if n == "languages" {
            v = v.replace("[", "").replace("]", "");
            *lang = v.split(",").map(|s| s.trim().to_string()).collect();
        }
    }
}

struct Parser {
    name: String,
    birth: String,
    age: u32,
    lang: Vec<String>,
}

impl Parser {
    fn new() -> Self {
        Parser {
            name: "".to_string(),
            birth: "".to_string(),
            age: 0,
            lang: Vec::from([]),
        }
    }

    fn read_from_json(&mut self) {
        parse_json_file(
            &mut self.name,
            &mut self.age,
            &mut self.birth,
            &mut self.lang,
        );
    }

    fn read_from_xml(&mut self) {
        parse_xml_file(
            &mut self.name,
            &mut self.age,
            &mut self.birth,
            &mut self.lang,
        );
    }

    fn write_to_json(&self) {
        create_json_file(&self.name, self.age, &self.birth, &self.lang);
    }

    fn write_to_xml(&self) {
        create_xml_file(&self.name, self.age, &self.birth, &self.lang);
    }

    fn print(&self) {
        println!("name: {}", self.name);
        println!("age: {}", self.age);
        println!("birth: {}", self.birth);
        println!("languages: [{}]", self.lang.join(","));
    }
}

fn main() {
    let name = String::from("Miguel");
    let birth = String::from("01/01/1990");
    let age = 36;
    let lang = Vec::from([String::from("C"), String::from("Python")]);
    create_xml_file(&name, age, &birth, &lang);
    create_json_file(&name, age, &birth, &lang);

    println!("XML content");
    println!("");
    let mut c = fs::read_to_string("klyone.xml").unwrap();
    println!("{}", c);
    println!("JSON content");
    c = fs::read_to_string("klyone.json").unwrap();
    println!("{}", c);
    println!("");

    let mut data1 = Parser::new();
    let mut data2 = Parser::new();

    data1.read_from_xml();
    data1.print();

    data2.read_from_json();
    data2.print();

    let _ = fs::remove_file("klyone.json");
    let _ = fs::remove_file("klyone.xml");

    data1.write_to_json();
    data2.write_to_xml();

    let _ = fs::remove_file("klyone.json");
    let _ = fs::remove_file("klyone.xml");
}
