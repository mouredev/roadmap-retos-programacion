//#47 - CALENDARIO DE ADVIENTO 
/*
 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 *
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
 */

let log = console.log;

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function drawCalendar(discoveredDays) {
    const COLUMNS_COUNT = 6;
    const CELL_WIDTH = 4;
    const CELL_HEIGHT = 3;

    let calendar = '';

    for (let row = 0; row < CELL_HEIGHT; row++) {
        for (let day = 1; day <= 24; day++) {
            if (row === 1) {
                calendar += discoveredDays.includes(day) ? '*'.repeat(CELL_WIDTH) : `*${String(day).padStart(2, '0')}*`;
            } else {
                calendar += '*'.repeat(CELL_WIDTH);
            }
            if (day % COLUMNS_COUNT === 0) {
                calendar += '\n';
            } else {
                calendar += ' ';
            }
        }
        calendar += '\n';
    }

    return calendar;
}

function handleUserInput(discoveredDays) {
    return new Promise((resolve) => {
        rl.question('Enter the day you want to discover (1-24):', (input) => {
            const day = parseInt(input, 10);

            if (isNaN(day) || day < 1 || day > 24) {
                log('\nInvalid day. Please enter a number between 1 and 24.\n');
                return resolve(discoveredDays);
            }

            if (discoveredDays.includes(day)) {
                log(`\nDay ${day} has already been discovered.\n`);
                return resolve(discoveredDays);
            } else {
                log(`\nGift of the day ${day}: ${prices[day - 1]} 🎁 `);
            }

            log(`\nYou have discovered day ${day}!\n`);
            return resolve([...discoveredDays, day]);
        });
    });
}

async function main() {
    let discoveredDays = [];

    while (discoveredDays.length < 24) {
        log('\n     Adviento Calendar!\n');
        log(drawCalendar(discoveredDays));
        discoveredDays = await handleUserInput(discoveredDays);
    }

    log('\n     Adviento Calendar!\n');
    log(drawCalendar(discoveredDays));
    log('Congratulations! You have discovered all 24 days.');
    rl.close();
}

const prices = [
    "$29.99 and Basic Linux Terminal Usage course",
    "$39.99 and How to Perform Smart Commits? course",
    "$49.99 and Introduction to Programming Logic course",
    "$49.99 and Database Fundamentals course",
    "$49.99 and Best Practices in Python course",
    "$59.99 and Functional Programming Fundamentals course",
    "$59.99 and IoT: Current Applications course",
    "$69.99 and Software Design Patterns in Python course",
    "$69.99 and 0 to Hero in PostgreSQL course",
    "$79.99 and Qt4 Interface Development course",
    "$79.99 and Applying SOLID Patterns in Java course",
    "$79.99 and Go: The Language of the Future? course",
    "$89.99 and C# Development course",
    "$89.99 and Artificial Intelligence Fundamentals course",
    "$99.99 and Agile Methodologies Diploma course",
    "$99.99 and Django Rest Framework (DRF) Primer course",
    "$99.99 and Optimization Algorithms in C++ course",
    "$109.99 and Building REST Services with AWS API Gateway and Lambda course",
    "$119.99 and Data Science with Python and R course",
    "$79.99 and Object-Oriented Programming in Java course",
    "$89.99 and Traditional Methodologies Paradigm: Still Relevant? Applicable Cases course",
    "$69.99 and NumPy and Pandas in Python course",
    "$59.99 and Blockchain Fundamentals course",
    "$79.99 and Microservices Architecture with Spring Boot course",
    "$89.99 and Ethical Hacking and Cybersecurity Essentials course"
];


main();
