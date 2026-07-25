/** #49 - JavaScript -> Jesus Antonio Escamilla */

/**
 * EL ALMACÉN DE PAPÁ NOEL.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function generateCodeSecret() {
    const item = ['A', 'B', 'C', '1', '2', '3'];
    let code = '';

    while (code.length < 4) {
        const indexRandom = Math.floor(Math.random() * item.length);
        const chart = item[indexRandom];
        if (!code.includes(chart)) {
            code += chart;
        }
    }

    return code;
}

function validateEntry(entrance) {
    if (entrance.length !== 4) {
        console.log('El código debe tener exactamente 4 caracteres.');
        return false;
    }

    const pattern = /^[A-C1-3]{4}$/;
    if (!pattern.test(entrance)) {
        console.log('El código solo puede contener letras (A-C) y números (1-3).');
        return false;
    }

    const uniqueCharacters = new Set(entrance);
    if (uniqueCharacters.size !== 4) {
        console.log('El código no debe contener caracteres repetidos.');
        return false;
    }

    return true;
}

function evaluateAttempt(secretCode, attempt) {
    const result = [];

    for (let i = 0; i < attempt.length; i++) {
        if (attempt[i] === secretCode[i]) {
            result.push('Correcto');
        } else if (secretCode.includes(attempt[i])) {
            result.push('Presente');
        } else {
            result.push('Incorrecto');
        }
    }

    return result;
}


function Security() {
    const codeSecret = generateCodeSecret();
    console.log('Papá Noel necesita tu ayuda para abrir el almacén de regalos.');
    console.log('Descifra el código secreto de 4 caracteres (letras: A-C, números: 1-3).');
    console.log('Tienes 10 intentos. ¡Buena suerte!');

    let remainingAttempt = 10;

    const askTry = () => {
        if (remainingAttempt <= 0) {
            console.log('Lo siento, has perdido. El código secreto era: ' + codeSecret);
            rl.close();
            return;
        }

        rl.question(`Introduce tu intento (${remainingAttempt} intentos restantes): `, (userInput) => {
            userInput = userInput.toUpperCase();

            if (!validateEntry(userInput)) {
                askTry();
                return;
            }

            const result = evaluateAttempt(codeSecret, userInput);
            console.log(`Resultado: ${result.join(', ')}`);

            if (userInput === codeSecret) {
                console.log('¡Felicidades! Has descifrado el código secreto y salvado la Navidad.');
                rl.close();
                return;
            }

            remainingAttempt--;
            askTry();
        });
    };

    askTry();
}

Security();