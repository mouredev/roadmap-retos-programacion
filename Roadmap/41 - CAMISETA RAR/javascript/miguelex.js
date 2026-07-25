const fs = require('fs');
const archiver = require('archiver');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function preguntar(query) {
    return new Promise(resolve => rl.question(query, resolve));
}

async function main() {
    console.log("Selecciona lo que quieres comprimir:");
    console.log("1. Archivo");
    console.log("2. Directorio");
    const tipoSeleccionado = await preguntar('Tu elección: ');

    let tipo;
    if (tipoSeleccionado === '1') {
        tipo = 'archivo';
    } else if (tipoSeleccionado === '2') {
        tipo = 'directorio';
    } else {
        console.log("Selección no válida");
        rl.close();
        return;
    }

    const inputPath = await preguntar(`Introduce la ruta del ${tipo} que deseas comprimir: `);
    const nombreSalida = await preguntar("Introduce el nombre de salida (sin la extensión): ") + '.zip';

    const output = fs.createWriteStream(nombreSalida);
    const archive = archiver('zip', {
        zlib: { level: 9 }
    });

    output.on('close', function () {
        console.log(`Archivo comprimido con éxito en ${nombreSalida}, total ${archive.pointer()} bytes`);
        rl.close();
    });

    archive.on('error', function (err) {
        throw err;
    });

    archive.pipe(output);

    if (tipo === 'archivo') {
        archive.file(inputPath, { name: require('path').basename(inputPath) });
    } else {
        archive.directory(inputPath, false);
    }

    archive.finalize();
}

main();
