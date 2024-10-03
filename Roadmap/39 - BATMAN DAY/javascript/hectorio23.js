// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23


//////////////////////////////////////////////////
///////////////////// RETO 1 /////////////////////
//////////////////////////////////////////////////

function calculateBatmanDay() {
    const currentYear = new Date().getFullYear();
    for (let year = currentYear; year <= 2039; year++) {
        const septemberFirst = new Date(year, 8, 1);  // Mes 8 es septiembre
        const dayOfWeek = septemberFirst.getDay();
        const thirdSaturday = new Date(septemberFirst);
        thirdSaturday.setDate(septemberFirst.getDate() + ((5 - dayOfWeek + 7) % 7) + 14);
        console.log(`Batman Day ${year}: ${thirdSaturday.toISOString().slice(0, 10)}`);
    }
}

calculateBatmanDay();


//////////////////////////////////////////////////
///////////////////// RETO 2 /////////////////////
//////////////////////////////////////////////////

function batcaveSecuritySystem(sensors) {
    const gridSize = 20;
    const threshold = 20;
    let maxThreat = 0;
    let criticalArea = null;

    // Analizar todas las áreas de 3x3 en la cuadrícula
    for (let i = 0; i <= gridSize - 3; i++) {
        for (let j = 0; j <= gridSize - 3; j++) {
            let threatSum = 0;
            for (let x = i; x < i + 3; x++) {
                for (let y = j; y < j + 3; y++) {
                    threatSum += sensors[`${x},${y}`] || 0;
                }
            }
            if (threatSum > maxThreat) {
                maxThreat = threatSum;
                criticalArea = [i + 1, j + 1];  // Centro de la cuadrícula
            }
        }
    }

    // Calcular distancia desde la Batcueva (0, 0)
    if (criticalArea) {
        const distance = Math.abs(criticalArea[0]) + Math.abs(criticalArea[1]);
        console.log(`Área más amenazada: ${criticalArea}, Amenazas: ${maxThreat}, Distancia a la Batcueva: ${distance}`);
        if (maxThreat > threshold) {
            console.log('Protocolo de seguridad activado.');
        }
    }
}

// Ejemplo de sensores
const sensors = {
    '5,5': 8, '5,6': 7, '5,7': 6,
    '6,5': 9, '6,6': 5, '6,7': 4,
    '7,5': 3, '7,6': 2, '7,7': 10
};

batcaveSecuritySystem(sensors);


