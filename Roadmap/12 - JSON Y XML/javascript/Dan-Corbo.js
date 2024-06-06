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
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */


/* Solucion */

// Importamos el módulo 'fs' para manejar archivos en Node.js
const fs = require('fs');

// Función para crear un perfil con los datos proporcionados
function crearPerfil(nombre, edad, nacimiento, lenguajes) {
  // Definición de la clase Perfil
  class Perfil {
    constructor(nombre, edad, nacimiento, lenguajes) {
        this.nombre = nombre;
        this.edad = edad;
        this.nacimiento = nacimiento;
        this.lenguajes = lenguajes;
    }
  }
  
  // Creamos y retornamos una nueva instancia de Perfil con los datos proporcionados
  return new Perfil(nombre, edad, nacimiento, lenguajes);
}

// Función para mostrar la información del perfil
function mostrarPerfil(variable) {
  // Formateamos los lenguajes en una cadena legible
  let elemento = "";
  if (variable.lenguajes.length === 1) {
    elemento = variable.lenguajes[0];
  } else if (variable.lenguajes.length === 2) {
    elemento = `${variable.lenguajes[0]} y ${variable.lenguajes[1]}`;
  } else {
    for (let i = 0; i < variable.lenguajes.length - 1; i++) {
      elemento += `${variable.lenguajes[i]}, `;
    }
    elemento += `y ${variable.lenguajes[variable.lenguajes.length - 1]}`;
  }

  // Construimos y retornamos la información del perfil formateada
  let mostrar = `
  Mi nombre es ${variable.nombre}, tengo ${variable.edad} años, 
  nací el ${variable.nacimiento} y los lenguajes que conozco 
  son ${elemento}.`;
  
  return mostrar;
}

// Función para convertir un objeto Perfil a formato XML
function convertirAXml(objeto) {
  let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  xml += '<persona>\n';
  xml += '\t<nombre>' + objeto.nombre + '</nombre>\n';
  xml += '\t<edad>' + objeto.edad + '</edad>\n';
  xml += '\t<nacimiento>' + objeto.nacimiento + '</nacimiento>\n';
  xml += '\t<lenguajes>\n';
  // Iteramos sobre los lenguajes para añadirlos al XML
  objeto.lenguajes.forEach(lenguaje => {
    xml += `\t\t<lenguaje>${lenguaje}</lenguaje>\n`;
  });
  xml += '\t</lenguajes>\n';
  xml += '</persona>';
  return xml;
}

// Creamos un perfil de ejemplo
let perfil = crearPerfil("Daniel", 24, "23/10/1999", ["Javascript", "Python", "Java", "C++", "Kotlin"]);

// Convertir el objeto a XML e Imprimirlo
const xmlData = convertirAXml(perfil);
console.log(`Archivo XML: \n${xmlData}\n`);

// Guardar archivo XML
fs.writeFile('perfil.xml', xmlData, (err) => {
  if (err) throw err;
  console.log('Archivo XML guardado correctamente.');
});

// Convertir el objeto a JSON e Imprimirlo
const jsonData = JSON.stringify(perfil);
console.log(`Archivo JSON: \n${jsonData}\n`);
fs.writeFile('perfil.json', jsonData, (err) => {
  if (err) throw err;
  console.log('Archivo JSON guardado correctamente.');
});

// Mostrar la información del perfil
console.log(`Perfil:${mostrarPerfil(perfil)}\n`);


// Borrar los archivos
fs.unlink('perfil.xml', (err) => {
  if (err) throw err;
  console.log('Archivo XML eliminado correctamente.');
});

fs.unlink('perfil.json', (err) => {
  if (err) throw err;
  console.log('Archivo JSON eliminado correctamente.');
});


/* Extra - Opcional */

//Requiere Node.Js para funcionar

// Definir la clase custom
/*class Perfil {
  constructor(nombre, edad, nacimiento, lenguajes) {
    this.nombre = nombre;
    this.edad = edad;
    this.nacimiento = nacimiento;
    this.lenguajes = lenguajes;
  }

  // Método para mostrar la información del perfil
  mostrarPerfil() {
    let elemento = "";
    // Formatear los lenguajes en una cadena legible
    if (this.lenguajes.length === 1) {
      elemento = this.lenguajes[0];
    } else if (this.lenguajes.length === 2) {
      elemento = `${this.lenguajes[0]} y ${this.lenguajes[1]}`;
    } else {
      for (let i = 0; i < this.lenguajes.length - 1; i++) {
        elemento += `${this.lenguajes[i]}, `;
      }
      elemento += `y ${this.lenguajes[this.lenguajes.length - 1]}`;
    }

    // Construir y retornar la información del perfil formateada
    let mostrar = `
    Mi nombre es ${this.nombre}, tengo ${this.edad} años, 
    nací el ${this.nacimiento} y los lenguajes que conozco 
    son ${elemento}.`;
    
    return mostrar;
  }
}

// Función para leer el archivo XML y transformarlo en un objeto Perfil
function leerXml(filePath) {
  // Leer el contenido del archivo XML
  const data = fs.readFileSync(filePath, 'utf-8');

  // Analizar el XML utilizando el módulo xml2js
  const parseString = require('xml2js').parseString;
  let parsedData;
  parseString(data, (err, result) => {
    if (err) throw err;
    parsedData = result.persona;
  });

  // Extraer los datos del objeto XML y crear un nuevo objeto Perfil
  const nombre = parsedData.nombre[0];
  const edad = parseInt(parsedData.edad[0]);
  const nacimiento = parsedData.nacimiento[0];
  const lenguajes = parsedData.lenguajes[0].lenguaje;

  return new Perfil(nombre, edad, nacimiento, lenguajes);
}

// Función para leer el archivo JSON y transformarlo en un objeto Perfil
function leerJson(filePath) {
  // Leer el contenido del archivo JSON
  const data = fs.readFileSync(filePath, 'utf-8');
  
  // Parsear el JSON y crear un nuevo objeto Perfil
  const jsonData = JSON.parse(data);
  return new Perfil(jsonData.nombre, jsonData.edad, jsonData.nacimiento, jsonData.lenguajes);
}

// Ruta de los archivos XML y JSON
const xmlFilePath = 'perfil.xml';
const jsonFilePath = 'perfil.json';

// Leer archivos y crear objetos Perfil
const perfilFromXml = leerXml(xmlFilePath);
const perfilFromJson = leerJson(jsonFilePath);

// Mostrar la información de los perfiles
console.log("Perfil desde XML:");
console.log(perfilFromXml.mostrarPerfil());

console.log("\nPerfil desde JSON:");
console.log(perfilFromJson.mostrarPerfil());*/
