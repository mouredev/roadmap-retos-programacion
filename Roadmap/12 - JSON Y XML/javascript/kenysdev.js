/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#12 JSON Y XML
---------------------------------------
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

// ________________________________________________________
import { writeFile, readFile, unlink } from "fs/promises";
import { extname } from "path";
import { parseStringPromise, Builder } from "xml2js";

// Datos iniciales
const dictUser = {
    name: "Ken",
    age: 121,
    dob: "1903-03-19",
    prog_langs: ["cs", "py", "vb", "rs", "js"],
};

(async () => {
    try {``
        //____________________________________
        // * JSON

        // Serialización: Convertir objeto a JSON
        const jsonUser = JSON.stringify(dictUser, null, 4);

        // Crear archivo JSON
        await writeFile("user.json", jsonUser, "utf8");
        console.log("Archivo JSON creado.");

        // Deserialización: Leer y convertir JSON a objeto
        const jsonData = await readFile("user.json", "utf8");
        const parsedJson = JSON.parse(jsonData);
        console.log("Objeto cargado desde JSON:", parsedJson);

        //____________________________________
        // * XML

        // Serialización: Crear XML a partir de objeto
        const builder = new Builder();
        const xmlUser = builder.buildObject({ user: dictUser });

        // Crear archivo XML
        await writeFile("user.xml", xmlUser, "utf8");
        console.log("Archivo XML creado.");

        // Deserialización: Leer y convertir XML a objeto
        const xmlData = await readFile("user.xml", "utf8");
        const parsedXml = await parseStringPromise(xmlData);
        console.log("Objeto cargado desde XML:", parsedXml.user);

        //____________________________________
        // DIFICULTAD EXTRA

        class XmlOrJson {
            constructor(filePath) {
                this.filePath = filePath;
                this.extension = extname(filePath).toLowerCase();
                this.data = {};
            }

            async asDict() {
                try {
                    if (this.extension === ".json") {
                        const jsonContent = await readFile(this.filePath, "utf8");
                        this.data = JSON.parse(jsonContent);
                        console.log("Archivo JSON cargado correctamente.");
                    } else if (this.extension === ".xml") {
                        const xmlContent = await readFile(this.filePath, "utf8");
                        const parsedXml = await parseStringPromise(xmlContent);
                        this.data = parsedXml.user;
                        console.log("Archivo XML cargado correctamente.");
                    } else {
                        throw new Error("Extensión de archivo no soportada.");
                    }
                    return this.data;
                } catch (error) {
                    console.error("Error al cargar archivo:", error.message);
                }
            }
        }

        //____________________________________
        console.log("\nDIFICULTAD EXTRA\n");

        // Leer JSON
        const jsonFile = new XmlOrJson("user.json");
        const jsonDict = await jsonFile.asDict();
        console.log("Datos desde JSON:", jsonDict);

        // Leer XML
        const xmlFile = new XmlOrJson("user.xml");
        const xmlDict = await xmlFile.asDict();
        console.log("Datos desde XML:", xmlDict);

        // Eliminar archivos
        await unlink("user.json");
        await unlink("user.xml");
        console.log("Archivos eliminados.");
    } catch (error) {
        console.error("Error general:", error.message);
    }
})();
