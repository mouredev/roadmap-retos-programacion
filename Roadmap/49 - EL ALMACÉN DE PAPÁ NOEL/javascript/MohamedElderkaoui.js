const readline = require('readline');

// Configuración para capturar la entrada del usuario
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// Generar el código secreto
function generateSecretCode() {
    const pool = ['A', 'B', 'C', '1', '2', '3'];
    const shuffled = pool.sort(() => Math.random() - 0.5);
    return shuffled.slice(0, 4).join('');
}

// Validar la entrada del usuario
function isValidInput(input) {
    if (input.length !== 4) return false;
    const validChars = new Set(['A', 'B', 'C', '1', '2', '3']);
    const seenChars = new Set();
    for (let char of input) {
        if (!validChars.has(char) || seenChars.has(char)) {
            return false;
        }
        seenChars.add(char);
    }
    return true;
}

// Evaluar el intento del usuario y generar pistas
function evaluateGuess(guess, secretCode) {
    const feedback = [];
    for (let i = 0; i < guess.length; i++) {
        if (guess[i] === secretCode[i]) {
            feedback.push(`${guess[i]}: Correcto`);
        } else if (secretCode.includes(guess[i])) {
            feedback.push(`${guess[i]}: Presente`);
        } else {
            feedback.push(`${guess[i]}: Incorrecto`);
        }
    }
    return feedback.join(' | ');
}

// Lógica principal del juego
function playGame() {
    const secretCode = generateSecretCode();
    console.log("¡El almacén de Papá Noel está cerrado!");
    console.log("Intenta adivinar el código secreto de 4 caracteres (Letras: A-C, Números: 1-3).");
    console.log("Tienes 10 intentos. ¡Buena suerte!");

    let attempts = 0;
    let hasGuessed = false;

    const askInput = () => {
        if (attempts >= 10 || hasGuessed) {
            if (hasGuessed) {
                console.log("¡Felicidades! Has descifrado el código secreto y salvado la Navidad. 🎅🎁");
            } else {
                console.log(`Oh no, no has logrado descifrar el código. 😔 El código era: ${secretCode}`);
            }
            rl.close();
            return;
        }

        rl.question(`Intento ${attempts + 1}/10: Escribe tu código: `, (userInput) => {
            userInput = userInput.toUpperCase();

            if (!isValidInput(userInput)) {
                console.log("Entrada inválida. Asegúrate de que sea de 4 caracteres (A-C y 1-3) sin repetidos.");
                askInput();
                return;
            }

            const feedback = evaluateGuess(userInput, secretCode);
            console.log(feedback);

            if (userInput === secretCode) {
                hasGuessed = true;
            } else {
                attempts++;
            }

            askInput();
        });
    };

    askInput();
}

// Iniciar el juego
playGame();
