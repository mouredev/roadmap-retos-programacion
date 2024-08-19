const readline = require('readline');

// Función que implementa el juego de adivinanzas
function miniGame() {
    // Inicializar la semilla del generador de números aleatorios
    Math.seedrandom(new Date().toISOString());

    console.log("Bienvenido al juego de adivinanzas!");
    console.log("Estoy pensando en un número entre 1 y 100. Adivina cuál es!");

    // Generar número aleatorio entre 1 y 100
    const numeroAleatorio = Math.floor(Math.random() * 100) + 1;
    let intentos = 0;
    let intentoUsuario;

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Ingresa tu intento: ', (answer) => {
        intentoUsuario = parseInt(answer);

        // Verificar que el número esté en el rango válido
        if (intentoUsuario >= 1 && intentoUsuario <= 100) {
            intentos++;

            if (intentoUsuario < numeroAleatorio) {
                console.log("El número que estoy pensando es mayor.");
            } else if (intentoUsuario > numeroAleatorio) {
                console.log("El número que estoy pensando es menor.");
            } else {
                console.log(`¡Felicidades! Has adivinado el número en ${intentos} intentos.`);
                rl.close();
                playAgain();
                return;
            }
        } else {
            console.log("El número debe estar entre 1 y 100.");
        }

        rl.close();
        miniGame();
    });
}

// Función para preguntar si desea jugar de nuevo
function playAgain() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('¿Quieres jugar de nuevo? (s/n): ', (answer) => {
        if (answer.toLowerCase() === 's') {
            rl.close();
            miniGame();
        } else {
            console.log("Gracias por jugar. ¡Hasta luego!");
            rl.close();
        }
    });
}

// Ejemplos de aserciones en JavaScript
console.assert(2 + 2 === 4);
console.log("Checkpoint #1");

console.assert(2 * 2 === 4, "Mensaje personalizado de aserción");
console.log("Checkpoint #2");

console.assert(0o10 + 0o10 === 16, "Otra forma de agregar un mensaje de aserción");
console.log("Checkpoint #3");

console.assert(2 + 2 % 3 === 1, "Success");
console.log("Checkpoint #4");

// Llamada a la función que implementa el juego de adivinanzas
miniGame();

console.assert(2 + 2 === 5, "Failed");
console.log("La ejecución continúa después de la última aserción");
