class Luchador {
    nombre: string;
    velocidad: number;
    ataque: number;
    defensa: number;
    salud: number = 100;

    constructor(nombre: string, velocidad: number, ataque: number, defensa: number) {
        this.nombre = nombre;
        this.velocidad = velocidad;
        this.ataque = ataque;
        this.defensa = defensa;
    }

    esquivar(): boolean {
        return Math.random() < 0.2;
    }
}

function batalla(luchador1: Luchador, luchador2: Luchador): Luchador {
    console.log(`¡Batalla entre ${luchador1.nombre} y ${luchador2.nombre}!`);
    let atacante = luchador1.velocidad >= luchador2.velocidad ? luchador1 : luchador2;
    let defensor = atacante === luchador1 ? luchador2 : luchador1;

    while (luchador1.salud > 0 && luchador2.salud > 0) {
        if (defensor.esquivar()) {
            console.log(`${defensor.nombre} esquivó el ataque de ${atacante.nombre}!`);
        } else {
            let danio = atacante.ataque - defensor.defensa;
            if (danio <= 0) {
                danio = atacante.ataque * 0.1;
            }
            defensor.salud -= danio;
            console.log(`${atacante.nombre} ataca a ${defensor.nombre} y causa ${danio.toFixed(2)} de daño. Salud restante de ${defensor.nombre}: ${defensor.salud.toFixed(2)}`);
        }
        [atacante, defensor] = [defensor, atacante];
    }

    const ganador = luchador1.salud > 0 ? luchador1 : luchador2;
    console.log(`¡${ganador.nombre} es el ganador de la batalla!\n`);
    return ganador;
}

async function main(): Promise<void> {
    const luchadores: Luchador[] = [];
    const numLuchadores = parseInt(prompt("Ingrese el número de luchadores (debe ser una potencia de 2): ")!);

    if ((numLuchadores & (numLuchadores - 1)) !== 0 || numLuchadores <= 0) {
        console.log("El número de luchadores debe ser una potencia de 2.");
        return;
    }

    for (let i = 0; i < numLuchadores; i++) {
        const nombre = prompt(`Ingrese el nombre del luchador ${i + 1}: `)!;
        const velocidad = parseInt(prompt(`Ingrese la velocidad de ${nombre} (0-100): `)!);
        const ataque = parseInt(prompt(`Ingrese el ataque de ${nombre} (0-100): `)!);
        const defensa = parseInt(prompt(`Ingrese la defensa de ${nombre} (0-100): `)!);
        luchadores.push(new Luchador(nombre, velocidad, ataque, defensa));
    }

    console.log("¡Comienza el torneo de Dragon Ball: Sparking! ZERO!\n");
    while (luchadores.length > 1) {
        const ganadores: Luchador[] = [];
        luchadores.sort(() => Math.random() - 0.5);

        for (let i = 0; i < luchadores.length; i += 2) {
            const ganador = batalla(luchadores[i], luchadores[i + 1]);
            ganadores.push(ganador);
        }
        luchadores.length = 0;
        luchadores.push(...ganadores);
    }

    console.log(`¡El ganador del torneo es ${luchadores[0].nombre}!`);
}

main();
