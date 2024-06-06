const fs = require('fs')
const readlineSync = require('readline-sync');
const { DOMImplementation: ImplementationDOM, XMLSerializer: SerializeXML } = require('xmldom');

// PARA CREAR ARCHIVO JSON

interface Content {
  nombre: string,
  edad: number,
  fecha_de_nacimiento: string,
  lista_lenguajes: Array<string>
}

let jsonContent: Content = {
  nombre: 'Andres Chapeton', 
  edad: 26, 
  fecha_de_nacimiento: '02/06/1997',
  lista_lenguajes: ['TypeScript', 'JavaScript', 'Python', 'C#']
} 

fs.writeFile(
  'data.json', 
  JSON.stringify(jsonContent), 
  (error:  NodeJS.ErrnoException | null) => {
  if(error) throw error
  console.log('JSON file created')
})

//Leer contenido del fichero JSON
fs.readFile('data.json', (error:  NodeJS.ErrnoException | null, data: any) => {
  if(error) throw error
  console.log(data.toString())
})

//Eliminar fichero JSON
fs.unlink('data.json', (error:  NodeJS.ErrnoException | null) => {
  if(error) throw error
  console.log('JSON file deleted')
})



// PARA CREAR ARCHIVO XML

// Crear un objeto DOMImplementation
const domImplementation = new ImplementationDOM();

//Crear un objeto XML Document
const xmlBaseDoc: XMLDocument = domImplementation.createDocument(null, 'root')

//Crear elementos y atributos
const main: HTMLElement = xmlBaseDoc.createElement('main')
const full_name: Attr = xmlBaseDoc.createAttribute('full_name')
const age: Attr = xmlBaseDoc.createAttribute('age')
const birth: Attr = xmlBaseDoc.createAttribute('birth')
const list: Attr = xmlBaseDoc.createAttribute('list')

//Agregar valures
full_name.value = 'Andres Chapeton'
age.value = '26'
birth.value = '02/06/1997'
list.value = 'TypeScript, JavaScript, Python, C#'

//Agregar elementos al documento
main.setAttributeNode(full_name)
main.setAttributeNode(age)
main.setAttributeNode(birth)
main.setAttributeNode(list)
main.textContent = 'Datos'
xmlBaseDoc.documentElement.appendChild(main)

//Convertir documento XML en cadena de texto
const xmlString: string = new SerializeXML().serializeToString(xmlBaseDoc)


//Crear fichero XML
fs.writeFile(
  'data.xml', 
  xmlString, 
  (error:  NodeJS.ErrnoException | null) => {
  if(error) throw error
  console.log('XML file created')
})

//Leer contenido del fichero XML
fs.readFile('data.xml', (error:  NodeJS.ErrnoException | null, data: any) => {
  if(error) throw error
  const xmlString: string = data.toString()
  console.log(xmlString)
})

//Eliminar fichero XML
fs.unlink('data.xml', (error:  NodeJS.ErrnoException | null) => {
  if(error) throw error
  console.log('JSON file deleted')
})