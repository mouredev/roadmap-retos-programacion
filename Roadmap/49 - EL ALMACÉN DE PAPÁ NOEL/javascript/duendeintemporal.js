//#49 - ALMACEN DE PAPÁ NOEL
/*
EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 *
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
 */

//Note: Run => Node + filename in a Node.js enviroitment to display the game interfaz

let log = console.log;

const readline = require('readline');

// Create an interface for input and output
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to generate a random code
function generateCode() {
    const characters = ['A', 'B', 'C', '1', '2', '3'];
    const codeSet = new Set();

    while (codeSet.size < 4) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        codeSet.add(characters[randomIndex]);
    }

    return Array.from(codeSet).join('');
}

// Function to provide feedback on the user's guess
function provideFeedback(secretCode, userGuess) {
    let feedback = {
        correct: 0,
        present: 0,
        incorrect: 0
    };

    const checkedIndices = new Set(); 
    const guessChecked = Array(userGuess.length).fill(false);

    // Check for correct positions
    for (let i = 0; i < secretCode.length; i++) {
        if (userGuess[i] === secretCode[i]) {
            feedback.correct++;
            checkedIndices.add(i); 
            guessChecked[i] = true; 
        }
    }

    // Check for present characters
    for (let i = 0; i < userGuess.length; i++) {
        if (!guessChecked[i]) {
            for (let j = 0; j < secretCode.length; j++) {
                if (userGuess[i] === secretCode[j] && !checkedIndices.has(j)) {
                    feedback.present++;
                    checkedIndices.add(j);
                    guessChecked[i] = true; 
                    break;
                }
            }
        }
    }

    // Calculate incorrect characters
    feedback.incorrect = userGuess.length - feedback.correct - feedback.present;

    return feedback;
}

const startGame = () => {
    const secretCode = generateCode();
    let attempts = 10;
    let gameWon = false;

    log("Welcome to the Secret Code Game!");
    log("You have 10 attempts to guess the 4-character code.");
    log("The code consists of letters (A, B, C) and numbers (1, 2, 3) without repetitions.");

    const askForGuess = () => {
        rl.question(`You have ${attempts} attempts left. Enter your guess (4 characters): `, (userGuess) => {
            // Validate input
            if (userGuess.length !== 4 || !/^[A-C1-3]+$/.test(userGuess)) {
                log("Invalid input. Please enter exactly 4 characters using A, B, C, 1, 2, or 3.");
                askForGuess(); // Ask again
                return;
            }

            const feedback = provideFeedback(secretCode, userGuess);
            log(`Feedback: Correct: ${feedback.correct}, Present: ${feedback.present}, Incorrect: ${feedback.incorrect}`);

            if (feedback.correct === 4) {
                gameWon = true;
                log("Congratulations! You've guessed the secret code!");
                rl.close(); // Close the readline interface
                return;
            }

            attempts--;
            if (attempts > 0) {
                askForGuess(); // Ask for the next guess
            } else {
                log(`Sorry, you've run out of attempts. The secret code was: ${secretCode}`);
                rl.close(); 
            }
        });
    };

    askForGuess(); 
}

startGame();
