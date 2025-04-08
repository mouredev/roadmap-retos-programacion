import * as readline from "readline";
import { setTimeout } from "timers/promises";

const askQuestion = (query: string): Promise<string> => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise((resolve) => {
    rl.question(query, (answer) => {
      resolve(answer);
      rl.close();
    });
  });
};

interface SuperHero {
  name: string;
  health: number;
  attackRange: Array<number>;
  evadePercentage: number;
  isRegenerating: boolean;
  isWinner: boolean;
}

const wolverine: SuperHero = {
  name: "Wolverine",
  health: 0,
  attackRange: [10, 100],
  evadePercentage: 0.2,
  isRegenerating: false,
  isWinner: false,
};

const deadpool: SuperHero = {
  name: "Deadpool",
  health: 0,
  attackRange: [10, 120],
  evadePercentage: 0.25,
  isRegenerating: false,
  isWinner: false,
};

const superHeroAttack = (superHero: SuperHero) => {
  const [min, max] = superHero.attackRange;
  return Math.floor(Math.random() * (max - min)) + min;
};

const superHeroEvade = (superHero: SuperHero) => {
  const { evadePercentage } = superHero;
  const random = Math.random() * 100;
  return random < evadePercentage;
};

const superHeroReceiveDamage = (damage: number, superHero: SuperHero) => {
  const { health } = superHero;
  const newhealth = health - damage;
  superHero.health = newhealth;
};

const executeTurn = async (
  attacker: SuperHero,
  victim: SuperHero,
  turnNumber: number
) => {
  console.log(`--- Turn ${turnNumber}: ${attacker.name} atack ---\n`);

  if (!attacker.isRegenerating) {
    const damage = superHeroAttack(attacker);
    if (superHeroEvade(victim)) {
      console.log(`${victim.name} avoided ${attacker.name} atack!`);
    } else {
      superHeroReceiveDamage(damage, victim);
      console.log(
        `${attacker.name} hits ${victim.name} with ${damage} points of damage!`
      );
      if (damage === attacker.attackRange[1]) {
        victim.isRegenerating = true;
        console.log(`Maximum damage! ${victim.name} will miss his next turn.`);
      }
    }
  } else {
    console.log(`${attacker.name} recovers and loses his turn.`);
    attacker.isRegenerating = false;
  }

  console.log(`\n[__${attacker.name} tiene ${attacker.health} de vida__]`);
  console.log(`[__${victim.name} tiene ${victim.health} de vida__]\n`);

  if (victim.health <= 0) {
    attacker.isWinner = true;
  }

  await setTimeout(1000);
};

const superHeroesFight = async (
  superHeroOne: SuperHero,
  superHeroTwo: SuperHero,
  turnCount: number
) => {
  await executeTurn(superHeroOne, superHeroTwo, turnCount);
  if (!superHeroTwo.isWinner) {
    await executeTurn(superHeroTwo, superHeroOne, turnCount + 1);
  }
};

const main = async (superHeroOne: SuperHero, superHeroTwo: SuperHero) => {
  superHeroOne.health = parseInt(
    await askQuestion(`Ingrese la vida de ${superHeroOne.name}: `)
  );
  superHeroTwo.health = parseInt(
    await askQuestion(`Ingrese la vida de ${superHeroTwo.name}: `)
  );

  console.log(
    `\nComienza la batalla entre ${superHeroOne.name} y ${superHeroTwo.name}\n`
  );

  let turnCount = 1;
  while (!superHeroOne.isWinner && !superHeroTwo.isWinner) {
    await superHeroesFight(superHeroOne, superHeroTwo, turnCount);
    turnCount += 2;
  }

  console.log(
    `The winner is ${
      superHeroOne.isWinner ? superHeroOne.name : superHeroTwo.name
    }!`
  );
};

main(wolverine, deadpool);
