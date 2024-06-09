//JSON
const fs = require("fs");

// Definir el nombre del archivo de texto
const fileNameTxt = "fileNameTXT.txt";

// Objeto JSON
const objetoJson = {
    nombre: "ocram1304",
    edad: 24,
    fechaCumple: "13/04/2000",
    lenguajes: ['JavaScript']
};

// Convertir el objeto a una cadena de texto JSON
const txtString = JSON.stringify(objetoJson,null,2);

// Escribir la cadena de texto en el archivo
fs.writeFileSync(fileNameTxt, txtString, (err) => {
    if (err) throw err;
    console.log("El archivo de texto ha sido creado correctamente");
});

// Leer los datos del archivo de texto
const datosTxt = fs.readFileSync(fileNameTxt, "utf-8");

// Mostrar los datos de texto en la consola
console.log(datosTxt);



//XML

const xmlbuilder = require("xmlbuilder");

// Definir el nombre del archivo XML
const fileNameXml = "fileNameXML.txt"; 

// Crear el documento XML con xmlbuilder
const xmlDoc = xmlbuilder.create({ version: '1.0' })
  .ele('root')
    .ele('Nombre', 'ocram1304').up()
    .ele('Edad', '24').up()
    .ele('FechaCumple','13/04/2000').up()
    .ele('Lenguajes','JavaScript')
  .end({ prettyPrint: true });

// Escribir los datos XML en el archivo
fs.writeFileSync(fileNameXml, xmlDoc, (err) => {
    if (err) throw err;
    console.log("El archivo XML ha sido creado correctamente");
});

// Leer los datos del archivo XML
const datosXml = fs.readFileSync(fileNameXml, "utf-8");

// Mostrar los datos XML en la consola
console.log(datosXml);




//Difucultad extra

class JSONYXML {
    nombre;
    edad; 
    fechaCumple;
    lenguajes;

    constructor(nombre,edad,fechaCumple,lenguajes){
       this.nombre = nombre;
       this.edad = edad;
       this.fechaCumple = fechaCumple;
       this.lenguajes = lenguajes;
    }

    
    transformarJSON(){
       const recursoJSON =  fs.readFileSync(fileNameTxt,"utf-8");
       const objetoJson = JSON.parse(recursoJSON);
       this.nombre = objetoJson.nombre;
       this.edad = objetoJson.edad;
       this.fechaCumple = objetoJson.fechaCumple;
       this.lenguajes = objetoJson.lenguajes;
       
    }
    transformarXML() {
        const xml2js = require("xml2js");
    
        return new Promise((resolve, reject) => {
            const recursoXML = fs.readFileSync(fileNameXml, "utf-8");
            xml2js.parseString(recursoXML, (err, res) => {
                if (err) {
                    console.error("Error al analizar el XML:", err);
                    reject(err);
                } else {
                    resolve(res);
                }
            });
        }).then(objXML => {
            // Verificar si objXML es un objeto válido
            if (objXML && typeof objXML === "object") {
                this.nombre = objXML.root.Nombre;
                this.edad = objXML.root.Edad;
                this.fechaCumple = objXML.root.FechaCumple;
                this.lenguajes = objXML.root.Lenguajes;
            } else {
                console.error("El objeto XML no es válido.");
            }
        }).catch(error => {
            console.error("Error al transformar el XML:", error);
        });
    }
    

    Mostrardatos(){

        if(this.nombre !== undefined || this.edad !== undefined || this.fechaCumple !== undefined || this.lenguajes !== undefined){
           const objMuestra = {
            nombre: this.nombre,
            edad: this.edad,
            fechaCumple: this.fechaCumple,
            lenguajes: this.lenguajes

        };
        console.log(objMuestra); 
        }
        else{
            console.log("No hay datos disponibles para mostrar");
        }
    }
    borrrarJSON(){
        fs.unlink(fileNameTxt);
    }
    borrarXML(){
        fs.unlink(fileNameXml);
    }
}
