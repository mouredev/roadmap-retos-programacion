/*
<-------------- Manejo de ficheros -------------->
Para manejar ficheros Node.js nos ofrece un módulo conocido como "fs" (File System) que nos permite interactuar
con los archivos del sistema; este módulo permite realizar procesos como crear archivos, escribir en ellos,
leerlos, renombrarlos, hacer copias, eliminarlos, etc.
*/

// Requerimos el módulo "fs" de Node.js y lo guardamos en una cosntante

const fs = require('fs')

// Datos para agregar al nuevo fichero llamado "seandsun.txt"

const datos = [
  'Nombre: Marisol',
  'Edad: 26',
  'Lenguaje de programación favorito: javascript'
]

// Crear archivo "seandsun.txt" y escribir los datos en él

fs.writeFile('seandsun.txt', datos.join('\n'), (error) => {
  if(error) {
    console.log(`Error: ${error}`)
  } else {
    console.log('Se ha creado el archivo correctamente')
  }
})

// Leer la información del archivo "seandsun.txt"

fs.readFile('seandsun.txt', 'utf-8', (error, data) => {
  if(!error) {
    console.log(data)
  } else {
    console.log(`Error: ${error}`)
  }
})

// Eliminar el archivo "seandsun.txt"

fs.unlink('seandsun.txt', (error) => {
  if(error) {
    console.log(`Error: ${error}`)    
  } else {
    console.log('Archivo borrado exitosamente')
  }
})