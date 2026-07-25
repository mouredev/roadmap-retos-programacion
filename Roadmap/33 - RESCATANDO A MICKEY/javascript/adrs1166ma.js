/*
EJERCICIO:
¡Disney ha presentado un montón de novedades en su D23! 
Pero... ¿Dónde está Mickey?
Mickey Mouse ha quedado atrapado en un laberinto mágico 
creado por Maléfica.
Desarrolla un programa para ayudarlo a escapar.
Requisitos:
1. El laberinto está formado por un cuadrado de 6x6 celdas.
2. Los valores de las celdas serán:
   - ⬜️ Vacío
   - ⬛️ Obstáculo
   - 🐭 Mickey
   - 🚪 Salida
Acciones:
1. Crea una matriz que represente el laberinto (no hace falta
que se genere de manera automática).
2. Interactúa con el usuario por consola para preguntarle hacia
donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
3. Muestra la actualización del laberinto tras cada desplazamiento.
4. Valida todos los movimientos, teniendo en cuenta los límites
del laberinto y los obstáculos. Notifica al usuario.
5. Finaliza el programa cuando Mickey llegue a la salida.
 */
// 🔥 SIMULADOR: ¡Ayuda a Mickey a escapar del laberinto mágico! 🔥

console.log("🎩 ¡Bienvenido al laberinto mágico de Maléfica! 🎩")
console.log("🐭 Mickey necesita tu ayuda para encontrar la salida (🚪).")

// 1. Crear el laberinto
const laberinto = [
    ["⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️"],
    ["⬜️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️"],
    ["🐭", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
    ["⬛️", "⬛️", "⬜️", "⬛️", "⬜️", "⬛️"],
    ["⬜️", "⬜️", "⬜️", "⬛️", "🚪", "⬛️"],
    ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬜️"]
];

// Posición inicial de Mickey
let posicionMickey = { fila: 2, columna: 0 };

// Función principal del programa
function iniciarLaberinto() {
    console.log("\n--- LABERINTO INICIAL ---");
    mostrarLaberinto();

    while (true) {
        const direccion = prompt("¿Hacia dónde quieres mover a Mickey? (arriba/abajo/izquierda/derecha): ").toLowerCase();

        // Validar dirección
        if (!["arriba", "abajo", "izquierda", "derecha"].includes(direccion)) {
            console.log("❌ Dirección no válida. Inténtalo de nuevo.");
            continue;
        }

        // Intentar mover a Mickey
        const nuevaPosicion = calcularNuevaPosicion(posicionMickey, direccion);
        if (!esMovimientoValido(nuevaPosicion)) {
            console.log("❌ Movimiento inválido. Hay un obstáculo o estás fuera del laberinto.");
            continue;
        }

        // Actualizar posición de Mickey
        laberinto[posicionMickey.fila][posicionMickey.columna] = "⬜️"; // Limpiar la posición anterior
        posicionMickey = nuevaPosicion; // Actualizar posición
        laberinto[posicionMickey.fila][posicionMickey.columna] = "🐭"; // Colocar a Mickey en la nueva posición

        // Mostrar el laberinto actualizado
        console.log(`\n--- MOVIMIENTO HACIA ${direccion.toUpperCase()} ---`);
        mostrarLaberinto();

        // Verificar si Mickey llegó a la salida
        if (laberinto[posicionMickey.fila][posicionMickey.columna] === "🚪") {
            console.log("🎉 ¡Felicidades! Mickey ha encontrado la salida. 🚪🐭");
            break;
        }
    }
}

// Función para mostrar el laberinto
function mostrarLaberinto() {
    laberinto.forEach(fila => console.log(fila.join(" ")));
}

// Función para calcular la nueva posición
function calcularNuevaPosicion(posicionActual, direccion) {
    const nuevaPosicion = { ...posicionActual };
    switch (direccion) {
        case "arriba":
            nuevaPosicion.fila -= 1;
            break;
        case "abajo":
            nuevaPosicion.fila += 1;
            break;
        case "izquierda":
            nuevaPosicion.columna -= 1;
            break;
        case "derecha":
            nuevaPosicion.columna += 1;
            break;
    }
    return nuevaPosicion;
}

// Función para validar el movimiento
function esMovimientoValido(posicion) {
    const { fila, columna } = posicion;

    // Verificar límites del laberinto
    if (fila < 0 || fila >= laberinto.length || columna < 0 || columna >= laberinto[0].length) {
        return false;
    }

    // Verificar obstáculos
    if (laberinto[fila][columna] === "⬛️") {
        return false;
    }

    return true;
}

iniciarLaberinto()