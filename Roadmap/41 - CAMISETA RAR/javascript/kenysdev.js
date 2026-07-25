/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#41 CAMISETA RAR
-------------------------------------------------------
* EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
 */
// ________________________________________________________
const fs = require('fs');
const path = require('path');
const archiver = require('archiver');

function compressFile(sourceFile, zipFile) {
    if (!fs.existsSync(sourceFile)) {
        throw new Error(`El archivo fuente '${sourceFile}' no existe.`);
    }

    const zipDir = path.dirname(zipFile) || '.';
    if (!fs.existsSync(zipDir)) {
        throw new Error(`El directorio '${zipDir}' no existe.`);
    }

    if (fs.existsSync(zipFile)) {
        throw new Error(`El archivo zip '${zipFile}' ya existe.`);
    }

    const output = fs.createWriteStream(zipFile);
    const archive = archiver('zip', {
        zlib: { level: 9 } // Nivel de compresión (máximo)
    });

    return new Promise((resolve, reject) => {
        output.on('close', () => {
            console.log(`Comprimido exitosamente '${sourceFile}' a '${zipFile}'`);
            resolve();
        });

        archive.on('error', (err) => {
            reject(new Error(`Se produjo un error al comprimir el archivo: ${err.message}`));
        });

        archive.pipe(output);
        archive.file(sourceFile, { name: path.basename(sourceFile) });
        archive.finalize();
    });
}

// Ejemplo de uso
compressFile('people.json', 'file.zip')
    .then(() => console.log('Operación completada.'))
    .catch(err => console.error(err.message));
