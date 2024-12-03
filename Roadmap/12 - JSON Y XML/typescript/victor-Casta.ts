const fs = require('fs')
const path = require('path')

/*
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

async function saveData(): Promise<void> {
  const JSONdata = {
    name: 'Victor',
    age: 21,
    dateOfBirth: new Date(2002, 11, 17).toDateString(),
    programmingLanguages: ['JavaScript', 'TypeScript', 'Python', 'PHP']
  }

  const xmlData = `
  <root>
    <name>Victor</name>
    <age>21</age>
    <dateOfBirth>2002-11-17</dateOfBirth>
    <programmingLanguages>
      <language>JavaScript</language>
      <language>TypeScript</language>
      <language>Python</language>
      <language>PHP</language>
    </programmingLanguages>
  </root>`


  await fs.writeFileSync('data.json', JSON.stringify(JSONdata))
  fs.writeFileSync('data.xml', xmlData, 'utf8')
  console.log(fs.readFileSync('data.xml', 'utf8'))
  console.log(fs.readFileSync('data.json', 'utf8'))
  // fs.unlinkSync('data.json')
  // fs.unlinkSync('data.xml')
}

saveData()

/*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
*/

class customData {
  file: string
  constructor(file: string) {
    this.file = file
  }

  async readData(): Promise<any> {
    if (path.extname(this.file) === '.json') {
      return JSON.parse(fs.readFileSync(this.file, 'utf8'))
    }
  }

  async updateData(): Promise<any> {
    if (path.extname(this.file) === '.xml') {
      return fs.readFileSync('data.xml', 'utf8')
    }
  }

  async deleteFile(): Promise<void> {
    fs.unlinkSync(this.file)
  }
}

const dataJson = new customData('data.json')
console.log(dataJson.readData())

const dataXml = new customData('data.xml')
console.log(dataXml.updateData())

dataJson.deleteFile()
dataXml.deleteFile()