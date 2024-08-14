
/* https://github.com/dfc201692
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

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function battle(deadpoolLife, wolverineLife) {
    let turn = 1;

    while (deadpoolLife > 0 && wolverineLife > 0) {
        console.log(`Turno ${turn}:`);
        
        // Deadpool ataca a Wolverine
        if (Math.random() > 0.25) { // Deadpool no evade
            let deadpoolDamage = getRandomInt(10, 100);
            console.log(`Deadpool ataca a Wolverine y causa ${deadpoolDamage} de daño.`);
            wolverineLife -= deadpoolDamage;
            if (deadpoolDamage === 100) {
                console.log("¡Wolverine recibe un ataque máximo y no puede atacar en el próximo turno!");
                turn++;
                continue; // Saltamos el turno de Wolverine
            }
        } else {
            console.log("¡Deadpool evade el ataque de Wolverine!");
        }

        // Wolverine ataca a Deadpool
        if (Math.random() > 0.2) { // Wolverine no evade
            let wolverineDamage = getRandomInt(10, 120);
            console.log(`Wolverine ataca a Deadpool y causa ${wolverineDamage} de daño.`);
            deadpoolLife -= wolverineDamage;
            if (wolverineDamage === 120) {
                console.log("¡Deadpool recibe un ataque máximo y no puede atacar en el próximo turno!");
                turn++;
                continue; // Saltamos el turno de Deadpool
            }
        } else {
            console.log("¡Wolverine evade el ataque de Deadpool!");
        }

        // Mostrar la vida restante
        console.log(`Vida de Deadpool: ${deadpoolLife > 0 ? deadpoolLife : 0}`);
        console.log(`Vida de Wolverine: ${wolverineLife > 0 ? wolverineLife : 0}`);
        console.log('----------------------------------------');

        turn++;
    }

    // Determinar el ganador
    if (deadpoolLife <= 0 && wolverineLife <= 0) {
        console.log("¡Es un empate! Ambos han caído en combate.");
    } else if (deadpoolLife <= 0) {
        console.log("¡Wolverine gana!");
    } else {
        console.log("¡Deadpool gana!");
    }
}

// Aquí es donde debes definir la vida inicial y ejecutar la batalla
let deadpoolLife = 300;  // Vida inicial de Deadpool
let wolverineLife = 300; // Vida inicial de Wolverine

battle(deadpoolLife, wolverineLife);
