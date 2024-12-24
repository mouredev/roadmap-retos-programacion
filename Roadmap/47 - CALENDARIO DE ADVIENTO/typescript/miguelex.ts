const GRID_WIDTH = 4;
const GRID_HEIGHT = 3;
const DAYS = 24;

const discovered: boolean[] = Array(DAYS).fill(false);

function drawCalendar(discovered: boolean[]): void {
    for (let row = 0; row < Math.ceil(DAYS / 6); row++) {
        for (let line = 0; line < GRID_HEIGHT; line++) {
            let rowOutput = "";
            for (let col = 0; col < 6; col++) {
                const day = row * 6 + col + 1;
                if (day > DAYS) break;

                switch (line) {
                    case 0:
                    case 2:
                        rowOutput += "*".repeat(GRID_WIDTH) + " ";
                        break;
                    case 1:
                        rowOutput += "*";
                        rowOutput += discovered[day - 1]
                            ? "*".repeat(GRID_WIDTH - 2)
                            : day.toString().padStart(2, "0").padEnd(GRID_WIDTH - 2, " ");
                        rowOutput += "* ";
                        break;
                }
            }
            console.log(rowOutput);
        }
    }
}

function promptUser(): void {
    drawCalendar(discovered);

    const readline = require("readline");
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question(`\nSeleccione un día (1-${DAYS}) para descubrir o escriba 0 para salir: `, (input: string) => {
        const day = parseInt(input, 10);

        if (day === 0) {
            console.log("¡Gracias por participar en el aDEViento!");
            rl.close();
            return;
        }

        if (isNaN(day) || day < 1 || day > DAYS) {
            console.log(`Por favor, elija un número válido entre 1 y ${DAYS}.`);
        } else if (discovered[day - 1]) {
            console.log(`El día ${day} ya ha sido descubierto.`);
        } else {
            discovered[day - 1] = true;
            console.log(`¡Has descubierto el día ${day}!`);
        }

        rl.close();
        promptUser();
    });
}


promptUser();
