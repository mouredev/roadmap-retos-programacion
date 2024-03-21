var fs = require('fs');
var readlineSync = require('readline-sync');
var _a = require('xmldom'), ImplementationDOM = _a.DOMImplementation, SerializeXML = _a.XMLSerializer;
var jsonContent = {
    nombre: 'Andres Chapeton',
    edad: 26,
    fecha_de_nacimiento: '02/06/1997',
    lista_lenguajes: ['TypeScript', 'JavaScript', 'Python', 'C#']
};
fs.writeFile('data.json', JSON.stringify(jsonContent), function (error) {
    if (error)
        throw error;
    console.log('JSON file created');
});
//Leer contenido del fichero JSON
fs.readFile('data.json', function (error, data) {
    if (error)
        throw error;
    console.log(data.toString());
});
//Eliminar fichero JSON
fs.unlink('data.json', function (error) {
    if (error)
        throw error;
    console.log('JSON file deleted');
});
// PARA CREAR ARCHIVO XML
// Crear un objeto DOMImplementation
var domImplementation = new ImplementationDOM();
//Crear un objeto XML Document
var xmlBaseDoc = domImplementation.createDocument(null, 'root');
//Crear elementos y atributos
var main = xmlBaseDoc.createElement('main');
var full_name = xmlBaseDoc.createAttribute('full_name');
var age = xmlBaseDoc.createAttribute('age');
var birth = xmlBaseDoc.createAttribute('birth');
var list = xmlBaseDoc.createAttribute('list');
//Agregar valures
full_name.value = 'Andres Chapeton';
age.value = '26';
birth.value = '02/06/1997';
list.value = 'TypeScript, JavaScript, Python, C#';
//Agregar elementos al documento
main.setAttributeNode(full_name);
main.setAttributeNode(age);
main.setAttributeNode(birth);
main.setAttributeNode(list);
main.textContent = 'Datos';
xmlBaseDoc.documentElement.appendChild(main);
//Convertir documento XML en cadena de texto
var xmlString = new SerializeXML().serializeToString(xmlBaseDoc);
//Crear fichero XML
fs.writeFile('data.xml', xmlString, function (error) {
    if (error)
        throw error;
    console.log('XML file created');
});
//Leer contenido del fichero XML
fs.readFile('data.xml', function (error, data) {
    if (error)
        throw error;
    var xmlString = data.toString();
    console.log(xmlString);
});
//Eliminar fichero XML
fs.unlink('data.xml', function (error) {
    if (error)
        throw error;
    console.log('JSON file deleted');
});
