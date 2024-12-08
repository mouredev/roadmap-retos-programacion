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

const data = {
    nombre: 'Caterina Rodríguez',
    edad: 25,
    fechaNacimiento: '12-08-1999',
    lenguajes: ['JavaScript', 'Python', 'Java']
};

const crearJSON = (data) => {
    const jsonContent = JSON.stringify(data);
    console.log(jsonContent);
    fs.writeFileSync("miJson.json", jsonContent);
}

const crearXML = (data) => {
    let xmlContent = '<?xml version="1.0" encoding="UTF-8"?>\n';
    xmlContent += '<persona>\n';
    xmlContent += '\t<nombre>' + data.nombre + '</nombre>\n';
    xmlContent += '\t<edad>' + data.edad + '</edad>\n';
    xmlContent += '\t<fechaNacimiento>' + data.fechaNacimiento + '</nacimiento>\n';
    xmlContent += '\t<lenguajes>\n';
    data.lenguajes.forEach(lenguaje => {
        xmlContent += `\t\t<lenguaje>${lenguaje}</lenguaje>\n`;
    });
    xmlContent += '\t</lenguajes>\n';
    xmlContent += '</persona>';
    console.log(xmlContent);
    fs.writeFileSync('miXML.xml', xmlContent);
}

crearJSON(data);
crearXML(data);