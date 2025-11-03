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

// EJERCICIO

const fs = require('fs')



const datos = {
    nombre: "Esteban",
    edad: 30,
    fechaNacimiento: "01/05/1987",
    lenguajes: ["Javascript", "Python", "Java"]
}

//JSON
function crearArchivoJSON(){
    const jsonContent = JSON.stringify(datos, null, 2)
    fs.writeFile("datos.json", jsonContent, (error) => {
        if(error){
            console.error("Error al cerar el archivo JSON:", error)
            return
        }
        console.log("Archivo JSON creado con exito")
        leerArchivoJson()
    })
}
function leerArchivoJson(){
    fs.readFile("datos.json", "utf8", (error, data)=> {
        if(error){
            console.error("Error al cerar el archivo JSON:", error)
            return
        }
        console.log("Data:")
        console.log(data)
    })

}
function borrarJSON(){
    fs.unlink("datos,json", (error) => {
        if (error && error.code !== 'ENOENT') {
            console.error("Error al borrar el archivo JSON:", error);
        } else {
            console.log("Archivo JSON borrado con éxito");
        }
    })
}


//XML

function crearArchivoXML(){
    const xmlContent = `
<datos>
    <nombre>${datos.nombre}</nombre>
    <edad>${datos.edad}</edad>
    <fechaNacimiento>${datos.fechaNacimiento}</fechaNacimiento>
    <lenguajes>
        ${datos.lenguajes.map(lenguaje => `        <lenguaje>${lenguaje}</lenguaje>`).join("\n")}
    </lenguajes>
</datos>`
    fs.writeFile("datos.xml", xmlContent, (error) => {
       if (error) {
            console.error("Error al crear el archivo XML:", error)
            return
        } 
        console.log("Archivo XML creado con éxito")
        leerArchivoXML()
    })
}
function leerArchivoXML(){
    fs.readFile("datos.xml", "utf8", (error,data)=> {
        if (error) {
            console.error("Error al crear el archivo XML:", error)
            return
        } 
        console.log("Datos: ")
        console.log(data)
    })
}
function borrarXML(){
    fs.unlink("datos.xml", (error)=> {
        if (error && error.code !== 'ENOENT') {
            console.error("✖️ Error al borrar el archivo XML:", error)
        } else {
            console.log("Archivo XML borrado con éxito")
        }
    })
}

crearArchivoJSON()
crearArchivoXML()
borrarJSON()
borrarXML()

// EXTRA

const xml2js = require('xml2js')

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

function crearArchivos() {
    const datos = {
        nombre: "Tu Nombre",
        edad: 25,
        fechaNacimiento: "01/01/1998",
        lenguajes: ["JavaScript", "Python", "Java"]
    };

    fs.writeFile("datos.json", JSON.stringify(datos, null, 2), (err) => {
        if (err) {
            console.error("Error al crear el archivo JSON:", err);
            return;
        }
        console.log("Archivo JSON creado con éxito.");
    });

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

function leerArchivos() {
    fs.readFile("datos.json", 'utf8', (err, jsonData) => {
        if (err) {
            console.error("Error al leer el archivo JSON:", err);
            return;
        }

        const datosJSON = JSON.parse(jsonData);

        fs.readFile("datos.xml", 'utf8', (err, xmlData) => {
            if (err) {
                console.error("Error al leer el archivo XML:", err);
                return;
            }

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

                borrarArchivos();
            });
        });
    });
}

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
