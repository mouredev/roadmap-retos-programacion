/*
  EJERCICIO:
  ¿Has visto la camiseta.rar?
  https://x.com/MoureDev/status/1841531938961592740
 
  Crea un programa capaz de comprimir un archivo 
  en formato .zip (o el que tú quieras).
  - No subas el archivo o el zip.
*/

const fs = require('fs');
const zlib = require('zlib');
const zip = zlib.createGzip();
const input = fs.createReadStream('archivo.txt');
const output = fs.createWriteStream('archivo.zip');

input.pipe(zip).pipe(output);

console.log(`El archivo fue comprimido.`);
