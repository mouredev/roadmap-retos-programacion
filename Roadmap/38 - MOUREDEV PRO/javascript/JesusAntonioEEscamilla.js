/** #38 - JavaScript -> Jesus Antonio Escamilla */

/**
 * MOUREDEV PRO.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const fs = require('fs');
const readline = require('readline');

// Función para leer los datos del CSV
function readCSV(filePath) {
    return new Promise((resolve, reject) => {
        const suscriptores = [];
        const rl = readline.createInterface({
            input: fs.createReadStream(filePath),
            crlfDelay: Infinity
        });

        rl.on('line', (line) => {
            const [id, email, status] = line.split(',');
            if (status === 'activo') {
                suscriptores.push({id, email});
            }
        });

        rl.on('close', () => {
            resolve(suscriptores);
        });

        rl.on('error', (err) => {
            reject(err);
        });
    });
}

// Función para seleccionar en ganador
function selectWinners(suscriptor) {
    const winners = [];
    while (winners.length < 3) {
        const randomIndex = Math.floor(Math.random() * suscriptor.length);
        const winner = suscriptor[randomIndex];
        if (!winners.some(w => w.email === winner.email)) {
            winners.push(winner);
        }
    }

    return {
        suscripcion: winners[0],
        descuento: winners[1],
        libro: winners[2]
    }
}

async function winnersMorueDevPRO() {
    try {
        const fileCSV = './suscriptores.csv'
        const emails = await readCSV(fileCSV)

        if (emails.length < 3) {
            console.log(`Error: No hay suficientes participantes activos. Se necesitan al menos 3, pero solo hay ${emails.length}.`);
            return;
        }

        const winners = selectWinners(emails)

        console.log(`Ganador suscripción: ${winners.suscripcion.email}`);
        console.log(`Ganador descuento: ${winners.descuento.email}`);
        console.log(`Ganador libro: ${winners.libro.email}`);
    } catch (error) {
        console.error('Error al iniciar el programa: ', error)
    }
}

// Usando el programa
winnersMorueDevPRO()