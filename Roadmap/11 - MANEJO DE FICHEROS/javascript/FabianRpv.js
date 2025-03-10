// Manejo de Ficheros

const fs = require('fs')


// Crear Archivo 

fs.writeFile('FabianRpv.txt', 'Hola! Soy Fabian \nTengo 20 Años \nMe Gusta JavaScript!', (error) => {
    if(error){
        console.log(error);
    }
    else {
        console.log('Archivo creado!')
    }
})


// Leer Archivo 

fs.readFile('FabianRpv.txt', 'utf-8', (error, data) => {
    if(error){
        console.log(error)
    }
    else {
        console.log(data)
    }
})


// Eliminar Archivo 

fs.unlink('FabianRpv.txt', (error) => {
    if(error){
        console.log(error)
    }
    else {
        console.log('Archivo Eliminado!')
    }
})