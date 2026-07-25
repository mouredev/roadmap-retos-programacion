// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const fs = require('fs');
const readline = require('readline');

// Leer archivo CSV
function leerCSV(filepath) {
    return new Promise((resolve, reject) => {
        const participantes = [];
        const rl = readline.createInterface({
            input: fs.createReadStream(filepath),
            crlfDelay: Infinity
        });

        rl.on('line', (line) => {
            const [id, email, status] = line.split(',');
            if (status === 'activo') {
                participantes.push({ id, email, status });
            }
        });

        rl.on('close', () => resolve(participantes));
    });
}

// Seleccionar ganadores de forma aleatoria
function seleccionarGanadores(participantes) {
    if (participantes.length < 3) {
        console.log("No hay suficientes participantes activos para seleccionar 3 ganadores.");
        return;
    }

    const shuffled = participantes.sort(() => 0.5 - Math.random());
    const ganadores = shuffled.slice(0, 3);

    console.log(`Ganador de suscripción: ID ${ganadores[0].id} | Email: ${ganadores[0].email}`);
    console.log(`Ganador de descuento: ID ${ganadores[1].id} | Email: ${ganadores[1].email}`);
    console.log(`Ganador de libro: ID ${ganadores[2].id} | Email: ${ganadores[2].email}`);
}

// Ejecutar el programa
async function main() {
    const participantes = await leerCSV('suscriptores.csv');
    seleccionarGanadores(participantes);
}

main();
