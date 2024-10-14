/*
  *  #12 JSON Y XML
*/

const fs = require('fs').promises;

// Datos a guardar
const datos = {
    nombre: 'cesar-ch',
    edad: 3,
    fechaNacimiento: '2021-02-03',
    lenguajes: ['JavaScript', 'Python', 'Java']
};

async function main() {
    // Guardar en archivo XML
    const datosXML = `<?xml version="1.0" encoding="UTF-8"?>
    <datos>
      <nombre>${datos.nombre}</nombre>
      <edad>${datos.edad}</edad>
      <fechaNacimiento>${datos.fechaNacimiento}</fechaNacimiento>
      <lenguajes>${datos.lenguajes.join(',')}</lenguajes>
    </datos>`;
    await fs.writeFile('datos.xml', datosXML);
    console.log('Archivo XML creado');

    // Guardar en archivo JSON
    const datosJSON = JSON.stringify(datos, null, 2);
    await fs.writeFile('datos.json', datosJSON);
    console.log('Archivo JSON creado');

    /*
       * DIFICULTAD EXTRA
    */

    // Leer archivo XML
    const xmlData = await fs.readFile('datos.xml', 'utf8');
    console.log('Contenido del archivo XML:', xmlData);

    // Leer archivo JSON
    const jsonData = await fs.readFile('datos.json', 'utf8');
    console.log('Contenido del archivo JSON:', jsonData);

    // Borrar archivo XML
    await fs.unlink('datos.xml');
    console.log('Archivo XML eliminado');

    // Borrar archivo JSON
    await fs.unlink('datos.json');
    console.log('Archivo JSON eliminado');
}
main();