/* 🔥 EJERCICIO:
¡Los JJOO de París 2024 han comenzado!
Crea un programa que simule la celebración de los juegos.
El programa debe permitir al usuario registrar eventos y participantes,
realizar la simulación de los eventos asignando posiciones de manera aleatoria
y generar un informe final. Todo ello por terminal.
Requisitos:
1. Registrar eventos deportivos.
2. Registrar participantes por nombre y país.
3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
5. Mostrar los ganadores por cada evento.
6. Mostrar el ranking de países según el número de medallas.
Acciones:
1. Registro de eventos.
2. Registro de participantes.
3. Simulación de eventos.
4. Creación de informes.
5. Salir del programa.
 */
console.log("🎉 ¡Bienvenido a los JJOO de París 2024! 🎉");

// Variables globales
const eventos = [];
const participantes = [];
const resultados = [];

// Función principal del programa
function iniciarPrograma() {
    let continuar = true;

    while (continuar) {
        console.log("\n--- MENÚ PRINCIPAL ---");
        console.log("1. Registrar evento.");
        console.log("2. Registrar participante.");
        console.log("3. Simular eventos.");
        console.log("4. Crear informe de resultados.");
        console.log("5. Salir del programa.");

        const opcion = prompt("Seleccione una opción (1-5): ");

        switch (opcion) {
            case "1":
                registrarEvento();
                break;
            case "2":
                registrarParticipante();
                break;
            case "3":
                simularEventos();
                break;
            case "4":
                crearInforme();
                break;
            case "5":
                console.log("👋 ¡Gracias por usar el simulador de los JJOO de París 2024! 👋");
                continuar = false;
                break;
            default:
                console.log("❌ Opción no válida. Intente de nuevo.");
        }
    }
}

// 1. Registrar evento
function registrarEvento() {
    const nombre = prompt("Ingrese el nombre del evento: ");
    if (!nombre) {
        console.log("❌ El nombre del evento no puede estar vacío.");
        return;
    }

    eventos.push({ nombre, participantes: [] });
    console.log(`✅ Evento "${nombre}" registrado.`);
}

// 2. Registrar participante
function registrarParticipante() {
    const nombre = prompt("Ingrese el nombre del participante: ");
    const pais = prompt("Ingrese el país del participante: ");

    if (!nombre || !pais) {
        console.log("❌ El nombre y el país del participante son obligatorios.");
        return;
    }

    participantes.push({ nombre, pais });
    console.log(`✅ Participante "${nombre}" (${pais}) registrado.`);
}

// 3. Simular eventos
function simularEventos() {
    if (eventos.length === 0) {
        console.log("❌ No hay eventos registrados para simular.");
        return;
    }

    if (participantes.length < 3) {
        console.log("❌ Se necesitan al menos 3 participantes para simular un evento.");
        return;
    }

    for (const evento of eventos) {
        const participantesAleatorios = seleccionarParticipantesAleatorios(3);
        const resultadosSimulados = simularResultados(participantesAleatorios);

        // Asignar medallas
        const medallas = ["Oro", "Plata", "Bronce"];
        resultadosSimulados.forEach((resultado, index) => {
            const medalla = medallas[index];
            resultados.push({ evento: evento.nombre, participante: resultado, medalla });
        });

        console.log(`\n🏆 Resultados del evento "${evento.nombre}":`);
        resultadosSimulados.forEach((participante, index) => {
            console.log(`${medallas[index]}: ${participante.nombre} (${participante.pais})`);
        });
    }
}

// Función auxiliar: Seleccionar participantes aleatorios
function seleccionarParticipantesAleatorios(cantidad) {
    const copiaParticipantes = [...participantes];
    const seleccionados = [];

    for (let i = 0; i < cantidad; i++) {
        const indiceAleatorio = Math.floor(Math.random() * copiaParticipantes.length);
        seleccionados.push(copiaParticipantes.splice(indiceAleatorio, 1)[0]);
    }

    return seleccionados;
}

// Función auxiliar: Simular resultados (orden aleatorio)
function simularResultados(participantesAleatorios) {
    return participantesAleatorios.sort(() => Math.random() - 0.5);
}

// 4. Crear informe de resultados
function crearInforme() {
    if (resultados.length === 0) {
        console.log("❌ No hay resultados disponibles para generar el informe.");
        return;
    }

    // Contar medallas por país
    const rankingPaises = {};
    for (const resultado of resultados) {
        const { pais } = resultado.participante;
        if (!rankingPaises[pais]) {
            rankingPaises[pais] = { Oro: 0, Plata: 0, Bronce: 0 };
        }
        rankingPaises[pais][resultado.medalla]++;
    }

    // Mostrar ganadores por evento
    console.log("\n--- GANADORES POR EVENTO ---");
    eventos.forEach(evento => {
        console.log(`\nEvento: ${evento.nombre}`);
        const resultadosEvento = resultados.filter(r => r.evento === evento.nombre);
        resultadosEvento.forEach(resultado => {
            console.log(`${resultado.medalla}: ${resultado.participante.nombre} (${resultado.participante.pais})`);
        });
    });

    // Mostrar ranking de países
    console.log("\n--- RANKING DE PAÍSES ---");
    const paisesOrdenados = Object.entries(rankingPaises).sort((a, b) => {
        return (
            b[1].Oro - a[1].Oro ||
            b[1].Plata - a[1].Plata ||
            b[1].Bronce - a[1].Bronce
        );
    });

    paisesOrdenados.forEach(([pais, medallas], index) => {
        console.log(
            `${index + 1}. ${pais}: Oro=${medallas.Oro}, Plata=${medallas.Plata}, Bronce=${medallas.Bronce}`
        );
    });
}

iniciarPrograma();