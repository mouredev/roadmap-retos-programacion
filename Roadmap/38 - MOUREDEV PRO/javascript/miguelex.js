const fs = require('fs');

function obtenerSuscriptoresActivos(archivoCsv) {
    const data = fs.readFileSync(archivoCsv, 'utf-8');
    const filas = data.split('\n').slice(1); // Saltar la primera fila (cabeceras)

    const suscriptores = [];
    for (let fila of filas) {
        const [id, email, status] = fila.split(',');
        if (status.trim().toLowerCase() === 'activo') {
            suscriptores.push({ id: id.trim(), email: email.trim() });
        }
    }

    return suscriptores;
}

function seleccionarGanadores(suscriptores, numeroGanadores) {
    if (suscriptores.length < numeroGanadores) {
        return null; 
    }

    const ganadores = [];
    const indicesSeleccionados = new Set();

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
