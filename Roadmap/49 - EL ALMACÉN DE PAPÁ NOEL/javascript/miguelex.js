const readline = require('readline');

function generateCode() {
    const chars = ['A', 'B', 'C', '1', '2', '3'];
    return chars.sort(() => Math.random() - 0.5).slice(0, 4).join('');
}

const code = generateCode();
let attempts = 10;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

console.log("¡Bienvenido! Tienes 10 intentos para descifrar el código.");

function askForInput() {
    if (attempts === 0) {
        console.log(`Lo siento, no lograste descifrar el código: ${code}`);
        rl.close();
        return;
    }

    rl.question(`Intento #${attempts}: Ingresa un código de 4 caracteres: `, (input) => {
        input = input.toUpperCase();

        if (input.length !== 4 || !/^[A-C1-3]{4}$/.test(input)) {
            console.log("Código inválido. Debe tener 4 caracteres (letras A-C, números 1-3).");
            return askForInput();
        }

        const result = input.split('').map((char, i) => {
            if (char === code[i]) return "Correcto";
            if (code.includes(char)) return "Presente";
            return "Incorrecto";
        });

        console.log(result.join(", "));

        if (input === code) {
            console.log(`¡Felicidades! Descifraste el código: ${code}`);
            rl.close();
        } else {
            attempts--;
            askForInput();
        }
    });
}

askForInput();
