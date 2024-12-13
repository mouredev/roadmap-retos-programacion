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

let deadPoolcounter = 1;
let wolverineCounter = 1;
let allWolverineDamage = [0];
let allDeadpoolDamage = [0];
let deadpoolIndexCounter = 0;
let wolverineIndexCounter = 0;

function epicBattle(wolverineInitialLife, deadpoolInitialLife) {
  const deadpoolAtack = Math.random() <= 0.25 ? 0 : Math.floor(Math.random() * (101 - 10) + 10);
  const wolverineAtack = Math.random() <= 0.20 ? 0 : Math.floor(Math.random() * (121 - 10) + 10);
  let deadpoolPreviousDamage = allDeadpoolDamage[deadpoolIndexCounter++];
  let wolverinePreviousDamage = allWolverineDamage[wolverineIndexCounter++];
  let wolverineLife = wolverineInitialLife;
  let deadpoolLife = deadpoolInitialLife;

  if (wolverineLife <= 0) {
    console.log("\n+++++++++ ⚔️ Deadpool derrotó a Wolverine +++++++++");

    return;
  } else if (deadpoolLife <= 0) {
    console.log("\n+++++++++ 🐺 Wolverine derrotó a Deadpool +++++++++");

    return;
  }

  if (deadPoolcounter === 1 && wolverineCounter === 1) {
    console.log(`Vida inicial de Wolverine: ${wolverineInitialLife} ||| Vida inicial de Deadpool: ${deadpoolInitialLife}`);
  }

  console.log(`\nTurno ${deadPoolcounter++} de Deadpool ----------`);

  if (wolverinePreviousDamage === 120) {
    allDeadpoolDamage.push(0);

    console.log("🚫 Deadpool se encuentra regenerándose.");
  } else {
    allDeadpoolDamage.push(deadpoolAtack);

    if (deadpoolAtack === 0) {
      console.log("🛡️ Wolverine evadió el ataque.");
    }

    console.log(`💥 Ataque de Deadpool: ${deadpoolAtack}`);
    console.log("🩸 Vida de Wolverine: ", wolverineLife - deadpoolAtack);
  }

  console.log(`\nTurno ${wolverineCounter++} de Wolverine ---------`);

  if (deadpoolPreviousDamage === 100) {
    allWolverineDamage.push(0);

    console.log("🚫 Wolverine se encuentra regenerándose.");
  } else {
    allWolverineDamage.push(wolverineAtack);

    if (wolverineAtack === 0) {
      console.log("🛡️ Deadpool evadió el ataqué.");
    }

    console.log(`💥 Ataque de Wolverine: ${wolverineAtack}`);
    console.log("🩸 Vida de Deadpool: ", deadpoolLife - wolverineAtack);
  }

  setTimeout(() => {
    return epicBattle(wolverinePreviousDamage === 120 ? wolverineInitialLife : wolverineInitialLife - deadpoolAtack, deadpoolPreviousDamage === 100 ? deadpoolInitialLife : deadpoolInitialLife - wolverineAtack);
  }, 1000);
}

epicBattle(300, 300);
