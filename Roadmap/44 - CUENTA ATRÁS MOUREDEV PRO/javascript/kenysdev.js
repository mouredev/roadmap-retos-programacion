/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#44 CUENTA ATRÁS MOUREDEV PRO
-------------------------------------------------------
* EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente.
 */
// ________________________________________________________
const readline = require('readline');

class ReverseTimer {
    constructor(endDate) {
        this.endDate = new Date(endDate);
        if (isNaN(this.endDate)) {
            throw new Error("La fecha de finalización no es válida.");
        }
    }

    timeRemaining() {
        const now = new Date();
        const delta = this.endDate - now;
        return Math.max(delta, 0);
    }

    hasFinished() {
        return this.timeRemaining() === 0;
    }

    toString() {
        const delta = this.timeRemaining();
        const days = Math.floor(delta / (1000 * 60 * 60 * 24));
        const hours = Math.floor((delta % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((delta % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((delta % (1000 * 60)) / 1000);
        return `${days} días, ${hours} horas, ${minutes} minutos, ${seconds} segundos.`;
    }

    printRemaining() {
        const interval = setInterval(() => {
            // Limpiar la consola
            readline.cursorTo(process.stdout, 0, 0);
            readline.clearScreenDown(process.stdout);

            console.log("Tiempo restante:");
            console.log(this.toString());

            if (this.hasFinished()) {
                console.log("¡Cuenta atrás finalizada!");
                clearInterval(interval);
            }
        }, 1000);
    }
}

// Uso del temporizador
const endDate = "2024-12-31T23:59:59.999Z"; // UTC explícito
const timer = new ReverseTimer(endDate);
timer.printRemaining();
