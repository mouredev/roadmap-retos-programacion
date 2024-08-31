

// MANEJO DE FICHEROS ====================

/*

En JavaScript se puede manejar ficheros utilizando 
el módulo fs trabajando en Node.js

es un módulo incorporado que proporciona funciones 
para trabajar con el sistema de archivos del sistema 
operativo. La abreviatura "fs" significa "file system" (sistema de archivos en inglés).

Este módulo fs permite realizar operaciones como leer archivos, 
escribir en archivos, crear directorios, eliminar archivos, entre 
otras operaciones relacionadas con el sistema de archivos del servidor 
o del sistema donde se esté ejecutando Node.js.

Algunos de los métodos más comunes que proporciona el módulo fs incluyen:

fs.readFile(): Lee el contenido de un archivo.
fs.writeFile(): Escribe datos en un archivo.
fs.appendFile(): Añade datos al final de un archivo.
fs.unlink(): Borra un archivo.
fs.readdir(): Lee el contenido de un directorio.
fs.mkdir(): Crea un nuevo directorio.

*/

const fs = require('fs');

// Nombre del archivo y contenido a escribir
const filename = 'ArticKun.txt';
const content = `ArticKun.\n34\nJavascript.`;

// Escribir en el archivo
fs.writeFile(filename, content, (err) => {
  if (err) {
    console.error('Error al crear el archivo:', err);
    return;
  }
  console.log(`Archivo '${filename}' creado con éxito.`);
  
  // Leer el contenido del archivo
  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) {
      console.error('Error al leer el archivo:', err);
      return;
    }
    console.log(`Contenido del archivo '${filename}':\n${data}`);
    
    // Borrar el archivo
    fs.unlink(filename, (err) => {
      if (err) {
        console.error('Error al borrar el archivo:', err);
        return;
      }
      console.log(`Archivo '${filename}' borrado con éxito.`);
    });
  });
});


//EXTRA
//Pendiente ....