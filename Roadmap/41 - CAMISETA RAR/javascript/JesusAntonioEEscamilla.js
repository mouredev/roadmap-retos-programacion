/** #41 - JavaScript -> Jesus Antonio Escamilla */

/**
 * CAMISETA RAR.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

// Los recursos requeridos para ejerció
const fs = require('fs');
const zlib = require('zlib');

// La función en concreto
function compressZip(inputFilePath, outputFilePath) {
    // Leemos el Archivo
    const input = fs.createReadStream(inputFilePath);

    // Escribimos el Archivo
    const output = fs.createWriteStream(outputFilePath);

    // El recursos de comprimir
    const gzip = zlib.createGzip();

    // Aquí se comprime el archivo
    input.pipe(gzip).pipe(output)
        .on('finish', () => console.log('Archivo comprimido con éxito.'))
        .on('error', (err) => console.error('Error al comprimir el archivo:', err))
}

// Se obtenía el archivo y como se llama después de comprimidlo
const inputFile = './archivo.txt';
const outputFile = './archivo.txt.gz';

// Ejecutado la función
compressZip(inputFile, outputFile)