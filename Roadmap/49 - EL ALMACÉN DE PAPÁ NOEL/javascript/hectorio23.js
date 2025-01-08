// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const readline = require("readline");

function generateSecretCode() {
    const pool = ['A', 'B', 'C', '1', '2', '3'];
    for (let i = pool.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [pool[i], pool[j]] = [pool[j], pool[i]];
    }
    return pool.slice(0, 4).join("");
}

function evaluateGuess(secret, guess) {
    for (let i = 0; i < 4; i++) {
        if (guess[i] === secret[i]) {
            console.log(`${guess[i]}: Correcto`);
        } else if (secret.includes(guess[i])) {
            console.log(`${guess[i]}: Presente`);
        } else {
            console.log(`${guess[i]}: Incorrecto`);
        }
    }
}

function isValidGuess(guess) {
    if (guess.length !== 4) {
        console.log("El código debe tener exactamente 4 caracteres.");
        return false;
    }

    const validChars = new Set(['A', 'B', 'C', '1', '2', '3']);
    for (const char of guess) {
        if (!validChars.has(char)) {
            console.log(`Caracter inválido encontrado: ${char}`);
            return false;
        }
    }

    return true;
}

async function main() {
    const secretCode = generateSecretCode();
    let attempts = 10;

    console.log("\n¡Bienvenido al juego del código secreto de Papá Noel!");
    console.log("Debes adivinar el código secreto de 4 caracteres.");
    console.log("Letras: A, B, C | Números: 1, 2, 3\n");

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    while (attempts > 0) {
        console.log(`\nIntentos restantes: ${attempts}`);
        const guess = await new Promise(resolve => rl.question("Introduce tu código: ", resolve));

        if (!isValidGuess(guess)) {
            continue;
        }

        if (guess === secretCode) {
            console.log(`¡Felicidades! Has descifrado el código secreto: ${secretCode}`);
            rl.close();
            return;
        }

        evaluateGuess(secretCode, guess);
        attempts--;
    }

    console.log(`\nLo siento, no has logrado descifrar el código secreto. Era: ${secretCode}`);
    rl.close();
}

main();
