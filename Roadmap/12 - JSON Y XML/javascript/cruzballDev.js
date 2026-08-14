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
/*
const fs = require("fs") // require("fs") importa el módulo File System de Node.js.Este módulo permite trabajar con archivos y carpetas.
                         // Lo guardamos en la constante fs para poder usar sus funciones.

// Los datos que van a tener los archivos
const persona = { // creamos el objeto persona
    nombre: "Antonio",
    edad: 47,
    fechaNacimiento: "1978-11-02",
    lenguajes: ["JavaScript", "Java", "Python", "C#"]
}

// Crear contenido JSON
 const jsonContenido = JSON.stringify(persona, null, 2) // JSON.stringify() convierte un objeto de JavaScript en texto con formato JSON. Recibe tres parámetros:
                                                       // persona → el objeto que queremos convertir; null → no queremos modificar ninguna propiedad; y 2 → agrega una indentación de 2 espacios para que sea más legible.


// creamos el archivo

fs.writeFileSync("persona.json", jsonContenido, "utf8") // writeFileSync() escribe un archivo. Parámetros: "persona.json" → nombre del archivo;
                                                      // jsonContenido → contenido que se escribirá; y "utf8" → codificación del texto.


// Mostrar un mensaje

console.log("¡Archivos creados correctamente!\n")

// Leer el archivo JSON

console.log("=== Contenido de persona.json ===")
console.log(fs.readFileSync("persona.json", "utf8"))

// Eliminar archivo
// fs.unlinkSync("persona.json")

// Mostrar mensaje final
console.log("¡Archivo eliminado correctamente!")
*/



// Crear contenido XML

// map() recorre cada elemento y genera un nuevo arreglo.
// join Une todos los elementos del arreglo en un solo texto. El separador es:\n → salto de línea, los espacios sirven para mantener la indentación.
// join tiene que tener dos espacios por cada etiqueta lenguaje y cuatro espacios extra
// porque ${persona.lenguajes está cuatro espacios más adentro que la etiqueta <lenguajes>.


/* const xmlContenido = `<?xml version="1.0" encoding="UTF-8"?>
    <persona>
        <nombre>${persona.nombre}</nombre>
        <edad>${persona.edad}</edad>
        <fechaNacimiento>${persona.fechaNacimiento}</fechaNacimiento>
        <lenguajes>
            ${persona.lenguajes
            .map((lenguaje) =>`<lenguaje>${lenguaje}</lenguaje>`)
            .join("\n            ")}
        </lenguajes>
    </persona>`

// creamos el archivo

fs.writeFileSync("persona.xml", xmlContenido, "utf8")

// Mostrar un mensaje

console.log("¡Archivos creados correctamente!\n")

// Leer el archivo XML
console.log(fs.readFileSync("persona.xml", "utf8"))
// Eliminar archivos
/* fs.unlinkSync("persona.xml") */

// Mostrar mensaje final
//console.log("¡Archivo eliminado correctamente!")

/*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
*/


// Con JSON

const fs = require("fs")

// clase personalizada

class Persona {
    constructor(nombre, edad, fechaNacimiento, lenguajes) {
        this.nombre = nombre
        this.edad = edad
        this.fechaNacimiento = fechaNacimiento
        this.lenguajes = lenguajes
    }
}

const persona = new Persona(
    "Juan",
    30,
    "1978-11-02",
    ["JavaScript", "Java", "Python", "C#"]
)

// Crear el JSON
fs.writeFileSync(
    "persona.json",
    JSON.stringify(persona, null, 2) // Convierte un objeto de JavaScript en una cadena JSON.
)

// Leer JSON
const jsonData = JSON.parse( // Convierte una cadena JSON en un objeto de JavaScript.
    fs.readFileSync("persona.json", "utf8")
)

// Crear un objeto de la clase persona, utilizando los datos leídos del JSON.
console.log("===================")
const personaJson = new Persona(
    jsonData.nombre,
    jsonData.edad,
    jsonData.fechaNacimiento,
    jsonData.lenguajes
)

// Mostrar el objeto
console.log("Objeto creado desde el JSON")
console.log(personaJson)

// Eliminar el objeto
fs.unlinkSync("persona.json")

// Con XML

// Crear el XML

const xml2js = require("xml2js") // traemos la libreria.


// Crear un objeto de la clase persona, utilizando los datos leídos del XML.
// El map() genera cada <lenguaje> con esos 8 espacios.
// El join("\n") los separa en líneas.
const xml = `<?xml version="1.0" encoding="UTF-8"?>
<persona>
    <nombre>${persona.nombre}</nombre>
    <edad>${persona.edad}</edad>
    <fechaNacimiento>${persona.fechaNacimiento}</fechaNacimiento>
    <lenguajes>
${persona.lenguajes
    .map(elemento => `        <lenguaje>${elemento}</lenguaje>`) // Alinear .map() y join() con las etiquetas para que salga todo alineado y luego en el template literal del .map añadir 8 espacios, porque es segunda anidación.
    .join("\n")}
    </lenguajes>
</persona>
`

// Guardar el XML
fs.writeFileSync("persona.xml", xml, "utf8")

// Leer XML
const parser = new xml2js.Parser() // traductor para trabajar con xml
const xmlLeido = fs.readFileSync("persona.xml", "utf8") // leemos el archivo

parser.parseString(xmlLeido, (error, resultado) => { // Convertimos el string a objeto mediante paseString aunque pueda parecer lo contrario. parse = analizar.

    if(error) {
        console.log(error)
        return
    }

    const p = resultado.persona

    const personaXml = new Persona(
        p.nombre[0],
        Number(p.edad[0]),
        p.fechaNacimiento[0],
        p.lenguajes[0].lenguaje
    )
    // Mostrar el objeto
    console.log("Objeto creado desde el XML")
    console.log(personaXml)
})

// Eliminar el objeto
fs.unlinkSync("persona.xml")