/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* JSON Y XML
-----------------------------------------
- son formatos de intercambio de datos que estructuran información.
- JSON (JavaScript Object Notation) y XML (Extensible Markup Language)

- Agregar biblioteca -> cargo add serde
                        cargo add serde-json
                        cargo add serde-xml-rs
[dependencies]
serde = { version = "1.0.197", features = ["derive"] }
serde_json = "1.0.115"
serde-xml-rs = "0.6.0"
____________________________________
* JSON (https://crates.io/crates/serde_json)

*/
use serde::{Deserialize, Serialize};
use std::fs::File;
use std::io::prelude::*;
use std::io::Result;
use std::io::{self, Error, ErrorKind};

#[derive(Debug, Serialize, Deserialize)]
pub struct User {
    name: String,
    age: u32,
    dob: String,
    prog_langs: Vec<String>,
}

fn write_json(user: &User) -> Result<()> {
    let json_data = serde_json::to_string_pretty(&user)?;
    let mut file = File::create("user.json")?;
    file.write_all(json_data.as_bytes())?;
    println!("JSON creado");
    Ok(())
}

pub fn read_json() -> Result<User> {
    let mut file = File::open("user.json")?;
    let mut json_data = String::new();
    file.read_to_string(&mut json_data)?;
    let user: User = serde_json::from_str(&json_data)?;
    Ok(user)
}

/* ____________________________________
* XML (https://crates.io/crates/serde-xml-rs)
*/

fn write_xml(user: &User) -> io::Result<()> {
    let xml_data = serde_xml_rs::to_string(user)
        .map_err(|e| Error::new(ErrorKind::Other, e))?;
    
    let mut file = File::create("user.xml")?;
    file.write_all(xml_data.as_bytes())?;
    println!("XML creado con éxito.");
    Ok(())
}

fn read_xml() -> io::Result<User> {
    let mut file = File::open("user.xml")?;
    let mut xml_data = String::new();
    file.read_to_string(&mut xml_data)?;

    let user: User = serde_xml_rs::from_str(&xml_data)
        .map_err(|e| Error::new(ErrorKind::Other, e))?;

    Ok(user)
}

fn delete_file(the_path: &str) {
    if let Err(err) = std::fs::remove_file(the_path) {
        println!("Error al eliminar {}: {}", the_path, err);
    } else {
        println!("* {} ha sido eliminado.", the_path);
    }
}

fn main(){
    let default_user = User {
        name: "Ken".to_string(),
        age: 121,
        dob: "1903-03-19".to_string(),
        prog_langs: vec!["cs", "py", "vb", "rs", "js"]
            .iter()
            .map(|s| s.to_string())
            .collect(),
    };

    //___________________________
    if let Err(e) = write_json(&default_user) {
        eprintln!("Error al escribir JSON: {}", e);
    }

    match read_json() {
        Ok(user) => println!("datos en el JSON deserializados:\n{:?}", user),
        Err(e) => eprintln!("Error al deserializar JSON: {}", e),
        /*
        Ok(user) => {
            println!("Nombre: {}", user.name);
            println!("Edad: {}", user.age);
            ...
        */
    }

    //___________________________
    if let Err(e) = write_xml(&default_user) {
        eprintln!("Error al escribir XML: {}", e);
    }

    match read_xml() {
        Ok(user) => println!("datos en el XML deserializados:\n{:?}", user),
        Err(e) => eprintln!("Error al deserializar XML: {}", e),
    }

    //___________________________
    delete_file("user.json");
    delete_file("user.xml");

}
