const fs = require ("fs");

//Creación de datos para almacenar
const datos = {
    nombre: "Maria",
    edad: 33,
    fechaNacimiento: "8/12/1990",
    lenguajes: ["HTML", "CSS", "JavaScript"]
};

//Funciones para crear ambos archivos
function escribirXML (datos) {
    const xmlDatos = `<?xml version="1.0" encoding="UTF-8"?>
    <datos>
        <nombre>${datos.nombre}</nombre>
        <edad>${datos.edad}</edad>
        <fechaNacimiento>${datos.fechaNacimiento}</fechaNacimiento>
        <lenguajes>
        ${datos.lenguajes.map(lenguaje => `<lenguaje>${lenguaje}</lenguaje>`).join("\n    ")}
        </lenguajes>
    </datos>`;

    fs.writeFileSync("datos.xml", xmlDatos);
    console.log("Archivo XML creado.");
}

function escribirJSON (datos) {
    fs.writeFileSync("datos.json", JSON.stringify(datos, null, 2));
    console.log("Archivo JSON creado.")
}

escribirJSON(datos);
escribirXML(datos);

//Funciones para leer y mostrar el contenido de los archivos
function mostrarXML() {
    const xmlDatos = fs.readFileSync("datos.xml", "utf-8");
    console.log("Contenido del archivo XML: " + xmlDatos);

}

function mostrarJSON () {
    const jsonDatos = fs.readFileSync("datos.json", "utf-8");
    console.log("Contenido del archivo JSON: " + jsonDatos);
}

mostrarXML();
mostrarJSON();

//Funciones para borrar archivos
function borrarArchivos () {
    fs.unlinkSync("datos.xml");
    fs.unlinkSync("datos.json");
    console.log("Archivos borrados con éxito.")
}

borrarArchivos();