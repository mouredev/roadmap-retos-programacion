const fs = require('fs');
const xml2js = require('xml2js');

// Datos de ejemplo
const persona = {
    nombre: "Juan",
    edad: 30,
    fechaNacimiento: "1993-05-15",
    lenguajesProgramacion: ["JavaScript", "Python", "Ruby"]
};

// Función para crear el archivo XML
function crearArchivoXML(datos) {
    const builder = new xml2js.Builder();
    const xml = builder.buildObject({ persona: datos });
    fs.writeFileSync('datos.xml', xml);
    console.log("Archivo XML creado.");
}

// Función para crear el archivo JSON
function crearArchivoJSON(datos) {
    fs.writeFileSync('datos.json', JSON.stringify(datos, null, 2));
    console.log("Archivo JSON creado.");
}

// Función para mostrar el contenido de un archivo
function mostrarContenidoArchivo(nombreArchivo) {
    console.log(`Contenido del archivo ${nombreArchivo}:`);
    console.log(fs.readFileSync(nombreArchivo, 'utf8'));
}

// Función para borrar un archivo
function borrarArchivo(nombreArchivo) {
    fs.unlinkSync(nombreArchivo);
    console.log(`El archivo ${nombreArchivo} ha sido borrado.`);
}

// Función para leer el archivo XML
function leerXML(nombreArchivo) {
    const xmlData = fs.readFileSync(nombreArchivo, 'utf8');
    return new Promise((resolve, reject) => {
        xml2js.parseString(xmlData, (err, result) => {
            if (err) {
                reject(err);
            } else {
                resolve(result.persona);
            }
        });
    });
}

// Función para leer el archivo JSON
function leerJSON(nombreArchivo) {
    const jsonData = fs.readFileSync(nombreArchivo, 'utf8');
    return JSON.parse(jsonData);
}

// Función principal asíncrona
async function main() {
    // Crear y mostrar archivo XML
    crearArchivoXML(persona);
    mostrarContenidoArchivo('datos.xml');

    // Crear y mostrar archivo JSON
    crearArchivoJSON(persona);
    mostrarContenidoArchivo('datos.json');

    // Borrar archivos
    borrarArchivo('datos.xml');
    borrarArchivo('datos.json');

    // DIFICULTAD EXTRA
    // Crear archivos nuevamente para la lectura
    crearArchivoXML(persona);
    crearArchivoJSON(persona);

    // Leer y transformar datos
    try {
        const personaXML = await leerXML('datos.xml');
        const personaJSON = leerJSON('datos.json');

        console.log("\nDatos leídos del XML:");
        console.log(personaXML);
        console.log("\nDatos leídos del JSON:");
        console.log(personaJSON);
    } catch (error) {
        console.error("Error al leer los archivos:", error);
    }

    // Borrar archivos nuevamente
    borrarArchivo('datos.xml');
    borrarArchivo('datos.json');
}

// Ejecutar la función principal
main().catch(console.error);