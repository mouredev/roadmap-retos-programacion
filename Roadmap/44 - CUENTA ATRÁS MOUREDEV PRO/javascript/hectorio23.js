// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const readline = require("readline");
const { clearInterval, setInterval } = require("timers");

// Leer entrada del usuario
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// Función para solicitar entrada
const prompt = (query) => new Promise((resolve) => rl.question(query, resolve));

// Función para iniciar la cuenta atrás
function startCountdown(targetDate) {
    const timer = setInterval(() => {
        const now = new Date();
        const diff = targetDate - now;

        if (diff <= 0) {
            console.clear();
            console.log("¡Cuenta atrás finalizada!");
            clearInterval(timer);
            rl.close();
            return;
        }

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((diff / (1000 * 60)) % 60);
        const seconds = Math.floor((diff / 1000) % 60);

        console.clear();
        console.log(`Tiempo restante: ${days} días, ${hours} horas, ${minutes} minutos, ${seconds} segundos`);
    }, 1000);
}

// Función principal
(async function main() {
    const day = await prompt("Día: ");
    const month = await prompt("Mes: ");
    const year = await prompt("Año: ");
    const hour = await prompt("Hora: ");
    const minute = await prompt("Minuto: ");
    const second = await prompt("Segundo: ");

    const targetDate = new Date(Date.UTC(year, month - 1, day, hour, minute, second));
    console.log(`Fecha objetivo (UTC): ${targetDate.toISOString()}`);
    startCountdown(targetDate);
})();
