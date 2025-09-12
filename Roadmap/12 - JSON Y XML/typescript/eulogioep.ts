import * as fs from 'fs';
import * as xml2js from 'xml2js';

// Definición de la interfaz para la estructura de datos de la persona
interface Persona {
    nombre: string;
    edad: number;
    fechaNacimiento: string;
    lenguajesProgramacion: string[];
}

// Datos de ejemplo
const persona: Persona = {
    nombre: "Juan",
    edad: 30,
    fechaNacimiento: "1993-05-15",
    lenguajesProgramacion: ["TypeScript", "JavaScript", "Python"]
};

// Función para crear el archivo XML
function crearArchivoXML(datos: Persona): void {
    const builder = new xml2js.Builder();
    const xml = builder.buildObject({ persona: datos });
    fs.writeFileSync('datos.xml', xml);
    console.log("Archivo XML creado.");
}

// Función para crear el archivo JSON
function crearArchivoJSON(datos: Persona): void {
    fs.writeFileSync('datos.json', JSON.stringify(datos, null, 2));
    console.log("Archivo JSON creado.");
}

// Función para mostrar el contenido de un archivo
function mostrarContenidoArchivo(nombreArchivo: string): void {
    console.log(`Contenido del archivo ${nombreArchivo}:`);
    console.log(fs.readFileSync(nombreArchivo, 'utf8'));
}

// Función para borrar un archivo
function borrarArchivo(nombreArchivo: string): void {
    fs.unlinkSync(nombreArchivo);
    console.log(`El archivo ${nombreArchivo} ha sido borrado.`);
}

// Función para leer el archivo XML
async function leerXML(nombreArchivo: string): Promise<Persona> {
    const xmlData = fs.readFileSync(nombreArchivo, 'utf8');
    return new Promise((resolve, reject) => {
        xml2js.parseString(xmlData, (err, result) => {
            if (err) {
                reject(err);
            } else {
                resolve(result.persona as Persona);
            }
        });
    });
}

// Función para leer el archivo JSON
function leerJSON(nombreArchivo: string): Persona {
    const jsonData = fs.readFileSync(nombreArchivo, 'utf8');
    return JSON.parse(jsonData) as Persona;
}

// Función principal asíncrona
async function main(): Promise<void> {
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

    try {
        // Leer y transformar datos
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