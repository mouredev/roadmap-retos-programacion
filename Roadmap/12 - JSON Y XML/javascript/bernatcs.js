// ** EJERCICIO

const fs = require('node:fs').promises
const { parse } = require('node:path')
const xmlbuilder = require('xmlbuilder')
const { DOMParser } = require('xmldom');


const data = {
    Nombre: 'Bernat',
    Edad: '29',
    FechaDeNacimiento: '29.02.1995',
    ListadoDeLenguajes: ['MaxMSP', 'JS', 'SwiftUI']
}

// JSON

const dataDocument = JSON.stringify(data, null, 2)

fs.writeFile('datos.json', dataDocument, (err) => {
    if (err) {
        console.error('Error al guardar el archivo JSON', err)
    } else {
        // console.log('Se ha guadado correctamente el archivo JSON')
    }
})

// XML

const xml = xmlbuilder.create('persona')
    .ele('nombre', data.Nombre).up()
    .ele('edad', data.Edad).up()
    .ele('fechadenacimiento', data.FechaDeNacimiento).up()
    .ele('listadodelenguajes')
        .ele('listadodelenguajes', data.ListadoDeLenguajes[0]).up()
        .ele('listadodelenguajes', data.ListadoDeLenguajes[1]).up()
        .ele('listadodelenguajes', data.ListadoDeLenguajes[2]).up()
        .ele('listadodelenguajes', data.ListadoDeLenguajes[3]).up()
    .end({ pretty: true });

fs.writeFile('datos.xml', xml, (err) => {
    if (err) {
        console.error('Error al guardar el archivo XML:', err)
    } else {
        // console.log('Se ha guadado correctamente el archivo XML')
    }
});

// ** DIFICULTAD EXTRA ** ----------------------------------------------------------------------------------------------------------------------------------------------------

// JSON

async function leerJSON(ruta_al_archivo) {
    try {
        const data = await fs.readFile(ruta_al_archivo, 'utf8');
        return JSON.parse(data);
    } catch (err) {
        console.error('Error al leer o parsear el archivo JSON:', err);
        throw err;
    }
}

async function guardarJSON(ruta_al_archivo, array) {
    try {
        const jsonData = await leerJSON(ruta_al_archivo);
        array.push(jsonData);
        console.log('Los archivos del JSON han sido guardados correctamente');
    } catch (error) {
        console.error('No ha sido posible guardar los archivos', error);
    }
}

let jsonData = []

guardarJSON('datos.json', jsonData).then(() => {
    console.log(jsonData);
}).catch(err => {
    console.error('Error al ejecutar guardarJSON:', err);
});


// XML --> Hay un problema a la hora de instalar las librerías de lectura y guardado de xml, por eso da error.

async function leerXML(ruta_al_archivo) {
    try {
        const xmlString = await fs.readFile(ruta_al_archivo, 'utf8');
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(xmlString, 'text/xml');

        // Verificar si se encontraron elementos 'persona'
        const personas = xmlDoc.getElementsByTagName('persona');
        if (personas.length === 0) {
            console.error('No se encontraron elementos <persona> en el archivo XML.');
            return [];  // Devolver un array vacío en caso de no encontrar elementos
        }

        const XMLData = [];

        for (let persona of personas) {
            const nombre = persona.getElementsByTagName('nombre')[0].textContent;
            const edad = persona.getElementsByTagName('edad')[0].textContent;
            const fechaDeNacimiento = persona.getElementsByTagName('fechadenacimiento')[0].textContent;

            const listadoDeLenguajes = [];
            const lenguajes = persona.getElementsByTagName('listadodelenguajes')[0].getElementsByTagName('listadodelenguajes');
            for (let lenguaje of lenguajes) {
                listadoDeLenguajes.push(lenguaje.textContent);
            }

            XMLData.push({
                nombre,
                edad,
                fechaDeNacimiento,
                listadoDeLenguajes
            });
        }

        return XMLData;

    } catch (err) {
        console.error('Error al leer o parsear el archivo XML:', err);
        throw err;
    }
}

async function guardarXML(ruta_al_archivo, array) {
    try {
        const jsonData = await leerXML(ruta_al_archivo);
        array.push(...jsonData); // Utilizamos spread operator para añadir los elementos individuales
        console.log('Los datos del XML han sido guardados correctamente');
    } catch (error) {
        console.error('No ha sido posible guardar los datos del XML', error);
    }
}

let XMLData = [];

const archivoXML = 'datos.xml';

guardarXML(archivoXML, XMLData)
    .then(() => {
        console.log('Datos finales del XML:', XMLData);
    })
    .catch(err => {
        console.error('Error al ejecutar guardarXML:', err);
    });