// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const TOTAL_DAYS = 24;
const COLUMNS = 6;
const GRID_WIDTH = 4;
const GRID_HEIGHT = 3;

// Función para dibujar el calendario
function drawCalendar(openedDays) {
    for (let row = 0; row < TOTAL_DAYS / COLUMNS; row++) {
        for (let h = 0; h < GRID_HEIGHT; h++) { // Cada fila de la cuadrícula
            let line = "";

            for (let col = 0; col < COLUMNS; col++) {
                const day = row * COLUMNS + col + 1;

                if (h === 0 || h === GRID_HEIGHT - 1) {
                    // Bordes superior e inferior
                    line += "**** ";
                } else if (h === Math.floor(GRID_HEIGHT / 2)) {
                    // Línea central con el número del día o asteriscos si está descubierto
                    if (openedDays[day - 1]) {
                        line += "**** ";
                    } else {
                        line += `*${String(day).padStart(2, '0')}* `;
                    }
                } else {
                    // Espaciado intermedio
                    line += "*  * ";
                }
            }
            console.log(line);
        }
    }
}

// Programa principal
function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const openedDays = new Array(TOTAL_DAYS).fill(false);

    console.log("\nBienvenido al calendario de aDEViento!\n");

    function askUser() {
        drawCalendar(openedDays);
        rl.question("\nSelecciona un día (1-24) o escribe 'salir' para terminar: ", (userInput) => {
            if (userInput.toLowerCase() === "salir") {
                console.log("Gracias por participar!\n");
                rl.close();
                return;
            }

            // Validar la entrada
            const selectedDay = parseInt(userInput, 10);
            if (isNaN(selectedDay)) {
                console.log("Entrada no válida. Inténtalo de nuevo.\n");
                return askUser();
            }

            if (selectedDay < 1 || selectedDay > TOTAL_DAYS) {
                console.log("Número fuera de rango. Inténtalo de nuevo.\n");
                return askUser();
            }

            // Verificar el estado del día seleccionado
            if (openedDays[selectedDay - 1]) {
                console.log(`El día ${selectedDay} ya ha sido descubierto.\n`);
            } else {
                openedDays[selectedDay - 1] = true;
                console.log(`Has descubierto el día ${selectedDay}! Felicidades!\n`);
            }
            askUser();
        });
    }

    askUser();
}

main();
