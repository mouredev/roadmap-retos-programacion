// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const fs = require('fs');
const zlib = require('zlib');
const argparse = require('argparse');

// Función para comprimir en formato gzip
function comprimirGzip(archivo) {
    const archivoSalida = archivo + '.gz';
    const input = fs.createReadStream(archivo);
    const output = fs.createWriteStream(archivoSalida);
    const gzip = zlib.createGzip();

    input.pipe(gzip).pipe(output).on('finish', () => {
        console.log(`Archivo comprimido exitosamente: ${archivoSalida}`);
    });
}

// Argumentos usando ArgumentParser
const parser = new argparse.ArgumentParser({
    description: 'Comprimir un archivo en formato gzip',
});
parser.add_argument('archivo', { help: 'El archivo que se desea comprimir' });
parser.add_argument('formato', {
    help: 'Formato de compresión (gzip por defecto)',
    choices: ['gzip'],
});

const args = parser.parseArgs();

// Llamar a la función de compresión
if (args.formato === 'gzip') {
    comprimirGzip(args.archivo);
}

