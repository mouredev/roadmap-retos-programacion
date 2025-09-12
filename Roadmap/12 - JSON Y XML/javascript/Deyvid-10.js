// XML y JSON

let fs = require('fs')

// Crear el archivo .json
function crearJSON()
{
    let contenido = {Nombre: 'Deyvid Marmolejo', Edad: 25, Nacimiento: '06-12-98', Lenguajes: ['JavaScript', 'Python']}
    let contenidoJSON = JSON.stringify(contenido, null, 2)  

    fs.writeFileSync('./#12/Deyvid-10.json', contenidoJSON, 'utf8')
    
    console.log("Archivo .json creado correctamente")
}

crearJSON()

// Leer el archivo .json
function leerJSON()
{
    let cont = JSON.parse(fs.readFileSync('./#12/Deyvid-10.json', 'utf8'))
   
    console.log("El contenido del archivo es:\n", cont);  

    return cont
}

leerJSON()

// Eliminar el archivo .json
function eliminarJSON()
{
    fs.unlinkSync('./#12/Deyvid-10.json')

    console.log("Archivo .json eliminado correctamente");
}

eliminarJSON()

// Crear el archivo .xml

let xml2js = require('xml2js')

function crearXML()
{
    let contenido2 = {root: {Nombre: 'Deyvid Marmolejo', Edad: 25, Nacimiento: '06-12-98', Lenguajes: ['JavaScript', 'Python']}}
    let xml = new xml2js.Builder()
    let contenidoXML = xml.buildObject(contenido2)

    fs.writeFileSync('./#12/Deyvid-10.xml', contenidoXML, 'utf8')

    console.log("Archivo .xml creado correctamente");
}

crearXML()

// Leer el archivo .xml
function leerXML()
{
    let objCont = ""

    let leer = fs.readFileSync('./#12/Deyvid-10.xml', 'utf8')
    let objetoXML = new xml2js.Parser()
    
    objetoXML.parseString(leer, (error, cont) => {
    if(error)
    {
        console.log("Error encontrado: ", error);
    }
    else
    {
        console.log("Contenido del archivo:\n", cont);
        objCont = cont
    }
    })

    return objCont
}

leerXML()

// Eliminar el archivo .xml
function eliminarXML()
{
    fs.unlinkSync('./#12/Deyvid-10.xml')

    console.log("Archivo .xml eliminado correctamente");
}

eliminarXML()

// DIFICULTAD EXTRA

class Extra
{
    constructor(nombre, edad, nacimiento, lenguajes)
    {
        this.contenido = nombre
        this.edad = edad
        this.nacimiento = nacimiento
        this.lenguajes = lenguajes
    }
}

crearJSON()
crearXML()

let json = leerJSON()
let extraJson = new Extra(json.Nombre, json.Edad, json.Nacimiento, json.Lenguajes)
eliminarJSON()

let xml = leerXML().root
let extraXml = new Extra(xml.Nombre[0], xml.Edad[0], xml.Nacimiento[0], xml.Lenguajes)
eliminarXML()

console.log(extraJson);
console.log(extraXml);