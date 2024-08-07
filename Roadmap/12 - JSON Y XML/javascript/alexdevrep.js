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

//Importamos las librerías necesarias

const fs = require('fs')
/*
    La función create es exportada por el módulo y esta función crea y retorna un nodo de documento XML en blanco.

    Un nodo de documento XML es el contenedor principal que organiza y estructura todos los elementos
    de un documento XML
*/
const { create } = require('xmlbuilder') 


//Creamos el documento XML

const xmlDoc = create({ version: '1.0' })
  .ele('raiz') //La función ele crea y devuelve un nodo
    .ele('Nombre', 'Alejandro').up()  //La función up devuelve el nodo de elemento elemento padre
    .ele('Edad', '24') .up()
    .ele('Lenguajes','javaScript')
    
  .end({ prettyPrint: true }) //End convierte el documento XML en su representación de cadena

//Especificamos el nombre del documento XML
const filePath = 'prueba.xml'

// Escribir el contenido en el archivo XML
fs.writeFile(filePath, xmlDoc, function (err) {
    if (err) {
      console.error('Error al escribir el archivo XML:', err)
    } else {
      console.log('El archivo XML ha sido creado correctamente en:', filePath)
    }
  
  
  })

//Mostramos el contenido del archivo XML
console.log(xmlDoc)

//Creamos el documento JSON
const jsonObject={
    nombre: 'Alejandro',
    edad: 24,
    lenguajes: ['JavaScript']
}

const jsonString= JSON.stringify(jsonObject,null,2)

const archivo = 'prueba.json'

// Escribir el contenido en el archivo json
fs.writeFile(archivo, jsonString, function (err) {
    if (err) {
      console.error('Error al escribir el archivo json:', err)
    } else {
      console.log('El archivo json ha sido creado correctamente en:', archivo)
    }
  
  
  })

//Mostramos el contenido del archivo JSON
console.log(jsonObject)

//Borramos los ficheros creados
function errorBorrar(err){
    if(err){
        console.log("Error al borrar el fichero",err)
    }
    else{
        console.log("Archivo borrado exitosamente")
    }
}
//Borramos el archivo Json
fs.unlink(archivo,errorBorrar)
//Borramos el archivo XML 
fs.unlink(filePath,errorBorrar)