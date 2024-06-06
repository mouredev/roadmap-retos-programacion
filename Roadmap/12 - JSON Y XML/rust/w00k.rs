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
 */

use std::fs;
use std::fs::File;
use std::io::Write;

// Struct base
#[derive(Debug)]
struct DevData {
    name: String,
    age: u8,
    birth_date: String,
    programming_languages_list: Vec<String>,
}

// Implementación de funciones json and xml
impl DevData {
    // Transforma el struct en string con formato json
    fn json(&self) -> String {
        let mut json = String::from("{");
        let end = String::from("}");
        let end_line = &*String::from(",");
        let quotes = &*String::from("\"");

        let name = String::from("\"name\":") + quotes + &*self.name + quotes + end_line;
        let age = String::from("\"age\":") + &*self.age.to_string() + end_line;
        let birth_date = String::from("\"birth_date\":") + quotes + &*self.birth_date + quotes + end_line;
        let programming_languages_list = String::from("\"programming_languages\":") + &*json_list(self.programming_languages_list.clone());

        json += &*(name + &*age + &*birth_date + &*programming_languages_list + &*end);
        return json;
    }
    // Transforma el struct en string con formato xml
    fn xml(&self) -> String {
        let mut xml = String::from("<data_dev>");
        let end_xml = String::from("</data_dev>");

        let name = "<name>".to_owned() + &*self.name + "</name>";
        let age = "<age>".to_owned() + &*self.age.to_string() + "</age>";
        let birth_date = "<birth_date>".to_owned() + &*self.birth_date + "</birth_date>";
        let programming_languages_list = xml_list(self.programming_languages_list.clone());

        xml += &*(name + &*age + &*birth_date + &*programming_languages_list + &*end_xml);

        return xml;
    }
}

// Utilidad para transformar el vector programming_languages en array json
fn json_list(dev_data_list: Vec<String>) -> String {
    let mut list = String::from("[");
    let end = &*String::from("]");
    let end_line = &*String::from(",");
    let quotes = &*String::from("\"");

    for (index, language) in dev_data_list.iter().enumerate() {
        if index == dev_data_list.len() -1 { // determino el último elemento,  por la coma al final
            list += &*(quotes.to_owned() + &*language.to_owned() + &*quotes);
        } else {
            list += &*(quotes.to_owned() + &*language.to_owned() + &*quotes + end_line);
        }

    }

    list += end;
    return list;
}

// Utilidad para transformar el vector programming_languages en array xml
fn xml_list(dev_data_list: Vec<String>) -> String {
    let mut xml = String::from("<programming_languages>");
    let end_xml = String::from("</programming_languages>");

    for language in dev_data_list {
        xml += &*("<language>".to_owned() + &*language.to_owned() + "</language>");
    }

    xml += &*end_xml;
    return xml;
}

// Utilidad para crear el archivo con data, nombre y extensión
fn create_file(data: String, file_name: &str, extension: &str) {
    let output_file_name = file_name.to_owned() + extension; // nombre del archivo con extensión
    let mut file = File::create(output_file_name.clone()).expect("Error creating file");

    file.write_all(data.as_bytes()).expect("Error writing to the file");
    println!("Successfully wrote data to {}", output_file_name);

    let contents = fs::read_to_string(output_file_name.as_str()).expect("Should have been able to read the file");
    println!("With text:{contents}");

    fs::remove_file(output_file_name.as_str()).expect("File not found");
    println!("Delete file\n");
}

fn main() {
    println!("Start");

    // nombre del archivo
    let file_name = "w00k";

    // extensiones
    let xml_extension = ".xml";
    let json_extension = ".json";

    let dev_data = DevData{
        name: String::from("w00k"),
        age: 41,
        birth_date: String::from("07/08/1982"), //mm/dd/yyyy
        programming_languages_list: vec![String::from("Java"), String::from("Go"), String::from("Rust")],
    };

    // imprimo el contenido del struct
    println!("dev data: {:?} \n", dev_data);

    create_file(dev_data.json(), file_name, json_extension);

    create_file(dev_data.xml(), file_name, xml_extension);

    println!("End");

}


