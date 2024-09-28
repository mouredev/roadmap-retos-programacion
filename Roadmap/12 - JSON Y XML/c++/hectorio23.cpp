#include <iostream>
#include <fstream>
#include <json/json.h>
// #include <libxml2/libxml/tree.h>  
// sudo pacman -S libxml2
// la anterior libreria podria importarse simplemente como #include <libxml/tree.h>,
// sin embargo, por alguna razon me da un error, por esta razon lo importo llamando
// libxm12
// #include <libxm12/libxml/xmlwriter.h>

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

// // Función para crear un archivo XML con los datos proporcionados
// void createXML(std::string name, int age, std::string dob, std::vector<std::string> languages) {
//     // Crear un nuevo documento XML
//     xmlDocPtr doc = xmlNewDoc(BAD_CAST "1.0");
//     xmlNodePtr root = xmlNewNode(NULL, BAD_CAST "Person");
//     xmlDocSetRootElement(doc, root);

//     // Crear nodos para cada dato y agregarlos al árbol XML
//     xmlNodePtr nameNode = xmlNewChild(root, NULL, BAD_CAST "Name", BAD_CAST name.c_str());
//     xmlNodePtr ageNode = xmlNewChild(root, NULL, BAD_CAST "Age", BAD_CAST std::to_string(age).c_str());
//     xmlNodePtr dobNode = xmlNewChild(root, NULL, BAD_CAST "DateOfBirth", BAD_CAST dob.c_str());

//     xmlNodePtr langListNode = xmlNewChild(root, NULL, BAD_CAST "ProgrammingLanguages", NULL);
//     for (const auto& lang : languages) {
//         xmlNodePtr langNode = xmlNewTextChild(langListNode, NULL, BAD_CAST "Language", BAD_CAST lang.c_str());
//     }

//     // Guardar el documento XML en un archivo
//     xmlSaveFormatFileEnc("./Person.xml", doc, "UTF-8", 1);
//     xmlFreeDoc(doc); // Liberar memoria
// }

// Función para crear un archivo JSON con los datos proporcionados
// Función para crear un archivo JSON con los datos proporcionados
void createJSON(std::string name, int age, std::string dob, std::vector<std::string> languages) {
    Json::Value root;
    root["Name"] = name;
    root["Age"] = age;
    root["DateOfBirth"] = dob;

    Json::Value langList(Json::arrayValue);
    for (const auto& lang : languages) {
        langList.append(lang);
    }
    root["ProgrammingLanguages"] = langList;

    std::ofstream jsonFile("./Person.json");
    jsonFile << root;
}

// Función para mostrar el contenido de un archivo
void displayFileContents(const std::string& filename) {
    std::ifstream file(filename);
    if (file.is_open()) {
        std::cout << "Contents of " << filename << ":\n";
        std::cout << file.rdbuf();
        std::cout << "\n";
        file.close();
    } else {
        std::cerr << "Unable to open file: " << filename << std::endl;
    }
}

// Función para borrar los archivos generados
void deleteFiles() {
    std::remove("./Person.json");
}

int main() {
    std::string name = "Hector Adan";
    int age = 19;
    std::string dob = "2004-06-28";
    std::vector<std::string> languages = {"C++", "Python", "JavaScript"};

    // Crear archivos XML y JSON con los datos proporcionados
    // createXML(name, age, dob, languages);
    createJSON(name, age, dob, languages);

    // Mostrar el contenido de los archivos creados
    displayFileContents("./Person.json");

    // Borrar los archivos generados
    deleteFiles();

    return EXIT_SUCCESS;
}

// TODO:  g++ hectorio23.cpp -ljsoncpp
