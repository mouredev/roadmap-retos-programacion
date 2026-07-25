import readline from "readline";

const colors = {
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  reset: "\x1b[0m",
}

class Asks {
  constructor() {
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
  }

  ask(question) {
    return new Promise((resolve) => {
      this.rl.question(question, (answer) => resolve(answer));
    });
  }

  close() {
    this.rl.close();
  }
}

class Character {
  constructor(name, health, maxDamage, probabilityOfEvasion) {
    this.name = name
    this.health = health
    this.minDamage = 10
    this.maxDamage = maxDamage
    this.probabilityOfEvasion = probabilityOfEvasion
  }

  attack() {
    return (Math.round(this.minDamage + (Math.random() * (this.maxDamage - this.minDamage))))
  }

  evade() {
    if ((Math.random() * 100) < this.probabilityOfEvasion) {
      return true
    } 

    return false
  }
}

const asks = new Asks()

function await1Second() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve()
    }, 1000);
  })
}

class FightManager {
  constructor(characterOne, characterTwo) {
    this.characterOne = characterOne
    this.characterTwo = characterTwo
    this.damage = 0
    this.didEvade = false
    this.round = 0
  }

  logRound() {
    this.round += 1
    console.log(`\n${colors.yellow}------- Round: ${this.round} -------${colors.reset}`)
  }

  processAttack(whoAttack) {
    let defender, attacker
    if ((whoAttack % 2) === 0) {
      attacker = this.characterTwo
      defender = this.characterOne
    } else {
      attacker = this.characterOne
      defender = this.characterTwo
    }

    this.damage = attacker.attack()

    this.didEvade = defender.evade()

    if (this.didEvade) {
      console.log(`${colors.green}${defender.name} evaded the attack${colors.reset}`)
    } else {
      defender.health = Math.max(0, defender.health - this.damage)

      console.log(`🗡️   ${attacker.name} inflicted ${this.damage} points of damage`)
    }
  }

  async shouldSkipTurn(whoAttack) {
    if ((whoAttack % 2) === 0 && this.damage === this.characterTwo.maxDamage) {
      this.logRound()

      console.log(`\n💥   ${this.characterTwo.name} has done MAX DAMAGE   💥\n${this.characterOne.name} nedds to regenerate`)

      await await1Second()

      return true
    } else if ((whoAttack % 2) === 1 && this.damage === this.characterOne.maxDamage) {
      this.logRound()

      console.log(`\n💥   ${this.characterOne.name} has done MAX DAMAGE   💥\n${this.characterTwo.name} nedds to regenerate`)

      await await1Second()

      return true
    } else return false
  }

  printStatus() {
    console.log(`❤️   ${colors.red}${this.characterOne.name} health: ${this.characterOne.health}` + '\n' +
                `❤️   ${this.characterTwo.name} health: ${this.characterTwo.health}${colors.reset}`
    )
  }

  checkWinner() {
    if (this.characterOne.health === 0) {
      console.log(`\nWINNER: ${this.characterTwo.name}`)
      return true
    }

    if (this.characterTwo.health === 0) {
      console.log(`\nWINNER: ${this.characterOne.name}`)
      return true
    }
  }
}

async function fight() {
  const healthCharacterOne = parseInt(await asks.ask("Insert Wolverine's health: "))
  const healthCharacterTwo = parseInt(await asks.ask("Insert Deadpool's health: "))

  if (isNaN(healthCharacterOne) || isNaN(healthCharacterTwo)) {
    console.warn('The health of the characters must be a number')
    fight()
  }

  const fightManager = new FightManager(new Character('Wolverine', healthCharacterOne, 120, 20), new Character('Deadpool' , healthCharacterTwo, 100, 25))

  const firstAttack = (await asks.ask('who will launch the first attack?' + '\n' +
                                      'W ---> Wolverine'  + '\n' +
                                      'D ---> Deadpool\n')).toUpperCase()

  if (firstAttack !== 'W' && firstAttack !== 'D') {
    console.warn('Invalid option')
    return fight()
  }

  let whoAttack = (firstAttack === 'W') ? 1 
                                    : 2 

  let finished = false

  while (!finished) {
    fightManager.logRound()
    fightManager.processAttack(whoAttack)
    fightManager.printStatus()
    if (fightManager.checkWinner()) finished = true

    await await1Second()

    if (await fightManager.shouldSkipTurn()) { whoAttack++ }

    whoAttack++
  }

  asks.close()
}

fight()