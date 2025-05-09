/*
EJERCICIO:
¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
¿Qué pasaría si tuvieras que encargarte de repartir los anillos
entre las razas de la Tierra Media?
Desarrolla un programa que se encargue de distribuirlos.
Requisitos:
1. Los Elfos recibirán un número impar.
2. Los Enanos un número primo.
3. Los Hombres un número par.
4. Sauron siempre uno.
Acciones:
1. Crea un programa que reciba el número total de anillos
   y busque una posible combinación para repartirlos.
2. Muestra el reparto final o el error al realizarlo.
 */
// 🔥 SIMULADOR: Reparto de los Anillos de Poder 🔥
console.log("💍 ¡Bienvenido al repartidor de los Anillos de Poder! 💍");

// Función principal del programa
function repartirAnillos() {
    const totalAnillos = parseInt(prompt("Ingrese el número total de anillos: "));

    if (isNaN(totalAnillos) || totalAnillos <= 0) {
        console.log("❌ El número de anillos debe ser un entero positivo.");
        return;
    }

    // Sauron siempre recibe 1 anillo
    const sauron = 1;
    const anillosRestantes = totalAnillos - sauron;

    // Buscar combinaciones válidas
    for (let elfos = 1; elfos < anillosRestantes; elfos += 2) { // Número impar para Elfos
        for (let enanos = 2; enanos < anillosRestantes; enanos++) { // Número primo para Enanos
            if (!esPrimo(enanos)) continue;

            const hombres = anillosRestantes - (elfos + enanos); // Número par para Hombres
            if (hombres > 0 && hombres % 2 === 0) {
                console.log("\n--- REPARTO FINAL ---");
                console.log(`Elfos: ${elfos} (número impar)`);
                console.log(`Enanos: ${enanos} (número primo)`);
                console.log(`Hombres: ${hombres} (número par)`);
                console.log(`Sauron: ${sauron}`);
                return;
            }
        }
    }

    // Si no se encuentra una combinación válida
    console.log("❌ No es posible repartir los anillos con las reglas dadas.");
}

// Función para verificar si un número es primo
function esPrimo(numero) {
    if (numero < 2) return false;
    for (let i = 2; i <= Math.sqrt(numero); i++) {
        if (numero % i === 0) return false;
    }
    return true;
}

repartirAnillos();