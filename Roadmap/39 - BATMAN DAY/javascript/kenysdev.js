/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#39 BATMAN DAY
-------------------------------------------------------
* EJERCICIO:
 * Cada año se celebra el Batman Day durante la tercera semana de septiembre... 
 * ¡Y este año cumple 85 años! Te propongo un reto doble:
 *
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
 * su 100 aniversario.
 *
 * RETO 2:
 * Crea un programa que implemente el sistema de seguridad de la Batcueva. 
 * Este sistema está diseñado para monitorear múltiples sensores distribuidos
 * por Gotham, detectar intrusos y activar respuestas automatizadas. 
 * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
 * que procese estos datos para tomar decisiones estratégicas.
 * Requisitos:
 * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 * - Cada sensor se identifica con una coordenada (x, y) y un nivel
 *   de amenaza entre 0 a 10 (número entero).
 * - Batman debe concentrar recursos en el área más crítica de Gotham.
 * - El programa recibe un listado de tuplas representando coordenadas de los 
 *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
 *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 * Acciones: 
 * - Identifica el área con mayor concentración de amenazas
 *   (sumatorio de amenazas en una cuadrícula 3x3).
 * - Si el sumatorio de amenazas es mayor al umbral, activa el 
 *   protocolo de seguridad.
 * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
 *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
 *   sus amenazas, la distancia a la Batcueva y si se debe activar el
 *   protocolo de seguridad.
 */
// ________________________________________________________
// Reto #1
const getThirdSaturdayOfSeptember = (year) => {
    const date = new Date(year, 8, 15); // Septiembre es el mes 8 (0-indexed)
    const day = date.getDay();
    const offset = (6 - day + 7) % 7; // Calcula el sábado más cercano
    date.setDate(date.getDate() + offset);
    return date.toISOString().slice(0, 10); // YYYY-MM-DD
};

const anniversaryDates = (totalAnniversaries) => {
    const batmanDayStart = 2014;
    const currentYear = new Date().getFullYear();
    if (currentYear < batmanDayStart) {
        console.log("Batman Day aún no ha comenzado.");
        return;
    }

    const pastAnniversaries = currentYear - batmanDayStart;
    console.log(`Aniversarios que ya han pasado: ${pastAnniversaries}`);
    
    for (let i = pastAnniversaries; i < totalAnniversaries; i++) {
        const num = i + 1;
        const date = getThirdSaturdayOfSeptember(currentYear + (i - pastAnniversaries));
        console.log(`- Aniversario #${num}: ${date}`);
    }
};

console.log("Batman Day");
anniversaryDates(100);


// ________________________________________________________
// Reto $2
const createMap = (size, batcave, sensors, threats) => {
    const gotham = Array.from({ length: size[0] }, () => Array(size[1]).fill('| '));
    gotham[batcave[0]][batcave[1]] = '|B';

    sensors.forEach(([x, y]) => {
        gotham[x][y] = '|S';
    });

    threats.forEach(([x, y]) => {
        gotham[x][y] = '|T';
    });

    return gotham;
};

const printMap = (gotham) => {
    console.log("\nMapa de Gotham:");
    gotham.forEach(row => console.log(row.join('')));
};

const scanMap = (gotham, sensors) => {
    const dangerList = sensors.map(([x, y, threat]) => {
        let dangerCounter = 0;
        for (let i = Math.max(0, x - 1); i <= Math.min(gotham.length - 1, x + 1); i++) {
            for (let j = Math.max(0, y - 1); j <= Math.min(gotham[0].length - 1, y + 1); j++) {
                if (gotham[i][j] === '|T') {
                    dangerCounter += threat;
                }
            }
        }
        return { location: [x, y], danger: dangerCounter };
    });

    const maxDanger = dangerList.reduce((max, current) => (current.danger > max.danger ? current : max), { danger: 0 });

    console.log("\nInforme:");
    console.log(`Cuadrícula más amenazada: '${maxDanger.location[0]}, ${maxDanger.location[1]}'`);
    console.log(`Máximo nivel de alerta: '${maxDanger.danger}'`);
    if (maxDanger.danger >= 20) {
        console.log("Protocolo de seguridad activado.");
        console.log(`Distancia: '${Math.abs(maxDanger.location[0]) + Math.abs(maxDanger.location[1])}'`);
    } else {
        console.log("No hay amenazas relevantes.");
    }
};

const batcave = [0, 0];
const sensors = [
    [2, 2, 10],
    [6, 8, 9],
    [10, 12, 8],
    [17, 15, 7]
];
const threats = [
    [2, 3],
    [2, 1],
    [6, 9],
    [17, 16],
    [15, 4]
];

const gotham = createMap([20, 20], batcave, sensors, threats);
printMap(gotham);
scanMap(gotham, sensors);
