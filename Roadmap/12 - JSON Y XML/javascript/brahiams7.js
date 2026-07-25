// * EJERCICIO:
//  * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
//  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
//  * - Nombre
//  * - Edad
//  * - Fecha de nacimiento
//  * - Listado de lenguajes de programación
//  * Muestra el contenido de los archivos.
//  * Borra los archivos.

const builder = require('xmlbuilder');
const fs = require('fs');
const xml2js = require('xml2js');

// CREAR UN ARCHIVO JSON
    const carpeta="brahiams7.json"
const crearJSON=()=>{
    const data={
        name:"Brahiam",
        age:19,
        birthDate:"05-08-2005",
        programmingLenguages:"SQL, Python, Node"
    }
    jsonData=JSON.stringify(data,null,2);
    fs.writeFile(carpeta,jsonData,"utf-8",(err)=>{
        if (err) console.log(err);
        
    })
}

// CREAR UN ARCHIVO XML
const crearXML=()=>{
    const xmlData=builder.create('usuario')
    .ele('name','Brahiam').up()
    .ele('age','19').up()
    .ele('birthDate','05-08-2005').up()
    .ele('programmingLenguages','SQL, Python, Node').up()
    .end({pretty:true})
    fs.writeFile("brahiams7.xml",xmlData,"utf-8",(err)=>{
    if (err) console.log(err);
    })
}



// CREANDO LA CLASE

    class Usuario {
    constructor(name,age,birthDate,programmingLenguages){
        this.name=name,
        this.age=age,
        this.birthDate=birthDate,
        this.programmingLenguages=programmingLenguages
    }
    mostrarDatos(){
        console.log(`Nombre: ${this.name}`);
        console.log(`age: ${this.age}`);
        console.log(`birthDate: ${this.birthDate}`);
        console.log(`programmingLenguages: ${this.programmingLenguages}\n`);
    }
}

const showJSON = ()=>{
        fs.readFile(carpeta,'utf-8',(err,result)=>{
        const datosJSON=JSON.parse(result)
        const usuarioJson = new Usuario(
        datosJSON.name,
        datosJSON.age,
        datosJSON.birthDate,
        datosJSON.programmingLenguages
    )
    usuarioJson.mostrarDatos();
    })
    
}

const showXML = ()=>{
    const dataXML=fs.readFileSync('brahiams7.xml','utf-8')
    xml2js.parseString(dataXML,(err,result)=>{
        if (err) throw err;
        const datosXML=result.usuario
        const usuarioXML= new Usuario (
            datosXML.name[0],
            datosXML.age[0],
            datosXML.birthDate[0],
            datosXML.programmingLenguages[0]
        )
        usuarioXML.mostrarDatos()
    })
}
const deleteData=()=>{
    fs.unlink(carpeta,(err)=>{
        if(err) console.log(err);
    })
    fs.unlink('brahiams7.xml',(err)=>{
        if(err) console.log(err);
    })
}

showJSON();
showXML();
deleteData()
