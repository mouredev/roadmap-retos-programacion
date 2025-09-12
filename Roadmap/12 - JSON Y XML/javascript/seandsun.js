// <-------------- json -------------->

// Requerimos el módulo "fs" de Node.js y lo guardamos en una cosntante
const fs = require('fs')

// Datos para agregar al nuevo fichero llamado "seandsun.json"
const datos = {
  nombre: "Marisol",
  edad: 26,
  fechaDeNacimiento: "11/07/98",
  lenguajesDeProgramacion: [
    "javascript", "python", "java"
  ]
}

// Convertir objeto tipo js a objeto json
let jsonDatos = JSON.stringify(datos)

// Crear archivo "seandsun.json" y escribir los datos en él
const jsonPath = './seandsun.json'

fs.writeFile(jsonPath, jsonDatos, (error) => {
  if(error) {
    console.log(`Error al crear el archivo: ${error}`)
  } else {
    console.log('Se ha creado el archivo .json correctamente')
  }
})

// Leer la información del archivo "seandsun.json"
let data = fs.readFileSync('seandsun.json')

// Convertir objeto tipo json a objeto js
let dataParseada = JSON.parse(data)
console.log(dataParseada)

// Eliminar el archivo "seandsun.json"
fs.unlink(jsonPath, (error) => {
  if(error) {
    console.log(`Error al eliminar el archivo .json: ${error}`)    
  } else {
    console.log('Archivo .json borrado exitosamente')
  }
})


// <-------------- xml -------------->

// Datos para agregar al nuevo fichero llamado "seandsun.xml"
const xmlDatos = `
<datos>
  <nombre>Marisol</nombre>
  <edad>26</edad>
  <fechaDeNacimiento>11/07/98</>
  <lenguajesDeProgramacion>
    <lenguaje>javascript</lenguaje>
    <lenguaje>python</lenguaje>
    <lenguaje>java</lenguaje>
  </lenguajesDeProgramacion>
</datos>
`

// Crear archivo "seandsun.xml" y escribir los datos en él
const xmlPath = './seandsun.xml'

fs.writeFile(xmlPath, xmlDatos, (error) => {
  if(error) {
    console.log(`Error al crear el archivo: ${error}`)
  } else {
    console.log('Se ha creado el archivo .xml correctamente')
  }
})

// Leer la información del archivo "seandsun.xml"
fs.readFile(xmlPath, 'utf-8', (error, data) => {
  if(!error) {
    console.log(data)
  } else {
    console.log(`Error al leer el archivo: ${error}`)
  }
})

// Eliminar el archivo "seandsun.xml"
fs.unlink(xmlPath, (error) => {
  if(error) {
    console.log(`Error al eliminar el archivo .xml: ${error}`)    
  } else {
    console.log('Archivo .xml borrado exitosamente')
  }
})