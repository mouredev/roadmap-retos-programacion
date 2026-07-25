const prices = [
    "Curso de lógica de programación", "Diplomado sobre Metodologías Ágiles",
    "Desarrollo de interfaces con Qt4", "Introducción a la programación funcional",
    "Desarrollo en C#", "Buenas prácticas de programación en Java Springboot",
    "¿Cómo hacer Smart Commits?", "Uso básico de la terminal Linux",
    "Primeros pasos en Django Rest Framework (DRF)",
    "Práctica aplicada de los patrones SOLID en Java",
    "Introducción de Base de Datos", "Buenas prácticas dentro de Python",
    "Paradigma de Metodologías Tradicionales ¿Aún tienen uso? ¿En qué casos es aplicable?",
    "Data Science con Python y R", "GO ¿El lenguaje del futuro?",
    "Patrones de Diseño de Software aplicados en Python",
    "Algoritmos de optimización aplicados en C++",
    "Fundamentos de la Inteligencia Artificial",
    "Aplicación en la actualidad del IoT",
    "Uso de librería numpy y pandas dentro de Python",
    "POO aplicada en Java", "0 a héroe en PostgreSQL",
    "Generación de servicios REST con AWS Api Gateway y Lambda"
];

// Array para rastrear los días descubiertos
const discovered = Array(24).fill(false);

// Función para imprimir el calendario
function printCalendar() {
    console.clear();
    console.log("Calendario de aDEViento:");
    for (let i = 0; i < 24; i++) {
        if (i % 6 === 0) console.log(); // Nueva fila cada 6 días

        if (discovered[i]) {
            // Mostrar cuadrícula llena si el día está descubierto
            process.stdout.write("**** ");
        } else {
            // Mostrar cuadrícula con el número del día
            process.stdout.write(`*${String(i + 1).padStart(2, '0')}* `);
        }
    }
    console.log("\n");
}

// Función principal
function startAdventCalendar() {
    while (true) {
        printCalendar();

        let input = prompt("Ingrese el día que quiere descubrir (1-24) o 0 para salir:");
        if (input === null) break; // Salir si el usuario cierra el prompt

        const day = parseInt(input, 10);

        if (isNaN(day)) {
            console.log("⚠️ Entrada no válida. Debes ingresar un número.");
            continue;
        }

        if (day === 0) {
            console.log("¡Gracias por participar en el aDEViento! 🎉");
            break;
        }

        if (day < 1 || day > 24) {
            console.log("⚠️ El día debe estar entre 1 y 24.");
            continue;
        }

        if (discovered[day - 1]) {
            console.log(`⚠️ El día ${day} ya ha sido descubierto.`);
        } else {
            discovered[day - 1] = true;
            console.log(`🎁 Regalo del día ${day}: ${prices[day - 1]}`);
        }
    }
}

// Iniciar el calendario
startAdventCalendar();
