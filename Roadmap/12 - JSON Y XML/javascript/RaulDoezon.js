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

const fs = require('node:fs');

console.log("+++++++++ JSON +++++++++");

const myObject = {
  name: "Raúl",
  age: 70,
  birthdate: "13/06/1954",
  programming_languages: {
    frontend: "JavaScript",
    backend: "Python"
  }
}

const myJSON = JSON.stringify(myObject);

try {
  fs.writeFileSync('./RaulDoezon.json', myJSON);

  console.log("¡El archivo JSON fue creado!\n");
} catch (writeJSONError) {
  console.log(writeJSONError);
}

try {
  const jsonData = fs.readFileSync('./RaulDoezon.json', 'utf8');

  console.log(JSON.parse(jsonData));
} catch (readJSONError) {
  console.log(readJSONError);
}

setTimeout(() => {
  try {
    fs.unlinkSync('./RaulDoezon.json');

    console.log("\n¡Se eliminó el archivo JSON!");
  } catch (unlinkJSONError) {
    console.log(unlinkJSONError);
  }
}, 2000);

console.log("\n+++++++++ XML +++++++++");

const myXML = `<?xml version="1.0"?>
<information>
  <name>Raúl</name>
  <age>70</age>
  <birthdate>13/06/1954</birthdate>
  <programming_languages>
    <frontend>JavaScript</frontend>
    <backend>Python"</backend>
  </programming_languages>
</information>`;

try {
  fs.writeFileSync('./RaulDoezon.xml', myXML);

  console.log("\n¡Fue creado el archivo XML!\n");
} catch (XMLWriteError) {
  console.log(XMLWriteError);
}

try {
  const xmlData = fs.readFileSync('./RaulDoezon.xml', 'utf8');

  console.log(xmlData);
} catch (readXMLError) {
  console.log(readXMLError);
}

setTimeout(() => {
  try {
    fs.unlinkSync('./RaulDoezon.xml');

    console.log("\n¡Se eliminó el archivo XML!");
  } catch (unlinkXMLError) {
    console.log(unlinkXMLError);
  }
}, 2000);
