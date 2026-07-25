/*
EJERCICIO:
¡Deadpool y Wolverine se enfrentan en una batalla épica!
Crea un programa que simule la pelea y determine un ganador.
El programa simula un combate por turnos, donde cada protagonista posee unos
puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
de regeneración y evasión de ataques.
Requisitos:
1. El usuario debe determinar la vida inicial de cada protagonista.
2. Cada personaje puede impartir un daño aleatorio:
   - Deadpool: Entre 10 y 100.
   - Wolverine: Entre 10 y 120.
3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
4. Cada personaje puede evitar el ataque contrario:
   - Deadpool: 25% de posibilidades.
   - Wolverine: 20% de posibilidades.
5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
Acciones:
1. Simula una batalla.
2. Muestra el número del turno (pausa de 1 segundo entre turnos).
3. Muestra qué pasa en cada turno.
4. Muestra la vida en cada turno.
5. Muestra el resultado final.
 */
// 🔥 SIMULADOR DE LA BATALLA ENTRE DEADPOOL Y WOLVERINE 🔥

console.log("⚔️ ¡Deadpool vs Wolverine: Batalla Épica! ⚔️")

// Función principal del programa
function iniciarBatalla() {
    console.log("\n--- CONFIGURACIÓN INICIAL ---");

    // 1. Configurar vida inicial
    const vidaDeadpool = parseInt(prompt("Ingrese la vida inicial de Deadpool (ej. 200): "));
    const vidaWolverine = parseInt(prompt("Ingrese la vida inicial de Wolverine (ej. 200): "));

    if (isNaN(vidaDeadpool) || isNaN(vidaWolverine) || vidaDeadpool <= 0 || vidaWolverine <= 0) {
        console.log("❌ La vida inicial debe ser un número positivo.");
        return;
    }

    // Estado inicial de los personajes
    let deadpool = { nombre: "Deadpool", vida: vidaDeadpool, maximoDanio: 100 };
    let wolverine = { nombre: "Wolverine", vida: vidaWolverine, maximoDanio: 120 };
    let turno = 1;

    // Variable para controlar si un personaje está en regeneración
    let deadpoolRegenerando = false;
    let wolverineRegenerando = false;

    console.log("\n--- COMIENZA LA BATALLA ---");

    while (deadpool.vida > 0 && wolverine.vida > 0) {
        console.log(`\n--- TURNO ${turno} ---`);

        // Deadpool ataca
        if (!deadpoolRegenerando) {
            const resultado = atacar(deadpool, wolverine);
            console.log(resultado);
            if (resultado.includes("máximo daño")) {
                wolverineRegenerando = true; // Wolverine no ataca en el siguiente turno
            }
        } else {
            console.log(`${deadpool.nombre} está regenerándose y no puede atacar.`);
            deadpoolRegenerando = false; // Regeneración completa
        }

        // Verificar si Wolverine ha perdido
        if (wolverine.vida <= 0) {
            console.log(`💀 ${wolverine.nombre} ha sido derrotado.`);
            break;
        }

        // Wolverine ataca
        if (!wolverineRegenerando) {
            const resultado = atacar(wolverine, deadpool);
            console.log(resultado);
            if (resultado.includes("máximo daño")) {
                deadpoolRegenerando = true; // Deadpool no ataca en el siguiente turno
            }
        } else {
            console.log(`${wolverine.nombre} está regenerándose y no puede atacar.`);
            wolverineRegenerando = false; // Regeneración completa
        }

        // Mostrar vida actual
        console.log(`❤️ Vida de ${deadpool.nombre}: ${deadpool.vida}`);
        console.log(`❤️ Vida de ${wolverine.nombre}: ${wolverine.vida}`);

        // Incrementar turno y pausa de 1 segundo
        turno++;
        pausa(1000);
    }

    // Resultado final
    console.log("\n--- RESULTADO FINAL ---");
    if (deadpool.vida > 0) {
        console.log(`🎉 ¡${deadpool.nombre} es el ganador! 🎉`);
    } else {
        console.log(`🎉 ¡${wolverine.nombre} es el ganador! 🎉`);
    }
}

// Función para simular un ataque
function atacar(atacante, defensor) {
    // Determinar si el ataque es evadido
    const evade = Math.random();
    if ((atacante.nombre === "Deadpool" && evade < 0.25) || (atacante.nombre === "Wolverine" && evade < 0.2)) {
        return `💨 ${defensor.nombre} ha evadido el ataque de ${atacante.nombre}.`;
    }

    // Calcular daño
    const danio = Math.floor(Math.random() * atacante.maximoDanio) + 10;
    defensor.vida -= danio;

    // Mensaje según el daño
    if (danio === atacante.maximoDanio) {
        return `💥 ${atacante.nombre} ha infligido el máximo daño (${danio}). ${defensor.nombre} debe regenerarse.`;
    } else {
        return `⚔️ ${atacante.nombre} ha atacado a ${defensor.nombre} causando ${danio} puntos de daño.`;
    }
}

// Función para pausa (simulación de tiempo)
function pausa(ms) {
    const inicio = Date.now();
    while (Date.now() - inicio < ms) {}
}

iniciarBatalla()