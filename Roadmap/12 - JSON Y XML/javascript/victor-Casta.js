/*
  *Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
  * - Nombre
  * - Edad
  * - Fecha de nacimiento
  * - Listado de lenguajes de programación
  * Muestra el contenido de los archivos.
  * Borra los archivos.
*/

// XML

const fs = require('fs')

const data = {
  name: 'Victor',
  age: 21,
  birthdate: '17-12-2002',
  languages: ['Javascript', 'TypeScript', 'Python']
}

fs.writeFileSync('victor-Casta.xml', `
  <root>
    <name>${data.name}</name>
    <age>${data.age}</age>
    <birthdate>${data.birthdate}</birthdate>
    <languages>${
      data.languages.map((item) => `<item>${item}</item>`).join('')
    }</languages>
  </root>
`)

console.log(fs.readFileSync('victor-Casta.xml', 'utf8'))



// JSON

fs.writeFileSync('victor-Casta.json', JSON.stringify(data))
console.log(fs.readFileSync('victor-Casta.json', 'utf-8'))


/*
   * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
*/

class xmlData {
  constructor(name, age, birthdate, programmingLanguages) {
    this.name = name;
    this.age = age;
    this.birthdate = birthdate;
    this.programmingLanguages = [programmingLanguages];
  }

  getData() {
    console.log(
      `{
        name: ${this.name},
        age: ${this.age},
        birthdate: ${this.birthdate},
        programmingLanguages: ${this.programmingLanguages}
      }`
    )
  }
}

const xmlContent = fs.readFileSync('victor-Casta.xml', 'utf-8');
const nameMatch = xmlContent.match(/<name>([^<]+)<\/name>/);
const ageMatch = xmlContent.match(/<age>([^<]+)<\/age>/);
const birthdateMatch = xmlContent.match(/<birthdate>([^<]+)<\/birthdate>/);
const languagesMatch = xmlContent.match(/<languages>([\s\S]*?)<\/languages>/);
const languagesContent = languagesMatch[1];
let lenguajesList = [];
const items = [...languagesContent.matchAll(/<item>([^<]+)<\/item>/g)];
items.forEach(item => lenguajesList.push(item[1]));

const xml = new xmlData(nameMatch[1], ageMatch[1], birthdateMatch[1], lenguajesList);
xml.getData();


class jsonData {
  constructor(name, age, birthdate, programmingLanguages) {
    this.name = name;
    this.age = age;
    this.birthdate = birthdate;
    this.programmingLanguages = programmingLanguages;
  }
  getData() {
    let rta = {
      name: this.name,
      age: this.age,
      birthdate: this.birthdate,
      programmingLanguages: this.programmingLanguages
    }
    console.log(rta);
  }
}

const jsonContent = fs.readFileSync('victor-Casta.json', 'utf-8');
const formatJson = JSON.parse(jsonContent);

const jsonRta = new jsonData(formatJson.name, formatJson.age, formatJson.birthdate, formatJson.languages)
jsonRta.getData();

fs.unlinkSync('victor-Casta.xml')
fs.unlinkSync('victor-Casta.json')