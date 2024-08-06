import * as fs from 'fs';
const filename = 'victoriaparraf.txt';

// Paso 1: Crear el archivo y añadir varias líneas
const data = `Nombre: Victoria Parra
Edad: 25
Lenguaje de programación favorito: TypeScript`;

// Escribir en el archivo
fs.writeFileSync(filename, data, 'utf8');

// Paso 2: Leer e imprimir el contenido del archivo
const fileContent = fs.readFileSync(filename, 'utf8');
console.log('Contenido del archivo:');
console.log(fileContent);

// Paso 3: Borrar el archivo
fs.unlinkSync(filename);
console.log(`El archivo ${filename} ha sido borrado.`);
