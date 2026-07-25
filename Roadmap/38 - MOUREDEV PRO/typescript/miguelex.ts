import * as fs from 'fs';

interface Suscriptor {
    id: string;
    email: string;
}

function obtenerSuscriptoresActivos(archivoCsv: string): Suscriptor[] {
    const data = fs.readFileSync(archivoCsv, 'utf-8');
    const filas = data.split('\n').slice(1); // Saltar la primera fila (cabeceras)

    const suscriptores: Suscriptor[] = [];
    for (const fila of filas) {
        const [id, email, status] = fila.split(',');
        if (status.trim().toLowerCase() === 'activo') {
            suscriptores.push({ id: id.trim(), email: email.trim() });
        }
    }

    return suscriptores;
}

function seleccionarGanadores(suscriptores: Suscriptor[], numeroGanadores: number): Suscriptor[] | null {
    if (suscriptores.length < numeroGanadores) {
        return null; 
    }

    const ganadores: Suscriptor[] = [];
    const indicesSeleccionados = new Set<number>();

    while (ganadores.length < numeroGanadores) {
        const indiceAleatorio = Math.floor(Math.random() * suscriptores.length);
        if (!indicesSeleccionados.has(indiceAleatorio)) {
            ganadores.push(suscriptores[indiceAleatorio]);
            indicesSeleccionados.add(indiceAleatorio);
        }
    }

    return ganadores;
}

const archivoCsv = 'suscriptores.csv';

const suscriptoresActivos = obtenerSuscriptoresActivos(archivoCsv);

if (suscriptoresActivos.length > 0) {
    const ganadores = seleccionarGanadores(suscriptoresActivos, 3);
    if (ganadores) {
        console.log("Ganador de la suscripción:", ganadores[0]);
        console.log("Ganador del descuento:", ganadores[1]);
        console.log("Ganador del libro:", ganadores[2]);
    } else {
        console.log("No hay suficientes suscriptores activos para seleccionar 3 ganadores.");
    }
} else {
    console.log("No hay suscriptores activos.");
}
