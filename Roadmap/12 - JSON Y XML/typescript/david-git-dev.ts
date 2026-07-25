import * as fs from 'fs';
import * as path from 'path';
import * as xmlbuilder from 'xmlbuilder';
import { parseString } from 'xml2js';
/*
const rutaArchivo = path.resolve('david-git-dev.txt');

fs.appendFileSync(rutaArchivo,'Nombre: David\n');
fs.appendFileSync(rutaArchivo,'Edad: 25 años\n',);
fs.appendFileSync(rutaArchivo,'Lenguajes de programacion favoritos: Javascript , Typescript,PHP,Flutter,Java\n',);//agregando datos
const data = fs.readFileSync(rutaArchivo,'utf8')//leyendo archivo
console.log(`Archivo creado en: ${rutaArchivo}\n con el contenido: \n ${data}`);
fs.unlinkSync(rutaArchivo) // borrando el archivo
//fs.writeFileSync(ruta,json) */
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
*/
class Ejercicio{
  private _data= {
    nombre: "david",
    edad: 25,
    fechaDeNacimiento: new Date(1999, 5, 13).toLocaleDateString(),
    lenguages: ["javascript", "php", "java"],
  };
createXML(){
  // let xml ='<?xml version="1.0" encoding="UTF-8"?>\n';
  const xml = xmlbuilder.create('persona')
  .ele('nombre', this._data.nombre).up()
  .ele('edad', this._data.edad).up()
  .ele('fechaDeNacimiento', this._data.fechaDeNacimiento).up()
  .ele('lenguajesDeProgramacion')
    .ele('lenguaje', this._data.lenguages[0] as string).up()
    .ele('lenguaje', this._data.lenguages[1]).up()
    .ele('lenguaje', this._data.lenguages[2]).up()
  .end({ pretty: true });

fs.writeFileSync('data.xml', xml);
const filePath = path.resolve('data.xml')
const data = fs.readFileSync(filePath,'utf8')
console.log(data)
fs.unlinkSync(filePath)
}
createJSON(){
  const url = path.resolve('data.json')
  fs.writeFileSync(url,JSON.stringify(this._data))
  const data = fs.readFileSync(url,'utf8')
  console.log(data)
  fs.unlinkSync(url)
}
}
const ejercicio = new Ejercicio();
ejercicio.createJSON()
ejercicio.createXML()

/*DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 * */
class Custom {
  private _data= {
    nombre: "david",
    edad: 25,
    fechaDeNacimiento: new Date(1999, 5, 13).toLocaleDateString(),
    lenguages: ["javascript", "php", "java"],
  };
  private _filePath: string;
  constructor(path:string){
    this._filePath = path
  }
  createXML(){
    // let xml ='<?xml version="1.0" encoding="UTF-8"?>\n';
    const xml = xmlbuilder.create('persona')
    .ele('nombre', this._data.nombre).up()
    .ele('edad', this._data.edad).up()
    .ele('fechaDeNacimiento', this._data.fechaDeNacimiento).up()
    .ele('lenguajesDeProgramacion')
      .ele('lenguaje', this._data.lenguages[0] as string).up()
      .ele('lenguaje', this._data.lenguages[1]).up()
      .ele('lenguaje', this._data.lenguages[2]).up()
    .end({ pretty: true });

  fs.writeFileSync('data.xml', xml);
  const filePath = path.resolve('data.xml')
  const data = fs.readFileSync(filePath,'utf8')
  console.log(data)
//fs.unlinkSync(filePath)
  }
  createJSON(){
    const filePath = path.resolve('data.json')
    fs.writeFileSync(filePath,JSON.stringify(this._data))
    const data = fs.readFileSync(filePath,'utf8')
    console.log(data)
//fs.unlinkSync(filePath)
  }
  transformJSON() {
    const filePath = path.resolve('data.json');
    const data = fs.readFileSync(filePath,'utf-8');
    console.log (JSON.stringify(JSON.parse(data)))
    fs.unlinkSync(filePath)
  }
transformXML(){
  const filePath = path.resolve(this._filePath);
  const xml = fs.readFileSync(filePath)
  parseString(xml, (err:any, result:any) => {
    if (err) {
      console.error('Error parsing XML:', err);
      return;
    }
    console.log(JSON.stringify(result, null, 2));
  });
  fs.unlinkSync(filePath)
}
}
const transform = new Custom('data.xml');
transform.createJSON()
transform.createXML()
transform.transformXML()
transform.transformJSON()