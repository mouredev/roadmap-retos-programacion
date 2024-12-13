// Autor:  Héctor Adán
// GitHub: https://github.com/hectorio23

/*
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
class Participant {
    constructor(name, country) {
        this.name = name;
        this.country = country;
    }
}

class Event {
    constructor(name) {
        this.name = name;
        this.participants = [];
    }
}

class OlympicGames {
    constructor() {
        this.events = [];
        this.medalTally = new Map();
    }

    registerEvent() {
        const eventName = prompt("Ingrese el nombre del evento:");
        this.events.push(new Event(eventName));
    }

    registerParticipant() {
        const eventName = prompt("Ingrese el nombre del evento:");
        const event = this.events.find(e => e.name === eventName);

        if (event) {
            const participantName = prompt("Ingrese el nombre del participante:");
            const country = prompt("Ingrese el país del participante:");
            event.participants.push(new Participant(participantName, country));
        } else {
            console.log("Evento no encontrado.");
        }
    }

    simulateEvent() {
        for (const event of this.events) {
            if (event.participants.length >= 3) {
                const shuffledParticipants = event.participants.slice().sort(() => 0.5 - Math.random());

                console.log(`Resultados del evento ${event.name}:`);
                console.log(`Oro: ${shuffledParticipants[0].name} (${shuffledParticipants[0].country})`);
                console.log(`Plata: ${shuffledParticipants[1].name} (${shuffledParticipants[1].country})`);
                console.log(`Bronce: ${shuffledParticipants[2].name} (${shuffledParticipants[2].country})`);

                this.medalTally.set(shuffledParticipants[0].country, (this.medalTally.get(shuffledParticipants[0].country) || 0) + 3);
                this.medalTally.set(shuffledParticipants[1].country, (this.medalTally.get(shuffledParticipants[1].country) || 0) + 2);
                this.medalTally.set(shuffledParticipants[2].country, (this.medalTally.get(shuffledParticipants[2].country) || 0) + 1);
            } else {
                console.log(`El evento ${event.name} no tiene suficientes participantes.`);
            }
        }
    }

    displayMedalTally() {
        console.log("\nRanking de Medallas por País:");
        const sortedTally = Array.from(this.medalTally.entries()).sort((a, b) => b[1] - a[1]);
        for (const [country, points] of sortedTally) {
            console.log(`${country}: ${points} puntos`);
        }
    }

    run() {
        while (true) {
            console.log("\n1. Registro de eventos\n2. Registro de participantes\n3. Simulación de eventos\n4. Creación de informes\n5. Salir");
            const option = parseInt(prompt("Seleccione una opción:"), 10);

            if (option === 1) {
                this.registerEvent();
            } else if (option === 2) {
                this.registerParticipant();
            } else if (option === 3) {
                this.simulateEvent();
            } else if (option === 4) {
                this.displayMedalTally();
            } else if (option === 5) {
                break;
            } else {
                console.log("Opción inválida.");
            }
        }
    }
}

// Inicializa el programa
(() => {
    const games = new OlympicGames();
    games.run();
})();
