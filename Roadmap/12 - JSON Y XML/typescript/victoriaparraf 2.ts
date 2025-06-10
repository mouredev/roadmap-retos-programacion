import * as fs from 'fs';
import { create } from 'xmlbuilder2';

// Datos a guardar
const data = {
    nombre: 'Victoria Parra',
    edad: 25,
    fechaDeNacimiento: '1999-05-15',
    lenguajesDeProgramacion: ['TypeScript', 'JavaScript', 'Python', 'Java']
};

// Función para crear archivo JSON
function crearArchivoJSON(filename: string, data: object): void {
    const jsonData = JSON.stringify(data, null, 2);
    fs.writeFileSync(filename, jsonData, 'utf8');
    console.log(`Archivo JSON ${filename} creado.`);
}

// Función para crear archivo XML
function crearArchivoXML(filename: string, data: any): void {
    const doc = create({ version: '1.0' })
        .ele('datos')
        .ele('nombre').txt(data.nombre).up()
        .ele('edad').txt(data.edad.toString()).up()
        .ele('fechaDeNacimiento').txt(data.fechaDeNacimiento).up()
        .ele('lenguajesDeProgramacion');
    
    data.lenguajesDeProgramacion.forEach((lenguaje: string) => {
        doc.ele('lenguaje').txt(lenguaje).up();
    });

    doc.up();
    const xmlData = doc.end({ prettyPrint: true });
    fs.writeFileSync(filename, xmlData, 'utf8');
    console.log(`Archivo XML ${filename} creado.`);
}

// Crear archivos JSON y XML
const jsonFilename = 'victoriaparraf.json';
const xmlFilename = 'victoriaparraf.xml';

crearArchivoJSON(jsonFilename, data);
crearArchivoXML(xmlFilename, data);

// Leer e imprimir el contenido de los archivos
function leerArchivo(filename: string): void {
    const content = fs.readFileSync(filename, 'utf8');
    console.log(`Contenido de ${filename}:`);
    console.log(content);
}

leerArchivo(jsonFilename);
leerArchivo(xmlFilename);

// Borrar archivos
function borrarArchivo(filename: string): void {
    fs.unlinkSync(filename);
    console.log(`Archivo ${filename} borrado.`);
}

borrarArchivo(jsonFilename);
borrarArchivo(xmlFilename);
