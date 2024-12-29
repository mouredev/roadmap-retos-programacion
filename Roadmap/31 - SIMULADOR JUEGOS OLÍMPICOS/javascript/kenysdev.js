/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#31 * SIMULADOR JUEGOS OLÍMPICOS
-------------------------------------------------------
* EJERCICIO:
* ¡Los JJOO de París 2024 han comenzado!
* Crea un programa que simule la celebración de los juegos.
* El programa debe permitir al usuario registrar eventos y participantes,
* realizar la simulación de los eventos asignando posiciones de manera aleatoria
* y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
*/
// ________________________________________________________

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const GlobalConstants = {
    MEDALS: ['🥇 Oro', '🥈 Plata', '🥉 Bronce'],
    MENU: `
SIMULADOR JUEGOS OLÍMPICOS:
--------------------------------------------------
| 1. Registrar evento        | 4. Crear informes |  
| 2. Registrar participante  | 5. Salir          |
| 3. Simulación de eventos   |                   |
--------------------------------------------------`
};

const data = {
    events: [],
    participants: [],
    simulations: []
};

function getInput(promptText, callback, type = "string") {
    rl.question(promptText, function processInput(input) {
        if (!input || input.trim() === "") {
            rl.question("La entrada no puede estar vacía. Intente de nuevo: ", processInput);
            return;
        }

        if (type === "number") {
            const numValue = Number(input.trim());
            if (isNaN(numValue)) {
                rl.question("Por favor ingresa un número válido: ", processInput);
                return;
            }
            callback(numValue);
            return;
        }
        
        callback(input.trim());
    });
}

function closeInput() {
    rl.close();
}

const Events = {
    addEvent(onComplete) {
        getInput("Deporte: ", (sport) => {
            data.events.push(sport);
            console.log(`${sport} fue agregado`);
            onComplete();
        });
    }
};

const Participants = {
    addParticipant(onComplete) {
        if (data.events.length === 0) {
            console.log("No existe evento en cuál participar. Agrega un evento primero.");
            onComplete();
            return;
        }

        console.log("Selecciona el evento donde participará:");
        data.events.forEach((event, i) => console.log(`${i}. ${event}`));

        getInput("Id del evento: ", (eventId) => {
            if (eventId < 0 || eventId >= data.events.length) {
                console.log("Id no encontrado.");
                onComplete();
                return;
            }

            getInput("Nombre del participante: ", (name) => {
                getInput("País del participante: ", (country) => {
                    data.participants.push({ name, country, eventId });
                    console.log(`${name} fue agregado`);
                    onComplete();
                });
            });
        }, "number");
    }
};

const Simulation = {
    startSimulation() {
        if (data.events.length === 0) {
            console.log("Debe haber al menos un evento.");
            return;
        }

        if (data.participants.length < 3) {
            console.log("Debe haber al menos tres participantes.");
            return;
        }

        const results = data.events.map((event, eventId) => {
            const participantsInEvent = data.participants.filter(p => p.eventId === eventId);
            if (participantsInEvent.length < 3) {
                return { event, winners: null };
            }

            participantsInEvent.forEach(p => (p.score = Math.floor(Math.random() * 100)));
            participantsInEvent.sort((a, b) => b.score - a.score);
            participantsInEvent.slice(0, 3).forEach((p, i) => (p.medal = GlobalConstants.MEDALS[i]));
            return { event, winners: participantsInEvent.slice(0, 3) };
        });

        data.simulations.push(results);
        console.log(`Simulación #${data.simulations.length} creada.`);
    }
};

const Reports = {
    generateReport() {
        if (data.simulations.length === 0) {
            console.log("Aún no hay simulaciones creadas.");
            return;
        }

        data.simulations.forEach((simulation, index) => {
            console.log(`\nSimulación #${index + 1}`);
            simulation.forEach(({ event, winners }) => {
                console.log(`\nEvento: ${event}`);
                if (!winners) {
                    console.log("Cancelado por falta de participantes.");
                    return;
                }

                winners.forEach(({ name, country, score, medal }, i) => {
                    console.log(`${i + 1}. ${name} (${country}) -> Puntos: ${score}, Medalla: ${medal}`);
                });
            });
        });
    }
};

function showMenu() {
    console.log(GlobalConstants.MENU);
    getInput("Opción: ", (option) => {
        switch (option) {
            case "1":
                Events.addEvent(() => showMenu());
                break;
            case "2":
                Participants.addParticipant(() => showMenu());
                break;
            case "3":
                Simulation.startSimulation();
                showMenu();
                break;
            case "4":
                Reports.generateReport();
                showMenu();
                break;
            case "5":
                console.log("Adiós.");
                closeInput();
                break;
            default:
                console.log("Selecciona una opción válida (1-5).");
                showMenu();
        }
    });
}

showMenu()
