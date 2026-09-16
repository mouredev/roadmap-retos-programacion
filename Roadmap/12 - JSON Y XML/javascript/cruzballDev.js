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

const fs = require("fs");

const persona = {
    nombre: "Manolo",
    edad: 47,
    fechaNacimiento: "1978-11-02",
    lenguajes: ["JavaScript", "Python", "Java", "C#"]
}

const jsContenido = JSON.stringify(persona, null, 2) // persona → el objeto que queremos convertir; null → no queremos modificar ninguna propiedad; 
                                     // y 2 → agrega una indentación de 2 espacios para que sea más legible.


fs.writeFileSync("pesona.json", jsContenido, "utf8") // Parámetros:"persona.json" → nombre del archivo; jsonContent → contenido que se escribirá;
                                                     // y "utf8" → codificación del texto.



/*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
*/

