// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23
 
"use strict";

const fs = require('fs');

// Función para crear un archivo JSON con los datos proporcionados
function createJSON(name, age, dob, languages) {
    const data = {
        Name: name,
        Age: age,
        DateOfBirth: dob,
        ProgrammingLanguages: languages
    };

    fs.writeFileSync('./Person.json', JSON.stringify(data, null, 4));
}

// Función para mostrar el contenido de un archivo
function displayFileContents(filename) {
    try {
        const content = fs.readFileSync(filename, 'utf8');
        console.log(`Contents of ${filename}:`);
        console.log(content);
    } catch (error) {
        console.error(`Unable to read file: ${filename}`, error);
    }
}

// Función para borrar los archivos generados
function deleteFiles() {
    try {
        fs.unlinkSync('./Person.json');
    } catch (error) {
        console.error(`Unable to delete file: ./Person.json`, error);
    }
}

function main() {
    const name = "Héctor Adán";
    const age = 19;
    const dob = "2004-06-28";
    const languages = ["C++", "Python", "JavaScript"];

    // Crear archivo JSON con los datos proporcionados
    createJSON(name, age, dob, languages);

    // Mostrar el contenido del archivo creado
    displayFileContents('./Person.json');

    // Borrar el archivo generado
    deleteFiles();
}

main();
