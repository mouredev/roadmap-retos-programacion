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

const fs = require("fs/promises");

async function main() {
  const data = {
    nombre: "Juan",
    edad: 30,
    fechaNacimiento: "1994-05-15",
    lenguajes: ["JavaScript", "Python", "Java"],
  };

  try {
    // Crear JSON
    const jsonData = JSON.stringify(data, null, 2);
    await fs.writeFile("datos.json", jsonData);

    // Crear XML
    const xmlData = `
<persona>
    <nombre>${data.nombre}</nombre>
    <edad>${data.edad}</edad>
    <fechaNacimiento>${data.fechaNacimiento}</fechaNacimiento>
    <lenguajes>
        ${data.lenguajes.map((lang) => `<lenguaje>${lang}</lenguaje>`).join("")}
    </lenguajes>
</persona>`;
    await fs.writeFile("datos.xml", xmlData);

    // Leer y mostrar contenido
    const readJsonData = await fs.readFile("datos.json", "utf-8");
    console.log("Contenido del archivo JSON:", readJsonData);

    const readXmlData = await fs.readFile("datos.xml", "utf-8");
    console.log("Contenido del archivo XML:", readXmlData);

    // Borrar archivos
    await fs.unlink("datos.json");
    await fs.unlink("datos.xml");
    console.log("Archivos borrados con éxito.");
  } catch (error) {
    console.error("Error:", error);
  }
}

main();
