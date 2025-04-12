import * as readline from "readline";
import { setTimeout } from "timers/promises";

//--------------------------------//
//             CONSTS             //
//--------------------------------//

const TURN_DELAY = 1000;

//--------------------------------//
//           INTERFACES           //
//--------------------------------//
interface SuperHero {
  name: string;
  health: number;
  attackRange: Array<number>;
  evadePercentage: number;
  isRegenerating: boolean;
  isWinner: boolean;
}

//--------------------------------//
//         UTILS FUNCTIONS        //
//--------------------------------//

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

//--------------------------------//
//       SUPERHERO CONFIG         //
//--------------------------------//

const createSuperHero = (
  name: string,
  attackRange: [number, number],
  evadePercentage: number
): SuperHero => ({
  name,
  health: 0,
  attackRange,
  evadePercentage,
  isRegenerating: false,
  isWinner: false,
});

//--------------------------------//
//       BATTLE MECHANICS         //
//--------------------------------//

const calculateAttack = (superHero: SuperHero): number => {
  const [min, max] = superHero.attackRange;
  return Math.floor(Math.random() * (max - min)) + min;
};

const attemptEvade = (superHero: SuperHero): boolean => {
  return Math.random() * 100 < superHero.evadePercentage;
};

const applyDamage = (damage: number, superHero: SuperHero): void => {
  superHero.health -= damage;
};

const executeTurn = async (
  attacker: SuperHero,
  victim: SuperHero,
  turnNumber: number
): Promise<void> => {
  console.log(`--- Turn ${turnNumber}: ${attacker.name} atack ---\n`);

  if (!attacker.isRegenerating) {
    const damage = calculateAttack(attacker);
    if (attemptEvade(victim)) {
      console.log(`${victim.name} avoided ${attacker.name} atack!`);
    } else {
      applyDamage(damage, victim);
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

  await setTimeout(TURN_DELAY);
};

const superHeroesFight = async (
  superHeroOne: SuperHero,
  superHeroTwo: SuperHero,
  turnCount: number
): Promise<void> => {
  await executeTurn(superHeroOne, superHeroTwo, turnCount);
  if (!superHeroOne.isWinner) {
    await executeTurn(superHeroTwo, superHeroOne, turnCount + 1);
  }
};

const initializeHeroes = async (
  heroOne: SuperHero,
  heroTwo: SuperHero
): Promise<void> => {
  heroOne.health = parseInt(
    await askQuestion(`Ingrese la vida de ${heroOne.name}: `)
  );
  heroTwo.health = parseInt(
    await askQuestion(`Ingrese la vida de ${heroTwo.name}: `)
  );
};

const startBattle = async (
  superHeroOne: SuperHero,
  superHeroTwo: SuperHero
): Promise<SuperHero> => {
  await initializeHeroes(superHeroOne, superHeroTwo);

  console.log(
    `\nComienza la batalla entre ${superHeroOne.name} y ${superHeroTwo.name}\n`
  );

  let turnCount = 1;
  while (!superHeroOne.isWinner && !superHeroTwo.isWinner) {
    await superHeroesFight(superHeroOne, superHeroTwo, turnCount);
    turnCount += 2;
  }

  const winner = superHeroOne.isWinner ? superHeroOne : superHeroTwo;
  console.log(`The winner is ${winner.name}!`);

  return winner;
};

//--------------------------------//
//              MAIN              //
//--------------------------------//

const wolverine = createSuperHero("Wolverine", [10, 100], 0.2);
const deadpool = createSuperHero("Deadpool", [10, 120], 0.25);

const main = async (): Promise<void> => {
  await startBattle(wolverine, deadpool);
};

main();
