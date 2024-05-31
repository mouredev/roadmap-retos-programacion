// Manejo de ficheros

let fs = require('fs')

let contenido = "Deyvid Marmolejo \n25 anos \nJavaScript"

// Crear el archivo .txt
fs.writeFile('Deyvid-10.txt', contenido, (error) =>
{
    if(error)
    {
        console.error("Se produjo un error al crear el archivo");        
    }
    else
    {
        console.log("Archivo creado correctamente");
    }
})

// Leer el archivo .txt
fs.readFile('Deyvid-10.txt', 'utf8', (error, cont) =>
{
    if(error)
    {
        console.error("Se produjo un error al crear el archivo");        
    }
    else
    {
        console.log("El contenido del archivo es:\n", cont);
    }
})
 
// Eliminar el archivo .txt
fs.unlink('Deyvid-10.txt', (error) =>
{
    if(error)
    {
        console.error("Se produjo un error al crear el archivo");        
    }
    else
    {
        console.log("Archivo eliminado correctamente correctamente");
    }
})