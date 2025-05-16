/*
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

EJERCICIO:
Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
- Nombre
- Edad
- Fecha de nacimiento
- Listado de lenguajes de programación
Muestra el contenido de los archivos.
Borra los archivos.

DIFICULTAD EXTRA (opcional):
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.
*/

const fs = require('fs');

const datos = {
    nombre: "Anderson",
    edad: 20,
    fechaNacimiento: "01/01/2005",
    lenguajes: ["JavaScript", "Python", "Java"]
};

// 🔥 JSON
function crearArchivoJSON() {
    const jsonContent = JSON.stringify(datos, null, 2); // Convertir a JSON con formato legible
    fs.writeFile("datos.json", jsonContent, (err) => {
        if (err) {
            console.error("Error al crear el archivo JSON:", err);
            return;
        }
        console.log("Archivo JSON creado con éxito. ✅");
        leerArchivoJSON();
    });
}

// 🔥 Leer
function leerArchivoJSON() {
    fs.readFile("datos.json", 'utf8', (err, data) => {
        if (err) {
            console.error("Error al leer el archivo JSON:", err);
            return;
        }
        console.log("Contenido del archivo JSON:");
        console.log(data);
        crearArchivoXML(); // Continuar con la creación del archivo XML
    });
}

// 🔥 Crear XML
function crearArchivoXML() {
    const xmlContent = `
<datos>
    <nombre>${datos.nombre}</nombre>
    <edad>${datos.edad}</edad>
    <fechaNacimiento>${datos.fechaNacimiento}</fechaNacimiento>
    <lenguajes>
        ${datos.lenguajes.map(lenguaje => `        <lenguaje>${lenguaje}</lenguaje>`).join("\n")}
    </lenguajes>
</datos>`;
    fs.writeFile("datos.xml", xmlContent, (err) => {
        if (err) {
            console.error("Error al crear el archivo XML:", err);
            return;
        }
        console.log("Archivo XML creado con éxito. ✅");
        leerArchivoXML();
    });
}

// 🔥 Leer XML
function leerArchivoXML() {
    fs.readFile("datos.xml", 'utf8', (err, data) => {
        if (err) {
            console.error("Error al leer el archivo XML:", err);
            return;
        }
        console.log("Contenido del archivo XML:");
        console.log(data);
        borrarArchivos(); // Borrar ambos archivos
    });
}

// 🔥 Borrar archivos
function borrarArchivos() {
    fs.unlink("datos.json", (err) => {
        if (err && err.code !== 'ENOENT') {
            console.error("Error al borrar el archivo JSON:", err);
        } else {
            console.log("Archivo JSON borrado con éxito. ✅");
        }
    });

    fs.unlink("datos.xml", (err) => {
        if (err && err.code !== 'ENOENT') {
            console.error("✖️ Error al borrar el archivo XML:", err);
        } else {
            console.log("Archivo XML borrado con éxito. ✅");
        }
    });
}

crearArchivoJSON();


// 🔥 Etra
// para iniciar el programa es necesario hacer:
// npm install xml2js

const fs = require('fs');
const xml2js = require('xml2js'); // Módulo para parsear XML

class Persona {
    constructor(nombre, edad, fechaNacimiento, lenguajes) {
        this.nombre = nombre
        this.edad = edad
        this.fechaNacimiento = fechaNacimiento
        this.lenguajes = lenguajes
    }

    mostrarDatos() {
        console.log("Datos de la persona:")
        console.log(`Nombre: ${this.nombre}`)
        console.log(`Edad: ${this.edad}`)
        console.log(`Fecha de nacimiento: ${this.fechaNacimiento}`)
        console.log(`Lenguajes: ${this.lenguajes.join(", ")}`)
    }
}

// Crear archivos iniciales
function crearArchivos() {
    const datos = {
        nombre: "Tu Nombre",
        edad: 25,
        fechaNacimiento: "01/01/1998",
        lenguajes: ["JavaScript", "Python", "Java"]
    };

    // Crear archivo JSON
    fs.writeFile("datos.json", JSON.stringify(datos, null, 2), (err) => {
        if (err) {
            console.error("Error al crear el archivo JSON:", err);
            return;
        }
        console.log("Archivo JSON creado con éxito.");
    });

    // Crear archivo XML
    const xmlContent = `
<datos>
    <nombre>${datos.nombre}</nombre>
    <edad>${datos.edad}</edad>
    <fechaNacimiento>${datos.fechaNacimiento}</fechaNacimiento>
    <lenguajes>
        ${datos.lenguajes.map(lenguaje => `        <lenguaje>${lenguaje}</lenguaje>`).join("\n")}
    </lenguajes>
</datos>`;
    fs.writeFile("datos.xml", xmlContent, (err) => {
        if (err) {
            console.error("Error al crear el archivo XML:", err);
            return;
        }
        console.log("Archivo XML creado con éxito.");
        leerArchivos();
    });
}

// Leer archivos y transformar en clase
function leerArchivos() {
    // Leer archivo JSON
    fs.readFile("datos.json", 'utf8', (err, jsonData) => {
        if (err) {
            console.error("Error al leer el archivo JSON:", err);
            return;
        }

        // Parsear JSON
        const datosJSON = JSON.parse(jsonData);

        // Leer archivo XML
        fs.readFile("datos.xml", 'utf8', (err, xmlData) => {
            if (err) {
                console.error("Error al leer el archivo XML:", err);
                return;
            }

            // Parsear XML
            const parser = new xml2js.Parser({ explicitArray: false });
            parser.parseString(xmlData, (err, result) => {
                if (err) {
                    console.error("Error al parsear el archivo XML:", err);
                    return;
                }

                const datosXML = {
                    nombre: result.datos.nombre,
                    edad: parseInt(result.datos.edad),
                    fechaNacimiento: result.datos.fechaNacimiento,
                    lenguajes: Array.isArray(result.datos.lenguajes.lenguaje)
                        ? result.datos.lenguajes.lenguaje
                        : [result.datos.lenguajes.lenguaje]
                };

                // Mostrar datos transformados
                console.log("\nDatos del archivo JSON:");
                const personaJSON = new Persona(
                    datosJSON.nombre,
                    datosJSON.edad,
                    datosJSON.fechaNacimiento,
                    datosJSON.lenguajes
                );
                personaJSON.mostrarDatos();

                console.log("\nDatos del archivo XML:");
                const personaXML = new Persona(
                    datosXML.nombre,
                    datosXML.edad,
                    datosXML.fechaNacimiento,
                    datosXML.lenguajes
                );
                personaXML.mostrarDatos();

                // Borrar archivos
                borrarArchivos();
            });
        });
    });
}

// Borrar archivos
function borrarArchivos() {
    fs.unlink("datos.json", (err) => {
        if (err && err.code !== 'ENOENT') {
            console.error("Error al borrar el archivo JSON:", err);
        } else {
            console.log("Archivo JSON borrado con éxito.");
        }
    });

    fs.unlink("datos.xml", (err) => {
        if (err && err.code !== 'ENOENT') {
            console.error("Error al borrar el archivo XML:", err);
        } else {
            console.log("Archivo XML borrado con éxito.");
        }
    });
}

crearArchivos();