// JSON Y XML

// Archivo JSON 

const fs = require('fs');

const datos = {
    nombre: "Fabian",
    edad: 20,
    fecha: "10-11-2004",
    lenguajes: ["JavaScript", "PHP", "C++"] 
}

const dataJson = JSON.stringify(datos, null, 2) 

fs.writeFile('Data.json', dataJson, (error) => {
    if(error){
        console.log(error)
    }
    else {
        console.log('.json Creado')
    }
})

fs.readFile('Data.json', 'utf8', (error, data) => {
    if(error){
        console.log(error);
    }
    else {
        console.log(JSON.parse(data))
    }
})

fs.unlink('Data.json', (error) => {
    if(error){
        console.log(error)
    }
    else {
        console.log('.json Eliminado')
    }
})


// Archivo XML

const {  Builder } = require ('xml2js')


const builder = new Builder();

const xml = builder.buildObject(datos)

fs.writeFile('Data.xml', xml, (error) => {
    if(error){
        console.log(error)
    }
    else {
        console.log(".xml Creado")
    }
})

fs.readFile('Data.xml', 'utf8', (error, data) => {
    if(error){
        console.log(error)
    }
    else{
        console.log(data)
    }
})

fs.unlink('Data.xml', (error) => {
    if(error){
        console.log(error)
    }
    else{
        console.log('.xml Eliminado')
    }
})