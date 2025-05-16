/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */

const readline = require('readline');
const rl = readline.createInterface(process.stdin, process.stdout);

console.log('BATALLA DEADPOOL VS WOLVERINE');

const menu = () => {
    rl.question("Vida inicial Deadpool ❤️❤️❤️ -> ", (resp) => {
        let vidaDeadpool = resp;
        rl.question("Vida inicial Wolverine ❤️❤️❤️ -> ", (resp) => {
            let vidaWolverine = resp;
            console.log("\n");
            let turno = 0;
            let regenerate = false;
            while (vidaDeadpool > 0 && vidaWolverine > 0) {
                turno += 1;
                console.log(`\nTurno ${turno}`);

                // deadpool ataca a wolverine
                if (regenerate) {
                    console.log('Deadpool se está regenerando, no puede atacar');
                    regenerate = false;
                }
                else if (Math.random() > 0.2) {
                    let ataqueDeadpool = Math.floor(Math.random() * (100 - 10 + 1)) + 10;

                    console.log(`Deadpool ataca a Wolverine con ${ataqueDeadpool} de daño ⚔️`);

                    if (ataqueDeadpool === 100) {
                        console.log('Deadpool ataca con DAÑO MÁXIMO a Wolverine!! Wolverine no atacará en el siguiente turno ya que tiene que regenerarse ⚔️⚔️⚔️');
                        regenerate = true;
                    }

                    vidaWolverine -= ataqueDeadpool;

                    if (vidaWolverine <= 0) {
                        console.log('\nKO - Wolverine ha sido derrotado :O');
                        console.log('\nBATALLA FINALIZADA!!!');
                        rl.close();
                        continue;
                    } else {
                        console.log('Vida Wolverine -> ', vidaWolverine);
                    }
                } else {
                    console.log('¡Deadpool intenta atacar a Wolverine pero este esquiva el ataque! 🥷');
                }

                // wolverine ataca a deadpool
                if (regenerate) {
                    console.log('Wolverine se está regenerando, no puede atacar');
                    regenerate = false;
                }
                if (Math.random() > 0.25) {
                    let ataqueWolverine = Math.floor(Math.random() * (120 - 10 + 1)) + 10;

                    console.log(`Wolverine ataca a Deadpool con ${ataqueWolverine} de daño ⚔️`);

                    if (ataqueWolverine === 120) {
                        console.log('Wolverine ataca con el DAÑO MÁXIMO a Deadpool! Deadpool no atacará en el siguiente turno ya que tiene que regenerarse ⚔️⚔️⚔️');
                        regenerate = true;
                    }

                    vidaDeadpool -= ataqueWolverine;

                    if (vidaDeadpool <= 0) {
                        console.log('\nKO - Deadpool ha sido derrotado :O');
                        console.log('\nBATALLA FINALIZADA!!!');
                        rl.close();
                        continue;
                    } else {
                        console.log('Vida Deadpool -> ', vidaDeadpool);
                    }
                } else {
                    console.log('¡Wolverine intenta atacar a Deadpool pero este esquiva el ataque! 🥷');
                }
            }
        })
    });
}

menu();