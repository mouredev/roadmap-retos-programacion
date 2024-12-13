/** #44 - JavaScript -> Jesus Antonio Escamilla */

/**
 * CUENTA ATRÁS MOUREDEV PRO.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

//-------AQUÍ SIN INGRESAR DATOS-------
function countdown(targetDate) {
    const interval = setInterval(() => {
        const now = new Date().getTime();
        const remainingTime = targetDate.getTime() - now;

        if (remainingTime <= 0) {
            console.clear();
            console.log("¡Cuenta atrás finalizada!");
            clearInterval(interval);
            return;
        }

        const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        console.clear();
        console.log(
            `Tiempo restante: ${days} días, ${hours} horas, ${minutes} minutos, ${seconds} segundos`
        );
    }, 1000);
}

const localDate = new Date("2024-12-09T04:46:00");
const targetDateUTC = new Date(localDate.toISOString());

countdown(targetDateUTC);



//-------AQUÍ CON INGRESAR DATOS-------
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const askQuestion = (query) => {
    return new Promise((resolve) => rl.question(query, (answer) => resolve(answer)));
};

(async function main() {
    console.log("\n--- Configuración de cuenta atrás ---\n");

    const day = await askQuestion("Día (dd): ");
    const month = await askQuestion("Mes (mm): ");
    const year = await askQuestion("Año (yyyy): ");
    const hour = await askQuestion("Hora (hh): ");
    const minute = await askQuestion("Minuto (mm): ");
    const second = await askQuestion("Segundo (ss): ");

    rl.close();

    const targetDate = new Date(`${year}-${month}-${day}T${hour}:${minute}:${second}Z`);

    if (isNaN(targetDate.getTime())) {
        console.error("\nFecha inválida. Por favor, intenta de nuevo.");
        return;
    }

    console.log("\nIniciando cuenta atrás...\n");

    countdown(targetDate);
})();

function countdown(targetDate) {
    const interval = setInterval(() => {
        const now = new Date().getTime();
        const remainingTime = targetDate.getTime() - now;

        if (remainingTime <= 0) {
            console.clear();
            console.log("¡Cuenta atrás finalizada!");
            clearInterval(interval);
            return;
        }

        const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        console.clear();
        console.log(
            `Tiempo restante: ${days} días, ${hours} horas, ${minutes} minutos, ${seconds} segundos`
        );
    }, 1000);
}
