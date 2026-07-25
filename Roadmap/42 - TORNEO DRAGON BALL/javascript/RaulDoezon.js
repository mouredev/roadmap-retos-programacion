/*
  EJERCICIO:
  ¡El último videojuego de Dragon Ball ya está aquí!
  Se llama Dragon Ball: Sparking! ZERO.

  Simula un Torneo de Artes Marciales, al más puro estilo
  de la saga, donde participarán diferentes luchadores, y el
  sistema decidirá quién es el ganador.

  Luchadores:
  - Nombre.
  - Tres atributos: velocidad, ataque y defensa
    (con valores entre 0 a 100 que tú decidirás).
  - Comienza cada batalla con 100 de salud.
  Batalla:
  - En cada batalla se enfrentan 2 luchadores.
  - El luchador con más velocidad comienza atacando.
  - El daño se calcula restando el daño de ataque del
    atacante menos la defensa del oponente.
  - El oponente siempre tiene un 20% de posibilidad de
    esquivar el ataque.
  - Si la defensa es mayor que el ataque, recibe un 10%
    del daño de ataque.
  - Después de cada turno y ataque, el oponente pierde salud.
  - La batalla finaliza cuando un luchador pierde toda su salud.
  Torneo:
  - Un torneo sólo es válido con un número de luchadores
    potencia de 2.
  - El torneo debe crear parejas al azar en cada ronda.
  - Los luchadores se enfrentan en rondas eliminatorias.
  - El ganador avanza a la siguiente ronda hasta que sólo
    quede uno.
  - Debes mostrar por consola todo lo que sucede en el torneo,
    así como el ganador.
*/

const fighters = [
  {
    name: "Goku",
    attributes: { speed: 90, attack: 90, defense: 65 },
    health: 100,
  },
  {
    name: "Vegeta",
    attributes: { speed: 85, attack: 85, defense: 70 },
    health: 100,
  },
  {
    name: "Piccolo",
    attributes: { speed: 75, attack: 75, defense: 70 },
    health: 100,
  },
  {
    name: "Gohan",
    attributes: { speed: 80, attack: 80, defense: 65 },
    health: 100,
  },
  {
    name: "Trunks",
    attributes: { speed: 70, attack: 70, defense: 55 },
    health: 100,
  },
  {
    name: "Goten",
    attributes: { speed: 70, attack: 65, defense: 60 },
    health: 100,
  },
  {
    name: "Krillin",
    attributes: { speed: 60, attack: 60, defense: 55 },
    health: 100,
  },
  {
    name: "Tien Shinhan",
    attributes: { speed: 65, attack: 60, defense: 60 },
    health: 100,
  },
];

if (Math.log2(fighters.length) % 1 === 0) {
  let definePositions = new Set();

  while(definePositions.size !== fighters.length) {
    definePositions.add(Math.floor(Math.random() * fighters.length));
  }

  let positions = [...definePositions];

  for (let roundIndex = 0; roundIndex <= positions.length; roundIndex++) {
    let numberOfFights = positions.length / 2;
    let fightCounter = 0;
    let positionsBackup = [];
    let fights = [];

    for (let index = 0; index < numberOfFights; index++) {
      fights.push(positions.slice(fightCounter, fightCounter + 2));

      function combat(fighter1Health, fighter2Health) {
        let fighter1 = fighters[fights[index][0]];
        let fighter2 = fighters[fights[index][1]];
        const fighter1Speed = fighter1.attributes.speed;
        const fighter2Speed = fighter2.attributes.speed;

        if (fighter2Speed > fighter1Speed) {
          fighter1 = fighters[fights[index][1]];
          fighter2 = fighters[fights[index][0]];
        }

        const fighter1Attack = Math.random() <= 0.20 ? 0 : fighter1.attributes.attack;
        const fighter2Attack = Math.random() <= 0.20 ? 0 : fighter2.attributes.attack;
        const fighter1Defense = fighter1.attributes.defense;
        const fighter2Defense = fighter2.attributes.defense;

        if (fighter1Health <= 0) {
          console.log(`\n✌🏼 ${fighter2.name} derrotó a ${fighter1.name}`);
          positionsBackup.push(fighters.findIndex(x => x.name === fighter2.name));

          return;
        } else if (fighter2Health <= 0) {
          console.log(`\n✌🏼 ${fighter1.name} derrotó a ${fighter2.name}`);
          positionsBackup.push(fighters.findIndex(x => x.name === fighter1.name));

          return;
        }

        console.log(`\n🏁 ${fighter1.name} (${fighter1Health}) vs ${fighter2.name} (${fighter2Health})`);
        console.log(`💥 ${fighter1.name} ataca`);

        if (fighter1Attack === 0) {
          console.log(`🔴 ${fighter2.name} esquivó el ataque`);
        } else {
          if (fighter1Attack > fighter2Defense) {
            fighter2Health = fighter2Health - (fighter1Attack - fighter2Defense);
          } else {
            fighter2Health = fighter2Health - ((fighter1Attack * 10) / 100);
          }
        }

        console.log(`💥 ${fighter2.name} ataca`);

        if (fighter2Attack === 0) {
          console.log(`🔴 ${fighter1.name} esquivó el ataque`);
        } else {
          if (fighter2Attack > fighter1Defense) {
            fighter1Health = fighter1Health - (fighter2Attack - fighter1Defense);
          } else {
            fighter1Health = fighter1Health - ((fighter2Attack * 10) / 100);
          }
        }

        return combat(fighter1Health, fighter2Health);
      }
      
      combat(100, 100);

      fightCounter = fightCounter + 2;

      console.log('----------------------------------');
    }

    positions = [...positionsBackup];

    console.log('--------- FINAL DE RONDA ---------');

    if (positions.length === 1) {
      console.log(`\n¡${fighters[positions[0]].name} es el campeón! 🏆`);
    }
  }
} else {
  console.log('El torneo no puede llevarse a cabo porque no hay participantes suficientes.');
}
