/** #39 - JavaScript -> Jesus Antonio Escamilla */

/**
 * BATMAN DAY.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

// RETO 1
function saturdayDay(years, month) {
    let date = new Date(years, month - 1, 1)
    let dayOfWeek = date.getDay()

    let daysUntilSaturday = (6 - dayOfWeek + 7) % 7

    date.setDate((date.getDate() + daysUntilSaturday) + 15)

    return date.toLocaleDateString()
}

function getBatmanDay(startYear, endYear, month) {
    let saturdays = [];

    for (let year = startYear; year <= endYear; year++) {
        let thirdSaturdayDay = saturdayDay(year, month)
        saturdays.push({year: year, date: thirdSaturdayDay})
    }

    return saturdays
}

// Ejecutando RETO 1
const saturdayBetween = (getBatmanDay(2024, 2024 + 15, 9))
console.group('RETO 1')
console.group('¡¡Los siguientes Batman Day en este año 2024 es 85 aniversario!!')
saturdayBetween.forEach(({year, date}) => {
    console.log(`Batman Day en el año ${year}: ${date}`)
})
console.groupEnd()
console.groupEnd()



// RETO 2
// Tamaño de la cuadricula y el umbral del protocolo de seguridad
const Grid_SIZE = 20;
const Threat_THRESHOLD = 20;

// Coordenadas de la Batcueva
const BATCAVE_X = 0;
const BATCAVE_Y = 0;

// Función para calcular la distancia de Manhattan
const calcularDistancia = (x, y) => {
    return Math.abs(BATCAVE_X - x) + Math.abs(BATCAVE_Y - y);
};

// Función para procesar la cuadrícula y encontrar el área más crítica
function analyzeSensors(sensors) {
    // Mapa de Gotham
    const grid = Array.from({ length: Grid_SIZE }, () => Array(Grid_SIZE).fill(0));

    // Rellenar con los niveles de amenaza a cada sensor
    sensors.forEach(([x, y, threat]) => {
        grid[x][y] = threat;
    })

    let maxThreat = 0;
    let coordinateMaximum = [0, 0];

    // Analizar el area 3x3 para encontrar mas critica
    for (let i = 0; i <= Grid_SIZE - 3; i++) {
        for (let j = 0; j <= Grid_SIZE - 3; j++) {
            let sumThreat = 0;

            // Calcular el sumatorio de amenazas en la cuadrícula 3x3
            for (let x = i; x < i + 3; x++) {
                for (let y = j; y < j + 3; y++) {
                    sumThreat += grid[x][y];
                }
            }

            // Actualizar si encontramos una zona con mayor concentración de amenazas
            if (sumThreat > maxThreat) {
                maxThreat = sumThreat;
                coordinateMaximum = [i + 1, j + 1]; // El centro de la cuadrícula 3x3
            }
        }
    }

    // Calcular la distancia desde la Batcueva
    const [xCenter, yCenter] = coordinateMaximum;
    const distance = calcularDistancia(xCenter, yCenter);

    // Imprimir solución
    console.group('RETO 2');
    console.log(`Coordenada más amenazada: (${xCenter}, ${yCenter})`);
    console.log(`Suma de amenazas: ${maxThreat}`);
    console.log(`Distancia a la Batcueva: ${distance}`);
    if (maxThreat > Threat_THRESHOLD) {
        console.log("Protocolo de seguridad activado");
    } else {
        console.log("Protocolo de seguridad no activado");
    }
    console.groupEnd();
};

// Ejemplo de uso: lista de sensores (x, y, nivel de amenaza)
const sensors = [
    [5, 5, 7],
    [6, 5, 8],
    [7, 5, 5],
    [10, 10, 9],
    [11, 10, 6],
    [12, 10, 8],
    [15, 15, 4],
    [16, 15, 2],
    [17, 15, 1],
];

// Ejecutando RETO 2
analyzeSensors(sensors);