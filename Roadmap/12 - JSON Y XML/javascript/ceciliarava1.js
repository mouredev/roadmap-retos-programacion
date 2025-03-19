/*
 Desarrolla un programa capaz de crear un archivo XML y JSON que guarde
 - Nombre
 - Edad
 - Fecha de nacimiento
 - Listado de lenguajes de programación
 Muestra el contenido de los archivos.
 Borra los archivos.
 */

const fs = require("fs")
const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

function createFile(name, age, dateOfBirth, programmingLanguages, extension) {
    if (extension == 'XML' || extension == 'JSON'){
        fs.appendFile(
            `person.${extension}`,
            `Name: ${name} \nAge: ${age} \nDate of birth: ${dateOfBirth} \nProgramming languages: ${programmingLanguages}`,
            (err) => {
                if (err) throw err
            }
        )
    } else {
        console.log('Type of extension not supported')
    }
}

function deleteFile(extension) {
    fs.unlink(`person.${extension}`, (err) => {
        if (err) throw err
        console.log(`File ${extension} deleted!`)
    })
}

function showFile(extension) {
    fs.readFile(`person.${extension}`, (err, data) => {
        if (err) throw err
        console.log(data.toString())
        deleteFile('XML')
        rl.close()
    })
}

createFile("Lia", 22, "13/09/20", "python, rust", 'XML')
showFile('XML')


/*
 Utilizando la lógica de creación de los archivos anteriores, crea un
 programa capaz de leer y transformar en una misma clase custom de tu 
 lenguaje los datos almacenados en el XML y el JSON.
 Borra los archivos.
 */
