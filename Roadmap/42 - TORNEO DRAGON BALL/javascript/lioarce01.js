//======= GLOBAL CONSTANTS =======//
const EVADE_CHANCE = 0.2;
const HEALTH = 100;
const FIGHTERS = [
  {
    name: "Goku",
    speed: 90,
    attack_damage: 100,
    defense: 80,
  },
  {
    name: "Vegeta",
    speed: 85,
    attack_damage: 95,
    defense: 85,
  },
  {
    name: "Piccolo",
    speed: 80,
    attack_damage: 85,
    defense: 90,
  },
  {
    name: "Gohan",
    speed: 88,
    attack_damage: 90,
    defense: 86,
  },
  {
    name: "Frieza",
    speed: 95,
    attack_damage: 98,
    defense: 70,
  },
  {
    name: "Cell",
    speed: 90,
    attack_damage: 95,
    defense: 75,
  },
  {
    name: "Buu",
    speed: 70,
    attack_damage: 92,
    defense: 100,
  },
  {
    name: "Broly",
    speed: 80,
    attack_damage: 110,
    defense: 90,
  },
  {
    name: "Trunks",
    speed: 82,
    attack_damage: 88,
    defense: 80,
  },
  {
    name: "Android 18",
    speed: 84,
    attack_damage: 89,
    defense: 82,
  },
  {
    name: "Tien Shinhan",
    speed: 75,
    attack_damage: 80,
    defense: 85,
  },
  {
    name: "Krillin",
    speed: 78,
    attack_damage: 75,
    defense: 78,
  },
  {
    name: "Yamcha",
    speed: 77,
    attack_damage: 73,
    defense: 75,
  },
  {
    name: "Goten",
    speed: 85,
    attack_damage: 80,
    defense: 70,
  },
  {
    name: "Pan",
    speed: 88,
    attack_damage: 82,
    defense: 72,
  },
  {
    name: "Raditz",
    speed: 80,
    attack_damage: 85,
    defense: 78,
  },
];

//===============================//

class Fighter {
  constructor(name, speed, attack_damage, defense) {
    this.name = name;
    this.speed = this.attributeCheck(speed, 100);
    this.attack_damage = this.attributeCheck(attack_damage, 100);
    this.defense = this.attributeCheck(defense, 100);
    this.health = HEALTH;
  }

  attributeCheck(value, max) {
    if (value < 0) {
      console.warn(`Attribute cannot be negative: ${attribute}. Setting to 0`);
      return 0;
    }

    if (value > max) {
      console.warn(`Attribute exceeds maximum of ${max}. Setting to ${max}`);
      return max;
    }

    return value;
  }

  resetHealth() {
    this.health = HEALTH;
  }

  attack(defender) {
    const evade = Math.random();

    if (!defender.isAlive()) {
      console.log(`${defender.name} has lost all of its health`);
      return;
    }

    if (evade < EVADE_CHANCE) {
      console.log(`${defender.name} has evaded the attack`);
      return;
    }

    let damage;

    if (defender.defense >= this.attack_damage) {
      damage = this.attack_damage * 0.1;
      console.log(
        `${this.name} has dealt ${damage.toFixed()} damage to ${defender.name}`
      );
    } else {
      damage = this.attack_damage - defender.defense;
    }

    defender.health = Math.max(defender.health - damage, 0);

    console.log(
      `${this.name} has dealt ${damage.toFixed()} damage to ${defender.name}, ${
        defender.name
      } has ${defender.health.toFixed()} health left`
    );
  }

  isAlive() {
    return this.health > 0;
  }

  showInfo() {
    console.log(`Name: ${this.name}`);
    console.log(`Speed: ${this.speed}`);
    console.log(`Attack: ${this.attack_damage}`);
    console.log(`Defense: ${this.defense}`);
    console.log(`Health: ${this.health.toFixed()}`);
  }
}

class Tournament {
  constructor(fighters) {
    if (fighters.length < 4 || fighters.length % 2 !== 0) {
      throw new Error(
        "Teams must have at least four fighters and an even number of fighters"
      );
    }

    this.teamA = fighters
      .slice(0, fighters.length / 2)
      .map((f) => new Fighter(f.name, f.speed, f.attack_damage, f.defense));
    this.teamB = fighters
      .slice(fighters.length / 2)
      .map((f) => new Fighter(f.name, f.speed, f.attack_damage, f.defense));
  }

  shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  start() {
    console.log("\n==== Tournament Begins ====");

    let winnerA = this.startKey(this.teamA, "A");
    let winnerB = this.startKey(this.teamB, "B");

    console.log(
      `\n${winnerA.name} and ${winnerB.name} resting for the final match`
    );

    winnerA.resetHealth();
    winnerB.resetHealth();

    this.finalMatch(winnerA, winnerB);
  }

  startKey(team, teamName) {
    let round = 1;

    this.shuffleArray(team);

    while (team.length > 1) {
      console.log(`=== Round ${round} of team ${teamName} ===`);

      this.shuffleArray(team);

      let nextRoundFighters = [];
      for (let i = 0; i < team.length; i += 2) {
        let fighter1 = team[i];
        let fighter2 = team[i + 1];

        console.log(`Battle between ${fighter1.name} and ${fighter2.name}`);
        let winner = this.fight(fighter1, fighter2);
        console.log(`${winner.name} WON THE BATTLE!`);
        nextRoundFighters.push(winner);
      }

      team = nextRoundFighters;
      round++;
    }

    console.log(`\n==== Team ${teamName} Winner: ${team[0].name} ====`);

    return team[0];
  }

  fight(fighter1, fighter2) {
    let turn = 0;

    while (fighter1.isAlive() && fighter2.isAlive()) {
      if (turn % 2 === 0) {
        fighter1.attack(fighter2);
      } else {
        fighter2.attack(fighter1);
      }

      turn++;
    }

    return fighter1.isAlive() ? fighter1 : fighter2;
  }

  finalMatch(winnerA, winnerB) {
    console.log("\n==== Grand Final ====");
    console.log(`\n==== ${winnerA.name} vs ${winnerB.name} ====`);

    let finalWinner = this.fight(winnerA, winnerB);
    console.log(`\n${finalWinner.name} WON THE TOURNAMENT!`);

    console.log(`\n==== WINNER STATS ====`);
    finalWinner.showInfo();
  }
}

let tournament = new Tournament(FIGHTERS);
tournament.start();
