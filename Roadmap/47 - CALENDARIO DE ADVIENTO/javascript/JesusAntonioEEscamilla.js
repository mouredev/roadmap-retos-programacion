/** #47 - JavaScript -> Jesus Antonio Escamilla */

/**
 * CALENDARIO DE ADVIENTO.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const DAYS = 24;

const calendar = Array.from({ length: DAYS }, (_, i) => ({
    day: (i + 1).toString().padStart(2, '0'),
    discovered: false,
}));

function drawCalendar() {
    let output = '';

    for (let i = 0; i < DAYS; i += 6) {
        output += '**** '.repeat(6).trim() + '\n';

        output += calendar
            .slice(i, i + 6)
            .map((cell) => (cell.discovered ? '****' : `*${cell.day}*`))
            .join(' ') + '\n';

        output += '**** '.repeat(6).trim() + '\n';    
    }

    console.log(output);
}

function discoverDay(day) {
    const index = day - 1;

    if (index < 0 || index >= DAYS) {
        console.log("Por favor, selecciona un número entre 1 y 24.\n");
        return;
    }

    if (calendar[index].discovered) {
        console.log(`El dia ${day} ya ha sido descubierto\n`);
    } else {
        console.log(`¡Has abierto el dia ${day}!\n`);
        calendar[index].discovered = true;
    }
}

function runCalendar() {
    drawCalendar();
    rl.question('Selecciona una dia par abrir (1-24): ', (input) => {
        if (input.toLowerCase() == " ") {
            rl.close();
            return;
        }

        const day = parseInt(input, 10);

        if (!isNaN(day) && day >= 1 && day <= 25) {
            discoverDay(day);
        }else {
            console.log("Por favor, ingresa un número válido.\n");
        }

        runCalendar();
    });
}

// Mostrar el calendario de adviento
console.log('¡Bienvenido al calendario del aDEViento!');
runCalendar();