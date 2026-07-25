/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#38 MOUREDEV PRO
-------------------------------------------------------
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
*/
// ________________________________________________________
// users.csv
/*
id,email,status
1,john.doe1@example.com,active
2,jane.smith2@example.com,active
3,michael.johnson3@example.com,active
4,emily.davis4@example.com,active
5,daniel.brown5@example.com,active
6,sarah.miller6@example.com,active
7,william.moore7@example.com,active
8,olivia.jones8@example.com,active
9,james.wilson9@example.com,active
10,lisa.taylor10@example.com,active
*/

const fs = require('fs');

const readCsv = (filePath) => {
    try {
        const data = fs.readFileSync(filePath, 'utf8');
        const lines = data.split('\n').map(line => line.trim());
        const headers = lines[0].split(',');
        const rows = lines.slice(1).filter(line => line).map(line => {
            const values = line.split(',');
            const entry = {};
            headers.forEach((header, index) => {
                entry[header.trim()] = values[index].trim();
            });
            return entry;
        });
        return rows;
    } catch (error) {
        console.error(`Error reading '${filePath}': ${error.message}`);
        return null;
    }
};

const getActiveEntries = (entries) => {
    return entries.filter(entry => entry.status.toLowerCase() === 'active')
        .map(({ id, email, status }) => ({ id, email, status }));
};

const selectWinners = (activeEntries, numWinners) => {
    const shuffled = [...activeEntries].sort(() => Math.random() - 0.5);
    return shuffled.slice(0, Math.min(numWinners, activeEntries.length));
};

const distributePrizes = (winners, prizes) => {
    const shuffledPrizes = [...prizes].sort(() => Math.random() - 0.5);
    winners.forEach((winner, index) => {
        const prize = shuffledPrizes[index];
        console.log(`${prize.padEnd(11)} -> Id(${winner.id}): ${winner.email}`);
    });
};

const main = () => {
    console.log("Usuarios ganadores de 'MOUREDEV PRO:'");
    const csvFile = 'users.csv';
    const prizes = ["Suscripción", "Descuento", "Libro"];

    const entries = readCsv(csvFile);
    if (entries) {
        const activeEntries = getActiveEntries(entries);
        const winners = selectWinners(activeEntries, 3);
        if (winners.length > 0) {
            distributePrizes(winners, prizes);
        } else {
            console.log("No se encontraron entradas activas.");
        }
    } else {
        console.log("No se pudieron leer los datos del archivo CSV.");
    }
};

main();
