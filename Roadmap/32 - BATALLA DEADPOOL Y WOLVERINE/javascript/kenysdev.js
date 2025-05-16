/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#32 * BATALLA DEADPOOL Y WOLVERINE
-------------------------------------------------------
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
*/
// ________________________________________________________
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function getInput(promptText, callback, type = "string") {
    rl.question(promptText, function processInput(input) {
        if (!input || input.trim() === "") {
            rl.question("The input cannot be empty. Please try again: ", processInput);
            return;
        }

        if (type === "number") {
            const numValue = Number(input.trim());
            if (isNaN(numValue)) {
                rl.question("Please enter a valid number: ", processInput);
                return;
            }
            callback(numValue);
            return;
        }
        
        callback(input.trim());
    });
}

function getInputAsync(promptText, type = "string") {
    return new Promise((resolve) => {
        getInput(promptText, resolve, type);
    });
}

class GlobalConfig {
    static TIME = 2;
    static MINIMUM_HP = 200;
    static CHARACTERS = {
        "Deadpool": {
            attacks: ["With weapon", "Hand to hand", "With reckless attack"],
            damageRange: [10, 100],
            defenseChance: 0.25
        },
        "Wolverine": {
            attacks: ["With adamantium claws", "With weapon", "Hand to hand"],
            damageRange: [10, 120],
            defenseChance: 0.20
        }
    };
    
    static MENU = `
BATTLE SIMULATOR:
------------------------------------------
| 1. Simulate a battle | 2. Exit         |
------------------------------------------`;
}

class Character {
    constructor(name, hp, attributes) {
        this.name = name;
        this.hp = hp;
        this.attacks = attributes.attacks;
        this.damageRange = attributes.damageRange;
        this.defenseChance = attributes.defenseChance;
        this.canAttack = true;
    }

    attack() {
        if (this.canAttack) {
            const selectedAttack = this.attacks[Math.floor(Math.random() * this.attacks.length)];
            const damage = Math.floor(Math.random() * (this.damageRange[1] - this.damageRange[0] + 1)) + this.damageRange[0];
            console.log(`|'${this.name}' attacks '${selectedAttack}' Causing: '-${damage}' 👊|`);
            return damage;
        } else {
            console.log(`|'${this.name}' is regenerating and cannot attack. 😴|`);
            return 0;
        }
    }

    defend() {
        if (Math.random() < this.defenseChance) {
            console.log(`|'${this.name}' managed to defend. 🛡️|`);
            return true;
        } else {
            console.log(`|'${this.name}' couldn't block the attack. 🤕|`);
            return false;
        }
    }
}

class BattleStrategy {
    execute(attacker, defender) {
        const damage = attacker.attack();
        
        if (damage === attacker.damageRange[1]) {
            console.log(`|'${defender.name}' 🚨received a critical hit and won't be able to attack.🚨|`);
            defender.canAttack = false;
        }
        
        if (attacker.canAttack) {
            if (!defender.defend()) {
                defender.hp -= damage;
            }
        } else {
            attacker.canAttack = true;
        }
        
        if (defender.hp <= 0) {
            console.log("\n____________________________");
            console.log(`|'${attacker.name}' 🏆 wins the battle. 🏆|`);
            return false;
        }
        
        return true;
    }
}

class BattleFeatures {
    constructor() {
        this.battleStrategy = new BattleStrategy();
        this.character1 = null;
        this.character2 = null;
    }

    async getCharacter(msg) {
        while (true) {
            console.log("\nAvailable characters:");
            Object.keys(GlobalConfig.CHARACTERS).forEach((name, i) => {
                console.log(`${i}. ${name}`);
            });

            const index = await getInputAsync(msg, "number");
            const keys = Object.keys(GlobalConfig.CHARACTERS);

            if (!(index >= 0 && index < keys.length)) {
                console.log("Incorrect character number.");
                continue;
            }

            if (this.character1 && keys[index] === this.character1.name) {
                console.log("Character already used.");
                continue;
            }

            const hp = await getInputAsync(`Set HP >= than '${GlobalConfig.MINIMUM_HP}': `, "number");
            if (hp < GlobalConfig.MINIMUM_HP) {
                console.log(`HP must be greater than '${GlobalConfig.MINIMUM_HP}'.`);
                continue;
            }

            const name = keys[index];
            const attributes = GlobalConfig.CHARACTERS[name];
            return { name, hp, attributes };
        }
    }

    showHP() {
        console.log("____________________________");
        console.log(`|${this.character1.name}: ❤️ ${this.character1.hp}| |${this.character2.name}: ❤️ ${this.character2.hp}|`);
    }

    async battle() {
        let turn = 1;
        while (true) {
            console.log(`\n----------------------------\nTurn #${turn}\n----------------------------`);

            this.showHP();
            if (!this.battleStrategy.execute(this.character1, this.character2)) break;
            
            this.showHP();
            if (!this.battleStrategy.execute(this.character2, this.character1)) break;

            turn++;
            await new Promise(resolve => setTimeout(resolve, GlobalConfig.TIME * 1000));
        }
        
        this.showHP();
    }

    async startSimulation() {
        const char1Data = await this.getCharacter("'First' character: ");
        this.character1 = new Character(char1Data.name, char1Data.hp, char1Data.attributes);

        const char2Data = await this.getCharacter("'Second' character: ");
        this.character2 = new Character(char2Data.name, char2Data.hp, char2Data.attributes);

        await this.battle();

        this.character1 = null;
        this.character2 = null;
        console.log(GlobalConfig.MENU);
    }
}

class Program {
    constructor() {
        this.features = new BattleFeatures();
    }

    async run() {
        console.log(GlobalConfig.MENU);
        while (true) {
            const option = await getInputAsync("\nOption: ", "number");
            switch (option) {
                case 1:
                    await this.features.startSimulation();
                    break;
                case 2:
                    console.log("Goodbye");
                    rl.close();
                    return;
                default:
                    console.log("Select from '1 to 2'");
            }
        }
    }
}

const program = new Program();
program.run().catch(console.error);
