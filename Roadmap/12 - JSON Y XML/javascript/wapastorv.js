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

/* DIFICULTAD EXTRA (opcional):
* Utilizando la lógica de creación de los archivos anteriores, crea un
* programa capaz de leer y transformar en una misma clase custom de tu 
* lenguaje los datos almacenados en el XML y el JSON.
* Borra los archivos.
*/

// Clase Persona
class Persona {
    constructor(nombre, edad, ciudad, fechaDeNacimiento, listadoDeLenguajesProgramacion) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
        this.fechaDeNacimiento = fechaDeNacimiento;
        this.listadoDeLenguajesProgramacion = listadoDeLenguajesProgramacion;
    }
}

// Leer el archivo XML

fs.readFile('persona.xml', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    } else {
        // Convertir XML a JSON
        const xml2js = require('xml2js');
        xml2js.parseString(data, (err, result) => {
            if (err) {
                console.error(err);
            } else {
                const personaXml = result.persona;
                const persona = new Persona(
                    personaXml.nombre[0],
                    parseInt(personaXml.edad[0]),
                    personaXml.ciudad[0],
                    personaXml.fechaDeNacimiento[0],
                    personaXml.listadoDeLenguajesProgramacion[0].split(',')
                );
                console.log(persona);
            }
        });
    }
});

// Leer el archivo JSON
fs.readFile('persona.json', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    } else {
        const jsonData = JSON.parse(data);
        const persona = new Persona(
            jsonData.nombre,
            jsonData.edad,
            jsonData.ciudad,
            jsonData.fechaDeNacimiento,
            jsonData.listadoDeLenguajesProgramacion
        );
        console.log(persona);
    }
});

// Borrar los archivos (opcional)
fs.unlink('persona.xml', (err) => {
    if (err) {
        console.error(err);
    } else {
        console.log('Archivo XML eliminado');
    }
});
fs.unlink('persona.json', (err) => {
    if (err) {
        console.error(err);
    } else {
        console.log('Archivo JSON eliminado');
    }
});

// Otra forma de hacerlo


/*
const fs = require('fs');
const xml2js = require('xml2js');

class Persona {
    constructor(nombre, edad, hobbies, ciudad, pais) {
        this.nombre = nombre;
        this.edad = edad;
        this.hobbies = hobbies;
        this.ciudad = ciudad;
        this.pais = pais;
    }
}

function unificarDatos(xmlData, jsonData) {
    const personaXml = new Persona(
        xmlData.persona.nombre[0],
        parseInt(xmlData.persona.edad[0]),
        xmlData.persona.hobbies[0].hobby
    );
    const personaJson = new Persona(    
        jsonData.nombre,
        jsonData.edad,
        [], // Inicializamos hobbies como un array vacío
        jsonData.ciudad,
        jsonData.pais
    );

    // Combinar hobbies:
    personaUnificada = { ...personaXml, ...personaJson };
    personaUnificada.hobbies = [...personaXml.hobbies, ...personaJson.hobbies];

    return personaUnificada;
}

// Leer el archivo XML
fs.readFile('persona.xml', 'utf8', (err, xmlData) => {
    if (err) throw err;

    // Convertir XML a JSON
    xml2js.parseString(xmlData, (err, result) => {
        if (err) throw err;

        // Leer el archivo JSON
        fs.readFile('persona.json', 'utf8', (err, jsonData) => {
            if (err) throw err;

            jsonData = JSON.parse(jsonData);

            // Unificar los datos
            const personaUnificada = unificarDatos(result, jsonData);
            console.log(personaUnificada);

            // Borrar los archivos (opcional)
            /*fs.unlink('persona.xml', (err) => {
                if (err) throw err;
                console.log('Archivo XML eliminado');
            });
            fs.unlink('persona.json', (err) => {
                if (err) throw err;
                console.log('Archivo JSON eliminado');
            });
        });
    });
});
*/