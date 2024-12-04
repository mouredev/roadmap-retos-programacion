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
const fs = require('fs');

// Datos para el archivo XML
const data ={
    nombre: "William Pastor",
    ciudad: "Madrid",
    edad: 18,
    fechaDeNacimiento: "13-12-1993",
    listadoDeLenguajesProgramacion : ['JavaScript', 'Python']
}

// Datos para el archivo XML
// Convertir el objeto a una cadena XML (simplificado)
const xmlString = `<persona>
    <nombre>${data.nombre}</nombre>
    <edad>${data.edad}</edad>
    <ciudad>${data.ciudad}</ciudad>
    <fechaDeNacimiento>${data.fechaDeNacimiento}</fechaDeNacimiento>
    <listadoDeLenguajesProgramacion>${data.listadoDeLenguajesProgramacion.join(',')}</listadoDeLenguajesProgramacion>
</persona>`;

// Crear el archivo XML
fs.writeFile('persona.xml', xmlString, (err) => {
    if (err) {
        console.error(err);
    } else {
        console.log('Archivo XML creado exitosamente');
    }
});

fs.readFile('persona.xml', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    } else {
        console.log(data); // Imprime el contenido del archivo XML
    }
});
// Convertir el objeto a una cadena JSON
const jsonString = JSON.stringify(data);

// Crear el archivo JSON
fs.writeFile('persona.json', jsonString, (err) => {
    if (err) {
        console.error(err);
    } else {
        console.log('Archivo JSON creado exitosamente');
    }
});
// Leer archivo JSON
fs.readFile('persona.json', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    } else {
        const jsonData = JSON.parse(data);
        console.log(jsonData); // Imprime el contenido del archivo JSON como un objeto
    }
});